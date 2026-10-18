"""Helpers for the course notebooks.

Load them at the top of every notebook with:

    %load_ext course_helpers

This gives you two things:

1. The %%node cell magic. A cell that starts with %%node is sent to Node.js
   and runs as JavaScript. Each %%node cell is a complete, separate program:
   variables do not carry over from one JavaScript cell to the next.

2. A check(actual, expected) function, in both Python and JavaScript cells.
   It prints ✅ when the two values are equal and ❌ when they are not.
   It is an ordinary function. In lesson 05 you write your own version.
"""

import os
import re
import shutil
import subprocess
import threading
from pathlib import Path

DEFAULT_TIMEOUT_SECONDS = 10
MAX_OUTPUT_LINES = 500

# Added to the end of a JavaScript cell when the cell uses check().
# Function declarations are "hoisted", so check() can be called above this
# line. Adding it at the end keeps the line numbers in error messages correct.
JS_CHECK = (
    "\n;function check(actual, expected, label = \"\") {"
    " const show = (v) => (v === undefined ? \"undefined\" : JSON.stringify(v));"
    " const prefix = label ? label + \": \" : \"\";"
    " if (show(actual) === show(expected)) console.log(`✅ ${prefix}got ${show(actual)}`);"
    " else console.log(`❌ ${prefix}expected ${show(expected)} but got ${show(actual)}`); }\n"
)
DECLARES_CHECK = re.compile(r"\b(function\s+check|(const|let|var)\s+check)\b")
USES_CHECK = re.compile(r"\bcheck\s*\(")


def check(actual, expected, label=""):
    """Print ✅ if actual == expected, otherwise print ❌ and both values."""
    prefix = f"{label}: " if label else ""
    if actual == expected:
        print(f"✅ {prefix}got {actual!r}")
    else:
        print(f"❌ {prefix}expected {expected!r} but got {actual!r}")


class _OutputCleaner:
    """Makes Node's error messages shorter and easier to read.

    - The long file path of the cell becomes just "cell", so errors read
      like "cell:4:30" (line 4, column 30 of the cell).
    - Lines about Node's own internal code are removed.
    """

    def __init__(self):
        self.cell_path = re.compile(r"(file:///\S*?)?\[eval\d*\]")
        self.cwd_url = Path.cwd().as_uri() + "/"
        self.colour_codes = re.compile(r"\x1b\[[0-9;]*m")

    def clean(self, line):
        """Return the cleaned line, or None if the line should be hidden."""
        line = self.colour_codes.sub("", line)
        line = self.cell_path.sub("cell", line).replace(self.cwd_url, "")
        if re.match(r"^\s+at .*\bnode:", line):
            # An error's extra details can start at the end of a hidden line.
            return "  {" if line.endswith(" {") else None
        if re.match(r"^Node\.js v\d", line):
            return None
        return line


def _parse_timeout(line):
    match = re.search(r"--timeout\s+(\d+)", line)
    return int(match.group(1)) if match else DEFAULT_TIMEOUT_SECONDS


def node(line, cell):
    """Run the cell as a JavaScript program with Node.js.

    Usage:  %%node               (stops after 10 seconds)
            %%node --timeout 30  (stops after 30 seconds)
    """
    node_exe = shutil.which("node")
    if node_exe is None:
        print("⛔ Node.js was not found. Install it from https://nodejs.org "
              "and restart VS Code / Jupyter.")
        return

    code = cell
    if USES_CHECK.search(code) and not DECLARES_CHECK.search(code):
        code += JS_CHECK

    timeout = _parse_timeout(line)
    # Jupyter asks programs for coloured output. Plain text is easier to read here.
    env = {k: v for k, v in os.environ.items() if k not in ("FORCE_COLOR", "CLICOLOR_FORCE")}
    env["NO_COLOR"] = "1"
    proc = subprocess.Popen(
        # --input-type=module lets us use `import` and top-level `await`.
        [node_exe, "--input-type=module", "--test-reporter=spec"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # errors and normal output, in order
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    timed_out = threading.Event()

    def stop_program():
        timed_out.set()
        proc.kill()

    timer = threading.Timer(timeout, stop_program)
    timer.start()
    cleaner = _OutputCleaner()
    printed = 0
    try:
        proc.stdin.write(code)
        proc.stdin.close()
        pending_blank = False
        for raw in proc.stdout:
            text = cleaner.clean(raw.rstrip("\n"))
            if text is None:
                pending_blank = False
                continue
            if text.strip() == "":
                if pending_blank:
                    print("", flush=True)
                pending_blank = True
                continue
            if pending_blank:
                print("", flush=True)
                pending_blank = False
            printed += 1
            if printed <= MAX_OUTPUT_LINES:
                print(text, flush=True)
            elif printed == MAX_OUTPUT_LINES + 1:
                print(f"… (more than {MAX_OUTPUT_LINES} lines, the rest is hidden)",
                      flush=True)
        proc.wait()
    except KeyboardInterrupt:
        proc.kill()
        print("⏹️ Stopped.")
    finally:
        timer.cancel()

    if timed_out.is_set():
        print(f"⏱️ Stopped after {timeout} seconds. Is there an infinite loop? "
              f"(For slow programs use: %%node --timeout 30)")


def load_ipython_extension(ipython):
    ipython.register_magic_function(node, magic_kind="cell", magic_name="node")
    ipython.push({"check": check})

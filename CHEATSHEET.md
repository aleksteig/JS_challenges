# JavaScript ↔ Python Cheat Sheet

Every *Rosetta Stone* table from the course in one place. The ideas are the same in every language;
only the spelling changes. When you learn a new language, make a third column for it.

## 01 · Getting Started: What Is a Program?

| Idea | JavaScript | Python |
|---|---|---|
| Show something on the screen | `console.log("Hi");` | `print("Hi")` |
| Comment | `// a note` | `# a note` |
| End of a statement | `;` (optional, but use it) | end of the line |
| Text (string) | `"hello"` or `'hello'` | `"hello"` or `'hello'` |
| Error: unknown name | `ReferenceError` | `NameError` |

## 02 · Values, Types & Variables

| Idea | JavaScript | Python |
|---|---|---|
| Create a variable | `let x = 5;` | `x = 5` |
| Constant | `const PI = 3.14;` | `PI = 3.14` (by convention only) |
| Numbers | `number` (one type) | `int` and `float` |
| True / false | `true` / `false` | `True` / `False` |
| Nothing | `undefined`, `null` | `None` |
| Type of a value | `typeof x` | `type(x)` |
| Values inside text | `` `Hi ${name}` `` | `f"Hi {name}"` |
| Length of a string | `s.length` | `len(s)` |
| Whole-number division | `Math.floor(7 / 2)` | `7 // 2` |
| Remainder | `7 % 2` | `7 % 2` |
| Text → number | `Number("5")` | `int("5")`, `float("5")` |
| Number → text | `String(5)` | `str(5)` |
| `"5" + 1` | `"51"` (converts quietly) | `TypeError` |
| Naming style | `camelCase` | `snake_case` |

## 03 · Booleans & Conditionals

| Idea | JavaScript | Python |
|---|---|---|
| Equal / not equal | `===` / `!==` | `==` / `!=` |
| And / or / not | `&&` / `\|\|` / `!` | `and` / `or` / `not` |
| If | `if (x > 0) { ... }` | `if x > 0:` + indented block |
| Else if | `else if (...) { ... }` | `elif ...:` |
| Short if | `cond ? a : b` | `a if cond else b` |
| Falsy values | `false 0 "" null undefined NaN` | `False 0 "" None` + empty collections |
| Value → boolean | `Boolean(x)` | `bool(x)` |

## 04 · Loops

| Idea | JavaScript | Python |
|---|---|---|
| While loop | `while (x < 5) { ... }` | `while x < 5:` |
| Count 0 to 4 | `for (let i = 0; i < 5; i++)` | `for i in range(5):` |
| Count 1 to 10 | `for (let i = 1; i <= 10; i++)` | `for i in range(1, 11):` |
| Loop over a string / list | `for (const x of things)` | `for x in things:` |
| Add one | `i++` or `i += 1` | `i += 1` |
| Leave the loop / skip a round | `break` / `continue` | `break` / `continue` |
| Is ch in a string? | `"aeiou".includes(ch)` | `ch in "aeiou"` |
| Lower case | `s.toLowerCase()` | `s.lower()` |

## 05 · Functions & Scope

| Idea | JavaScript | Python |
|---|---|---|
| Define a function | `function f(a, b) { return a + b; }` | `def f(a, b):` + `return a + b` |
| Short function | `const f = (a, b) => a + b;` | `f = lambda a, b: a + b` |
| Default value | `function f(x = 1)` | `def f(x=1):` |
| No return value | `undefined` | `None` |
| Missing argument | becomes `undefined` | `TypeError` |
| What creates a new scope | every `{ }` block (`let` / `const`) | functions only |

## 06 · Arrays & Objects (Lists & Dictionaries)

| Idea | JavaScript | Python |
|---|---|---|
| List of values | `const a = [1, 2, 3];` | `a = [1, 2, 3]` |
| First / last item | `a[0]` / `a.at(-1)` | `a[0]` / `a[-1]` |
| Length | `a.length` | `len(a)` |
| Add to end / remove from end | `a.push(x)` / `a.pop()` | `a.append(x)` / `a.pop()` |
| Is x in it? | `a.includes(x)` | `x in a` |
| Slice | `a.slice(1, 3)` | `a[1:3]` |
| Loop with index | `for (let i = 0; i < a.length; i++)` | `for i, x in enumerate(a):` |
| Key → value | `const o = { name: "Ada" };` | `d = {"name": "Ada"}` |
| Read a key | `o.name` or `o["name"]` | `d["name"]` or `d.get("name")` |
| Missing index / key | `undefined` | `IndexError` / `KeyError` |
| Loop over keys and values | `for (const [k, v] of Object.entries(o))` | `for k, v in d.items():` |
| Split text into words | `s.split(" ")` | `s.split(" ")` |
| Data → JSON text | `JSON.stringify(x)` | `json.dumps(x)` |
| JSON text → data | `JSON.parse(s)` | `json.loads(s)` |

## 07 · References, Mutation & Functions as Values

| Idea | JavaScript | Python |
|---|---|---|
| Copy an array / list | `[...a]` | `a.copy()` |
| Copy an object / dict | `{ ...o }` | `d.copy()` |
| Deep copy | `structuredClone(x)` | `copy.deepcopy(x)` |
| Same contents? | compare yourself (e.g. with JSON) | `a == b` |
| Same object? | `a === b` | `a is b` |
| Transform every item | `a.map((x) => x * 2)` | `[x * 2 for x in a]` |
| Keep some items | `a.filter((x) => x > 0)` | `[x for x in a if x > 0]` |
| Combine into one value | `a.reduce((s, x) => s + x, 0)` | `sum(a)` or a loop |
| Sort numbers (as a copy) | `[...a].sort((x, y) => x - y)` | `sorted(a)` |
| Sort by a property | `[...a].sort((x, y) => x.age - y.age)` | `sorted(a, key=lambda x: x["age"])` |

## 08 · Errors & Debugging

| Idea | JavaScript | Python |
|---|---|---|
| Create an error | `throw new Error("msg")` | `raise ValueError("msg")` |
| Catch errors | `try { } catch (err) { }` | `try:` / `except ValueError as err:` |
| Always run | `finally { }` | `finally:` |
| The error's message | `err.message` | `str(err)` |
| Order of the stack trace | most recent call **first** | most recent call **last** |
| Divide by zero | `Infinity` / `NaN` | `ZeroDivisionError` |
| Is it NaN? | `Number.isNaN(x)` | `math.isnan(x)` |

## 09 · Modules, Testing & Documentation

| Idea | JavaScript | Python |
|---|---|---|
| Export from a module | `export function f() {}` | (everything at the top level) |
| Import from a module | `import { f } from "./file.mjs";` | `from file import f` |
| Built-in maths | `Math.sqrt(16)` | `import math` → `math.sqrt(16)` |
| Assertion | `assert.equal(a, b)` | `assert a == b` |
| Test tool | `node --test` | `pytest` |
| Install a package | `npm install name` | `pip install name` |
| Ends with / remove spaces | `s.endsWith(".pdf")` / `s.trim()` | `s.endswith(".pdf")` / `s.strip()` |
| Documentation | developer.mozilla.org | docs.python.org |

## 10 · Classes & Objects

| Idea | JavaScript | Python |
|---|---|---|
| Define a class | `class Dog { }` | `class Dog:` |
| Constructor | `constructor(name) { this.name = name; }` | `def __init__(self, name): self.name = name` |
| The current object | `this` | `self` |
| Method | `speak() { ... }` | `def speak(self): ...` |
| Create an instance | `new Dog("Rex")` | `Dog("Rex")` |
| Inherit | `class Dog extends Animal` | `class Dog(Animal):` |
| Call the parent's constructor | `super(name)` | `super().__init__(name)` |

## 11 · Async: Waiting for Things & Fetching Data

| Idea | JavaScript | Python |
|---|---|---|
| Run something later | `setTimeout(fn, 1000)` | `time.sleep(1)` (blocks) / `await asyncio.sleep(1)` |
| Async function | `async function f() {}` | `async def f():` |
| Wait for a result | `await f()` | `await f()` |
| Wait for several at once | `await Promise.all([a(), b()])` | `await asyncio.gather(a(), b())` |
| A value that arrives later | `Promise` | coroutine / `Task` |
| Get JSON from a URL | `await (await fetch(url)).json()` | `requests.get(url).json()` |
| Did the request succeed? | `response.ok` | `HTTPError` is raised if not |

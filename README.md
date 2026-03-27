> ⚠️ This project is in early development. I'm not accepting contributions at this time.
# Jhansi
A minimal procedural language designed for systems programming - including operating systems.

Jhansi is a minimal procedural language being built from scratch - interpreter first, C compiler next, self-hosting after that. No garbage collector, no runtime, no features you wouldn't need to write a compiler or kernel. The syntax is Go-flavored. The philosophy is C-honest.

The interpreter is being built in Python, then rewritten in Jhansi itself. When the solf-hosted compiler can compile itself and the outputs match, the Python compiler is deleted.

---

## Why

C is the right language for systems programming. But it carries 50 years of baggage - implicit integer promotions, `char` pretending to be text, undefined behaviour as a design choice.

Go cleaned up C's ergonomics. But Go brought a runtime, a garbage collector, and a scheduler - none of which belong inside a kernel.

Jhansi asks: what would a minimal, honest systems language look like today? Go's readbility. C's memory model. No runtime. No surprises.

The long-term goal is - a bootable OS written entirely in Jhansi.

---

## Design Principles
- **A byte is a `u8`.** There is no `char` type. `char` implies text. `u8` says what it actually is: an 8-bit unsigned integer. Single-quote literals (`'a'`, `'\n'`) are `u8` values - syntactic sugar for small integers.
- **No GC.** Memory is stack-allocated by default. Heap allocation goes through an explicit arena allocator.
- **No runtime.** The language produces C. The C produces a binary. Nothing in between.
- **Only include a feature if you'd need it to write a compiler.** Every addition is filtered through this constraint.

---

## Type System

| Type | Description |
|------|-------------|
| `int` | Signed integer - default integer type |
| `u8` | 8-bit unsigned integer. Replaces `char` entirely |
| `bool` | Boolean - `true` / `false` |
| `void` | No return value |
| `*T` | Raw pointer |
| `[N]T` | Fixed array - stack allocated, size known at compile time |
| `struct` | Named field grouping. No inheritance |
| `enum` | With optional payloads |

*Fixed-width integers (`u16`, `u32`, `u64`, `i8`, `i16`, `i32`, `i64`) arrive in V2 when codegen needs to emit real C types.*

---

## Syntax

*This section will be filled in as features land.*

```
// coming soon
```

---

## Roadmap

### V1 - Interpreter
A fully functional interpreter with semantic analysis. Every AST node is annotated with its resolved type - this annotation is the contract V2 codegen depends on.

Features: `int`, `u8`, `bool`, variable declarations, assignment, arithmetic, comparison, logical operators, `if`/`else`, `for` loops, functions, structs, arrays.

**Status: in progress (rewrite underway)**

---

### V2 - C Codegen
Walk the type-annotated AST and emit valid C. Hand it to gcc. Get a real binary.

Introduces: pointers, fixed-width integers, `unsafe` blocks.

---

### V3 - Self-Hosting
Add the minimum features needed to write Jhansi compiler in Jhansi itself.

- Enums (needed for `TokenType` and AST node kinds)
- Casting syntax
- `sizeof`
- Variadic functions (needed for `printf` in codegen output)
- Arena allocator - written in Jhansi, the first non-trivial Jhansi program

Then: port each compiler stage to Jhansi - lexer -> parser -> sema -> codegen. Compile the compiler with Python compiler. COmpile it again with itself. If the outputs match - self-hosted. Delete the Python compiler.

---

### The OS
The language is now proven. Build a bootable kernel, memory manager, VFS, scheduler and shell in Jhansi.

Reference scale: Unix (1973) was ~10,000 lines of C. xv6 (MIT's teaching OS) is the same. The OS targets that range.

---

## Running the interpreter

**Requirements:**Python 3.12+

```bash
git clone https://github.com/thearun85/jhansi.git
cd jhansi
python -m jhansi
```

*Full usage instructions will be added as the CLI stabilises.*

---

## Versioned History
| Tag | Description |
|-----|-------------|
| `v0.1.0` | First working interpreter - int, bool, char, variables, if/else. Built feature-by-feature. |

---

## Status

Early and deliberate. This is not a weekend project - it is being built to last.


# 19. Computer Architecture Introduction — Von Neumann, Performance, Memory Map

> **Source:** Unit 3 Slides 3.6.1, 3.14.2 | Textbook: Harris & Harris Ch. 6, 7

---

## Von Neumann vs Harvard Architecture

| Feature | Von Neumann | Harvard |
|---------|-------------|---------|
| **Memory** | Unified (Code+Data) | Separate Instruction/Data |
| **Bus** | Single shared bus | Separate I/D buses |
| **Bottleneck** | Yes (von Neumann bottleneck) | No |
| **Example** | Most general CPUs | DSPs, Microcontrollers |

---

## MIPS Memory Map (32-bit → 4 GB)

| Address Range | Segment | Description |
|---------------|---------|-------------|
| 0x00000000 – 0x003FFFFC | Reserved | — |
| **0x00400000 – 0x0FFFFFFC** | **Text** | PC starts at 0x00400000; ~256 MB for code |
| **0x10000000 – 0x1000FFFC** | **Global Data** | $gp = 0x10008000 (middle); 64 KB globals |
| **0x10010000 – 0x7FFFFFFC** | **Dynamic Data** | Heap (bottom ↑), Stack (top ↓, $sp=0x7FFFFFFC) |
| 0x80000000 – 0xFFFFFFFC | Reserved | OS, interrupts, memory-mapped I/O |

---

## Memory Segments Detail

### Text Segment
- Stores machine language program
- PC starts at 0x00400000
- Top 4 bits of all text addresses = 0 → `j` instruction can jump anywhere
- **Analogy:** Recipe book; PC = finger on current line

### Global Data Segment
- Stores global variables (declared outside functions in C)
- Accessed via `$gp` (global pointer) = 0x10008000
- `$gp` does **not** change during execution
- Any global accessed via base addressing with 16-bit offset from `$gp`

### Dynamic Data Segment (Stack & Heap)
| Property | Stack | Heap |
|----------|-------|------|
| **Use** | Save/restore registers; local variables/arrays | `malloc` (C), `new` (C++/Java) |
| **Allocation** | LIFO stack frames | Any order |
| **Direction** | Grows **down** from 0x7FFFFFFC | Grows **up** from 0x10010000 |
| **Collision** | If stack/heap meet → data corruption → OOM error |

### Reserved Segments
- Used by OS; cannot be used directly by program
- Interrupts, memory-mapped I/O

---

## Program Translation & Execution Pipeline

```
High-level code (C)
      ↓ Compiler
Assembly code (.s)
      ↓ Assembler (2 passes)
Object file (.o) — machine code + symbol table
      ↓ Linker
Executable (header + text + data)
      ↓ Loader (OS)
Memory (text + data + stack + heap)
      ↓ jal 0x00400000
Execution begins
```

### Assembler Two Passes
| Pass | Function |
|------|----------|
| **Pass 1** | Assign instruction addresses; build symbol table (labels, globals) |
| **Pass 2** | Produce machine code using symbol table for label/global addresses |

**Example:** `sw $a0, 0x8000($gp)` stores to global `f`
- 0x8000 sign-extended = 0xFFFF8000
- `$gp + 0xFFFF8000 = 0x10008000 + 0xFFFF8000 = 0x10000000` (address of `f`)

### Loader Steps
1. Read text segment from disk → memory text segment (0x00400000)
2. Set `$gp = 0x10008000` (middle of global data)
3. Set `$sp = 0x7FFFFFFC` (top of stack)
4. `jal 0x00400000` to start program

---

## Performance Metrics

### Latency
- Time required for **one task** from input to output
- `Latency = Time for one task`

### Throughput
- Number of tasks completed per unit time
- `Throughput = Completed tasks / Unit Time`
- For non-parallel: `Throughput = 1 / Latency`

### Key Distinction
- **Latency** = time per task (lower = faster response)
- **Throughput** = tasks per second (higher = more work)
- **Parallelism improves throughput, NOT latency**

---

## Amdahl's Law
```
Speedup = 1 / [(1 - f) + f/s]
```
- `f` = fraction of program that can be improved
- `s` = speedup of improved portion

**Example:** If 40% of program can be sped up 10×:
- Speedup = 1 / [0.6 + 0.4/10] = 1 / 0.64 = 1.56×

---

## Key Formulas (Memorize)

```
MIPS Memory:      2³² bytes = 4 GB
Text segment:     0x00400000–0x0FFFFFFC (PC starts at 0x00400000)
Global data:      0x10000000–0x1000FFFC ($gp=0x10008000)
Stack:            grows down from 0x7FFFFFFC
Heap:             grows up from 0x10010000
Latency:          time per task
Throughput:       tasks/second
Non-parallel TP:  1 / Latency
Amdahl's Law:     1 / [(1-f) + f/s]
```

---

## MCQ Patterns

1. **Von Neumann bottleneck** — single shared bus for code+data
2. **MIPS memory map segments** — text, global, dynamic, reserved
3. **$gp vs $sp** — $gp fixed at 0x10008000; $sp changes
4. **Stack vs Heap** — Stack grows down, Heap grows up
5. **Assembler passes** — Pass 1: symbol table; Pass 2: machine code
6. **Loader steps** — Load text, set $gp/$sp, jal to start
7. **Amdahl's Law** — diminishing returns on partial speedup
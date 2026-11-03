# 23. Compiling, Assembling, Linking & Loading — Program Translation Pipeline

> **Source:** Unit 3 Slides 3.14.2 | Textbook: Harris & Harris Ch. 6, 7

---

## Translation Pipeline Overview

```
High-level Code (C)
        ↓ Compiler
Assembly Code (.s)
        ↓ Assembler (2 passes)
Object File (.o) — Machine code + Symbol Table
        ↓ Linker
Executable — Header + Text Segment + Data Segment
        ↓ Loader (OS)
Memory (Text + Data + Stack + Heap)
        ↓ jal 0x00400000
Execution Begins
```

**In practice:** Most compilers (gcc, clang) combine compile+assemble+link in one command.

---

## Step 1: Compilation (C → Assembly)

Compiler translates high-level code into assembly.

### Example: Sum Function

**C Code:**
```c
int f, g, y;              // global variables
int main(void) {
    f = 2;
    g = 3;
    y = sum(f, g);
    return y;
}
int sum(int a, int b) {
    return (a + b);
}
```

**MIPS Assembly:**
```assembly
.data
f:                      # global f
g:                      # global g
y:                      # global y

.text
main:
    addi $sp, $sp, -4       # make stack frame
    sw   $ra, 0($sp)        # store $ra on stack
    addi $a0, $0, 2         # $a0 = 2
    sw   $a0, f             # f = 2
    addi $a1, $0, 3         # $a1 = 3
    sw   $a1, g             # g = 3
    jal  sum                # call sum(f, g)
    sw   $v0, y             # y = sum(f, g)
    lw   $ra, 0($sp)        # restore $ra
    addi $sp, $sp, 4        # restore stack pointer
    jr   $ra                # return to OS

sum:
    add  $v0, $a0, $a1      # $v0 = a + b
    jr   $ra                # return to caller
```

**Directives:**
- `.data` — start of data segment (globals)
- `.text` — start of text segment (code)
- Labels `f:`, `g:`, `y:` name globals; addresses assigned by assembler

---

## Step 2: Assembling (Assembly → Object File)

Assembler converts assembly to machine code in an **object file**. Two passes:

### Pass 1: Assign Addresses & Build Symbol Table

| Address | Instruction |
|---------|-------------|
| 0x00400000 | main: addi $sp, $sp, -4 |
| 0x00400004 | sw $ra, 0($sp) |
| 0x00400008 | addi $a0, $0, 2 |
| 0x0040000C | sw $a0, f |
| 0x00400010 | addi $a1, $0, 3 |
| 0x00400014 | sw $a1, g |
| 0x00400018 | jal sum |

...continues for all instructions...

### Pass 2: Generate Machine Code Using Symbol Table

**Symbol Table (after Pass 1):**
| Symbol | Address | Type |
|--------|---------|------|
| main | 0x00400000 | Label |
| sum | 0x0040002C | Label |
| f | 0x10000000 | Global |
| g | 0x10000004 | Global |
| y | 0x10000008 | Global |

Globals assigned in global data segment starting at 0x10000000.

### Object File Contents
- Machine code (text section)
- Data section (global variable addresses)
- Symbol table (for linking)

---

## Step 3: Linking (Object Files → Executable)

### Why Link?
- Large programs = many source files
- Change one file → only recompile that file
- Library files rarely change
- Unchanged files → reuse object files

### Linker Functions
1. **Combine** all object files into one machine-language file (executable)
2. **Relocate** data/instructions so they don't overlap
3. **Resolve** addresses using symbol tables (adjust relocated globals/labels)

**In our example:** Single object file → no relocation needed.

---

## Step 4: The Executable Structure

**Three Sections:**
| Section | Content |
|---------|---------|
| **Header** | Text size, Data size |
| **Text Segment** | Instructions in memory order |
| **Data Segment** | Global variable addresses |

### Example: First Store Instruction
```
Assembly: sw $a0, f
Machine:  sw $a0, 0x8000($gp)
```
- `$gp = 0x10008000` (middle of global data)
- Offset `0x8000` = 16-bit signed → sign-extended to `0xFFFF8000`
- Effective Address = `$gp + 0xFFFF8000 = 0x10008000 + 0xFFFF8000 = 0x10000000`
- This is address of global `f` ✓

---

## Step 5: Loading (Executable → Memory)

OS loads program by:
1. **Read text segment** from disk → memory text segment (0x00400000)
2. **Set `$gp = 0x10008000`** (middle of global data segment)
3. **Set `$sp = 0x7FFFFFFC`** (top of dynamic data segment)
4. **`jal 0x00400000`** to jump to program start

### Memory at Start of Execution
| Segment | Address Range | Content |
|---------|---------------|---------|
| Text | 0x00400000–0x00400030 | 13 instructions |
| Globals (f,g,y) | 0x10000000–0x10000008 | 3 words |
| Stack | Top at 0x7FFFFFFC | Empty initially |
| Heap | Bottom at 0x10010000 | Empty initially |
| **PC** | **0x00400000** | Points to `main` |

---

## MIPS Memory Map (32-bit = 4 GB)

| Range | Segment | Notes |
|-------|---------|-------|
| 0x00000000 – 0x003FFFFC | Reserved | — |
| **0x00400000 – 0x0FFFFFFC** | **Text** | PC starts at 0x00400000 (~256 MB) |
| **0x10000000 – 0x1000FFFC** | **Global Data** | $gp = 0x10008000 (middle) |
| **0x10010000 – 0x7FFFFFFC** | **Dynamic Data** | Heap (bottom↑), Stack (top↓, $sp=0x7FFFFFFC) |
| 0x80000000 – 0xFFFFFFFC | Reserved | OS, interrupts, MMIO |

### Segment Details

**Text Segment:**
- Stores program code
- Top 4 bits of all text addresses = 0
- **Why?** So `j` instruction (26-bit addr) can reach any text address

**Global Data:**
- Variables declared outside functions in C
- Accessed via `$gp` with 16-bit offset
- `$gp` fixed at 0x10008000 (doesn't change)
- Offset known at assembly time → efficient base addressing

**Dynamic Data (Stack + Heap):**
| Property | Stack | Heap |
|----------|-------|------|
| Use | Save/restore regs; local vars/arrays | malloc/new |
| Allocation | LIFO frames | Any order |
| Direction | Grows **down** from 0x7FFFFFFC | Grows **up** from 0x10010000 |
| Collision | Stack/heap meet → corruption → OOM error | — |

**Reserved:** OS, interrupts, memory-mapped I/O

---

## Key Formulas (Memorize)

```
Pipeline:     C → Assembly → Object → Executable → Memory → Run
Assembler:    Pass 1: addresses + symbol table; Pass 2: machine code
Linker:       Combine + Relocate + Resolve symbols
Loader:       Load text, set $gp=0x10008000, $sp=0x7FFFFFFC, jal 0x00400000

MIPS Memory:  2³² = 4 GB
Text:         0x00400000– (PC starts here)
Global:       0x10000000– ($gp=0x10008000)
Stack:        Grows down from 0x7FFFFFFC
Heap:         Grows up from 0x10010000

Global access:  EA = $gp + SignExt(16-bit offset)
               Offset known at assembly time
```

---

## MCQ Patterns

1. **Translation order** — Compile → Assemble → Link → Load
2. **Assembler passes** — Pass 1: addresses + symbols; Pass 2: machine code
3. **Linker purpose** — Combine object files, relocate, resolve symbols
4. **Loader steps** — Load text, set $gp/$sp, jal to start
5. **MIPS memory map** — Text at 0x00400000, Global at 0x10000000, Stack at 0x7FFFFFFC
6. **$gp vs $sp** — $gp fixed (0x10008000); $sp changes
7. **Global access** — $gp + 16-bit offset (base addressing)
8. **Stack/Heap direction** — Stack DOWN, Heap UP
9. **Text segment top bits** — All 0 → enables `j` to reach anywhere
10. **sw $a0, 0x8000($gp)** — offset sign-extended: 0x8000 → 0xFFFF8000 → EA = 0x10000000
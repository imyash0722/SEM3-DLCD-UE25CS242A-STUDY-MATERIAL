# 26. Unit 3 MCQ Practice — Architecture, Assembly, Memory, Parallelism

> **Source:** Unit 3 Slides (3.14.1, 3.14.2, 3.15.1, 3.17.1) MCQs | Textbook: Harris & Harris Ch. 6, 7

---

## Addressing Modes (3.14.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | Register-only addressing used by which MIPS instructions? | R-type |
| 2 | In immediate addressing, the constant operand is: | Encoded within the instruction itself |
| 3 | Which MIPS instructions use base addressing? | lw and sw |
| 4 | In base addressing, effective address = | Base Register + Sign-Extended Offset |
| 5 | PC-relative addressing mainly used by: | Conditional branch instructions (beq, bne) |
| 6 | In PC-relative, branch target calculated relative to: | PC + 4 |
| 7 | Which addressing mode used by j and jal? | Pseudo-direct Addressing |

**Answer Key:** Q1:C, Q2:C, Q3:C, Q4:B, Q5:C, Q6:B, Q7:D

---

## Compiling, Assembling, Loading (3.14.2)

| # | Question | Answer |
|---|----------|--------|
| 1 | Which segment does j instruction rely on? | Text — top 4 bits of addresses are 0 |
| 2 | Value of $gp at program start? | 0x10008000 (middle of global data) |
| 3 | Why can globals be reached efficiently via $gp? | 16-bit offset known at assembly time, base addressing |
| 4 | Correct statement about dynamic data segment? | Stack grows down from 0x7FFFFFFC, heap grows up |
| 5 | What does assembler do on Pass 1? | Assigns instruction addresses, finds all symbols |
| 6 | sw $a0, 0x8000($gp) stores to which address? | 0x10008000 + 0xFFFF8000 = 0x10000000 |
| 7 | Correct order of translation steps? | Compile → Assemble → Link → Load |

**Answer Key:** Q1:B, Q2:C, Q3:B, Q4:B, Q5:C, Q6:B, Q7:C

---

## Parallelism (3.15.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | Parallelism primarily aims to improve: | Throughput |
| 2 | A token in a parallel system refers to: | A unit of work moving through the system |
| 3 | Which parallelism uses multiple hardware units? | Spatial Parallelism |
| 4 | Pipeline registers are inserted to: | Divide combinational logic into stages |
| 5 | Modern processors combine: | Spatial and temporal parallelism |
| 6 | Increasing pipeline stages generally: | Improves throughput but may increase latency |
| 7 | Metric indicating useful work over time: | Throughput |
| 8 | Real-world example of temporal parallelism: | Assembly line (different stages on different products) |

**Answer Key:** Q1:B, Q2:B, Q3:B, Q4:B, Q5:C, Q6:A, Q7:B, Q8:B

---

## Assembly & Machine Language (3.7.1, 3.9.1, 3.11.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | Primary role of Program Counter (PC)? | Hold address of next instruction to execute |
| 2 | Assembly vs Machine code distinction? | Assembly is human-readable, must be translated to machine code |
| 3 | Which instruction transfers control when two registers equal? | beq |
| 4 | Instruction commonly used to return from function? | jr |
| 5 | In if-else, why is `j done` used? | To skip else block after executing if block |
| 6 | In while loop, which instruction causes repeat? | j while |
| 7 | Correct for-loop execution order? | Initialization → Condition → Statement → Update |
| 8 | Array base 0x10007000, what address accessed? | (Depends on index: base + 4×index) |
| 9 | In R-type, which field identifies ALU op when op=0? | funct |
| 10 | Which immediates use zero extension? | andi, ori, xori |
| 11 | In sra, new MSBs filled with: | Sign bit |
| 12 | In sllv, shift amount from: | Lower 5 bits of rs |
| 13 | Instruction format for j? | J-type |
| 14 | beq vs bne? | beq: branch if equal; bne: branch if not equal |

**Answer Key:** Q1:B, Q2:C, Q3:C, Q4:D, Q5:B, Q6:C, Q7:B, Q8:B, Q9:B, Q10:B, Q11:B, Q12:B, Q13:C, Q14:beq=equal, bne=not equal

---

## Classwork Problems (3.17.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | 32-bit Up/Down counter: Q⁺ when Reset=0, Up=1? | Q + 1 |
| 2 | Up/Down counter convenient form: Q⁺ = Q + (2·Up - 1)? | Up=1→+1, Up=0→-1 |
| 3 | 32-bit counter adding 4: Q⁺ = ? | Q + 4 |
| 4 | 16×3 ROM address inputs? | 4 (A,B,C,D) |
| 5 | Byte address of memory word 42? | 42 × 4 = 168 = 0xA8 |
| 6 | Word 42 spans which byte addresses? | 0xA8, 0xA9, 0xAA, 0xAB |
| 7 | Big-endian stores 0xFF223344 at 0xA8: | A8:FF, A9:22, AA:33, AB:44 |
| 8 | Little-endian stores 0xFF223344 at 0xA8: | A8:44, A9:33, AA:22, AB:FF |
| 9 | Byte address of memory word 15? | 15 × 4 = 60 = 0x3C |

---

## High-Yield Unit 3 MCQ Patterns

| Topic | Pattern |
|-------|---------|
| **Addressing Modes** | Register=R-type, Immediate=constant in instr, Base=lw/sw (Base+Offset), PC-Rel=beq/bne ((PC+4)+Off×4), Pseudo-Direct=j/jal (26-bit+PC[31:28]) |
| **Memory Map** | Text@0x00400000, Global@0x10000000 ($gp=0x10008000), Stack@0x7FFFFFFC↓, Heap@0x10010000↑ |
| **Translation Pipeline** | Compile→Assemble(2 pass)→Link→Load; Pass1=addresses+symbols, Pass2=machine code |
| **Global Access** | $gp fixed, offset known at assembly, base addressing |
| **Stack/Heap** | Stack grows DOWN, Heap grows UP |
| **Function Calls** | Args→$a0-$a3, Return→$v0, Call→jal ($ra=PC+4), Return→jr $ra, Preserved=$s0-$s7,$ra,$sp |
| **Branches** | beq=branch if equal, bne=branch if not equal, offset from PC+4 |
| **Loops** | while: beq exit + j loop; for: init→beq exit→body→update→j for |
| **Arrays** | int: base+4i, char: base+i; lbu=zero-extend, lb=sign-extend, sb=store byte |
| **Endianness** | Big: MSB@low addr; Little: LSB@low addr |
| **Parallelism** | Throughput not latency; Spatial=more HW, Temporal=pipelining |
| **Pipeline** | Clock=slowest stage; TP=1/Tc; Latency=N×Tc; Hazards: Data(RAW)=forwarding, Control=prediction, Structural=duplicate HW |
| **Amdahl's Law** | Speedup = 1/[(1-f)+f/s] |
| **Machine Code** | op=0→R-type(check funct); op=35→lw; op=43→sw; op=4→beq; op=2→j; funct: add=32, sub=34, jr=8 |
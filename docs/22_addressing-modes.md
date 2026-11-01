# 22. Addressing Modes — MIPS Operand Location Methods

> **Source:** Unit 3 Slides 3.14.1 | Textbook: Harris & Harris Ch. 6

---

## What is an Addressing Mode?

An **addressing mode** specifies how the CPU locates the operand(s) required to execute an instruction. Operands may be in registers, memory, or within the instruction itself.

**Why Important:**
- Determine operand location
- Influence execution speed and memory usage
- Provide flexibility for constants, variables, arrays, loops, function calls
- Reduce instruction size while improving efficiency

---

## MIPS Addressing Modes (5 Types)

| Mode | Operand Location | Example Instructions |
|------|------------------|---------------------|
| **Register** | CPU Registers | `add $s0, $t2, $t3` |
| **Immediate** | Constant in Instruction | `addi $s0, $s0, 10` |
| **Base (Displacement)** | Memory (Base + Offset) | `lw $t0, 8($sp)` |
| **PC-Relative** | Memory (PC + Offset) | `beq $t0, $0, Loop` |
| **Pseudo-Direct** | Memory (Partial Address) | `j main`, `jal func` |

---

## 1. Register-Only Addressing

**Definition:** Operands stored entirely in CPU registers. No memory access.

**Used By:** All R-type instructions (add, sub, and, or, slt, shifts, jr)

**Format:** `op rd, rs, rt` or `op rd, rt, shamt`

**Example:**
```
add $s0, $t2, $t3
# $s0 = $t2 + $t3
# Source: $t2, $t3 | Destination: $s0
```

**Characteristics:**
- ALU reads operands directly from register file
- Result stored back to register
- **Fastest** addressing mode (registers = fastest storage)
- No memory access during execution

---

## 2. Immediate Addressing

**Definition:** One operand is a 16-bit constant encoded directly in the instruction.

**Used By:** I-type instructions (addi, andi, ori, xori, lui, addiu, slti)

**Format:** `op rt, rs, imm`

**Immediate Handling:**
| Instruction Type | Extension |
|------------------|-----------|
| **Arithmetic** (addi, addiu) | **Sign-extend** to 32 bits |
| **Load/Store** (lw, sw) | **Sign-extend** to 32 bits |
| **Branch** (beq, bne) | **Sign-extend** to 32 bits |
| **Logical** (andi, ori, xori) | **Zero-extend** to 32 bits |
| **lui** | Place in upper 16 bits, lower 16 = 0 |

**Examples:**
```
addi $s4, $t5, -73       # $s4 = $t5 + (-73)  [sign-extended]
ori  $t3, $t7, 0xFF      # $t3 = $t7 | 0x00FF [zero-extended]
lui  $s0, 0x6D5E         # $s0 = 0x6D5E0000
```

**Advantage:** Constant in instruction → no memory access → faster execution

**Applications:** Initialize registers, loop counters, increment/decrement, arithmetic with constants

---

## 3. Base Addressing (Displacement/Indexed)

**Definition:** Memory access using base register + 16-bit signed offset.

**Used By:** Memory instructions — `lw`, `sw`, `lb`, `lbu`, `sb`

**Effective Address Calculation:**
```
Effective Address = Base Register + Sign-Extended Offset
```

**Format:** `op rt, offset(rs)` — reads as "load/store rt from/to memory at rs+offset"

**Examples:**
```
lw  $s4, 72($0)     # EA = $0 + 72 = 72. Load word from addr 72 to $s4
sw  $t2, -25($t1)   # EA = $t1 - 25. Store $t2 to memory 25 bytes before $t1
lw  $t1, 4($s0)     # Load array[1] (int array: $s0=base, offset=4)
```

**Offset Properties:**
- 16-bit signed → range -32768 to +32767 bytes
- Can be positive or negative
- Allows access before/after base address

**Applications:** Arrays, stack variables, structures, dynamic memory

**Key Point:** Base addressing enables efficient memory access with constant offsets known at assembly time.

---

## 4. PC-Relative Addressing

**Definition:** Conditional branches use 16-bit signed offset relative to **PC+4**.

**Used By:** Branch instructions — `beq`, `bne`

**Branch Target Address Formula:**
```
BTA = (PC + 4) + (Sign-Extended Offset × 4)
```

**Why ×4?** MIPS instructions are 4 bytes (word-aligned). Offset counts **instructions**, not bytes.

**Example:**
```
Assembly:
0x10   beq  $t0, $0, else
0x14   addi $v0, $0, 1
0x18   addi $sp, $sp, 8
0x1C   jr   $ra
0x20 else: addi $a0, $a0, -1
0x24       j    factorial

Machine: beq $t0, $0, 3
# offset = 3 (3 instructions from 0x14 to 0x20)
# BTA = (0x10+4) + (3×4) = 0x14 + 0xC = 0x20 ✓
```

**Key Observation:** Immediate field stores **number of instructions to jump**, not byte address.

**Advantage:** Compact (16-bit offset vs 32-bit address); allows forward/backward branching.

---

## 5. Pseudo-Direct Addressing

**Definition:** Jump instructions use 26-bit address field; processor constructs full 32-bit target.

**Used By:** `j` (Jump), `jal` (Jump and Link)

**Jump Target Address Formula:**
```
JTA = { PC+4[31:28], Address[25:0], 00 }
```

**Construction Steps:**
1. Take upper 4 bits of PC+4
2. Append 26-bit address field from instruction
3. Add two trailing 0 bits (word alignment)

**Example:**
```
Assembly:
0x0040005C      j   sum
...
0x004000A0  sum: add $v0, $a0, $a1

Calculation:
JTA = 0x004000A0
26-bit field = 0x00100028
Opcode for j = 000010

Machine: 0x08100028
```

**Why Shift Left by 2?**
- Every MIPS instruction = 4 bytes = 32 bits
- Instruction addresses are **word-aligned** (last 2 bits always `00`)
- These bits omitted from instruction, restored by processor

**Limitation:** Can only jump within same **256 MB region** (upper 4 bits of PC+4 fixed).

---

## Comparison Table

| Aspect | Register | Immediate | Base | PC-Relative | Pseudo-Direct |
|--------|----------|-----------|------|-------------|---------------|
| **Operand** | Register | Constant in instr | Memory | Memory | Memory |
| **Instr Type** | R-type | I-type | I-type (lw/sw) | I-type (beq/bne) | J-type (j/jal) |
| **Address Calc** | None | None | Base + Offset | (PC+4) + Offset×4 | {PC+4[31:28], addr, 00} |
| **Range** | 32 regs | ±32K (sign) / 64K (zero) | ±32K from base | ±128K instructions | 256 MB region |
| **Speed** | Fastest | Fast | Memory access | Memory access | Memory access |

---

## MIPS Instruction Categories by Addressing Mode

| Category | Instructions | Addressing Mode |
|----------|--------------|-----------------|
| **Arithmetic/Logic** | add, sub, and, or, slt, sll, srl, sra | Register |
| **Immediate Arithmetic** | addi, addiu, slti | Immediate |
| **Immediate Logical** | andi, ori, xori | Immediate (zero-extend) |
| **Load Upper** | lui | Immediate (upper 16) |
| **Memory Access** | lw, sw, lb, lbu, sb | Base (Base + Offset) |
| **Conditional Branch** | beq, bne | PC-Relative |
| **Unconditional Jump** | j, jal | Pseudo-Direct |
| **Register Jump** | jr | Register |

---

## Key Formulas (Memorize)

```
Register:        rd = rs op rt
Immediate:       rt = rs op imm
Base (lw/sw):    EA = BaseReg + SignExt(Offset)
PC-Relative:     BTA = (PC + 4) + (SignExt(Offset) × 4)
Pseudo-Direct:   JTA = {PC+4[31:28], Addr[25:0], 00}

Offset ranges:
  Immediate (sign):     -32768 to +32767
  Immediate (zero):     0 to 65535
  Base offset:          -32768 to +32767 bytes
  Branch offset:        -32768 to +32767 instructions (×4 bytes)
  Jump address:         26 bits → 256 MB region
```

---

## MCQ Patterns

1. **Register-only** — used by R-type (add, sub, jr); fastest
2. **Immediate** — constant in instruction; addi=sign-extend, andi=zero-extend
3. **Base addressing** — lw/sw; EA = Base + SignExt(Offset)
4. **PC-relative** — beq/bne; BTA = (PC+4) + Offset×4; offset counts instructions
5. **Pseudo-direct** — j/jal; 26-bit field + PC+4[31:28] + 00; 256 MB range
6. **No nori** — use ori + nor $zero
7. **lui** — loads upper 16 bits, clears lower 16
8. **Shift left 2** — word alignment (instructions=4 bytes)
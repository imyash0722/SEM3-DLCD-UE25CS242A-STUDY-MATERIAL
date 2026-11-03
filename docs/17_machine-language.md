# 21. Machine Language — Instruction Encoding, Decoding, Stored Program

> **Source:** Unit 3 Slides 3.9.1 | Textbook: Harris & Harris Ch. 6

---

## MIPS Machine Language Formats

All MIPS instructions are **32 bits (4 bytes)**. Word addresses divisible by 4.

### R-Type Format
```
31          25 24    20 19    15 14    10 9     5 4        0
┌─────────────┬───────┬───────┬───────┬───────┬───────────┐
│   op (6)    │ rs(5) │ rt(5) │ rd(5) │shamt(5)│ funct(6) │
└─────────────┴───────┴───────┴───────┴───────┴───────────┘
```
- **op = 0** for all R-type
- **funct** determines exact operation

### I-Type Format
```
31          25 24    20 19    15 14                0
┌─────────────┬───────┬───────┬─────────────────────┐
│   op (6)    │ rs(5) │ rt(5) │       imm(16)       │
└─────────────┴───────┴───────┴─────────────────────┘
```
- rs = source register (base for load/store)
- rt = destination (load) or source (store)
- imm = 16-bit immediate (sign-extended for arithmetic/load/store/branch, zero-extended for logical)

### J-Type Format
```
31          25 24                              0
┌─────────────┬─────────────────────────────────┐
│   op (6)    │          addr(26)               │
└─────────────┴─────────────────────────────────┘
```
- 26-bit address field
- Shifted left 2 (×4) for word alignment
- Combined with PC+4[31:28] for full 32-bit target

---

## Opcode and Funct Values (Key Subset)

| Instruction | op | funct | Format |
|-------------|-----|-------|--------|
| **add** | 0 | 32 (0x20) | R |
| **sub** | 0 | 34 (0x22) | R |
| **and** | 0 | 36 (0x24) | R |
| **or** | 0 | 37 (0x25) | R |
| **xor** | 0 | 38 (0x26) | R |
| **nor** | 0 | 39 (0x27) | R |
| **slt** | 0 | 42 (0x2A) | R |
| **sll** | 0 | 0 | R |
| **srl** | 0 | 2 | R |
| **sra** | 0 | 3 | R |
| **jr** | 0 | 8 | R |
| **addi** | 8 (0x08) | — | I |
| **addiu** | 9 (0x09) | — | I |
| **andi** | 12 (0x0C) | — | I |
| **ori** | 13 (0x0D) | — | I |
| **xori** | 14 (0x0E) | — | I |
| **lw** | 35 (0x23) | — | I |
| **sw** | 43 (0x2B) | — | I |
| **beq** | 4 | — | I |
| **bne** | 5 | — | I |
| **slti** | 10 (0x0A) | — | I |
| **lui** | 15 (0x0F) | — | I |
| **j** | 2 | — | J |
| **jal** | 3 | — | J |

---

## Encoding Examples

### Example 1: `add $t0, $s4, $s5`
- $t0 = 8, $s4 = 20, $s5 = 21
- op=0, rs=20, rt=21, rd=8, shamt=0, funct=32
- Binary: `000000 10100 10101 01000 00000 100000`
- Hex: **0x02954020**

### Example 2: `lw $s3, -24($s4)`
- $s3 = 19, $s4 = 20
- op=35 (0x23), rs=20, rt=19, imm=-24 = 0xFFE8
- Binary: `100011 10100 10011 1111111111101000`
- Hex: **0x8D93FFE8**

### Example 3: `addi $s7, $s1, -15`
- $s7 = 23, $s1 = 17
- op=8 (0x08), rs=17, rt=23, imm=-15 = 0xFFF1
- Binary: `001000 10001 10111 1111111111110001`
- Hex: **0x223FFFF1**

### Example 4: `j sum` (PC=0x0040005C, sum=0x004000A0)
- op=2, addr = 0x004000A0 >> 2 = 0x00100028
- Binary: `000010 00000100000000000000101000`
- Hex: **0x08100028**

---

## Decoding Machine Code

### Strategy
1. **Read opcode** (bits 31-26)
2. **If op = 0** → R-type → inspect **funct** (bits 5-0)
3. **If op ≠ 0** → Use opcode to identify I-type or J-type
4. **Extract register fields** → map to register names ($0-$31)
5. **Interpret immediate** → signed (addi, lw, sw, beq, bne) or unsigned (andi, ori, xori, lui)

### Worked Example: `0x223FFFF1`
```
Binary: 001000 10001 10111 1111111111110001
op = 001000₂ = 8 → addi (I-type)
rs = 10001₂ = 17 → $s1
rt = 10111₂ = 23 → $s7
imm = 1111111111110001₂ = -15 (sign-extended)
Result: addi $s7, $s1, -15
```

### Worked Example: `0x02F34022`
```
Binary: 000000 10111 10011 01000 00000 100010
op = 0 → R-type
funct = 100010₂ = 34 → sub
rs = 10111₂ = 23 → $s7
rt = 10011₂ = 19 → $s3
rd = 01000₂ = 8 → $t0
Result: sub $t0, $s7, $s3
```

---

## Stored Program Concept

### Machine Code
- Executed directly by CPU
- Binary/hex format (e.g., `0x8C0A0020`)
- Difficult for humans

### Assembly Code
- Human-readable mnemonics (e.g., `lw $t2, 32($0)`)
- Must be **assembled** into machine code

### Program Counter (PC)
- Special register holding **address of next instruction**
- Incremented by 4 after each fetch (MIPS 32-bit = 4 bytes)
- Modified by branch/jump instructions

### Memory Organization
- **Both instructions and data in same memory** (Von Neumann)
- Instructions fetched from text segment
- Data accessed from data/stack/heap segments

---

## Register Reference (for Encoding)

| Number | Name | Number | Name | Number | Name | Number | Name |
|--------|------|--------|------|--------|------|--------|------|
| 0 | $zero | 8 | $t0 | 16 | $s0 | 24 | $t8 |
| 1 | $at | 9 | $t1 | 17 | $s1 | 25 | $t9 |
| 2 | $v0 | 10 | $t2 | 18 | $s2 | 26 | $k0 |
| 3 | $v1 | 11 | $t3 | 19 | $s3 | 27 | $k1 |
| 4 | $a0 | 12 | $t4 | 20 | $s4 | 28 | $gp |
| 5 | $a1 | 13 | $t5 | 21 | $s5 | 29 | $sp |
| 6 | $a2 | 14 | $t6 | 22 | $s6 | 30 | $fp/$s8 |
| 7 | $a3 | 15 | $t7 | 23 | $s7 | 31 | $ra |

---

## Key Formulas (Memorize)

```
R-type:  op(6)|rs(5)|rt(5)|rd(5)|shamt(5)|funct(6)    op=0
I-type:  op(6)|rs(5)|rt(5)|imm(16)
J-type:  op(6)|addr(26)                               addr = target>>2

Branch target:  BTA = (PC+4) + (signExt(imm) × 4)
Jump target:    JTA = {PC+4[31:28], addr[25:0], 00}

Hex conversion:  4 bits → 1 hex digit
0x8C0A0020 = 10001100 00001010 00000000 00100000
```

---

## MCQ Patterns

1. **Opcode identification** — op=0 → R-type (check funct); op=35 → lw; op=43 → sw; op=4 → beq; op=5 → bne; op=2 → j; op=3 → jal
2. **R-type funct codes** — add=32, sub=34, and=36, or=37, slt=42, sll=0, jr=8
3. **I-type opcodes** — addi=8, andi=12, ori=13, lw=35, sw=43, beq=4, bne=5, lui=15
4. **J-type opcodes** — j=2, jal=3
5. **Immediate sign** — arithmetic/load/store/branch = sign-extend; logical = zero-extend
6. **Register mapping** — know $t0=8, $s0=16, $a0=4, $v0=2, $ra=31, $sp=29
7. **Machine code → assembly** — extract fields, interpret by format
8. **Jump address calc** — shift 26-bit addr left 2, combine with PC+4[31:28]
8. **Branch offset** — offset = (target - (PC+4)) / 4
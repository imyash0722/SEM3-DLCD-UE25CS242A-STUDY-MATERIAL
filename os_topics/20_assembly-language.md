# 20. Assembly Language — MIPS Instructions, Registers, Pseudoinstructions

> **Source:** Unit 3 Slides 3.7.1, 3.11.1 | Textbook: Harris & Harris Ch. 6

---

## MIPS Registers (32 General Purpose: x0–x31 / $0–$31)

| Register | Name | Use | Preserved? |
|----------|------|-----|------------|
| $0 ($zero) | zero | Hardwired 0 | N/A |
| $1 ($at) | assembler temp | Reserved for assembler | No |
| $2–$3 ($v0–$v1) | return values | Function results | No |
| $4–$7 ($a0–$a3) | arguments | First 4 function args | No |
| $8–$15 ($t0–$t7) | temporaries | Caller-saved (non-preserved) | **No** |
| $16–$23 ($s0–$s7) | saved | Callee-saved (preserved) | **Yes** |
| $24–$25 ($t8–$t9) | temporaries | Caller-saved | No |
| $26–$27 ($k0–$k1) | kernel | Reserved for OS | No |
| $28 ($gp) | global pointer | Middle of global data | Yes |
| $29 ($sp) | stack pointer | Top of stack | Yes |
| $30 ($fp/$s8) | frame pointer | Stack frame base | Yes |
| $31 ($ra) | return address | Function return address | Yes |

**Key:** Callee must save/restore `$s0–$s7`, `$ra`, `$sp`, `$fp` if used. Caller saves `$t0–$t9`, `$a0–$a3`, `$v0–$v1`.

---

## Instruction Formats

### R-Type (Register)
```
op(6) | rs(5) | rt(5) | rd(5) | shamt(5) | funct(6)
```
- 3 register operands (rs, rt, rd)
- ALU ops: add, sub, and, or, xor, nor, slt
- Shifts: sll, srl, sra (shamt = shift amount)
- Variable shifts: sllv, srlv, srav (rs = shift amount)
- jr (jump register)

### I-Type (Immediate)
```
op(6) | rs(5) | rt(5) | imm(16)
```
- 2 registers + 16-bit immediate
- Arithmetic: addi, addiu
- Logical: andi, ori, xori (zero-extend); addi/lw/sw (sign-extend)
- Load/Store: lw, sw, lb, lbu, sb
- Branch: beq, bne (PC-relative)

### J-Type (Jump)
```
op(6) | addr(26)
```
- 26-bit address (shifted left 2)
- Jump: j, jal

---

## Arithmetic Instructions

| Instruction | Format | Operation | Notes |
|-------------|--------|-----------|-------|
| `add rd, rs, rt` | R | rd = rs + rt | Overflow trap |
| `addu rd, rs, rt` | R | rd = rs + rt | No overflow trap |
| `sub rd, rs, rt` | R | rd = rs - rt | Overflow trap |
| `subu rd, rs, rt` | R | rd = rs - rt | No overflow trap |
| `addi rt, rs, imm` | I | rt = rs + imm | Sign-extended, overflow trap |
| `addiu rt, rs, imm` | I | rt = rs + imm | Sign-extended, no overflow |

---

## Logical Instructions

| Instruction | Format | Operation | Extension |
|-------------|--------|-----------|-----------|
| `and rd, rs, rt` | R | rd = rs & rt | — |
| `or rd, rs, rt` | R | rd = rs \| rt | — |
| `xor rd, rs, rt` | R | rd = rs ^ rt | — |
| `nor rd, rs, rt` | R | rd = ~(rs \| rt) | — |
| `andi rt, rs, imm` | I | rt = rs & imm | **Zero-extend** |
| `ori rt, rs, imm` | I | rt = rs \| imm | **Zero-extend** |
| `xori rt, rs, imm` | I | rt = rs ^ imm | **Zero-extend** |

**No `nori`** — use `ori` + `nor` with `$zero`:
```
ori $t0, $s1, 0x00FF
nor $t0, $t0, $zero  # $t0 = ~($s1 | 0x00FF)
```

---

## Shift Instructions

| Instruction | Type | Operation | Fill Bits | Use |
|-------------|------|-----------|-----------|-----|
| `sll rd, rt, shamt` | R | rd = rt << shamt | 0s on right | Multiply by 2ᴺ |
| `srl rd, rt, shamt` | R | rd = rt >> shamt | 0s on left | Unsigned / bit extract |
| `sra rd, rt, shamt` | R | rd = rt >>> shamt | **Sign bit** | Signed divide by 2ᴺ |

**Variable Shifts** (amount in lower 5 bits of rs):
| Instruction | Type | Syntax | Notes |
|-------------|------|--------|-------|
| `sllv rd, rt, rs` | R | rd = rt << rs[4:0] | shamt=0 |
| `srlv rd, rt, rs` | R | rd = rt >> rs[4:0] | shamt=0 |
| `srav rd, rt, rs` | R | rd = rt >>> rs[4:0] | shamt=0 |

---

## Generating Constants

### 16-bit Constant
```
addi $s0, $0, 0x4F3C   # $s0 = 0x00004F3C
```

### 32-bit Constant (lui + ori)
```
lui  $s0, 0x6D5E       # $s0 = 0x6D5E0000
ori  $s0, $s0, 0x4F3C  # $s0 = 0x6D5E4F3C
```

---

## Multiplication & Division

| Instruction | Result Location | Notes |
|-------------|-----------------|-------|
| `mult rs, rt` | HI:LO = 64-bit product | HI=upper 32, LO=lower 32 |
| `multu rs, rt` | HI:LO = 64-bit product | Unsigned |
| `div rs, rt` | LO=quotient, HI=remainder | Signed |
| `divu rs, rt` | LO=quotient, HI=remainder | Unsigned |
| `mul rd, rs, rt` | rd = rs × rt (32-bit) | Low 32 bits only |
| `mfhi rd` | rd = HI | Move from HI |
| `mflo rd` | rd = LO | Move from LO |

**Example:** `$s0=20, $s1=6` → div gives mflo $t0 = 3 (quotient) and mfhi $t1 = 2 (remainder).

---

## Load/Store Instructions

| Instruction | Format | Operation | Notes |
|-------------|--------|-----------|-------|
| `lw rt, offset(rs)` | I | rt = Mem[rs + offset] | Sign-extend offset |
| `sw rt, offset(rs)` | I | Mem[rs + offset] = rt | Sign-extend offset |
| `lb rt, offset(rs)` | I | rt = sign-extend(Mem[rs+offset]) | Byte load |
| `lbu rt, offset(rs)` | I | rt = zero-extend(Mem[rs+offset]) | Unsigned byte |
| `sb rt, offset(rs)` | I | Mem[rs+offset] = rt[7:0] | Byte store |

---

## Branch Instructions (PC-Relative)

| Instruction | Format | Condition | Target |
|-------------|--------|-----------|--------|
| `beq rs, rt, label` | I | rs == rt | PC+4 + (imm×4) |
| `bne rs, rt, label` | I | rs != rt | PC+4 + (imm×4) |
| `slt rd, rs, rt` | R | rd = (rs < rt) ? 1 : 0 | Magnitude compare |

**Branch Target Address:**
```
BTA = (PC + 4) + (SignExtendedOffset × 4)
```

---

## Jump Instructions

| Instruction | Format | Target Calculation |
|-------------|--------|-------------------|
| `j label` | J | JTA = {PC+4[31:28], addr[25:0], 00} |
| `jal label` | J | $ra = PC+4; JTA = {PC+4[31:28], addr[25:0], 00} |
| `jr rs` | R | PC = rs |

**Pseudo-Direct Addressing:**
- 26-bit address field → shifted left 2 → combined with upper 4 bits of PC+4
- Allows jumps within 256 MB region

---

## High-Level Constructs in MIPS

### If Statement
```c
if (i == j) f = g + h;
f = f - i;
```
```mips
bne  $s3, $s4, L1      # if i != j, skip
add  $s0, $s1, $s2     # f = g + h
L1:  sub  $s0, $s0, $s3 # f = f - i
```

### If-Else Statement
```c
if (i == j) f = g + h;
else f = f - i;
```
```mips
bne  $s3, $s4, L1      # if i != j, go to else
add  $s0, $s1, $s2     # f = g + h
j    done              # skip else
L1:  sub  $s0, $s0, $s3 # f = f - i
done:
```

### While Loop
```c
while (pow != 128) {
  pow = pow * 2;
  x = x + 1;
}
```
```mips
while: beq  $s0, $t0, done   # if pow == 128, exit
       sll  $s0, $s0, 1      # pow *= 2
       addi $s1, $s1, 1      # x++
       j    while
done:
```

### For Loop
```c
for (i = 0; i != 10; i++) sum = sum + i;
```
```mips
addi $s1, $0, 0       # sum = 0
add  $s0, $0, $0      # i = 0
addi $t0, $0, 10      # limit = 10
for:  beq  $s0, $t0, done
      add  $s1, $s1, $s0
      addi $s0, $s0, 1
      j    for
done:
```

### Array Access
```c
int array[5];
array[i] = array[i] * 8;
```
```mips
sll  $t0, $s1, 2      # $t0 = i × 4
add  $t0, $t0, $s0    # address of array[i]
lw   $t1, 0($t0)      # load array[i]
sll  $t1, $t1, 3      # × 8
sw   $t1, 0($t0)      # store
```

### Character Array (bytes)
```c
for (i = 0; i != 10; i++)
  chararray[i] = chararray[i] - 32;  // lowercase to uppercase
```
```mips
addi $s1, $0, 0       # i = 0
addi $t0, $0, 10
loop:
  beq  $t0, $s1, done
  add  $t1, $s1, $s0  # address = base + i (1 byte each)
  lb   $t2, 0($t1)    # load byte
  addi $t2, $t2, -32  # 'a'(0x61) - 0x20 = 'A'(0x41)
  sb   $t2, 0($t1)    # store byte
  addi $s1, $s1, 1
  j    loop
done:
```

---

## Function Calls

### Caller/Callee Convention
| Category | Registers | Responsibility |
|----------|-----------|----------------|
| **Arguments** | $a0–$a3 | Caller places args |
| **Return** | $v0–$v1 | Callee places result |
| **Preserved** | $s0–$s7, $ra, $sp | Callee saves if used |
| **Non-preserved** | $t0–$t9, $a0–$a3, $v0–$v1 | Caller saves if needed |

### Call Sequence
```mips
# Caller
addi $a0, $0, 2     # arg1
addi $a1, $0, 3     # arg2
jal  diffofsums     # $ra = PC+4; jump
add  $s0, $v0, $0   # save return value

# Callee (diffofsums)
add  $t0, $a0, $a1
add  $t1, $a2, $a3
sub  $s0, $t0, $t1
add  $v0, $s0, $0   # return value
jr   $ra            # return
```

### Stack Frame (Callee-saved registers)
```mips
# Prologue
addi $sp, $sp, -12   # allocate 3 words
sw   $s0, 8($sp)
sw   $t0, 4($sp)
sw   $t1, 0($sp)

# ... function body ...

# Epilogue
lw   $t1, 0($sp)
lw   $t0, 4($sp)
lw   $s0, 8($sp)
addi $sp, $sp, 12    # deallocate
jr   $ra
```

### Recursive Factorial
```mips
factorial:
  addi $sp, $sp, -8
  sw   $a0, 4($sp)   # save n
  sw   $ra, 0($sp)   # save return addr
  addi $t0, $0, 2
  slt  $t0, $a0, $t0 # n < 2?
  beq  $t0, $0, else
  addi $v0, $0, 1    # base case: return 1
  addi $sp, $sp, 8
  jr   $ra
else: addi $a0, $a0, -1  # n-1
  jal  factorial     # recursive call
  lw   $ra, 0($sp)
  lw   $a0, 4($sp)   # restore n
  addi $sp, $sp, 8
  mul  $v0, $a0, $v0 # n * factorial(n-1)
  jr   $ra
```

---

## Key Formulas (Memorize)

```
R-type:     op(6)|rs(5)|rt(5)|rd(5)|shamt(5)|funct(6)
I-type:     op(6)|rs(5)|rt(5)|imm(16)
J-type:     op(6)|addr(26)
Branch:     BTA = (PC+4) + (offset×4)
Jump:       JTA = {PC+4[31:28], addr[25:0], 00}
Array addr: base + 4×i (int), base + i (char)
32-bit const: lui upper16 + ori lower16
Function:   Args→$a0-$a3, Return→$v0, Call→jal, Return→jr $ra
Stack:      $sp grows DOWN (subtract to allocate)
```

---

## MCQ Patterns

1. **Register conventions** — $s0–$s7 preserved, $t0–$t9 non-preserved
2. **Branch vs Jump** — beq/bne=PC-relative, j/jal=pseudo-direct
3. **Immediate extension** — addi/lw/sw=sign-extend, andi/ori/xori=zero-extend
4. **Shift right** — srl=0-fill, sra=sign-fill
5. **Function call** — jal saves $ra=PC+4; jr $ra returns
6. **Stack** — grows downward (subtract), $sp points to top
7. **Array indexing** — int: base+4i, char: base+i
8. **Multiplication** — mult→HI:LO (64-bit), mul→32-bit result
8. **Division** — div→LO=quotient, HI=remainder
9. **Pseudoinstructions** — lui+ori for 32-bit constants
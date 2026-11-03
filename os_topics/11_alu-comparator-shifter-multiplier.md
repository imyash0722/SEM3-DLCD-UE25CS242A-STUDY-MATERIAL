# 11. ALU, Comparators, Shifters & Multipliers

> **Source:** Harris & Harris Ch. 5, Unit 2 Slides 88–103

---

## ALU (Arithmetic Logic Unit)

### 32-bit ALU Operations (F₂:₀)
| F₂ | F₁ | F₀ | Operation |
|----|----|----|-----------|
| 0  | 0  | 0  | A AND B   |
| 0  | 0  | 1  | A OR B    |
| 0  | 1  | 0  | A + B     |
| 0  | 1  | 1  | (unused)  |
| 1  | 0  | 0  | A AND ~B  |
| 1  | 0  | 1  | A OR ~B   |
| 1  | 1  | 0  | A - B     |
| 1  | 1  | 1  | SLT       |

### ALU Structure
- Multiple operation units in parallel
- **MUX selects output** based on F₂:₀
- **F₂=1** → inverters on B + Cin=1 (for SUB/SLT)

### SLT (Set Less Than)
- Computes `A - B` using subtractor
- If result negative (sign bit = 1) → A < B
- Output = sign bit zero-extended (0x00000001 or 0x00000000)
- **Example:** A=25, B=32 → 25-32=-7 → S₃₁=1 → Y=1

---

## Comparators

### Equality (A == B)
- **Per bit:** XNOR (Aᵢ ⊙ Bᵢ = 1 if equal)
- **Overall:** N-input AND of all XNORs
- `Eq = Π(Aᵢ ⊙ Bᵢ)`

### Less Than (A < B) — Unsigned
- Compare MSB to LSB
- First differing bit decides
- Can use subtractor: A < B iff (A-B) sign = 1

### Less Than (A < B) — Signed (2's comp)
- Same as unsigned if no overflow
- With overflow: sign bit inverted
- `V = C_in,MSB ⊕ C_out,MSB`

---

## Shifters

### Types
| Shift | Left (<<) | Right (>>) | Notes |
|-------|-----------|------------|-------|
| **Logical** | Fill 0 | Fill 0 | Unsigned |
| **Arithmetic** | Fill 0 | Replicate MSB | Signed (preserves sign) |
| **Rotate** | Circular | Circular | Bits wrap around |

### Examples (11001)
| Operation | Result |
|-----------|--------|
| Logical >> 2 | 00110 |
| Arithmetic >> 2 | 11110 (sign=1) |
| Rotate ROR 2 | 01110 |
| Logical << 2 | 00100 |
| Arithmetic << 2 | 00100 |
| Rotate ROL 2 | 00111 |

### Barrel Shifter
- **Log₂N stages** of 2:1 MUXes
- Stage i shifts by 2ⁱ positions
- **16-bit:** 4 stages (1, 2, 4, 8)
- **Delay:** O(log N)

### Shifts as Multiply/Divide
- `A << N = A × 2ᴺ`
- `A >>> N = A ÷ 2ᴺ` (arithmetic, signed)

---

## Multipliers

### 4×4 Array Multiplier
- Partial products: each multiplier bit × multiplicand
- Shifted and summed
- **Result:** N+M bits for N×M multiply

### 32×32 Multiplier
- **Product size:** 64 bits

---

## Dividers

### 4×4 Divider Algorithm
```
R' = 0
for i = N-1 downto 0:
    R = {R' << 1, Aᵢ}
    D = R - B
    if D < 0:  Qᵢ = 0, R' = R
    else:      Qᵢ = 1, R' = D
```

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| ALU F₂=1 means? | Invert B, Cin=1 (subtract) |
| SLT implementation? | A-B, take sign bit |
| Equality comparator? | N XNORs + N-input AND |
| Logical vs Arithmetic right shift? | Logical=0-fill, Arithmetic=sign-fill |
| 11001 >>> 2? | 11110 |
| 16-bit barrel shifter stages? | 4 (log₂16) |
| 32×32 multiplier product bits? | 64 |

---

## Exam-Relevant MCQ Patterns

1. **ALU control decode** — F₂:₀ mapping (Q70, Q79)
2. **SLT uses sign bit** — of A-B result (Q23, Q86)
3. **Equality = XNOR + AND** (Q18, Q87)
4. **Logical vs Arithmetic shift** — MSB fill (Q19, Q20, Q80)
5. **Barrel shifter stages** — log₂N (Q21)
6. **Multiply bits** — N+M for N×M (Q22, Q82)
7. **Shift = multiply/divide by 2ᴺ** (Q77)
8. **Subtraction Cin=1** (Q26, Q88)
9. **CLA vs Prefix for wide adders** — log delay (Q84, Q94)
10. **Overflow in signed add** — two positives → negative (Q81)

---

## Key Formulas (Memorize)

```
Equality:  Eq = Π(Aᵢ ⊙ Bᵢ)
SLT:       Y = sign(A - B) zero-extended
Logical >>:  fill 0
Arithmetic >>: replicate MSB
<< N:       × 2ᴺ
>>> N:      ÷ 2ᴺ (signed)
Barrel stages: log₂N
Multiply N×M: N+M bits
```
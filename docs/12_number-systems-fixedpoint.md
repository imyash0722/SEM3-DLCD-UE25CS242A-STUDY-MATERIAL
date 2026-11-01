# 12. Number Systems — Fixed-Point & Signed Representations

> **Source:** Unit 2 Slides 111–130 | Textbook: Harris & Harris Ch. 1

---

## Binary Number Representations

| Type | Range | Notes |
|------|-------|-------|
| **Unsigned** | 0 to 2ᴺ-1 | Positive only |
| **Sign/Magnitude** | -(2ᴺ⁻¹-1) to +(2ᴺ⁻¹-1) | MSB=sign, two zeros |
| **One's Complement** | -(2ᴺ⁻¹-1) to +(2ᴺ⁻¹-1) | Invert bits, two zeros |
| **Two's Complement** | -2ᴺ⁻¹ to +(2ᴺ⁻¹-1) | **Preferred** — unique zero, simple add/sub |

---

## Two's Complement (Memorize!)

### Negation Algorithm
```
1. Invert all bits (1's complement)
2. Add 1 to LSB
```

**Example: -5 in 8-bit**
- +5 = 0000 0101
- Invert = 1111 1010
- Add 1 = 1111 1011 = 0xFB

### Range (N bits)
- **Min:** -2ᴺ⁻¹ (e.g., -128 for 8-bit)
- **Max:** +2ᴺ⁻¹ - 1 (e.g., +127 for 8-bit)
- **One extra negative** because zero is unique

### Why 2's Complement Wins
- Single zero representation
- Addition/subtraction identical hardware
- No end-around carry needed

---

## Fixed-Point Numbers

### Format: Q-format (e.g., Q4.4 = 4 integer, 4 fraction bits)
**Binary point is IMPLIED** — not stored

### Example: 4 integer + 4 fraction bits
```
Binary:    0110.1100
           └┬┘ └┬┘
         int frac
Value:  6 + 0.5 + 0.25 = 6.75
```

### Fractional Weights
| Position | Weight |
|----------|--------|
| 2⁻¹ | 0.5 |
| 2⁻² | 0.25 |
| 2⁻³ | 0.125 |
| 2⁻⁴ | 0.0625 |

### Conversions

**Decimal → Fixed-Point (4.4):**
- 7.5 → 7 = 0111, 0.5 = 1000 → **0111.1000**
- 3.625 → 3 = 0011, 0.625 = 1010 → **0011.1010**
- -7.5 (2's comp): +7.5=0111.1000 → invert=1000.0111 → +1=**1000.1000**

**Fixed-Point → Decimal:**
- 0011.1010 = 3 + 0.5 + 0.125 = **3.625**
- 1000.1000 (2's comp, negative) → invert=0111.0111 → +1=0111.1000 = **-7.5**

---

## Fixed-Point Arithmetic
- **Addition:** Same as integer (align binary points)
- **Multiplication:** Qm.n × Qp.q = Q(m+p).(n+q) — double fraction bits
- **Overflow:** Same as integer

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| 8-bit 2's comp range? | -128 to +127 |
| Sign/Magnitude zero? | +0=00000000, -0=10000000 |
| 2's comp zero? | Only 00000000 |
| Negate 2's comp? | Invert + add 1 |
| 3.625 in Q4.4? | 0011.1010 |
| -7.5 in Q4.4 (2's comp)? | 1000.1000 |
| Q4.4 smallest fraction? | 2⁻⁴ = 0.0625 |

---

## Exam-Relevant MCQ Patterns

1. **2's complement range** — -2ᴺ⁻¹ to 2ᴺ⁻¹-1 (Q24)
2. **Negation procedure** — invert + 1 (Q27, Q113)
3. **Fixed-point conversion** — integer + fraction parts (Q26, Q27, Q93-Q112)
4. **Binary point implied** — not stored, must be agreed (Q91, Q110, Q115)
5. **Smallest fractional weight** — 2⁻ⁿ for n fraction bits (Q114)
6. **Sign/Magnitude vs 2's comp** — sign bit flip vs invert+1 (Q104)
7. **Fixed-point addition** — align points, add as integers (Q109)
8. **Why 2's comp preferred** — same adder for +/- (Q106)

---

## Key Formulas (Memorize)

```
2's Complement N-bit:  [-2ᴺ⁻¹, 2ᴺ⁻¹-1]
Negation:  invert + 1
Qm.n format:  m integer bits, n fraction bits
Fraction weight:  2⁻¹, 2⁻², ..., 2⁻ⁿ
Fixed-point add:  align binary points, integer add
Multiply Qm.n × Qp.q:  Q(m+p).(n+q)
```
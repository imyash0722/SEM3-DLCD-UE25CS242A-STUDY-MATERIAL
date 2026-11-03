# 13. Floating-Point — IEEE 754 Single/Double Precision

> **Source:** Harris & Harris Ch. 1, Unit 2 Slides 120–138

---

## IEEE 754 Single Precision (32-bit)

```
| S |    E (8 bits)    |      F (23 bits)       |
| 31| 30 ────────── 23 | 22 ──────────────── 0 |
```

| Field | Bits | Description |
|-------|------|-------------|
| **Sign (S)** | 1 | 0=positive, 1=negative |
| **Exponent (E)** | 8 | Biased: E = e + 127 |
| **Fraction (F)** | 23 | Significand = 1.F (implicit leading 1) |

**Value:** `(-1)ˢ × 1.F × 2ᴱ⁻¹²⁷`

---

## Encoding Steps (Decimal → IEEE 754)

### Example: 228₁₀
1. **Binary:** 228 = 11100100₂
2. **Normalize:** 1.11001₂ × 2⁷
3. **Sign:** 0 (positive)
4. **Exponent:** 7 + 127 = 134 = 10000110₂
5. **Fraction:** 11001 + zeros = 11001000000000000000000
6. **Result:** `0 10000110 11001000000000000000000` = **0x43640000**

### Example: -58.25₁₀
1. **Binary:** 58.25 = 111010.01₂
2. **Normalize:** 1.1101001₂ × 2⁵
3. **Sign:** 1 (negative)
4. **Exponent:** 5 + 127 = 132 = 10000100₂
5. **Fraction:** 1101001 + zeros
6. **Result:** `1 10000100 11010010000000000000000` = **0xC2690000**

---

## Special Values

| Value | Exponent | Fraction | Notes |
|-------|----------|----------|-------|
| **±0** | 00000000 | 000...0 | S=0/1 |
| **Denormalized** | 00000000 | ≠0 | 0.F × 2⁻¹²⁶ |
| **±∞** | 11111111 | 000...0 | S=0/1 |
| **NaN** | 11111111 | ≠0 | Not a Number |
| **Normalized** | 00000001–11111110 | any | 1.F × 2ᴱ⁻¹²⁷ |

---

## Double Precision (64-bit)
| Field | Bits |
|-------|------|
| Sign | 1 |
| Exponent | 11 (bias = 1023) |
| Fraction | 52 |
**Value:** `(-1)ˢ × 1.F × 2ᴱ⁻¹⁰²³`

---

## Floating-Point Addition (8 Steps)

1. **Extract** sign, exponent, fraction
2. **Prepend** implicit leading 1 → mantissa (1.F)
3. **Compare** exponents
4. **Shift** smaller mantissa right by |E₁-E₂|
5. **Add** mantissas
6. **Normalize** result (shift if ≥2 or <1)
7. **Round** (to 23 fraction bits)
8. **Assemble** back to IEEE format

### Example: 0x3FC00000 + 0x40500000
| Step | N1 (1.5) | N2 (3.25) |
|------|----------|-----------|
| 1. Extract | S=0, E=127, F=.1 | S=0, E=128, F=.101 |
| 2. Mantissa | 1.1 | 1.101 |
| 3. Compare | 127 vs 128 | diff = 1 |
| 4. Shift N1 | 1.1 >> 1 = 0.11 | (×2¹) |
| 5. Add | 0.11 + 1.101 = 10.011 | (×2¹) |
| 6. Normalize | 1.0011 × 2² | |
| 7. Round | fits 23 bits | |
| 8. Result | S=0, E=129, F=0011... | **0x40980000** |

---

## Rounding Modes
| Mode | Behavior |
|------|----------|
| **To nearest** | Round to closest (ties to even) |
| **Toward zero** | Truncate |
| **Down** | Toward -∞ |
| **Up** | Toward +∞ |

---

## Precision
| Format | Significant Digits (decimal) |
|--------|------------------------------|
| Single (32-bit) | ~7 |
| Double (64-bit) | ~15 |

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Single precision bias? | 127 |
| Double precision bias? | 1023 |
| Implicit leading bit? | Always 1 for normalized |
| +∞ encoding? | S=0, E=255, F=0 |
| NaN encoding? | E=255, F≠0 |
| Denormalized? | E=0, F≠0 (value = 0.F × 2⁻¹²⁶) |
| FP add step 2? | Prepend implicit 1 |

---

## Exam-Relevant MCQ Patterns

1. **Single precision layout** — 1/8/23 bits (Q28)
2. **Exponent bias** — 127 (Q29, Q120)
3. **Implicit leading 1** — always 1 for normalized (Q30)
4. **+∞ encoding** — E=all 1s, F=0 (Q31)
5. **NaN encoding** — E=all 1s, F≠0 (Q32)
6. **Denormalized** — E=0, F≠0 (Q33)
7. **Decimal → IEEE encoding** — normalize, bias, drop leading 1 (Q34, Q35, Q122-Q131)
8. **FP add step order** — extract→prepend 1→compare→shift→add→normalize→round→assemble (Q36, Q37)
9. **Shift smaller mantissa** — align exponents (Q37)
10. **Excess-127 NOT fixed-point** — it's floating-point exponent bias (Q38, Q116)

---

## Key Formulas (Memorize)

```
Single:    S(1) | E(8, bias=127) | F(23)
Double:    S(1) | E(11, bias=1023) | F(52)
Value:     (-1)ˢ × 1.F × 2ᴱ⁻ᵇⁱᵃˢ
Normalize: 1.xxxx × 2ᵉ
Denorm:    0.F × 2⁻¹²⁶ (single)
+∞:        E=255, F=0
NaN:       E=255, F≠0
FP Add:    1)Extract 2)Prepend 1 3)Compare 4)Shift 5)Add 6)Normalize 7)Round 8)Assemble
```
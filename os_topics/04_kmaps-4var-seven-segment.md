# 04. K-Maps (4-Variable) & Seven-Segment Decoder

> **Source:** Harris & Harris Ch. 2, Unit 1 Slides 94–123

---

## 4-Variable K-Map Structure

```
        CD
       00  01  11  10
AB 00  m0  m1  m3  m2
AB 01  m4  m5  m7  m6
AB 11  m12 m13 m15 m14
AB 10  m8  m9  m11 m10
```

### Critical Properties

1. **Rows & Columns:** Gray code (00, 01, 11, 10) — adjacent differ by 1 bit
2. **Wrap-Around:** **Left↔Right AND Top↔Bottom** — torus topology
   - m₀ adjacent to m₂, m₈, m₄
   - m₁₅ adjacent to m₁₃, m₇, m₁₄

> **MCQ Trap:** 4-var K-map wraps in **both** dimensions (Q119)

---

## Worked Examples

### Example 1: `F = Σ(5, 7, 13, 15)`

```
        CD
       00  01  11  10
00    0   0   0   0
01    0   1   1   0
11    0   1   1   0
10    0   0   0   0
```

**Groups:**
- {5,7,13,15} — columns 01&11, rows 01&11 → **BD** (A,C change)
- {5,7} vertical? No, need 4-cell groups for max simplification
- Actually: {5,7,13,15} = columns where C=1,D=1? Let's check:
  - 5=0101, 7=0111, 13=1101, 15=1111 → C=1, D=1, A/B vary → **CD**

Wait, let me recalculate:
- m₅ = 0101 (A=0,B=1,C=0,D=1)
- m₇ = 0111 (A=0,B=1,C=1,D=1)
- m₁₃ = 1101 (A=1,B=1,C=0,D=1)
- m₁₅ = 1111 (A=1,B=1,C=1,D=1)

Common: B=1, D=1 → **BD** ✓

**From slides:** Required PIs = `bd, b'd'` — two groups of 4
- Group 1: {m₁,m₃,m₉,m₁₁} → B=0,D=0 → **B̄D̄**
- Group 2: {m₅,m₇,m₁₃,m₁₅} → B=1,D=1 → **BD**

---

### Seven-Segment Display Decoder (4-bit input D₃:₀)

Each segment Sₐ–S₉ is a function of 4 inputs.

#### Without Don't-Cares (0–9 only, 10–15 = 0)
```
Sa = D3'D1 + D3'D2D0 + D2'D1'D0' + D3D2'D1'
Sb = D3'D2' + D2'D1' + D3'D1D0 + D3'D1'D0'
Sc = D3'D0 + D3'D2 + D2'D1'
Sd = D3'D2'D1 + D3'D2D1'D0 + D2'D1'D0' + D3'D1D0
Se = D3'D1D0' + D2'D1'D0'
Sf = D3'D2D0' + D3'D2D1' + D3D2'D1' + D3'D1'D0'
Sg = D3'D1D0' + D3'D2'D1 + D3'D2D1' + D3D2'D1'
```

#### With Don't-Cares (10–15 = X)
**Significantly simpler!**
```
Sa = D3 + D2D0 + D2'D0' + D1
Sb = D2' + D1'D0' + D1D0
Sc = D0 + D2 + D1'
Sd = D1D0' + D2'D1 + D0'D2' + D2D1'D0
Se = D1D0' + D2'D0'
Sf = D3 + D2D0' + D2D1' + D1'D0'
Sg = D3 + D1D0' + D2'D1 + D2D1'
```

> **Key Insight:** Don't-cares allow **larger groups** → fewer terms, fewer literals.

---

## Think About It Exercises (From Slides)

| # | Function | Minimized Result |
|---|----------|------------------|
| 1 | `f(a,b,c) = Σ(0, 3, 5)` | `a'b'c' + a'bc + ab'c` |
| 2 | `f(a,b,c) = Σ(0, 1, 2, 4, 5, 6)` | `a' + b'c'` or similar |
| 3 | `f(a,b,c) = Σ(0, 2, 3, 4, 6, 7)` | `a + c` |
| 4 | `f(a,b) = Σ(0, 1, 2, 3)` | `1` (all 1s) |
| 5 | `f(a,b,c,d) = Σ(0, 1, 5, 7, 15, 14, 10)` | Use K-map with X |

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| 4-var K-map wrap-around? | Both horizontal AND vertical |
| 7-seg without don't-cares? | 10–15 produce blank (0) |
| 7-seg with don't-cares? | 10–15 = X, simpler equations |
| Group of 8 in 4-var? | Eliminates 3 vars → 1 literal |

---

## Exam-Relevant MCQ Patterns

1. **4-var wrap-around** — both row and column edges (Q119)
2. **Don't-care meaning** — unspecified, use for larger groups (Q120)
3. **Don't-care benefit** — impossible inputs can be 0 or 1 (Q121)
4. **7-segment decoder** — classic 4-var K-map application

---

## Key Formulas (Memorize)

```
4-var K-map: 16 cells (m0-m15)
Group sizes: 1, 2, 4, 8, 16
Literals remaining = 4 - log₂(group_size)
Don't-care (X): can be 0 or 1
```
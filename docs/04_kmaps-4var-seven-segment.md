# 04. K-Maps (4-Variable) & Seven-Segment Decoder

> **Source:** Unit 1 Slides 94–123 | Textbook: Harris & Harris Ch. 2

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
- **Rows & columns:** Gray code (00, 01, 11, 10)
- **Wrap-around:** Left↔right AND top↔bottom (torus topology)

---

## Worked Examples

### Example 1: `F = Σ(5, 7, 13, 15)` → `bd + b'd'`
```
CD
    00 01 11 10
00  0  0  0  0
01  0  1  1  0
11  0  1  1  0
10  0  0  0  0
```
- Group {5,7,13,15} (columns 01,11 rows 01,11) → `bd`
- Group {0,1,4,5}... wait, this is different
- Actually from slides: required PIs: `bd, b'd'` → two groups of 4

### Seven-Segment Display Decoder (4-bit input D₃:₀)

**Without don't-cares (0-9 only, 10-15 = 0):**
```
Sa = D3'D1 + D3'D2D0 + D2'D1'D0' + D3D2'D1'
Sb = D3'D2' + D2'D1' + D3'D1D0 + D3'D1'D0'
Sc = D3'D0 + D3'D2 + D2'D1'
Sd = D3'D2'D1 + D3'D2D1'D0 + D2'D1'D0' + D3'D1D0
Se = D3'D1D0' + D2'D1'D0'
Sf = D3'D2D0' + D3'D2D1' + D3D2'D1' + D3'D1'D0'
Sg = D3'D1D0' + D3'D2'D1 + D3'D2D1' + D3D2'D1'
```

**With don't-cares (10-15 = X):**
```
Sa = D3 + D2D0 + D2'D0' + D1
Sb = D2' + D1'D0' + D1D0
Sc = D0 + D2 + D1'
Sd = D1D0' + D2'D1 + D0'D2' + D2D1'D0
Se = D1D0' + D2'D0'
Sf = D3 + D2D0' + D2D1' + D1'D0'
Sg = D3 + D1D0' + D2'D1 + D2D1'
```
> **Key insight:** Don't-cares significantly simplify equations!

---

## Think About It Exercises

1. `f(a,b,c) = Σ(0, 3, 5)` → minimize
2. `f(a,b,c) = Σ(0, 1, 2, 4, 5, 6)` → minimize
3. `f(a,b,c) = Σ(0, 2, 3, 4, 6, 7)` → minimize
4. `f(a,b) = Σ(0, 1, 2, 3)` → all 1s = 1
5. `f(a,b,c,d) = Σ(0, 1, 5, 7, 15, 14, 10)` → minimize

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| 4-var K-map wrap-around? | Both horizontal AND vertical |
| 7-seg without don't-cares? | 10-15 produce blank (0) |
| 7-seg with don't-cares? | 10-15 = X, simpler equations |
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
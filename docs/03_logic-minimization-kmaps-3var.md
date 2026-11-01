# 03. Logic Minimization — Boolean Algebra & K-Maps (3-Variable)

> **Source:** Unit 1 Slides 33–93 | Textbook: Harris & Harris Ch. 2

---

## Boolean Algebra Minimization

### Laws Used
| Law | Formula | Example |
|-----|---------|---------|
| **Distributive** | `A(B+C) = AB + AC` | `bc(a'+a) + ac'(b'+b)` |
| **Complement** | `A + A' = 1` | `(a'+a) = 1` |
| **Identity** | `A·1 = A` | `bc(1) = bc` |

### Step-by-Step Example
```
y = a'bc + ab'c' + abc' + abc
  = bc(a' + a) + ac'(b' + b)    [Distributive]
  = bc(1) + ac'(1)               [Complement]
  = bc + ac'                     [Identity]
```

---

## Karnaugh Maps (3-Variable)

### Structure
```
        BC
       00  01  11  10
A  0   m0  m1  m3  m2
A  1   m4  m5  m7  m6
```
- **Gray code order:** 00, 01, 11, 10 (adjacent differ by 1 bit)
- **Wrap-around:** left↔right edges adjacent

### Key Definitions
| Term | Definition |
|------|------------|
| **Implicant** | Rectangle of 1s (size 1, 2, 4, 8...) |
| **Prime Implicant (PI)** | Largest possible grouping (can't enlarge) |
| **Essential PI (EPI)** | PI covering a 1 not in any other PI |

### Minimization Algorithm
1. Plot 1s from truth table
2. Find **all** prime implicants (largest groups)
3. Identify **essential** PIs (cover unique 1s)
4. Select **required** PIs: all EPIs + minimal extra to cover all 1s
5. Convert groups → product terms (keep variables constant in group)

---

## Worked Examples

### Example 1: `F = Σ(3, 4, 6, 7)`
```
BC
    00 01 11 10
A=0  0  0  1  0
A=1  0  1  1  1
```
- Group {3,7} → `bc` (A changes)
- Group {4,6} → `ac'` (B changes)
- **Result:** `F = bc + ac'`

### Example 2: `F = Σ(0, 2, 3, 4, 6, 7)`
```
BC
    00 01 11 10
A=0  1  0  1  1
A=1  1  0  1  1
```
- Group {0,2,4,6} → `a` (B,C change)
- Group {3,7} or {2,3,6,7} → `c` or `b'c+bc'`
- **Two minimal forms:** `F = a + c` or `F = a + b'c + bc'`

> **Non-uniqueness:** Multiple equally minimal solutions possible (Q32, Q92)

---

## Don't-Care Conditions (X)
- Output **unspecified** for certain inputs (never occur or don't matter)
- Treat as **0 or 1** — whichever gives larger groups
- **Example:** 3-input, `111` never occurs → `X` at m₇

```
F = Σ(0,1,4,5,6) + d(7)
Groups: {0,1,4,5} → b'  and  {4,5,6,7} → a
Result: F = a + b'
```

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| K-map order? | Gray code: 00, 01, 11, 10 |
| Wrap-around? | Left↔right (and top↔bottom for 4-var) adjacent |
| Prime Implicant? | Largest valid grouping of 1s |
| Essential PI? | Covers a 1 no other PI covers |
| Don't-care (X)? | Treat as 0 or 1 to maximize groups |

---

## Exam-Relevant MCQ Patterns

1. **Gray code reason** — adjacent squares differ by 1 literal (Q26)
2. **Wrap-around** — both horizontal and vertical edges (Q31, Q119)
3. **EPI identification** — unique coverage makes it mandatory (Q10, Q39)
4. **Non-unique minimum** — different non-EPI choices = equally valid (Q32)
5. **Don't-care usage** — assign to simplify, not mandatory (Q11, Q27)
6. **Group size → literals** — 8 cells→1 lit, 4→2, 2→3, 1→4 (Q41)

---

## Key Formulas (Memorize)

```
Group of 2ᵏ cells in n-var K-map → eliminates k variables → (n-k) literals
3-var: 1 cell=3 lits, 2=2, 4=1, 8=0 (constant 1)
4-var: 1=4, 2=3, 4=2, 8=1, 16=0
```
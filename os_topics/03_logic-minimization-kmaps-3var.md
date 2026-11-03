# 03. Logic Minimization — Boolean Algebra & K-Maps (3-Variable)

> **Source:** Harris & Harris Ch. 2, Unit 1 Slides 33–93

---

## Boolean Algebra Minimization

### Laws Used (Memorize!)

| Law | Formula | Application |
|-----|---------|-------------|
| **Distributive** | `A(B+C) = AB + AC` | Factoring common terms |
| **Complement** | `A + Ā = 1` | Eliminate variable |
| **Identity** | `A·1 = A` | Cleanup after factoring |
| **Idempotent** | `A + A = A` | Remove duplicates |
| **Absorption** | `A + AB = A` | Remove redundant terms |
| **Consensus** | `AB + ĀC + BC = AB + ĀC` | Remove consensus term |
| **De Morgan** | `Ā + B̄ = Ā·B̄` | SOP ↔ POS, NAND/NOR |

### Step-by-Step Worked Example

**Minimize:** `Y = ĀBC + AB̄C̄ + ABC̄ + ABC`

```
Y = ĀBC + AB̄C̄ + ABC̄ + ABC
  = BC(Ā + A) + AC̄(B̄ + B)    [Distributive: factor BC from 1&4, AC̄ from 2&3]
  = BC(1) + AC̄(1)              [Complement: Ā+A=1, B̄+B=1]
  = BC + AC̄                    [Identity: X·1=X]
```

**Result:** 2 terms, 4 literals (vs original 4 terms, 12 literals)

---

## Why K-Maps? Limitations of Algebraic Minimization

| Aspect | Algebraic | K-Map |
|--------|-----------|-------|
| **Guarantee** | Heuristic — no optimal guarantee | **Algorithmic — guarantees minimum for ≤4 vars** |
| **Process** | Requires insight, trial-and-error | Systematic visual grouping |
| **Don't-cares** | Hard to handle | Natural fit — use as 0 or 1 |

> **Key Point:** K-maps provide **provably minimal** SOP/POS for ≤4 variables. For >4 vars, use Quine-McCluskey or CAD tools.

---

## Karnaugh Maps (3-Variable)

### Structure

```
        BC
       00  01  11  10
A  0   m0  m1  m3  m2
A  1   m4  m5  m7  m6
```

### Critical Properties

1. **Gray Code Order:** 00, 01, 11, 10 — **adjacent cells differ by exactly 1 bit**
2. **Wrap-Around:** Left ↔ Right edges are adjacent (m₀ adjacent to m₂, m₄ to m₆)

> **Why Gray Code?** Ensures adjacent squares differ by exactly 1 literal → valid grouping by Boolean algebra

---

## Key Definitions

| Term | Definition |
|------|------------|
| **Implicant** | Rectangle of 1s (size 1, 2, 4, 8...) — may include X's |
| **Prime Implicant (PI)** | **Largest** possible grouping (cannot be enlarged further) |
| **Essential PI (EPI)** | PI covering at least one 1 **not covered by any other PI** — **MUST include** |

---

## Minimization Algorithm (Guaranteed Optimal for ≤4 vars)

1. **Plot 1s** from truth table (and X's for don't-cares)
2. **Find ALL Prime Implicants** — identify largest valid rectangles (size 2ᵏ)
3. **Identify Essential PIs** — cover at least one 1 uniquely
4. **Select minimum non-EPIs** to cover remaining uncovered 1s
5. **Read equation** — variables **constant** across group (eliminate changing ones)

---

## Worked Examples

### Example 1: `F = Σ(3, 4, 6, 7)`

```
        BC
       00  01  11  10
A  0    0   0   1   0   (m₃=1)
A  1    0   1   1   1   (m₄,m₆,m₇=1)
```

**Step 1: Find all PIs**
- Group {m₃,m₇} vertical → **BC** (A changes, eliminated)
- Group {m₄,m₆} horizontal → **AC̄** (B changes, eliminated)

**Step 2: Essential PIs**
- m₃ only in {m₃,m₇} → **BC essential**
- m₄ only in {m₄,m₆} → **AC̄ essential**
- m₆ covered by both, m₇ covered by BC

**Result:** `F = BC + AC̄`

---

### Example 2: `F = Σ(0, 2, 3, 4, 6, 7)`

```
        BC
       00  01  11  10
A  0    1   0   1   1
A  1    1   0   1   1
```

**PIs:**
- {0,2,4,6} (cols 00,10) → **A** (B,C change)
- {3,7} → **C** (A,B change)
- {2,3,6,7} → **B̄C + BC̄** (not maximal)

**EPIs:**
- {0,2,4,6} covers m₀,m₄ uniquely → **A essential**
- {3,7} covers m₃ uniquely → **C essential**
- All 1s covered!

**Result:** `F = A + C` (minimal) or `F = A + B̄C + BC̄` (also minimal)

> **Non-Uniqueness:** Multiple equally minimal solutions possible (Q32, Q92)

---

### Example 3: Don't-Care Conditions

**Problem:** `F = Σ(0,1,4,5,6) + d(7)` — input 111 never occurs

```
        BC
       00  01  11  10
A  0    1   1   X   0
A  1    1   1   1   0
```

**Using X at m₇ to enlarge groups:**
- {0,1,4,5} → **B̄** (A,C change)
- {4,5,6,7} → **A** (B,C change, using X at m₇)

**Result:** `F = A + B̄`

> **Don't-Care Rule:** Treat X as 0 or 1 — **whichever gives larger groups**. Not mandatory to use all X's.

---

## POS Minimization Using K-Maps

### Procedure (Group the 0s)
1. Plot 0s from truth table
2. Group 0s into rectangles (size 2ᵏ)
3. Each group → Sum Term (variables **constant** = complemented)
4. AND the sum terms

### Example: Same `F = Σ(3,4,6,7)` → 0s at m₀,m₁,m₂,m₅

```
        BC
       00  01  11  10
A  0    0   0   1   0
A  1    0   1   1   1

0-groups: {m₀,m₁} → A+B    {m₁,m₅} → B̄+C    {m₀,m₂} → A+C̄
```

Wait, let's do this properly:

For 0s at m₀(000), m₁(001), m₂(010), m₅(101):
- {m₀,m₁} vertical → A=0,B=0 constant → **A+B**
- {m₁,m₅} diagonal? No, not adjacent
- {m₀,m₂} horizontal → A=0,C=0 constant → **A+C̄**

Actually: Let's check the groups:
- {m₀,m₁}: A=0,B=0 → A+B
- {m₂}: isolated → A+B̄+C̄
- {m₅}: isolated → Ā+B+C̄

POS = (A+B)(A+B̄+C̄)(Ā+B+C̄) — not minimal, confirms SOP is better here.

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| K-map order? | Gray code: 00, 01, 11, 10 |
| Wrap-around? | Left↔right (and top↔bottom for 4-var) adjacent |
| Prime Implicant? | Largest valid grouping of 1s |
| Essential PI? | Covers a 1 no other PI covers |
| Don't-care (X)? | Treat as 0 or 1 to maximize groups |
| POS vs SOP? | Group 0s for POS, group 1s for SOP |

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

3-var:  1 cell=3 lits,  2=2,  4=1,  8=0 (constant 1)
4-var:  1 cell=4 lits,  2=3,  4=2,  8=1,  16=0
```
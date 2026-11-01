# 02. Boolean Equations — Minterms, Maxterms, SOP & POS Forms

> **Source:** Unit 1 Slides 13–42 | Textbook: Harris & Harris Ch. 2

---

## Key Terminology

| Term | Definition | Example (3 vars) |
|------|------------|------------------|
| **Literal** | Variable or its complement | `A`, `A'`, `B`, `B'` |
| **Implicant** | Product of literals | `AB`, `A'C`, `BC'` |
| **Minterm** | Product with **all** input variables | `A'B'C'`, `ABC` (8 total for 3 vars) |
| **Maxterm** | Sum with **all** input variables | `A+B+C`, `A'+B'+C'` |

> **Minterm notation:** `mᵢ` where `i` = decimal of binary input
> **Maxterm notation:** `Mᵢ` where `i` = decimal of binary input

---

## Sum-of-Products (SOP) Form
- **Canonical SOP:** OR of all minterms where output = 1
- **Sigma notation:** `F = Σ(m₁, m₃, m₅)` = `F = Σ(1, 3, 5)`
- **Construction:** Each 1-row → minterm → OR them

**Example:** `Y = A'B + AB = Σ(1, 3)`

---

## Product-of-Sums (POS) Form
- **Canonical POS:** AND of all maxterms where output = 0
- **Pi notation:** `F = Π(M₀, M₂)` = `F = Π(0, 2)`
- **Construction:** Each 0-row → maxterm → AND them

**Example:** `Y = (A+B)(A'+B) = Π(0, 2)`

---

## Truth Table → Boolean Formula

| A | B | C | Y | Minterm | Maxterm |
|---|---|---|---|---------|---------|
| 0 | 0 | 0 | 0 | m₀ | M₀ = A+B+C |
| 0 | 0 | 1 | 1 | m₁ | M₁ = A+B+C' |
| 0 | 1 | 0 | 0 | m₂ | M₂ = A+B'+C |
| 0 | 1 | 1 | 1 | m₃ | M₃ = A+B'+C' |
| 1 | 0 | 0 | 1 | m₄ | M₄ = A'+B+C |
| 1 | 0 | 1 | 1 | m₅ | M₅ = A'+B+C' |
| 1 | 1 | 0 | 0 | m₆ | M₆ = A'+B'+C |
| 1 | 1 | 1 | 1 | m₇ | M₇ = A'+B'+C' |

**SOP:** `Y = m₁ + m₃ + m₄ + m₅ = Σ(1,3,4,5)`
**POS:** `Y = M₀·M₂·M₆ = Π(0,2,6)`

---

## Ben Bitdiddle Picnic Example
> Ben enjoys picnic if **NOT** raining AND **NO** ants
- A = ants (1 = yes), R = rain (1 = yes), E = enjoy
- `E = A'R'` or `E = Σ(0)` — only row 00 gives 1

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Minterm for 3 variables? | Product with all 3 variables (e.g., `A'B'C`) |
| Maxterm for 3 variables? | Sum with all 3 variables (e.g., `A+B+C'`) |
| SOP uses which rows? | Output = 1 rows (minterms) |
| POS uses which rows? | Output = 0 rows (maxterms) |
| `M₆` for 3 vars (A,B,C)? | `A' + B' + C` (binary 110) |

---

## Exam-Relevant MCQ Patterns

1. **Minterm definition** — product with ALL inputs (Q1, Q9, Q34)
2. **POS construction** — product of maxterms for 0 outputs (Q2, Q24)
3. **Minterm count** — `2ⁿ` for n variables (Q14)
4. **Shared characteristic** — find common bits in minterm list (Q35: `m(3,7,11,15)` all have `D=1`)

---

## Key Formulas (Memorize)

```
Minterms for n vars = 2ⁿ
Minterm index = binary value of inputs
Maxterm index = binary value of inputs
SOP: F = Σ(minterms where Y=1)
POS: F = Π(maxterms where Y=0)
```
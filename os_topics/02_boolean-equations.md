# 02. Boolean Equations — Minterms, Maxterms, SOP & POS Forms

> **Source:** Harris & Harris Ch. 2, Unit 1 Slides 13–42

---

## Key Terminology

| Term | Definition | Example (3 vars) |
|------|------------|------------------|
| **Literal** | A variable or its complement | `A`, `Ā`, `B`, `B̄` |
| **Implicant** | Product of one or more literals | `AB`, `ĀC`, `BC̄` |
| **Minterm (mᵢ)** | Product containing **ALL** input variables (exactly once each) | `ĀB̄C̄`, `ABC` (8 total for 3 vars) |
| **Maxterm (Mᵢ)** | Sum containing **ALL** input variables (exactly once each) | `A+B+C`, `Ā+B̄+C̄` |

> **Notation:**
> - **Minterm:** `mᵢ` where `i` = decimal value of binary input combination
> - **Maxterm:** `Mᵢ` where `i` = decimal value of binary input combination

---

## Truth Table → Minterms/Maxterms (3 Variables)

| A | B | C | Y | Minterm (mᵢ) | Maxterm (Mᵢ) |
|---|---|---|---|--------------|--------------|
| 0 | 0 | 0 | 0 | m₀ = ĀB̄C̄ | M₀ = A+B+C |
| 0 | 0 | 1 | 1 | m₁ = ĀB̄C | M₁ = A+B+C̄ |
| 0 | 1 | 0 | 0 | m₂ = ĀBC̄ | M₂ = A+B̄+C |
| 0 | 1 | 1 | 1 | m₃ = ĀBC | M₃ = A+B̄+C̄ |
| 1 | 0 | 0 | 1 | m₄ = AB̄C̄ | M₄ = Ā+B+C |
| 1 | 0 | 1 | 1 | m₅ = AB̄C | M₅ = Ā+B+C̄ |
| 1 | 1 | 0 | 0 | m₆ = ABC̄ | M₆ = Ā+B̄+C |
| 1 | 1 | 1 | 1 | m₇ = ABC | M₇ = Ā+B̄+C̄ |

**Key Observations:**
- **Minterm = 1** for exactly one input combination
- **Maxterm = 0** for exactly one input combination
- Minterm index = binary value of inputs (e.g., 011₂ = 3 → m₃)
- Maxterm index = binary value of inputs (e.g., 011₂ = 3 → M₃)

---

## Sum-of-Products (SOP) Form

### Canonical SOP
OR of all minterms where output = 1
```
F = Σ m(list of indices where Y=1)
```

**Example:** `Y = A'B + AB = Σ(1, 3)`

### Standard SOP (Minimized)
Not necessarily canonical — terms may not include all variables
```
F = A'B + AB = B(A' + A) = B
```

### Constructing SOP from Truth Table
1. Identify rows where output = 1
2. Write minterm for each (include all variables)
3. OR them together

---

## Product-of-Sums (POS) Form

### Canonical POS
AND of all maxterms where output = 0
```
F = Π M(list of indices where Y=0)
```

**Example:** `Y = (A+B)(A'+B) = Π(0, 2)`

### Standard POS (Minimized)
```
F = (A+B)(A'+B) = B
```

### Constructing POS from Truth Table
1. Identify rows where output = 0
2. Write maxterm for each (include all variables)
3. AND them together

---

## SOP ↔ POS Conversion

### Duality Principle
```
F = Σ m(indices)  ⇔  F = Π M(complement of indices)
```

**Example (3 variables):**
```
If F = Σ m(1, 3, 5)  →  F = Π M(0, 2, 4, 6, 7)
```

**Proof:** By De Morgan's Theorem
```
F = m₁ + m₃ + m₅
F' = m₀·m₂·m₄·m₆·m₇ = M₀·M₂·M₄·M₆·M₇
F = (F')' = M₀ + M₂ + M₄ + M₆ + M₇  ← Not quite right...
```

Actually: Complement of minterm is maxterm with same index
- `mᵢ' = Mᵢ` (by De Morgan)
- `F = Σ m(i) = (Π M(i)')' = Π M(i)` for i NOT in list

---

## Ben Bitdiddle Picnic Example (From Textbook)

> **Problem:** Ben enjoys picnic if **NOT** raining AND **NO** ants
> - A = ants (1 = yes), R = rain (1 = yes), E = enjoy
> - Only enjoys when A=0, R=0 → row 00 gives 1

**Truth Table:**
| A | R | E |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

**SOP:** `E = ĀR̄ = Σ m(0)` — only row 00 gives 1
**POS:** Rows 1,2,3 are 0 → `E = (A+R)(A'+R)(A'+R') = Π M(1,2,3)`

---

## Minterm/Maxterm Count

| Variables (n) | Minterms (2ⁿ) | Maxterms (2ⁿ) |
|---------------|---------------|---------------|
| 2 | 4 | 4 |
| 3 | 8 | 8 |
| 4 | 16 | 16 |
| n | 2ⁿ | 2ⁿ |

> **MCQ Pattern:** "How many minterms for 3 variables?" → **8** (Q14)

---

## Finding Shared Characteristics (MCQ Pattern)

**Question:** Minterms `m(3, 7, 11, 15)` for 4 variables (A,B,C,D) — what do they share?

| Index | Binary | A | B | C | D |
|-------|--------|---|---|---|---|
| 3 | 0011 | 0 | 0 | 1 | 1 |
| 7 | 0111 | 0 | 1 | 1 | 1 |
| 11 | 1011 | 1 | 0 | 1 | 1 |
| 15 | 1111 | 1 | 1 | 1 | 1 |

**Answer:** C=1, D=1 for all → `F = C·D` (Q35)

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Minterm for 3 variables? | Product with all 3 variables (e.g., `ĀB̄C`) |
| Maxterm for 3 variables? | Sum with all 3 variables (e.g., `A+B+C̄`) |
| SOP uses which rows? | Output = 1 rows (minterms) |
| POS uses which rows? | Output = 0 rows (maxterms) |
| `M₆` for 3 vars (A,B,C)? | `Ā + B̄ + C` (binary 110) |
| `Σ m(1,3,5)` = Π M(?) | `Π M(0,2,4,6,7)` |

---

## Exam-Relevant MCQ Patterns

1. **Minterm definition** — product with ALL inputs (Q1, Q9, Q34)
2. **POS construction** — product of maxterms for 0 outputs (Q2, Q24)
3. **Minterm count** — `2ⁿ` for n variables (Q14)
4. **Shared characteristic** — find common bits in minterm list (Q35: `m(3,7,11,15)` all have `C=1, D=1`)

---

## Key Formulas (Memorize)

```
Minterms for n vars = 2ⁿ
Minterm index = binary value of inputs
Maxterm index = binary value of inputs
SOP: F = Σ(minterms where Y=1)
POS: F = Π(maxterms where Y=0)
```
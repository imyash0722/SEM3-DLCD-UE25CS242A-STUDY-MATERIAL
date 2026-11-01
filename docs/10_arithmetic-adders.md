# 10. Arithmetic Circuits — Adders (RCA, CLA, Prefix)

> **Source:** Unit 2 Slides 68–100 | Textbook: Harris & Harris Ch. 5

---

## Half Adder
| A | B | Sum | Cout |
|---|---|-----|------|
| 0 | 0 | 0   | 0    |
| 0 | 1 | 1   | 0    |
| 1 | 0 | 1   | 0    |
| 1 | 1 | 0   | 1    |

**Equations:**
- `Sum = A ⊕ B`
- `Cout = A·B`

---

## Full Adder
| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 | 0   | 0   | 0    |
| 0 | 0 | 1   | 1   | 0    |
| 0 | 1 | 0   | 1   | 0    |
| 0 | 1 | 1   | 0   | 1    |
| 1 | 0 | 0   | 1   | 0    |
| 1 | 0 | 1   | 0   | 1    |
| 1 | 1 | 0   | 0   | 1    |
| 1 | 1 | 1   | 1   | 1    |

**Equations:**
- `Sum = A ⊕ B ⊕ Cin`
- `Cout = A·B + A·Cin + B·Cin`

**Implementation:** 2 Half Adders + 1 OR gate

---

## Ripple-Carry Adder (RCA)
- Chain N full adders
- Carry ripples LSB → MSB
- **Delay:** `t_ripple = N × t_FA`
- **32-bit, t_FA=300ps:** 9.6 ns

**Disadvantage:** Slow for large N (O(N) delay)

---

## Carry-Lookahead Adder (CLA)

### Generate & Propagate
- **Generate (Gᵢ):** Stage creates carry → `Gᵢ = Aᵢ·Bᵢ`
- **Propagate (Pᵢ):** Stage passes carry → `Pᵢ = Aᵢ ⊕ Bᵢ` (or `Aᵢ + Bᵢ`)

### Carry Equations
```
C₁ = G₀ + P₀·C₀
C₂ = G₁ + P₁·G₀ + P₁·P₀·C₀
C₃ = G₂ + P₂·G₁ + P₂·P₁·G₀ + P₂·P₁·P₀·C₀
C₄ = G₃ + P₃·G₂ + P₃·P₂·G₁ + P₃·P₂·P₁·G₀ + P₃·P₂·P₁·P₀·C₀
```

### Block CLA (k-bit blocks)
- Compute block G and P
- Carry jumps block-to-block
- **Delay:** `t_CLA = t_pg + t_pg_block + (N/k - 1)t_AND_OR + k·t_FA`

**32-bit, 4-bit blocks, t_AND_OR=200ps:** ~3.3 ns

---

## Prefix Adder (Fastest)

### Principle
- Compute all carries in parallel using prefix tree
- **log₂N stages** of prefix cells (black/gray)
- **Delay:** `t_PA = t_pg + log₂N(t_pg_prefix) + t_XOR`

**32-bit:** ~1.2 ns

### Prefix Cell (Black Cell)
```
G_out = G_upper + P_upper·G_lower
P_out = P_upper·P_lower
```

### Gray Cell
```
G_out = G_upper + P_upper·G_lower
P_out = P_lower (pass through)
```

---

## Delay Comparison (32-bit)

| Adder Type | Delay | Formula |
|------------|-------|---------|
| Ripple-Carry | 9.6 ns | N·t_FA |
| CLA (4-bit blocks) | 3.3 ns | t_pg + t_pg_block + 7·t_AND_OR + 4·t_FA |
| Prefix | 1.2 ns | t_pg + log₂N·t_pg_prefix + t_XOR |

**Parameters:** t_FA=300ps, t_AND_OR=200ps, t_pg=100ps, t_pg_prefix=200ps, t_XOR=100ps

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Half Adder Sum? | A ⊕ B |
| Full Adder Cout? | AB + ACin + BCin |
| RCA delay scaling? | O(N) |
| CLA block size benefit? | Parallel carry within block |
| Prefix delay scaling? | O(log N) |
| Fastest for 32-bit? | Prefix Adder |

---

## Exam-Relevant MCQ Patterns

1. **Half/Full Adder equations** — Sum XOR, Cout majority (Q10, Q66, Q67)
2. **RCA delay** — N × t_FA (Q12, Q74)
3. **CLA Generate** — Gᵢ = Aᵢ·Bᵢ (Q13)
4. **CLA Propagate** — Pᵢ = Aᵢ ⊕ Bᵢ (or Aᵢ + Bᵢ) (Q13)
5. **Block P** — P₃:₀ = P₃·P₂·P₁·P₀ (Q14)
6. **Prefix delay** — O(log N) (Q15, Q74)
7. **Subtraction via 2's complement** — invert B, Cin=1 (Q16)
8. **Overflow detection** — C_in,MSB ⊕ C_out,MSB (Q17)
9. **Adder selection for CPU** — Prefix for speed despite area (Q75, Q84)

---

## Key Formulas (Memorize)

```
Half Adder:  S = A⊕B,    Cout = AB
Full Adder:  S = A⊕B⊕Cin, Cout = AB + ACin + BCin
RCA:         t = N × t_FA
CLA (k-block): t = t_pg + t_pg_block + (N/k-1)t_AND_OR + k·t_FA
Prefix:      t = t_pg + log₂N·t_pg_prefix + t_XOR
Subtract:    A - B = A + B' + 1 (Cin=1)
Overflow:    V = C_in,MSB ⊕ C_out,MSB
```
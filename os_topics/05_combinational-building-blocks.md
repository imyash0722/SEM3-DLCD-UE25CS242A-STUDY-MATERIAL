# 05. Combinational Building Blocks — Mux, Decoder, Encoder

> **Source:** Unit 1 Slides 124–160 | Textbook: Harris & Harris Ch. 2

---

## Multiplexer (MUX)

### 2:1 MUX
- **Select (S):** 1 bit → chooses D₀ (S=0) or D₁ (S=1)
- **Equation:** `Y = S'·D₀ + S·D₁`
- **Implementations:**
  1. **Logic gates** (AND-OR)
  2. **Tristate buffers** — only one enabled at a time (outputs Z = high-Z)

### 4:1 MUX
- **Select:** S₁, S₀ (2 bits)
- **Truth table:**
  | S₁ | S₀ | Y |
  |----|----|---|
  | 0  | 0  | D₀ |
  | 0  | 1  | D₁ |
  | 1  | 0  | D₂ |
  | 1  | 1  | D₃ |

### MUX as Lookup Table (Implementing Logic)
- Connect select lines to inputs
- Connect data inputs to 0/1 per truth table row

**Example: AND gate with 4:1 MUX (A,B as selects)**
| A | B | Y | D₀ | D₁ | D₂ | D₃ |
|---|---|---|----|----|----|----|
| 0 | 0 | 0 | 0  |    |    |    |
| 0 | 1 | 0 |    | 0  |    |    |
| 1 | 0 | 0 |    |    | 0  |    |
| 1 | 1 | 1 |    |    |    | 1  |
→ `D₀=0, D₁=0, D₂=0, D₃=1`

**Reducing MUX size (Shannon expansion):**
- Use one variable as data input instead of select
- `N-input function` → `2^{N-1}:1 MUX`
- Example: 3-var AND with 2:1 MUX (A=select, B=data)

---

## MUX Cascading (Building Larger MUXes)

| Target | Using 2:1 MUXes | Formula |
|--------|------------------|---------|
| 4:1    | 3                | 2+1     |
| 8:1    | 7                | 4+2+1   |
| 16:1   | 15               | 8+4+2+1 |
| 2ⁿ:1   | 2ⁿ - 1           | Σ 2ⁱ    |

| Target | Using 4:1 MUXes | Formula |
|--------|------------------|---------|
| 8:1    | 2 + 1 = 3        | 2¹ + 2⁰ |
| 16:1   | 4 + 1 = 5        | 4¹ + 4⁰ |
| 64:1   | 16 + 4 + 1 = 21  | 4²+4¹+4⁰ |

---

## Decoder

### N:2ᴺ Decoder
- **N inputs** → **2ᴺ outputs** (one-hot)
- Exactly **one output HIGH** per input combination
- **Outputs = minterms** of inputs

### 2:4 Decoder
| A₁ | A₀ | Y₀ | Y₁ | Y₂ | Y₃ |
|----|----|----|----|----|----|
| 0  | 0  | 1  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  | 0  | 0  |
| 1  | 0  | 0  | 0  | 1  | 0  |
| 1  | 1  | 0  | 0  | 0  | 1  |

### Logic Using Decoders
- Generate all minterms via decoder
- OR required minterms for function
- **N-input function** → **N:2ᴺ decoder + M-input OR gate**

---

## Encoder

### Types
| Encoder | Inputs | Outputs | Notes |
|---------|--------|---------|-------|
| 4:2     | 4      | 2       | One-hot input |
| 8:3 (Octal) | 8   | 3       | Binary code out |
| 10:4 (BCD) | 10  | 4       | Decimal→BCD |
| **Priority** | 2ᴺ | N       | Highest priority wins |

### Priority Encoder (4:2)
| Y₃ | Y₂ | Y₁ | Y₀ | A₁ | A₀ | V |
|----|----|----|----|----|----|---|
| 0  | 0  | 0  | 1  | 0  | 0  | 1 |
| 0  | 0  | 1  | X  | 0  | 1  | 1 |
| 0  | 1  | X  | X  | 1  | 0  | 1 |
| 1  | X  | X  | X  | 1  | 1  | 1 |
| 0  | 0  | 0  | 0  | X  | X  | 0 |

- **V (Valid)** = 1 if any input active, else 0
- **Y₃ highest priority**, Y₀ lowest

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| 4:1 MUX select lines? | 2 (log₂4) |
| 2:1 MUX equation? | `Y = S'D₀ + SD₁` |
| Decoder outputs? | One-hot (exactly one HIGH) |
| 3:8 decoder for 3-var function? | Connect minterm outputs to OR |
| Priority encoder purpose? | Resolve multiple active inputs |

---

## Exam-Relevant MCQ Patterns

1. **MUX select lines** — log₂N (Q5, Q29)
2. **2:1 MUX equation** — `S'D₀ + SD₁` (Q10)
3. **Decoder one-hot** — exactly one output HIGH (Q20, Q160)
4. **Decoder + OR for logic** — N:2ᴺ decoder generates all minterms (Q38)
5. **Tristate MUX** — 0, 1, Z states (Q23)
6. **MUX as lookup** — data inputs = truth table outputs
7. **Cascading formula** — 2ⁿ:1 needs 2ⁿ-1 two-to-one MUXes

---

## Key Formulas (Memorize)

```
MUX: N inputs → log₂N select lines
2:1 MUX: Y = S'D₀ + SD₁
Decoder: N inputs → 2ᴺ outputs (one-hot)
N:2ᴺ Decoder + OR gate = any N-input function
Priority Encoder: V=0 only when all inputs=0
```
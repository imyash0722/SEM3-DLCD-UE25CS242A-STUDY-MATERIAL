# 01. Digital Circuits — Introduction & Combinational vs Sequential Logic

> **Source:** Unit 1 Slides 2–12 | Textbook: Harris & Harris Ch. 1–2

---

## Key Concepts

### What is a Digital Circuit?
A **digital circuit** is a network that processes discrete-valued variables (binary 0/1).

**Black-box view:**
- **Input terminals** — signals from external system
- **Output terminals** — signals to external system
- **Functional specification** — relationship between inputs and outputs (e.g., `Y = A·B`)
- **Timing specification** — delay between input change and output response

### Nodes
| Type | Description |
|------|-------------|
| **Input** | A, B, C — receives from outside |
| **Output** | Y, Z — sends to outside |
| **Internal** | n1 — connects elements inside |

### Combinational Logic
- **Memoryless** — output depends **only** on current inputs
- **Examples:** Adders, Multiplexers, Decoders, Encoders, Comparators

### Sequential Logic
- **Has memory** — output depends on **current + previous** inputs
- **Examples:** Registers, Counters, Flip-flops, Memory devices

---

## Rules of Combinational Composition
A circuit is combinational **iff**:
1. Every circuit element is itself combinational
2. Every node is either an input or connects to **exactly one** output terminal
3. **No cyclic paths** — every path visits each node at most once

> **MCQ Pattern:** A circuit with a cyclic path and no register is **not combinational** (Q13, Unit 1 MCQs)

---

## Propagation Delay
- Elements in **parallel**: delay = `max(delay1, delay2)`
- Elements in **series**: delay = `delay1 + delay2`

**Example:** E1=5ns, E2=8ns (parallel), E3=4ns (after both) → `max(5,8) + 4 = 12ns`

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| What are the two specifications of a digital circuit? | Functional + Timing |
| Combinational vs Sequential difference? | Memoryless vs Has memory |
| When is a circuit NOT combinational? | Cyclic path exists without register |
| Worst-case delay for parallel then series? | `max(parallel) + series` |

---

## Exam-Relevant MCQ Patterns

1. **Black-box specifications** — always both functional AND timing (Q8)
2. **Combinational classification** — cyclic path = NOT combinational (Q13)
3. **Delay calculation** — parallel = max, series = sum (Q12)
4. **Circuit type identification** — Adders/Mux/Decoder = combinational; Counter/Reg/FF = sequential (Q15)

---

## Key Formulas (Memorize)

```
Parallel delay = max(d₁, d₂, ...)
Series delay   = d₁ + d₂ + ...
Combinational  = no feedback loops
Sequential     = has memory/state
```
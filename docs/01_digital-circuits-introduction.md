# 01. Digital Circuits — Introduction & Combinational vs Sequential Logic

> **Source:** Harris & Harris Ch. 1–2, Unit 1 Slides 2–12

---

## What is a Digital Circuit?

A **digital circuit** is a network that processes **discrete-valued variables** (binary 0/1). Unlike analog circuits that handle continuous signals, digital circuits operate on two well-defined voltage levels.

### Black-Box View

Every digital circuit can be viewed as a black box with:

| Component | Description |
|-----------|-------------|
| **Input Terminals** | Receive external signals (A, B, C, ...) |
| **Output Terminals** | Drive external loads (Y, Z, ...) |
| **Functional Specification** | Logical I/O relationship — Truth Table / Boolean Equation (e.g., `Y = A·B`) |
| **Timing Specification** | Propagation delay (`t_pd`) — time between input change and output response |

> **Key Insight:** Two circuits can have **identical functional specs** but **different timing specs**. Both compute `Y = A·B`, but one may be faster (lower `t_pd`) due to better layout, transistor sizing, or logic family.

---

## Nodes in a Circuit

| Type | Description | Example |
|------|-------------|---------|
| **Input** | Receives from outside | A, B, C |
| **Output** | Sends to outside | Y, Z |
| **Internal** | Connects elements inside | n₁ (output of first gate, input to second) |

---

## Combinational vs Sequential Logic

| Property | Combinational Logic | Sequential Logic |
|----------|---------------------|------------------|
| **Memory** | None (Memoryless) | Yes — stores state |
| **Output depends on** | Current inputs **only** | Current + **previous** inputs (state) |
| **Feedback** | Forbidden | Required (via registers) |
| **Examples** | Adder, MUX, Decoder, Encoder, Comparator | Register, Counter, Flip-flop, FSM, Memory |

### Combinational Circuit Definition

A circuit is **combinational** **iff** all three rules hold:

1. **Element Rule:** Every circuit element is itself combinational
2. **Node Rule:** Every node is either an input or connects to **exactly one** output terminal (no shorted outputs)
3. **Acyclic Rule:** **No cyclic paths** (feedback loops) — every path visits each node at most once

> **MCQ Trap:** A circuit with a cyclic path and **no register** is **NOT combinational** (it's either sequential or unstable/astable).

---

## Propagation Delay

### Key Formulas

```
Elements in PARALLEL:  delay = max(delay₁, delay₂, ...)
Elements in SERIES:    delay = delay₁ + delay₂ + ...
```

### Worked Example

```
E1 = 5 ns (parallel)     E2 = 8 ns (parallel)
              ↓
         E3 = 4 ns (series after both)
         
Total delay = max(5, 8) + 4 = 8 + 4 = 12 ns
```

### Timing Diagram
```
A ────────┐
          ├── E1 (5ns) ──┐
B ────────┤              ├── max(5,8)=8ns ──┐
          ├── E2 (8ns) ──┘                  ├── E3 (4ns) ── Y
C ────────┘                                     (12ns total)
```

---

## Voltage Thresholds & Noise Margins (Ch. 1)

For a 1.8V system:

| Parameter | Value | Description |
|-----------|-------|-------------|
| **V_OH** | ≥ 1.35V | Output HIGH min voltage |
| **V_OL** | ≤ 0.45V | Output LOW max voltage |
| **V_IH** | ≥ 1.26V | Input recognized as HIGH |
| **V_IL** | ≤ 0.54V | Input recognized as LOW |
| **NM_H** | V_OH − V_IH = 0.09V | HIGH noise margin |
| **NM_L** | V_IL − V_OL = 0.09V | LOW noise margin |

**Forbidden Zone:** 0.54V < V < 1.26V → undefined behavior

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| What are the two specifications of a digital circuit? | Functional + Timing |
| Combinational vs Sequential difference? | Memoryless vs Has memory/state |
| When is a circuit NOT combinational? | Cyclic path exists without register |
| Worst-case delay for parallel then series? | `max(parallel) + series` |
| What are the three combinational rules? | 1) All elements combinational 2) Each node driven by one output 3) No cyclic paths |

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
# 09. State Encoding & Factoring State Machines

> **Source:** Unit 2 Slides 24–54 | Textbook: Harris & Harris Ch. 3

---

## State Encoding Techniques

| Encoding | FFs for K States | Advantages | Disadvantages |
|----------|------------------|------------|---------------|
| **Binary** | ⌈log₂K⌉ | Fewest FFs, compact | Complex next-state logic |
| **One-Hot** | K | Simple logic, fast | More FFs, higher cost |
| **Gray** | ⌈log₂K⌉ | Single-bit transitions | Complex logic |
| **Custom** | — | Application-specific | Manual effort |

---

## Divide-by-3 Counter: Binary vs One-Hot

### Binary Encoding (2 FFs)
| State | Code |
|-------|------|
| S0 | 00 |
| S1 | 01 |
| S2 | 10 |
| (11) | Unused |

**Next-state logic:** More complex, multi-bit changes

### One-Hot Encoding (3 FFs)
| State | Code |
|-------|------|
| S0 | 001 |
| S1 | 010 |
| S2 | 100 |

**Next-state logic:** Simple shifts (S0→S1→S2→S0 = rotate left)

---

## Choosing Encoding
- **Small FSMs / speed critical:** One-Hot
- **Large FSMs / area critical:** Binary
- **CAD tools** can optimize automatically
- **Trade-off:** FFs vs logic complexity vs speed

---

## Factoring State Machines

### Problem: State Explosion
Complex FSM → many states → hard to design/debug

### Solution: Decompose into Smaller Interacting FSMs
```
Unfactored:        Factored:
  1 Large FSM    →   FSM_A + FSM_B
  N₁×N₂ states       N₁ + N₂ states
```

### Traffic Light with Parade Mode
**Unfactored:** 8 states (S0-S3 normal, S4-S7 parade)
- Two nearly identical halves
- Complex, hard to modify

**Factored:**
| Sub-FSM | Function | States |
|---------|----------|--------|
| **Mode FSM** | Tracks Normal/Parade | 2 |
| **Lights FSM** | Controls lights (uses Mode) | 4 |

**Interaction:** Mode FSM output `M` → Lights FSM input
**Result:** 2+4=6 states vs 8, modular, easier to extend

---

## Factored vs Unfactored Comparison

| Aspect | Unfactored | Factored |
|--------|------------|----------|
| Structure | Single large FSM | Multiple small FSMs |
| States | N₁ × N₂ | N₁ + N₂ |
| Transitions | Complex | Simple per FSM |
| Debugging | Difficult | Easier |
| Modularity | Low | High |
| Extensibility | Hard | Easy |

---

## Deriving FSM from Schematic

### Steps
1. Identify Inputs, Outputs, State bits
2. Write next-state & output equations
3. Create next-state & output tables
4. Remove unreachable states
5. Assign symbolic names
6. Draw state diagram
7. Describe function

### Example: Keypad Lock Circuit
**Given:** 2 state bits (S₁,S₀), inputs (A₁,A₀), output (Unlock)
**Equations:**
- S₁' = S₀·A₁·A₀
- S₀' = S₁'·S₀·A₁·A₀
- Unlock = S₁

**Result:** 3 reachable states → pattern detector

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Binary FFs for 8 states? | 3 (2³=8) |
| One-Hot FFs for 8 states? | 8 |
| Binary FFs for 5 states? | 3 (2²=4<5, 2³=8≥5) |
| Factoring benefit? | N₁×N₂ → N₁+N₂ states |
| Parade mode factoring? | Mode FSM + Lights FSM |

---

## Exam-Relevant MCQ Patterns

1. **Binary encoding states** — 2ᵏ for k FFs (Q2, Q3, Q42)
2. **One-Hot FFs** — equals number of states (Q2)
3. **Factoring advantage** — multiplicative → additive states (Q9)
4. **Binary vs One-Hot trade-off** — FFs vs logic complexity (Q26, Q27)
5. **Deriving FSM** — steps from circuit to diagram (Q55)

---

## Key Formulas (Memorize)

```
Binary:    K states → ⌈log₂K⌉ FFs
One-Hot:   K states → K FFs
Factored:  N₁×N₂ states → N₁+N₂ states
```
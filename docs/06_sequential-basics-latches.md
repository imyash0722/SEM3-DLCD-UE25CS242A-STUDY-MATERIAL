# 06. Sequential Logic Basics — Latches, SR Latch, D Latch

> **Source:** Unit 1 Slides 162–186 | Textbook: Harris & Harris Ch. 3

---

## Combinational vs Sequential

| Property | Combinational | Sequential |
|----------|---------------|------------|
| Memory | None | Yes (state) |
| Output depends on | Current inputs only | Current + past inputs |
| Example | Adder, MUX, Decoder | Register, Counter, FF |

---

## Memory Elements

### Bistable Element (Cross-Coupled Inverters)
- Two stable states: `Q=0, Q'=1` or `Q=1, Q'=0`
- **Problem:** No inputs to control state

### SR Latch (NOR-based)
```
     S ──┐      ┌── Q
         NOR──┘
     R ──┘      ┌── Q'
         NOR──┘
```
| S | R | Action | Q | Q' |
|---|---|--------|---|---|
| 0 | 0 | Hold   | Q | Q' |
| 0 | 1 | Reset  | 0 | 1  |
| 1 | 0 | Set    | 1 | 0  |
| 1 | 1 | **Invalid** | 0 | 0 |

- **S=R=1 invalid:** Q=Q'=0 (not complementary), race on release
- **Awkward:** "What to store" and "When to change" mixed

---

## D Latch (Solves SR Problems)

| D | CLK | Action | Q |
|---|-----|--------|---|
| X | 0   | Hold   | Q |
| 0 | 1   | Reset  | 0 |
| 1 | 1   | Set    | 1 |

- **D = WHAT to store**
- **CLK = WHEN to change**
- **Transparent** when CLK=1 (Q follows D)
- **Opaque** when CLK=0 (holds value)
- Guarantees S≠R internally

---

## D Latch vs D Flip-Flop

| Property | D Latch | D Flip-Flop |
|----------|---------|-------------|
| Triggering | Level-sensitive | Edge-triggered |
| Transparent | CLK=1 | Only at edge |
| Symbol | No triangle | Triangle at CLK |
| Symbol (pos-edge) | — | `CLK ▷` |

**Problem with latch:** While CLK=1, D changes → Q changes unpredictably
**Solution:** Flip-flop samples **only at clock edge**

---

## Clock Edges
| Edge | Transition | Name |
|------|------------|------|
| Rising | 0→1 | Positive edge |
| Falling | 1→0 | Negative edge |

---

## Traffic Light Example

| Element | Behavior | Problem |
|---------|----------|---------|
| **Latch** | Transparent during CLK=1 | Glitch during HIGH → wrong state |
| **Flip-Flop** | Updates only at edge | Glitches ignored until next edge |

> **Flip-flop preferred** for reliable sequential control

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| SR latch invalid state? | S=1, R=1 → Q=Q'=0 |
| D latch transparent when? | CLK=1 |
| D latch holds when? | CLK=0 |
| Latch vs FF difference? | Level vs edge triggered |
| Why FF better for traffic light? | Ignores glitches between edges |

---

## Exam-Relevant MCQ Patterns

1. **SR latch invalid** — S=R=1 gives Q=Q'=0 (Q47)
2. **D latch transparency** — CLK=1 means transparent (Q28)
3. **Latch vs FF** — level vs edge sensitive (Q4, Q7, Q183-186)
4. **Cross-coupled inverters** — two stable states = 1 bit storage (Q40)
5. **Ring oscillator** — 3 inverters loop, period = 2·N·tₚd (Q46, Q59, Q60)

---

## Key Formulas (Memorize)

```
Ring oscillator: T = 2 × N × tₚd,  f = 1/T
SR latch: S=1→Set, R=1→Reset, S=R=1→Invalid
D latch: CLK=1→Transparent (Q=D), CLK=0→Hold
```
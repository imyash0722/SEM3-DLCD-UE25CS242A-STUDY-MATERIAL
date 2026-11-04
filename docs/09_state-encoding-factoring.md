# 09. State Encoding & Factoring State Machines

> **Source:** Harris & Harris Ch. 3, Unit 2 Slides 24–54, Unit 3 FSM Slides

---

## State Encoding Techniques

| Encoding | FFs for K States | Advantages | Disadvantages |
|----------|------------------|------------|---------------|
| **Binary** | ⌈log₂K⌉ | Fewest FFs, compact | Complex next-state logic |
| **One-Hot** | K | Simple logic, fast | More FFs, higher cost |
| **Gray** | ⌈log₂K⌉ | Single-bit transitions | Complex logic |
| **Custom** | — | Application-specific | Manual effort |

---

## Binary Encoding

In Binary Encoding, each state is represented using a binary number.
For an FSM with K states, the number of bits required is: ⌈log₂K⌉

**Example: 4 states**
| State | Binary Code |
|-------|-------------|
| S0 | 00 |
| S1 | 01 |
| S2 | 10 |
| S3 | 11 |

**Advantages:**
- Uses fewer state bits and requires fewer flip-flops
- Efficient hardware utilization
- Compact state register

---

## One-Hot Encoding

In One-Hot Encoding, each state is assigned a separate bit.
Only one bit is HIGH (1) at any given time, while all other bits remain LOW (0).
For K states, K bits are required.

**Example: 3 states**
| State | Encoding |
|-------|----------|
| S0 | 001 |
| S1 | 010 |
| S2 | 100 |

**Advantages:**
- Simpler combinational logic and faster implementation
- Easier to debug and modify

**Disadvantages:**
- Requires more flip-flops and higher hardware cost

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

## State Transition Tables

### Divide-by-3 Counter (Moore)

**State Transition Table:**
| Current State | Next State | Output Y |
|---------------|------------|----------|
| S0 | S1 | 1 |
| S1 | S2 | 0 |
| S2 | S0 | 0 |

**Output Table:**
| Current State | Output Y |
|---------------|----------|
| S0 | 1 |
| S1 | 0 |
| S2 | 0 |

---

## Binary vs One-Hot Encoding Comparison

| Aspect | Binary | One-Hot |
|--------|--------|---------|
| FFs for 4 states | 2 | 4 |
| Next-state logic | Complex | Simple (shift) |
| Speed | Slower | Faster |
| Area | Smaller | Larger |
| Power | Lower | Higher |

---

## FSM Implementation

### Binary Encoding Implementation
```
next_state_logic → state_register → output_logic
```

### One-Hot Encoding Implementation
```
next_state_logic → state_register (one-hot) → output_logic
```
One-hot allows direct decode of outputs from state bits.

---

## Moore vs Mealy Machines

| Property | Moore | Mealy |
|----------|-------|-------|
| **Output depends on** | Current state only | Current state + inputs |
| **Output formula** | Y = g(S) | Y = g(S, X) |
| **States needed** | More (usually) | Fewer |
| **Output timing** | State-synchronous | Can be asynchronous |
| **Glitch immunity** | High | Lower |
| **Diagram** | Outputs **in** circles | Outputs **on** arcs |

---

## Pattern Recognizer: 1011 (Overlapping)

### Moore (5 states)
| State | Matched | Output |
|-------|---------|--------|
| S0 | — | 0 |
| S1 | 1 | 0 |
| S2 | 10 | 0 |
| S3 | 101 | 0 |
| S4 | 1011 | **1** |

**Overlap transitions from S4:**
- Input 1 → S1 (new '1' starts next pattern)
- Input 0 → S2 ('10' suffix matches prefix)

### Mealy (4 states)
| State | Matched |
|-------|---------|
| S0 | — |
| S1 | 1 |
| S2 | 10 |
| S3 | 101 |

**Output:** Detect=1 when in S3 **and** input=1 (on transition)

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

---

## Traffic Light with Parade Mode (Factoring Example)

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
- S₀' = S̄₁·S₀·A₁·A₀
- Unlock = S₁

**Result:** 3 reachable states → pattern detector

---

## FSM Design Procedure

1. Identify the inputs and outputs
2. Draw the State Transition Diagram
3. Create State Transition Table
3. Create Output Table
4. Select a suitable State Encoding
4. Write Next-State Equations and Output Equations
6. Design the circuit schematic

---

## FSM Design Example: Soda Machine

**Problem:** Design an FSM controller for a soda machine.
- Sodas cost 25 cents
- Inputs: Nickel (5¢), Dime (10¢), Quarter (25¢)
- Exactly one coin inserted per cycle
- Outputs: Dispense, ReturnNickel, ReturnDime, ReturnTwoDimes
- When 25¢ reached: assert Dispense + appropriate change
- Then ready for next soda

**State Definition:** State = amount of money entered
- S0 = 0¢
- S5 = 5¢ (Nickel)
- S10 = 10¢ (Dime)
- S15 = 15¢ (Nickel + Dime)
- S20 = 20¢ (2 Dimes or Dime+Nickel×2)
- S25 = 25¢ (Dispense + reset to S0)

---

## FSM Review Questions

1. **Output depends on:** In the keypad lock example, Unlock = S₁ — depends on **current state only** (Moore)
2. **5 flip-flops + Binary Encoding:** Max states = 2⁵ = **32**
3. **8 states + Binary Encoding:** Flip-flops needed = ⌈log₂8⌉ = **3**
4. **Default case in Verilog:** Handles invalid/unused state encodings, provides safe recovery (next_state = S0)

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

## Key Formulas (Memorize)

```
Binary:    K states → ⌈log₂K⌉ FFs
One-Hot:   K states → K FFs
Factored:  N₁×N₂ states → N₁+N₂ states
```
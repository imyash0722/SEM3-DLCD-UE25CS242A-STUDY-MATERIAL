# 08. Finite State Machines — Moore vs Mealy, Design Process

> **Source:** Harris & Harris Ch. 3, Unit 2 Slides 2–64, Unit 3 FSM Slides

---

## FSM Components

| Component | Function |
|-----------|----------|
| **M Inputs** | External signals |
| **N Outputs** | External signals |
| **k-bit State Register** | Stores current state (2ᵏ states) |
| **Clock** | Controls state updates |
| **Reset (optional)** | Initializes to known state |

---

## Three-Block Structure

```
         ┌──────────────┐
Inputs ──►│ Next-State   │──► Next State
          │   Logic      │
State ───►│ (Combinational)│
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │  State Reg   │──► Current State (k FFs)
          │  (k FFs)     │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │  Output      │──► Outputs
          │  Logic       │
          └──────────────┘
```

**Working Principle:** On every clock edge, the FSM:
1. Reads the current state
2. Accepts the current inputs
3. Computes the next state
4. Updates the state register
5. Produces the required outputs

---

## Traffic Light Controller Example

**Inputs:** Tₐ (Academic Ave sensor), Tᵦ (Bravado Blvd sensor)
**Outputs:** Lₐ, Lᵦ (traffic lights)
**Clock:** 5-second period

**States (Moore):**
| State | Meaning | Lₐ | Lᵦ |
|-------|---------|----|----|
| S0 | Academic Green | G | R |
| S1 | Academic Yellow | Y | R |
| S2 | Bravado Green | R | G |
| S3 | Bravado Yellow | R | Y |

**State Encoding (Binary):** S0=00, S1=01, S2=10, S3=11

**State Transitions:**
- Reset → S0 (always)
- S0 → S1: If Tₐ = 0 (Academic Ave has no traffic)
- S1 → S2: After 5 seconds automatically
- S2 → S3: If Tᵦ = 0 (Bravado Blvd has no traffic)
- S3 → S0: After 5 seconds, completing one cycle
- S0 → S0 when Tₐ = 1 (Academic Ave has traffic)
- S2 → S2 when Tᵦ = 1 (Bravado Blvd has traffic)

---

## Moore vs Mealy

| Property | Moore | Mealy |
|----------|-------|-------|
| **Output depends on** | Current state only | Current state + inputs |
| **Output formula** | Y = g(S) | Y = g(S, X) |
| **States needed** | More (usually) | Fewer |
| **Output timing** | State-synchronous | Can be asynchronous |
| **Glitch immunity** | High | Lower |
| **Diagram** | Outputs **in** circles | Outputs **on** arcs |

---

## Traffic Light Example (Moore vs Mealy)

### Moore Machine (3 states)
- States represent the previous input history
- Output depends only on current state
- Requires 3 states for the snail pattern recognizer example

### Mealy Machine (2 states)
- Outputs are generated during state transitions
- Each transition labeled as `Input / Output`
- Requires only 2 states for the same pattern recognizer

---

## Pattern Recognizer (1011, Overlapping)

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

## FSM Design Procedure

1. **Identify inputs/outputs**
2. **Draw State Transition Diagram**
3. **Create State Transition Table**
4. **Create Output Table**
5. **Select State Encoding** (Binary, One-Hot, etc.)
6. **Derive Next-State Equations** (K-maps/inspection)
7. **Derive Output Equations**
8. **Draw Circuit Schematic**

---

## Divide-by-3 Counter (Moore)

| State | Binary | One-Hot | Output Y |
|-------|--------|---------|----------|
| S0 | 00 | 001 | 1 |
| S1 | 01 | 010 | 0 |
| S2 | 10 | 100 | 0 |

**Sequence:** S0 → S1 → S2 → S0 → ...
**Output:** Y=1 only in S0 (1 cycle out of 3)

---

## Pattern Recognizer (1011, Overlapping)

### Moore FSM Verilog Code

```verilog
module moore_1011 (
    input  wire clk,
    input  wire reset,
    input  wire x,
    output reg  detect
);

    localparam S0 = 3'b000,
               S1 = 3'b001,
               S2 = 3'b010,
               S3 = 3'b011,
               S4 = 3'b100;

    reg [2:0] state, next_state;

    // State Register
    always @(posedge clk or posedge reset) begin
        if (reset) state <= S0;
        else       state <= next_state;
    end

    // Next State Logic
    always @(*) begin
        next_state = S0;
        case (state)
            S0: if (x) next_state = S1; else next_state = S0;
            S1: if (x) next_state = S1; else next_state = S2;
            S2: if (x) next_state = S3; else next_state = S0;
            S3: if (x) next_state = S4; else next_state = S2;
            S4: if (x) next_state = S1; else next_state = S2;  // Overlap recovery
            default: next_state = S0;
        endcase
    end

    // Moore Output Logic
    always @(*) begin
        detect = (state == S4);
    end
endmodule
```

---

## Mealy FSM for 1011 (4 states)

```verilog
module mealy_1011 (
    input  wire clk,
    input  wire reset,
    input  wire x,
    output reg  detect
);

    localparam S0 = 2'b00, S1 = 2'b01, S2 = 2'b10, S3 = 2'b11;

    reg [1:0] state, next_state;

    always @(posedge clk or posedge reset) begin
        if (reset) state <= S0;
        else       state <= next_state;
    end

    always @(*) begin
        next_state = S0;
        detect = 1'b0;
        case (state)
            S0: if (x) next_state = S1; else next_state = S0;
            S1: if (x) next_state = S1; else next_state = S2;
            S2: if (x) next_state = S3; else next_state = S0;
            S3: if (x) begin detect = 1'b1; next_state = S1; end
                else begin next_state = S2; end
            default: next_state = S0;
        endcase
    end
endmodule
```

**Key Difference:** Mealy output `detect` is asserted on transition (S3 + x=1), not in a state.

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Moore output depends on? | Current state only |
| Mealy output depends on? | Current state + inputs |
| Which has fewer states? | Mealy |
| Which has glitch-free output? | Moore |
| Divide-by-3 states? | 3 (S0, S1, S2) |
| Moore 1011 states? | 5 (S0-S4) |
| Mealy 1011 states? | 4 (S0-S3) |

---

## Exam-Relevant MCQ Patterns

1. **Moore vs Mealy definition** — output dependency (Q1, Q49, Q50)
2. **State count comparison** — Moore = N+1, Mealy = N for N-bit pattern (Q5, Q52, Q59)
3. **Binary encoding** — k FFs → 2ᵏ states (Q2, Q3, Q42)
4. **One-Hot encoding** — K states → K FFs (Q2)
5. **Divide-by-3 frequency** — f_out = f_in / 3 (Q6, Q39)
6. **Overlap detection** — suffix becomes prefix (Q57, Q62)
7. **Verilog default case** — prevents latches, safe recovery (Q8, Q47)
8. **Non-blocking (≤)** — state register block (Q7)

---

## Key Formulas (Memorize)

```
Binary encoding: k FFs → 2ᵏ states
One-Hot: K states → K FFs
Divide-by-N: f_out = f_in / N
Moore 1011: 5 states, Mealy 1011: 4 states
```
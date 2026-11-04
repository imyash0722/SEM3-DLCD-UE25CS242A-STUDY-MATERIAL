# 26. Exam Strategy & Quick Reference Card

> **Exam Date:** Check course schedule | **Course:** DLCD (UE25CS242A / UE25CS152B)

---

## Topic Weightage (Estimated)

| Unit | Topics | Weight |
|------|--------|--------|
| **Unit 1** | Combinational/Sequential Logic, Boolean Algebra, K-Maps, Building Blocks, Latches/FFs, Timing | ~50% |
| **Unit 2** | FSMs, State Encoding, Factoring, Arithmetic, Number Systems, FP | ~50% |

---

## High-Yield Topics (Must Master)

### Unit 1
1. ✅ **K-Map Minimization** (3 & 4 var, don't-cares, EPI identification)
2. ✅ **SOP/POS Conversion** (minterms/maxterms, Σ/Π notation)
3. ✅ **Boolean Minimization** (distributive, complement, identity laws)
4. ✅ **MUX/Decoder/Encoder** (implement logic, cascading formulas)
5. ✅ **SR Latch → D Latch → D FF** (transparency, edge-triggering)
6. ✅ **Setup/Hold/Metastability** (formulas, calculations)
6. ✅ **Timing Analysis** (RCA/CLA/Prefix delays, max frequency)

### Unit 2
1. ✅ **Moore vs Mealy** (output dependency, state count, overlap)
2. ✅ **FSM Design** (diagram → table → encoding → equations)
3. ✅ **State Encoding** (Binary vs One-Hot, factoring)
4. ✅ **Adders** (RCA, CLA, Prefix - delays, G/P signals)
5. ✅ **ALU/Comparator/Shifter/Multiplier** (operations, hardware)
6. ✅ **Fixed-Point** (Q-format, conversion, 2's complement, arithmetic)
7. ✅ **IEEE 754** (encoding/decoding, special values, FP addition)

---

## MCQ Answering Strategies

### K-Map Questions
1. Plot the map correctly (Gray code order!)
2. Find **all** prime implicants (largest groups)
3. Identify **essential** PIs (unique coverage)
4. Select minimum required PIs
5. **Watch for:** non-unique solutions, don't-cares, wrap-around

### Timing Questions
1. Identify: tpcq, tpd, tsetup, thold, tccq, tcd
2. **Setup check:** Tc ≥ tpcq + tpd + tsetup
2. **Hold check:** tccq + tcd ≥ thold
3. **Max freq:** 1 / (tpcq + tpd + tsetup)
4. **Ring osc:** f = 1/(2·N·tpd)

### FSM Questions
1. **Moore:** output in state circle
2. **Mealy:** output on transition arrow
3. **1011 pattern:** Moore=5 states, Mealy=4 states
4. **Overlap:** suffix becomes prefix
5. **Encoding:** Binary=log₂K FFs, One-Hot=K FFs
6. **Verilog:** non-blocking (≤) in state reg, default case

### Number System Questions
1. **2's comp range N-bit:** -2ⁿ⁻¹ to 2ⁿ⁻¹-1
2. **Negate:** invert + 1
3. **Fixed-point:** separate integer + fraction
4. **IEEE 754:** normalize → bias → drop leading 1
5. **Special:** E=0/F≠0=denorm, E=255/F=0=∞, E=255/F≠0=NaN

---

## Common Trap Questions

| Trap | Correct Approach |
|------|------------------|
| "Minimize using Boolean algebra" | Show each law step by step |
| "Essential PI" | Must cover a 1 no other PI covers |
| "Wrap-around" | Both row AND column edges (4-var) |
| "Don't-care" | Use only if it enlarges a group |
| "Setup vs Hold" | Setup=before edge, Hold=after edge |
| "Moore vs Mealy states" | Moore=N+1, Mealy=N for N-bit pattern |
| "Binary vs One-Hot FFs" | Binary=log₂K, One-Hot=K |
| "FP add first step after extract" | Prepend implicit 1 |
| "Shift right arithmetic" | Replicate MSB (sign bit) |
| "Ring oscillator even N" | Won't oscillate (stable) |

---

## Last-Minute Review Checklist

### Morning of Exam
- [ ] Formula card memorized
- [ ] K-map Gray code order: 00, 01, 11, 10
- [ ] Wrap-around: 4-var = both axes
- [ ] Setup: Tc ≥ tpcq + tpd + tsetup
- [ ] Hold: tccq + tcd ≥ thold
- [ ] 2's comp negate: invert + 1
- [ ] IEEE 754 single: 1/8/23, bias=127
- [ ] Moore 1011: 5 states, Mealy: 4 states
- [ ] Divide-by-3: 3 states, f/3
- [ ] MUX selects: log₂N
- [ ] Decoder outputs: 2ᴺ

### During Exam
- [ ] Read ALL options before choosing
- [ ] Eliminate obviously wrong answers
- [ ] For numerical: show work, box answer
- [ ] For K-maps: draw map, circle groups
- [ ] For Verilog: check non-blocking in seq
- [ ] Manage time: 1 min/MCQ, 10 min/descriptive

---

## Quick Reference: One-Page Cheat Sheet

```
┌─────────────────────────────────────────────────────────────┐
│                    DLCD EXAM QUICK REF                       │
├─────────────────────────────────────────────────────────────┤
│ K-MAP:     00 01 11 10  (Gray code)  Wrap: edges adjacent  │
│ EPI:       Covers minterm no other PI covers                │
│ DON'T CARE: X = 0 or 1, use to enlarge groups              │
├─────────────────────────────────────────────────────────────┤
│ SETUP:     Tc ≥ tpcq + tpd + tsetup    → fmax = 1/Tc       │
│ HOLD:      tccq + tcd ≥ thold                                │
│ METASTABLE: D changes in aperture → Q unstable             │
│ RING OSC:  f = 1/(2·N·tpd)                                  │
├─────────────────────────────────────────────────────────────┤
│ 2'S COMP:  [-2ⁿ⁻¹, 2ⁿ⁻¹-1]  Negate: invert + 1             │
│ FIXED Qm.n: m int, n frac  Weights: 2⁻¹,2⁻²...2⁻ⁿ          │
│ IEEE 754:  S(1)|E(8,bias=127)|F(23)  Value=(-1)ˢ·1.F·2ᴱ⁻¹²⁷│
│ SPECIAL:   E=0/F≠0=denorm  E=255/F=0=∞  E=255/F≠0=NaN      │
├─────────────────────────────────────────────────────────────┤
│ MOORE:     Out=state only  1011=5 states  Glitch-free      │
│ MEALY:     Out=state+input 1011=4 states  Faster response  │
│ OVERLAP:   Suffix → next prefix                             │
│ ENCODING:  Binary=⌈log₂K⌉ FFs  One-Hot=K FFs               │
│ FACTORING: N₁×N₂ states → N₁+N₂ states                     │
├─────────────────────────────────────────────────────────────┤
│ ADDERS:    RCA=N·tFA  CLA=parallel carry  Prefix=log N     │
│ G/P:       Gᵢ=AᵢBᵢ  Pᵢ=Aᵢ⊕Bᵢ                                │
│ SUB:       A-B = A+B̄+1 (Cin=1)                            │
│ OVERFLOW:  C_in,MSB ⊕ C_out,MSB                            │
│ COMPARATOR: N XNOR + N-input AND                            │
│ SHIFTER:   Logical=0-fill  Arith=sign-fill  Rotate=circular│
│ BARREL:    log₂N stages                                     │
│ MULT:      N+M bits                                         │
│ MUX:       N inputs → log₂N selects  Y=S̄D₀+SD₁            │
│ DECODER:   N:2ᴺ one-hot outputs                             │
│ VERILOG:   Seq=≤ @(posedge)  Comb=@(*)  Default in case    │
└─────────────────────────────────────────────────────────────┘
```

---

## Descriptive Question Prep

### Must-Practice Derivations
1. SOP → POS conversion (both directions)
2. Boolean minimization with law names
3. K-map grouping with PI/EPI identification
4. MUX/Decoder logic implementation
5. SR → D Latch → D FF evolution
6. Setup/Hold derivation from timing diagram
7. FSM: Diagram → Table → Encoding → Equations → Circuit
8. Binary ↔ Fixed-point ↔ IEEE 754 conversions
9. FP addition 8-step procedure
10. RCA/CLA/Prefix delay derivations

### Key Definitions to Write
- Minterm, Maxterm, Implicant, Prime Implicant, Essential PI
- Combinational vs Sequential circuit rules
- Setup time, Hold time, Metastability
- Moore vs Mealy machine
- One-Hot vs Binary encoding
- Normalized vs Denormalized FP
- Generate/Propagate signals

---

## Worked Examples (Full Traces)

### Example 1: K-Map Minimization (3-Var)
**Function:** F = Σ(3, 4, 6, 7)

**Step 1: Plot K-map**
```
BC
    00 01 11 10
A=0  0  0  1  0   (m3=1)
A=1  0  1  1  1   (m4,m6,m7=1)
```

**Step 2: Identify Prime Implicants**
- {m3,m7} vertical → bc (A changes)
- {m4,m6} horizontal → ac' (B changes)

**Step 3: Essential PIs**
- m3 only in {m3,m7} → bc essential
- m4 only in {m4,m6} → ac' essential
- m6 covered by both, m7 covered by bc

**Result:** F = bc + ac'

---

### Example 2: K-Map with Don't-Cares (4-Var)
**Function:** F = Σ(0,1,4,5,6) + d(7)

```
CD
    00 01 11 10
00   1  1  X  0
01   1  1  1  0
11   0  0  0  0
10   0  0  0  0
```

**Groups using X at m7:**
- {0,1,4,5} → b' (A,C change)
- {4,5,6,7} → a (B,C change with X)

**Result:** F = a + b'

---

### Example 3: Adder Delay Calculations (32-bit)

**Given:** t_FA = 300ps, t_AND_OR = 200ps, t_pg = 100ps, t_pg_prefix = 200ps, t_XOR = 100ps

**Ripple-Carry:**
t_RCA = 32 × 300ps = 9600ps = 9.6 ns

**CLA (4-bit blocks):**
N=32, k=4
t_pg = 100ps (gen all P,G)
t_pg_block = 600ps (4-bit block gen)
(N/k - 1) = 7 block carries
k·tFA = 4 × 300ps = 1200ps

t_CLA = 100 + 600 + 7×200 + 1200 = 3300ps = 3.3 ns

**Prefix Adder:**
log₂32 = 5
t_PA = 100 + 5×200 + 100 = 1200ps = 1.2 ns

---

### Example 4: Fixed-Point Arithmetic (Q4.4)

**Addition:** 2.125 + (-1.8125)

```
2.125  = 0010.0010
-1.8125 = 1110.0011  (2's comp: +1.8125=0001.1101 → inv=1110.0010 → +1=1110.0011)

Add:
  0010.0010
+ 1110.0011
= 0000.0101  (discard carry out)

Result: 0000.0101 = 0.3125 ✓ (2.125 - 1.8125 = 0.3125)
```

---

### Example 5: IEEE 754 Encoding (228₁₀ → 0x43640000)

```
1. 228 = 11100100₂
2. Normalize: 1.11001₂ × 2⁷
3. S = 0
4. E = 7 + 127 = 134 = 10000110₂
5. F = 11001 000... (23 bits)
6. Binary: 0 10000110 11001000000000000000000
7. Hex: 0100 0011 0110 0100 0000 0000 0000 0000 = 0x43640000
```

---

### Example 6: FP Addition (12.5 + 0.375 = 12.875)

```
12.5  = 1100.1₂ = 1.1001 × 2³
0.375 = 0.011₂  = 1.1 × 2⁻²

Align to exp 3:
0.375 mantissa: 1.1 >> 5 = 0.000011

Add mantissas:
  1.100100
+ 0.000011
= 1.100111 (×2³)

Normalize: already 1.xxx
Round: exact
Result: S=0, E=3+127=130=10000010, F=100111...
Hex: 0x40980000
```

---

### Example 7: Ring Oscillator

**3 Inverters, 2ns each:**
T = 2 × N × t_pd = 2 × 3 × 2ns = 12ns
f = 1/T = 83.33 MHz

**5 Inverters, 1ns each:**
T = 2 × 5 × 1ns = 10ns
f = 100 MHz

---

### Example 8: State Encoding Comparison

**Divide-by-3: Binary (2 FFs) vs One-Hot (3 FFs)**
```
Binary:
S0=00, S1=01, S2=10
Next-state logic complex

One-Hot:
S0=001, S1=010, S2=100
Next-state = rotate left (simple!)
```

---

## MCQ Patterns (Comprehensive)

### Unit 1 MCQs (60 Questions)

| # | Question | Answer |
|---|----------|--------|
| 1 | Registers in sync circuit share clock because... | Race condition avoidance |
| 2 | Essential prime implicant definition | Covers minterm no other PI covers |
| 3 | POS form construction | Product of maxterms for 0 outputs |
| 4 | D latch vs D FF key difference | Level vs edge triggered |
| 5 | 4:1 MUX select lines | 2 |
| 6 | AND gate with feedback (no FF) | Neither combinational nor sync seq |
| 7 | D latch vs FF with D changing at CLK=1 | Latch tracks all, FF only at edge |
| 8 | Black box specs | Functional + Timing |
| 9 | Minterm for 3 vars | Product with all 3 inputs |
| 10 | 2:1 MUX equation | Y = S'D₀ + SD₁ |
| ... | ... | ... |
| 53 | f_max calc 1+3.5+0.5=5ns | 200 MHz |
| 60 | 5-stage, 200ps each | 500 MHz |

### Unit 2 MCQs (Key Patterns)

| Topic | Pattern |
|-------|---------|
| Moore vs Mealy | Moore: state only, Mealy: state+input |
| 1011 Moore | 5 states |
| 1011 Mealy | 4 states |
| Binary Encoding | ⌈log₂K⌉ FFs |
| One-Hot | K FFs |
| Factoring | N₁×N₂ → N₁+N₂ states |
| Adders | RCA=O(N), CLA=parallel, Prefix=O(log N) |
| FP Add step 2 | Prepend implicit 1 |
| FP Special | E=0/F≠0=denorm, E=255/F=0=∞ |

---

## Verilog Quick Reference

```verilog
// D Flip-Flop
always @(posedge clk or posedge reset) begin
    if (reset) q <= 1'b0;
    else       q <= d;
end

// Enabled D FF (NO CLOCK GATING!)
always @(posedge clk or posedge reset) begin
    if (reset) q <= 1'b0;
    else if (en) q <= d;
end

// FSM Template (Moore)
always @(posedge clk or posedge reset) begin
    if (reset) state <= S0;
    else       state <= next_state;
end

always @(*) begin
    case (state)
        S0: next_state = x ? S1 : S0;
        S1: next_state = x ? S2 : S0;
        default: next_state = S0;
    endcase
end

always @(*) begin
    detect = (state == S4);  // Moore output
end

// FSM Template (Mealy)
always @(*) begin
    case (state)
        S0: begin
            next_state = x ? S1 : S0;
            detect = 1'b0;
        end
        S1: begin
            next_state = x ? S1 : S2;
            detect = x;
        end
    endcase
end
```

**Key Rules:**
- Sequential: Non-blocking (≤) in `@(posedge clk)`
- Combinational: Blocking (=) in `@(*)`
- Default case in FSM prevents latches
- No clock gating (use enable MUX at D)

---

## Final Tips

1. **Practice numerical problems** with timer
2. **Draw K-maps** for every minimization question
3. **Show all steps** in Boolean minimization (law names)
4. **Label FSM diagrams** clearly (states, transitions, outputs)
5. **Check units** in timing calculations (ns vs ps)
6. **Verify IEEE 754** by decoding back to decimal
7. **Read Verilog code** carefully (blocking vs non-blocking)
8. **Stay calm** — you know this material!

---

> **Good luck on your exam!** 🎓  
> *Consistent practice with K-maps, timing analysis, FSM design, number system conversions, MIPS assembly, and pipelining is the key to success.*
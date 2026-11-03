# 17. Exam Strategy & Quick Reference Card

> **Exam Date:** Check course schedule | **Course:** DLCD (UE25CS242A)

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
3. **Hold check:** tccq + tcd ≥ thold
4. **Max freq:** 1 / (tpcq + tpd + tsetup)
5. **Ring osc:** f = 1/(2·N·tpd)

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

## Final Tips

1. **Practice numerical problems** with timer
2. **Draw K-maps** for every minimization question
3. **Show all steps** in Boolean minimization (law names)
4. **Label FSM diagrams** clearly (states, transitions, outputs)
5. **Check units** in timing calculations (ns vs ps)
6. **Verify IEEE 754** by decoding back to decimal
7. **Read Verilog code** carefully (blocking vs non-blocking)
8. **Stay calm** — you know this material!
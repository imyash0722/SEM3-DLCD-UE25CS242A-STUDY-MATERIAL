# DLCD Exam Prep — UE25CS242A

> **Complete Study Guide for Digital Logic & Computer Design (Units 1-3)**  
> **Exam Date:** Check course schedule | **Textbook:** Harris & Harris, *Digital Design and Computer Architecture*

---

## 📚 Navigation

### Unit 1: Combinational & Sequential Logic Design
1. [01. Digital Circuits — Introduction & Combinational vs Sequential](01_digital-circuits-introduction.md)
2. [02. Boolean Equations — Minterms, Maxterms, SOP & POS](02_boolean-equations.md)
3. [03. Logic Minimization — Boolean Algebra & K-Maps (3-Var)](03_logic-minimization-kmaps-3var.md)
4. [04. K-Maps (4-Variable) & Seven-Segment Decoder](04_kmaps-4var-seven-segment.md)
5. [05. Combinational Building Blocks — Mux, Decoder, Encoder](05_combinational-building-blocks.md)
6. [06. Sequential Logic Basics — Latches, SR Latch, D Latch](06_sequential-basics-latches.md)
7. [07. Flip-Flops — D FF, Master-Slave, Timing, Metastability](07_flipflops-timing-metastability.md)

### Unit 2: FSMs & Digital Building Blocks
8. [08. Finite State Machines — Moore vs Mealy, Design Process](08_fsm-moore-mealy-design.md)
9. [09. State Encoding & Factoring State Machines](09_state-encoding-factoring.md)
10. [10. Arithmetic Circuits — Adders (RCA, CLA, Prefix)](10_arithmetic-adders.md)
11. [11. ALU, Comparators, Shifters & Multipliers](11_alu-comparator-shifter-multiplier.md)
12. [12. Number Systems — Fixed-Point & Signed Representations](12_number-systems-fixedpoint.md)
13. [13. Floating-Point — IEEE 754 Single/Double Precision](13_floating-point-ieee754.md)

### Practice & Reference
14. [14. Lab Code Patterns — Verilog Examples](14_lab-verilog-patterns.md)
15. [15. Comprehensive MCQ Practice — Unit 1 & 2](15_mcq-practice-comprehensive.md)
16. [16. Numerical Examples — Full Traces & Worked Solutions](16_numerical-examples-full-traces.md)
17. [17. Exam Strategy & Quick Reference Card](17_exam-strategy-quick-ref.md)

---

## ✅ Study Checklist

### Unit 1: Combinational & Sequential Logic
- [ ] **Digital Circuits** — Black box specs, combinational vs sequential, propagation delay
- [ ] **Boolean Equations** — Minterms, maxterms, SOP/POS, Σ/Π notation, conversions
- [ ] **Logic Minimization** — Boolean laws (distributive, complement, identity), step-by-step
- [ ] **K-Maps (3-var)** — Structure, Gray code, wrap-around, PI/EPI, don't-cares
- [ ] **K-Maps (4-var)** — Structure, wrap-around (both axes), 7-seg decoder, don't-cares
- [ ] **Building Blocks** — MUX (2:1, 4:1, cascading, lookup), Decoder (N:2ᴺ, logic), Encoder (priority)
- [ ] **Latches** — SR latch (NOR), invalid state, D latch (transparent/opaque), D = WHAT, CLK = WHEN
- [ ] **Flip-Flops** — Master-slave D FF, edge-triggering, setup/hold/metastability, timing constraints
- [ ] **Timing Analysis** — Setup constraint, hold constraint, max frequency, ring oscillator
- [ ] **Enabled/Resettable FFs** — MUX at D (no clock gating), sync vs async reset
- [ ] **T/JK from D FF** — D = T⊕Q, D = JQ'+K'Q

### Unit 2: FSMs & Digital Building Blocks
- [ ] **FSM Basics** — 3-block structure, Moore vs Mealy, state register, next-state/output logic
- [ ] **FSM Design** — Traffic light, divide-by-3, pattern recognizer (1011)
- [ ] **Moore 1011** — 5 states, overlap transitions, output in S4
- [ ] **Mealy 1011** — 4 states, detect on S3+input=1 transition
- [ ] **State Encoding** — Binary (⌈log₂K⌉ FFs) vs One-Hot (K FFs), trade-offs
- [ ] **Factoring** — Unfactored (N₁×N₂) vs Factored (N₁+N₂), parade mode example
- [ ] **Adders** — Half/Full adder, RCA (O(N)), CLA (G/P, block), Prefix (O(log N)), delay formulas
- [ ] **Subtraction** — 2's complement, Cin=1, overflow = C_in,MSB ⊕ C_out,MSB
- [ ] **ALU** — F₂:₀ control, SLT uses sign bit of A-B
- [ ] **Comparators** — Equality: XNOR+AND, Magnitude: MSB-first or subtractor
- [ ] **Shifters** — Logical (0-fill), Arithmetic (sign-fill), Rotate, Barrel (log N stages)
- [ ] **Multipliers/Dividers** — Array multiplier, shift-add, N×M → N+M bits
- [ ] **Fixed-Point** — Q-format, implied binary point, 2's complement, conversion, arithmetic
- [ ] **Floating-Point** — IEEE 754 single (1/8/23, bias=127), double (1/11/52, bias=1023)
- [ ] **FP Special Values** — ±0, denorm, ±∞, NaN
- [ ] **FP Addition** — 8 steps: extract→prepend 1→compare→shift→add→normalize→round→assemble

---

## 🎯 High-Yield MCQ Patterns

| Topic | Key Patterns |
|-------|--------------|
| **K-Maps** | Gray code order, wrap-around (both axes 4-var), EPI = unique coverage, don't-care enlarges groups |
| **Timing** | Tc ≥ tpcq+tpd+tsetup, tccq+tcd≥thold, fmax=1/(tpcq+tpd+tsetup), ring osc f=1/(2N·tpd) |
| **FSM** | Moore=state only (N+1 states for N-bit pattern), Mealy=state+input (N states), overlap=suffix→prefix |
| **Encoding** | Binary FFs=⌈log₂K⌉, One-Hot FFs=K, Factoring=N₁×N₂→N₁+N₂ |
| **Adders** | RCA=O(N), CLA=parallel G/P, Prefix=O(log N), fastest=Prefix |
| **Number Systems** | 2's comp range=[-2ⁿ⁻¹,2ⁿ⁻¹-1], negate=invert+1, FP bias=127/1023 |
| **FP** | +∞=E=255/F=0, NaN=E=255/F≠0, denorm=E=0/F≠0, add step 2=prepend 1 |
| **Verilog** | Seq=non-blocking (≤), Comb=blocking (=), default in case, no clock gating |

---

## 📝 Numerical Problem Types to Practice

1. **K-Map Minimization** — 3 & 4 variable, with don't-cares
2. **Propagation Delay** — RCA/CLA/Prefix with given parameters
3. **Max Frequency** — Given tpcq, tpd, tsetup → find fmax
4. **Hold Time Check** — Given tccq, tcd, thold → pass/fail
5. **Ring Oscillator** — N inverters, tpd → period/freq
6. **2's Complement** — Negate, range, arithmetic
7. **Fixed-Point** — Decimal ↔ Qm.n conversion, addition
8. **IEEE 754** — Decimal ↔ hex encoding/decoding
9. **FP Addition** — Full 8-step trace
10. **State Encoding** — Binary vs One-Hot FF count
11. **Divide-by-N** — f_out = f_in/N

---

## 📖 Recommended Study Order

### Week 1: Unit 1 Foundations
1. Topics 1–2: Digital circuits, Boolean equations
2. Topics 3–4: K-Maps (3 & 4 var) — **CRITICAL**
3. Topics 5–6: Building blocks, Latches
4. Topic 7: Flip-flops & timing — **CRITICAL**

### Week 2: Unit 2 Core
1. Topic 8: FSM basics, Moore vs Mealy
2. Topic 9: State encoding, Factoring
3. Topic 10: Adders (delays, G/P) — **CRITICAL**
4. Topic 11: ALU, Comparator, Shifter, Multiplier

### Week 3: Number Systems & Practice
1. Topics 12–13: Fixed-point, Floating-point — **CRITICAL**
2. Topic 14: Verilog patterns
3. Topic 15: MCQ practice (all 155+ questions)
4. Topic 16: Numerical examples with full traces

### Week 4: Final Review
1. Topic 17: Exam strategy & quick reference card
2. Re-do all MCQs, focus on wrong answers
3. Practice numerical problems under time pressure
4. Memorize quick reference card

---

## 🔑 Memorize These Formulas

```
Setup:       Tc ≥ tpcq + tpd + tsetup
Hold:        tccq + tcd ≥ thold
f_max:       1 / (tpcq + tpd + tsetup)
Ring osc:    f = 1/(2·N·tpd)
2's comp:    [-2ⁿ⁻¹, 2ⁿ⁻¹-1]     Negate: invert + 1
IEEE 754 S:  1|8|23  bias=127    Value=(-1)ˢ·1.F·2ᴱ⁻¹²⁷
IEEE 754 D:  1|11|52 bias=1023
RCA:         N × tFA
CLA:         t_pg + t_pg_block + (N/k-1)t_AND_OR + k·tFA
Prefix:      t_pg + log₂N·t_pg_prefix + t_XOR
MUX sel:     log₂N
Dec out:     2ᴺ
Div-N:       f_out = f_in/N
Bin FFs:     ⌈log₂K⌉
One-Hot:     K
Factored:    N₁+N₂
Equality:    Π(Aᵢ ⊙ Bᵢ)
<< N:        × 2ᴺ
>>> N:       ÷ 2ᴺ (signed)
Mult:        N+M bits
```

---

## 📚 Source Materials Referenced

- **Lecture Slides:** Unit 1 (Slides 2–210), Unit 2 (Slides 2–138), Unit 3 (Slides 3.1–3.17)
- **Textbook:** Harris & Harris, *Digital Design and Computer Architecture* (Ch. 1–5)
- **Question Banks:** Unit 1 (110 Qs), Unit 2 (32 Qs) — deduplicated
- **MCQs:** Unit 1 (60 Qs), Unit 2 (135 Qs) — with explanations
- **Lab:** Week 8 — Prefix Adder, Comparator Verilog

---

## 🌐 Site Features

- **Dark/Light mode** — Toggle in top-right header
- **Search** — Full-text search across all topics
- **Table of Contents** — Auto-generated per page
- **Code Copy** — One-click copy for Verilog examples
- **Task Lists** — Interactive checkboxes in study checklist
- **Tabs** — Organized content sections

---

> **Good luck on your exam!** 🎓  
> *Consistent practice with K-maps, timing analysis, FSM design, and number system conversions is the key to success.*
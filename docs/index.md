# DLCD Exam Prep — UE25CS242A

> **Complete Study Guide for Digital Logic & Computer Design (Units 1-3)**  
> **Exam Date:** Check course schedule | **Textbook:** Harris & Harris, *Digital Design and Computer Architecture*

**🌐 Live Site:** https://imyash0722.github.io/SEM3-DLCD-UE25CS242A-STUDY-MATERIAL/
**📁 Repository:** https://github.com/imyash0722/SEM3-DLCD-UE25CS242A-STUDY-MATERIAL

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

### Unit 3: Computer Architecture
14. [14. Sequential Building Blocks — Registers, Memory, Counters](14_sequential-building-blocks.md)
15. [15. Computer Architecture Intro — Von Neumann, Memory Map, Performance](15_computer-architecture-intro.md)
16. [16. Assembly Language — MIPS Instructions, Registers, Functions](16_assembly-language.md)
17. [17. Machine Language — Instruction Encoding, Decoding, Stored Program](17_machine-language.md)
18. [18. Addressing Modes — Register, Immediate, Base, PC-Relative, Pseudo-Direct](18_addressing-modes.md)
19. [19. Compiling, Assembling, Linking & Loading — Program Translation Pipeline](19_compiling-assembling-loading.md)
20. [20. Parallelism — Spatial vs Temporal, Pipelining, Hazards, Performance](20_parallelism.md)
21. [21. Classwork Problems — Worked Exercises (Counters, ROM, Memory, FSM)](21_classwork-problems.md)
22. [22. Unit 3 MCQ Practice — Architecture, Assembly, Memory, Parallelism](22_unit3-mcq-practice.md)

### Lab & Practice
23. [23. Lab Code Patterns — Verilog Examples](23_lab-verilog-patterns.md)
24. [24. Comprehensive MCQ Practice — Unit 1 & 2](24_mcq-practice-comprehensive.md)
25. [25. Numerical Examples — Full Traces & Worked Solutions](25_numerical-examples-full-traces.md)
26. [26. Exam Strategy & Quick Reference Card](26_exam-strategy-quick-ref.md)

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

### Unit 3: Computer Architecture
- [ ] **Sequential Building Blocks** — Registers, register file, SRAM/DRAM, counters
- [ ] **Architecture Intro** — Von Neumann vs Harvard, MIPS memory map, performance metrics
- [ ] **Assembly Language** — MIPS registers, instruction formats, arithmetic/logical/shift/load/store/branch/jump
- [ ] **Machine Language** — R/I/J-type encoding, decoding, stored program concept
- [ ] **Addressing Modes** — Register, Immediate, Base, PC-Relative, Pseudo-Direct (formulas, examples)
- [ ] **Compiling/Assembling/Loading** — 2-pass assembler, linker, loader, MIPS memory map
- [ ] **Parallelism** — Spatial vs temporal, pipelining, hazards, Amdahl's Law, cookie analogy
- [ ] **Classwork Problems** — Counters, ROM, memory endianness, FSM derivation
- [ ] **MCQ Practice** — 60+ Unit 3 MCQs with explanations

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
| **Architecture** | Von Neumann bottleneck, MIPS memory map segments, $gp vs $sp, Amdahl's Law |
| **Assembly** | Register conventions, branch vs jump, immediate extension, function calls, stack |
| **Addressing** | Register=R-type, Immediate=constant, Base=lw/sw, PC-Rel=beq/bne, Pseudo-Direct=j/jal |
| **Pipeline** | Clock=slowest stage, TP=1/Tc, Latency=N×Tc, Hazards: Data=forwarding, Control=prediction |
| **MCU** | op=0→R-type, op=35→lw, op=43→sw, op=4→beq, op=2→j; funct: add=32, sub=34, jr=8 |

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
12. **Pipeline Timing** — Non-pipelined vs 2/3-stage with given stage delays
13. **Cookie/Parallelism** — Spatial vs Temporal throughput calculations
14. **Endianness** — Byte ordering, detection
15. **Branch Offset** — (target - (PC+4)) / 4

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

### Week 3: Unit 2 Number Systems & Unit 3 Intro
1. Topics 12–13: Fixed-point, Floating-point — **CRITICAL**
2. Topic 14: Sequential Building Blocks
3. Topic 15: Architecture Intro & Memory Map

### Week 4: Unit 3 Core
1. Topic 16: Assembly Language (MIPS)
2. Topic 17: Machine Language & Addressing Modes
3. Topic 18: Compiling/Assembling/Loading
4. Topic 19: Parallelism & Pipelining

### Week 5: Unit 3 Practice & Review
1. Topic 20: Classwork Problems
2. Topic 21: Unit 3 MCQ Practice
3. Topic 22: Lab Verilog Patterns
4. Topic 23: Comprehensive MCQ Practice (Units 1 & 2)
5. Topic 24: Numerical Examples with full traces

### Week 6: Final Review
1. Topic 25: Exam Strategy & Quick Reference Card
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
- **Textbook:** Harris & Harris, *Digital Design and Computer Architecture* (Ch. 1–7)
- **Question Banks:** Unit 1 (110 Qs), Unit 2 (32 Qs) — deduplicated
- **MCQs:** Unit 1 (60 Qs), Unit 2 (135 Qs), Unit 3 (60 Qs) — with explanations
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

## 🌐 Site Links

**🌐 Live Site:** https://imyash0722.github.io/SEM3-DLCD-UE25CS242A-STUDY-MATERIAL/
**📁 GitHub Repo:** https://github.com/imyash0722/SEM3-DLCD-UE25CS242A-STUDY-MATERIAL

---

> **Good luck on your exam!** 🎓  
> *Consistent practice with K-maps, timing analysis, FSM design, number system conversions, MIPS assembly, and pipelining is the key to success.*
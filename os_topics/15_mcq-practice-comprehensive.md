# 15. Comprehensive MCQ Practice — Unit 1 & 2

> **Source:** DLCD_Unit_1_MCQs.md, DLCD_Unit_2_MCQs.md

---

## Unit 1 MCQs (Combinational & Sequential Logic)

### Digital Circuits & Boolean Algebra
| # | Question | Answer | Key |
|---|----------|--------|-----|
| 1 | Registers in sync circuit share clock because... | Race condition avoidance | Q1 |
| 2 | Essential prime implicant definition | Covers minterm no other PI covers | Q2 |
| 3 | POS form construction | Product of maxterms for 0 outputs | Q3 |
| 4 | D latch vs D FF key difference | Level vs edge triggered | Q4 |
| 5 | 4:1 MUX select lines | 2 | Q5 |
| 6 | AND gate with feedback (no FF) | Neither combinational nor sync seq | Q6 |
| 7 | D latch vs FF with D changing at CLK=1 | Latch tracks all, FF only at edge | Q7 |
| 8 | Black box specs | Functional + Timing | Q8 |
| 9 | Minterm for 3 vars | Product with all 3 inputs | Q9 |
| 10 | 2:1 MUX equation | Y = S'D₀ + SD₁ | Q10 |
| 11 | a'+a=1 law | Complement law | Q11 |
| 12 | Parallel E1=5, E2=8, then E3=4 | 12 ns | Q12 |
| 13 | Cyclic path no register | Not combinational | Q13 |
| 14 | Minterms for n vars | 2ⁿ | Q14 |
| 15 | Only combinational set | Adder, Mux, Decoder | Q15 |
| 16 | Minimize a'bc+ab'c'+abc'+abc | bc + ac' | Q16 |
| 17 | Ben picnic SOP | E = A'R' | Q17 |
| 18 | Unresolved race = unstable | Depends on timing/order | Q18 |
| 19 | K-map Σ(1,3,4,5,6,7) minimal | a + c | Q19 |
| 20 | Decoder one-hot | Exactly one output HIGH | Q20 |
| 21 | Reset on FF | Forces Q=0 overriding D | Q21 |
| 22 | Don't-care 111, Σ(0,1,4,5,6)+d(7) | a + b' | Q22 |
| 23 | Tristate states | 0, 1, Z | Q23 |
| 24 | SOP construction | OR minterms for Y=1 | Q24 |
| 25 | Master-slave CLK=0 | Master transparent, slave opaque | Q25 |
| 26 | K-map Gray code reason | Adjacent differ by 1 bit | Q26 |
| 27 | X in K-map | Unspecified, use 0 or 1 | Q27 |
| 28 | D latch transparent | CLK = 1 | Q28 |
| 29 | N:2ᴺ decoder outputs | 2ᴺ | Q29 |
| 30 | Literal definition | Variable or complement | Q30 |
| 31 | Wrap-around | Edges adjacent | Q31 |
| 32 | Non-unique minimal | Different non-EPI choices | Q32 |
| 33 | Combinational vs Sequential | Memoryless vs has state | Q33 |
| 34 | Maxterm M₆ (3 vars) | a' + b' + c | Q34 |
| 35 | Σ(3,7,11,15) common | C=1, D=1 | Q35 |
| 36 | Moore's Law | Transistors double ~18mo | Q36 |
| 37 | Sync sequential rule | All cycles have reg, common clock | Q37 |
| 38 | 3-var func with decoder | 3:8 decoder + OR | Q38 |
| 39 | EPI identification | Unique coverage → essential | Q39 |
| 40 | Cross-coupled inverters | Two stable states = 1 bit | Q40 |
| 41 | Group of 8 in 4-var | 1 literal | Q41 |
| 42 | Prime implicant def | Largest grouping can't enlarge | Q42 |
| 43 | 3-var func Σ(1,3,6) decoder | 3:8 decoder, outputs 1,3,6 to OR | Q43 |
| 44 | SR latch construction | 2 cross-coupled NOR | Q44 |
| 45 | Maxterm definition | Sum with all inputs | Q45 |
| 46 | 3-inv ring osc, 1ns each | 6 ns period | Q46 |
| 47 | NOR SR latch S=R=1 | Q=Q'=0 invalid | Q47 |
| 48 | N-bit register | N FFs, common CLK | Q48 |
| 49 | 2:1 MUX for AND | I₀=0, I₁=B (S=A) | Q49 |
| 50 | Setup time def | D stable before CLK↑ | Q50 |
| 51 | Hold time def | D stable after CLK↑ | Q51 |
| 52 | Setup constraint | Tc ≥ tpcq + tpd + tsetup | Q52 |
| 53 | f_max calc 1+3.5+0.5=5ns | 200 MHz | Q53 |
| 54 | Hold constraint | tccq + tcd ≥ thold | Q54 |
| 55 | Metastability | D in aperture → unstable Q | Q55 |
| 56 | T FF from D FF | D = T ⊕ Q | Q56 |
| 57 | Enabled FF no clock gate | MUX at D: EN·D + EN'·Q | Q57 |
| 58 | Sync vs Async reset | Sync at edge, async immediate | Q58 |
| 59 | Ring osc freq formula | f = 1/(2·N·tpd) | Q59 |
| 60 | 5-stage, 200ps each | 500 MHz | Q60 |

---

## Unit 2 MCQs (FSM, Arithmetic, Number Systems)

### FSM
| # | Question | Answer | Key |
|---|----------|--------|-----|
| 1 | Moore vs Mealy diff | Moore: state only, Mealy: state+input | Q1 |
| 2 | 8 states One-Hot FFs | 8 | Q2 |
| 3 | 5 FFs binary max states | 32 | Q3 |
| 4 | Moore advantage | Glitch-free, sync outputs | Q4 |
| 5 | Moore 1011 states | 5 | Q5 |
| 6 | Divide-by-3, 30MHz in | 10 MHz out | Q6 |
| 7 | Verilog state reg non-block | ≤ in clocked block | Q7 |
| 8 | Default case in FSM | Prevent latches, safe recovery | Q8 |
| 9 | Factored FSM advantage | N₁×N₂ → N₁+N₂ states | Q9 |

### Arithmetic
| # | Question | Answer | Key |
|---|----------|--------|-----|
| 10 | Half Adder Sum, Cout | S=A⊕B, Cout=AB | Q10 |
| 11 | Full Adder from HA | 2 HA + 1 OR | Q11 |
| 12 | RCA delay | N × tFA | Q12 |
| 13 | CLA Generate | Gᵢ = Aᵢ·Bᵢ | Q13 |
| 14 | CLA Block P₃:₀ | P₃·P₂·P₁·P₀ | Q14 |
| 15 | Prefix delay | O(log N) | Q15 |
| 16 | Subtraction 2's comp | Invert B, Cin=1 | Q16 |
| 17 | Overflow signed | C_in,MSB ⊕ C_out,MSB | Q17 |
| 18 | Equality comparator | N XNOR + N-input AND | Q18 |
| 19 | Logical vs Arith shift | Logical=0 fill, Arith=sign fill | Q19 |
| 20 | 11110000 >>> 2 | 11111100 (-4) | Q20 |
| 21 | 16-bit barrel shifter stages | 4 (log₂16) | Q21 |
| 22 | N×M multiply bits | N+M | Q22 |
| 23 | SLT hardware | A-B, take sign bit | Q23 |
| 24 | 2's comp range N-bit | -2ᴺ⁻¹ to 2ᴺ⁻¹-1 | Q24 |
| 25 | Why 2's comp preferred | Same adder, unique zero | Q25 |
| 26 | Fixed 0011.1010 (4.4) | 3.625 | Q26 |
| 27 | -7.5 in Q4.4 2's comp | 1000.1000 | Q27 |
| 28 | IEEE 754 single bits | 1/8/23 | Q28 |
| 29 | IEEE 754 bias | 127 | Q29 |
| 30 | Implicit leading 1 | Always 1 normalized | Q30 |
| 31 | +∞ encoding | S=0, E=255, F=0 | Q31 |
| 32 | NaN encoding | E=255, F≠0 | Q32 |
| 33 | E=0, F≠0 | Denormalized | Q33 |
| 34 | 228 IEEE 754 hex | 0x43640000 | Q34 |
| 35 | -58.25 IEEE 754 hex | 0xC2690000 | Q35 |
| 36 | FP add step after extract | Prepend implicit 1 | Q36 |
| 37 | Shift smaller mantissa | Align exponents | Q37 |
| 38 | NOT signed fixed-point | Excess-127 | Q38 |
| 39 | Divide-by-3 purpose | f_out = f_in/3 | Q39 |
| 40 | Divide-by-3 states | 3 | Q40 |
| 41 | After S2 in div-3 | S0 | Q41 |
| 42 | Min bits for 3 states | 2 | Q42 |
| 43 | Verilog state update | always @(posedge clk) | Q43 |
| 44 | Reset purpose | Initialize to known state | Q44 |
| 45 | Div-3 transitions | S0→S1→S2→S0 | Q45 |
| 46 | next_state purpose | State for next clock edge | Q46 |
| 47 | Default case FSM | Handle invalid states | Q47 |
| 48 | After S1 in S0→S1→S2→S0 | S2 | Q48 |
| 49 | Pattern recognizer purpose | Detect bit sequence | Q49 |
| 50 | Moore output depends on | Present state only | Q50 |
| 51 | 1011 Moore detect state | Final detection state | Q51 |
| 52 | Moore 1011 states | 5 | Q52 |
| 53 | 1011 progression | S0→S1→S2→S3→S4 | Q53 |
| 54 | Verilog next-state | case statement | Q54 |
| 55 | Moore output block | Output from state only | Q55 |
| 56 | Reset purpose | Known initial state | Q56 |
| 57 | Overlap detection | Suffix = next prefix | Q57 |
| 58 | Default next-state | Safe recovery | Q58 |
| 59 | Mealy 1011 states | 4 | Q59 |
| 60 | Mealy detect when | In matched-101, input=1 | Q60 |
| 61 | Mealy vs Moore diff | Mealy: state+input, Moore: state | Q61 |
| 62 | Overlap meaning | Bit shared between patterns | Q62 |

### Additional Arithmetic (Q63-Q95)
| # | Question | Answer |
|---|----------|--------|
| 63 | CPA types | Ripple, CLA, Prefix, Skip |
| 64 | RCA delay | N × tFA |
| 65 | Prefix delay | t_pg + log₂N·t_pg_prefix + t_XOR |
| 66 | Half Adder Sum | A ⊕ B |
| 67 | Full Adder Cout | AB + ACin + BCin |
| 68 | Fastest large adder | Prefix |
| 69 | CLA speedup | Parallel carry compute |
| 70 | ALU does | Arithmetic + Logic |
| 71 | << 1 = | × 2 |
| 72 | Comparator | Magnitude compare |
| 73 | Multiply partial products | AND per bit |
| 74 | log₂N delay | Prefix adder |
| 75 | 32-bit fastest adder | Prefix, 1.2ns |
| 76 | Subtraction hardware | Invert B, +1, Cin=1 |
| 77 | Multiply by 16 | Logical << 4 |
| 78 | A-B sign=1 means | A < B |
| 79 | F2=1, F1:0=10 → | A - B |
| 80 | 11001 LSR 2 | 00110 |
| 81 | 7+4=11 in 4-bit signed | Overflow (flag=1) |
| 82 | 32×32 mult product | 64 bits |
| 83 | 16-bit log shifter MUXes | 16×16 |
| 84 | Prefix for 128-bit | Logarithmic delay |
| 85 | 64-bit RCA vs CLA | CLA faster (~3.9ns vs 16ns) |
| 86 | A=25,B=32,SLT→Y | 1 |
| 87 | 4-bit equality gate | XNOR |
| 88 | A-B Cin | 1 |
| 89 | CLA faster because | Parallel carry via G/P |
| 90 | Half adder outputs | Sum, Cout |

### Fixed-Point (Q91-Q115)
| # | Question | Answer |
|---|----------|--------|
| 91 | Fixed-point binary point | Fixed predetermined |
| 92 | 8-bit 4.4 format | 0110.1100 |
| 93 | 0110.1100 decimal | 6.75 |
| 94 | Rightmost weight Q4.4 | 2⁻⁴ |
| 95 | 0.1000₂ decimal | 0.5 |
| 96 | 0.75 Q4.4 | 0000.1100 |
| 97 | Signed fixed-point reps | 2's comp or sign-mag |
| 98 | Sign-mag MSB | Sign |
| 99 | 0.625 binary | 0.1010 |
| 100 | Min frac Q4.4 | 2⁻⁴ |
| 101 | 0011.0110 decimal | 3.375 |
| 102 | +2.375 sign-mag neg | 1010.0110 |
| 103 | +2.375 2's comp neg | 1101.1010 |
| 104 | Sign-mag vs 2's comp | Sign bit flip vs invert+1 |
| 105 | Fixed-point value | 2.6875 |
| 106 | 2's comp advantage | Same adder for +/- |
| 107 | +0.75 Q4.4 | 0000.1100 |
| 108 | +0.625 2's comp neg Q4.4 | 1111.0110 |
| 109 | Fixed-point add | 0000.0010 |
| 110 | 01101100 value unknown | Need binary point pos |
| 111 | Pattern value | 3.25 |
| 112 | 00110100 2 frac bits | 13 |
| 113 | -2.375 Q4.4 2's comp | 1101.1010 |
| 114 | LSB weight Q4.4 | 0.0625 |
| 115 | FALSE fixed-point | Binary point from bits |

### Floating-Point (Q116-Q135+)
| # | Question | Answer |
|---|----------|--------|
| 116 | FP advantage | Wide range large/small |
| 117 | FP analogous to | Scientific notation |
| 118 | IEEE 754 single bits | 32 |
| 119 | Sign bit 0 | Positive |
| 120 | Bias single | 127 |
| 121 | Actual exp -3 → biased | 124 |
| 122 | 20 normalized | 1.01 × 2⁴ |
| 123 | 12 normalized | 1.1 × 2³ |
| 124 | 1.101×2⁴ actual exp | 4 |
| 125 | Leading 1 not stored | Always 1 normalized |
| 126 | Actual +10 → biased | 137 |
| 127 | Biased 130 → actual | 3 |
| 128 | E=10000010 → actual | 3 |
| 129 | 40=1.01×2⁵ biased | 132 |
| 130 | +40 IEEE 754 | 0 10000100 01000... |
| 131 | 18.5 normalized | 1.00101 × 2⁴ |
| 132 | 1 10000011 00101... | -5 |
| 133 | 1 10000010 11101... | 123 |
| 134 | ∞/NaN exponent | All 1s |
| 135 | Double precision digits | ~15 |

---

## High-Yield Patterns to Memorize

1. **Setup constraint:** `Tc ≥ tpcq + tpd + tsetup`
2. **Hold constraint:** `tccq + tcd ≥ thold`
3. **Max freq:** `1 / (tpcq + tpd + tsetup)`
4. **Ring osc:** `f = 1/(2·N·tpd)`
5. **2's comp range N-bit:** `[-2ⁿ⁻¹, 2ⁿ⁻¹-1]`
6. **Negation:** invert + 1
7. **IEEE 754 single:** `S(1)|E(8,bias=127)|F(23)`
8. **FP add order:** Extract→Prepend 1→Compare→Shift→Add→Normalize→Round→Assemble
9. **RCA delay:** `N × tFA`
10. **CLA delay:** `t_pg + t_pg_block + (N/k-1)t_AND_OR + k·tFA`
11. **Prefix delay:** `t_pg + log₂N·t_pg_prefix + t_XOR`
12. **Moore 1011:** 5 states, Mealy 1011: 4 states
13. **Divide-by-N:** `f_out = f_in/N`
14. **Binary FFs:** `⌈log₂K⌉`, One-Hot: `K`
15. **Factoring:** `N₁×N₂ → N₁+N₂`
16. **Equality:** `N XNOR + AND`
17. **SLT:** Sign of A-B
18. **Shift:** `<<N = ×2ᴺ`, `>>>N = ÷2ᴺ`
19. **Multiply N×M:** `N+M` bits
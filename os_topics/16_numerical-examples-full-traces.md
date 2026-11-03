# 16. Numerical Examples — Full Traces & Worked Solutions

> **Source:** Question Banks, Lecture Slides, MCQ Explanations

---

## K-Map Minimization Traces

### Example 1: 3-Var `F = Σ(3, 4, 6, 7)`
```
Step 1: Plot K-map
BC
    00 01 11 10
A=0  0  0  1  0   (m3=1)
A=1  0  1  1  1   (m4,m6,m7=1)

Step 2: Identify Prime Implicants
- {m3,m7} vertical → bc (A changes)
- {m4,m6} horizontal → ac' (B changes)

Step 3: Essential PIs
- m3 only in {m3,m7} → bc essential
- m4 only in {m4,m6} → ac' essential
- m6 covered by both, m7 covered by bc

Step 4: Result
F = bc + ac'
```

---

### Example 2: 3-Var `F = Σ(0, 2, 3, 4, 6, 7)`
```
BC
    00 01 11 10
A=0  1  0  1  1
A=1  1  0  1  1

PIs:
- {0,2,4,6} (col 00,10) → a (B,C change)
- {3,7} → c (A,B change)
- {2,3,6,7} → b'c+bc' (but not maximal)

EPIs: {0,2,4,6} covers m0,m4 uniquely → a essential
{3,7} covers m3 uniquely → c essential
All 1s covered!

Result: F = a + c  (or a + b'c + bc')
```

---

### Example 3: 4-Var with Don't-Cares `F = Σ(0,1,4,5,6) + d(7)`
```
CD
    00 01 11 10
00   1  1  X  0
01   1  1  1  0
11   0  0  0  0
10   0  0  0  0

Groups using X at m7:
- {0,1,4,5} → b' (A,C change)
- {4,5,6,7} → a (B,C change with X)

Result: F = a + b'
```

---

## Adder Delay Calculations

### Example: 32-bit Adders
**Given:** `t_FA = 300ps`, `t_AND_OR = 200ps`, `t_pg = 100ps`, `t_pg_prefix = 200ps`, `t_XOR = 100ps`

#### Ripple-Carry
```
t_RCA = 32 × 300ps = 9600ps = 9.6 ns
```

#### CLA (4-bit blocks)
```
N=32, k=4
t_pg = 100ps (gen all P,G)
t_pg_block = 600ps (4-bit block gen)
(N/k - 1) = 7 block carries
k·tFA = 4 × 300ps = 1200ps

t_CLA = 100 + 600 + 7×200 + 1200 = 3300ps = 3.3 ns
```

#### Prefix Adder
```
log₂32 = 5
t_PA = 100 + 5×200 + 100 = 1200ps = 1.2 ns
```

---

## FSM Timing Analysis

### Divide-by-3 Counter (30 MHz input)
```
States: S0(00) → S1(01) → S2(10) → S0
Output Y=1 only in S0

Period: 3 cycles
f_out = f_in / 3 = 30 MHz / 3 = 10 MHz
```

### Moore 1011 Pattern Recognizer
```
State sequence for input 1,0,1,1:
S0 --1--> S1 --0--> S2 --1--> S3 --1--> S4 (detect=1)
Overlap: S4 --1--> S1, S4 --0--> S2
```

---

## Fixed-Point Arithmetic

### Q4.4 Addition: 2.125 + (-1.8125)
```
2.125  = 0010.0010
-1.8125 = 1110.0011  (2's comp: +1.8125=0001.1101 → inv=1110.0010 → +1=1110.0011)

Add:
  0010.0010
+ 1110.0011
= 0000.0101  (discard carry out)

Result: 0000.0101 = 0.3125 ✓ (2.125 - 1.8125 = 0.3125)
```

### Q4.4: -4.375 + (-2.8125)
```
-4.375 = 1011.1000
-2.8125 = 1101.0011

Add:
  1011.1000
+ 1101.0011
= 10001.1011 (carry out discarded)
= 0001.1011  (5-bit, but we have 4 int bits → overflow!)

4 int bits range: -8 to +7.9375
-4.375 + -2.8125 = -7.1875 (in range)

Sign-extend to 5 int bits:
  11011.1000
+ 11101.0011
= 110001.1011
= 10001.1011 = -7.1875
```

---

## IEEE 754 Encoding Traces

### 228₁₀ → 0x43640000
```
1. 228 = 11100100₂
2. Normalize: 1.11001₂ × 2⁷
3. S = 0
4. E = 7 + 127 = 134 = 10000110₂
5. F = 11001 000... (23 bits)
6. Binary: 0 10000110 11001000000000000000000
7. Hex: 0100 0011 0110 0100 0000 0000 0000 0000 = 0x43640000
```

### -58.25₁₀ → 0xC2690000
```
1. 58.25 = 111010.01₂
2. Normalize: 1.1101001₂ × 2⁵
3. S = 1
4. E = 5 + 127 = 132 = 10000100₂
5. F = 1101001 000...
6. Binary: 1 10000100 11010010000000000000000
7. Hex: 1100 0010 0110 1001 0000 0000 0000 0000 = 0xC2690000
```

### FP Addition: 12.5 + 0.375 = 12.875
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

## Ring Oscillator

### 3 Inverters, 2ns each
```
T = 2 × N × t_pd = 2 × 3 × 2ns = 12ns
f = 1/T = 83.33 MHz
```

### 5 Inverters, 1ns each
```
T = 2 × 5 × 1ns = 10ns
f = 100 MHz
```

---

## State Encoding Comparison

### Divide-by-3: Binary (2 FFs) vs One-Hot (3 FFs)
```
Binary:
S0=00, S1=01, S2=10
Next-state logic complex

One-Hot:
S0=001, S1=010, S2=100
Next-state = rotate left (simple!)
```

---

## Quick Formula Reference Card

| Category | Formula |
|----------|---------|
| **Setup** | Tc ≥ tpcq + tpd + tsetup |
| **Hold** | tccq + tcd ≥ thold |
| **f_max** | 1 / (tpcq + tpd + tsetup) |
| **Ring osc** | f = 1/(2·N·tpd) |
| **2's comp N-bit** | [-2ⁿ⁻¹, 2ⁿ⁻¹-1] |
| **Negate 2's comp** | invert + 1 |
| **IEEE 754 single** | S(1)\|E(8,127)\|F(23) |
| **IEEE 754 double** | S(1)\|E(11,1023)\|F(52) |
| **RCA delay** | N × tFA |
| **CLA delay** | t_pg + t_pg_block + (N/k-1)t_AND_OR + k·tFA |
| **Prefix delay** | t_pg + log₂N·t_pg_prefix + t_XOR |
| **MUX selects** | log₂N |
| **Decoder outputs** | 2ᴺ |
| **Divide-by-N** | f_out = f_in/N |
| **Binary FFs K states** | ⌈log₂K⌉ |
| **One-Hot FFs K states** | K |
| **Factored states** | N₁+N₂ |
| **Equality** | Π(Aᵢ ⊙ Bᵢ) |
| **<< N** | × 2ᴺ |
| **>>> N (signed)** | ÷ 2ᴺ |
| **Multiply N×M bits** | N+M |

---

## Exam Strategy: Numerical Problems

1. **Identify given parameters** (delays, bits, frequencies)
2. **Select correct formula** from reference card
3. **Plug in values** with units
4. **Convert units** consistently (ns, ps, MHz)
5. **Check answer** against options
6. **Box final answer** with units
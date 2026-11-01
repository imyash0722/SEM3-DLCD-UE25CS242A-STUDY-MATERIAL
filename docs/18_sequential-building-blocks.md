# 18. Sequential Building Blocks — Registers, Memory Arrays, Counters

> **Source:** Unit 3 Slides 3.1.1, 3.3.1 | Textbook: Harris & Harris Ch. 5, 6

---

## Registers

### N-Bit Register
An N-bit register is a bank of N D-flip-flops sharing a common clock, reset, and enable. It stores an N-bit word → 2ᴺ possible values.

**Interface:**
- **Inputs:** D[N-1:0], CLK, Reset, Enable
- **Outputs:** Q[N-1:0]

**Behavior:**
- **Reset (sync):** Q ← 0
- **Enable=1:** Q ← D
- **Enable=0:** Q holds previous value

### Enabled Flip-Flop (Load/Hold) — Preferred: Mux at D-Input
```
D_FF = EN · D_in + EN̄ · Q
// EN=1: Load D_in. EN=0: Recirculate Q (Hold). Clock runs continuously.
```
**Avoid: Clock Gating** (CLK_FF = CLK · EN). EN changing while CLK=1 creates **Clock Glitch** (Runt pulse) → Metastability.

---

## Register File

A register file is an array of registers with multiple read and write ports.

**Parameters:**
- **Depth (N):** Number of registers (e.g., 32)
- **Width (W):** Bits per register (e.g., 32)
- **Read Ports (R):** Number of simultaneous reads (typically 2 for MIPS)
- **Write Ports (W):** Number of simultaneous writes (typically 1)

**Interface:**
```
Inputs:  CLK, WE, WA[log₂N-1:0], WD[W-1:0], RA1[log₂N-1:0], RA2[log₂N-1:0]
Outputs: RD1[W-1:0], RD2[W-1:0]
```

**Operation:**
- Read: Combinational — RD1 = MEM[RA1], RD2 = MEM[RA2]
- Write: On CLK↑ if WE=1 — MEM[WA] ← WD

**MIPS Register File:** 32 registers × 32 bits, 2 read ports, 1 write port.

---

## Memory Arrays

### SRAM (Static RAM) — 6T Cell
```
Cross-coupled inverters (2) + Access transistors (2) = 6 Transistors
```
- **Read:** Precharge bit lines → Assert word line → Sense amp detects differential voltage
- **Write:** Drive bit lines to desired value → Assert word line → Overwrite cell

**Characteristics:**
- No refresh needed (static)
- Fast access (~ns)
- Low density, higher cost per bit
- Used for caches, register files

### DRAM (Dynamic RAM) — 1T1C Cell
```
1 Transistor + 1 Capacitor
```
- **Refresh Required:** Charge leaks from capacitor → Periodic refresh (every ~64ms)
- **Row/Column Addressing:** RAS/CAS multiplexing
- **Slower** than SRAM but higher density
- Used for main memory

### Memory Organization

| Expansion | Description | Example |
|-----------|-------------|---------|
| **Width** | Parallel chips | 4 × 1M×4 = 1M×16 |
| **Depth** | Chip select decoding | 2 × 1M×8 = 2M×8 |

---

## Counters

### Synchronous Counter
All FFs share common CLK. Next state computed combinationally from current state.

### Up/Down Counter (Exercise 5.43)
**Inputs:** Reset, Up, CLK
**Output:** Q[31:0]

**Behavior:**
- Reset=1 → Q=0
- Reset=0, Up=1 → Count up (Q+1)
- Reset=0, Up=0 → Count down (Q-1)

**Implementation:**
- 32-bit register
- 32-bit adder/subtractor (controlled by Up)
- MUX selecting between 0, Q+1, Q-1
- Constant 1

**Equation:**
```
Q⁺ = { 0      if Reset=1
     { Q+1    if Reset=0, Up=1
     { Q-1    if Reset=0, Up=0
```

### Counter Adding 4 (Exercise 5.44)
**Inputs:** Reset, CLK
**Output:** Q[31:0]

**Behavior:**
- Reset → Q = 0
- Every clock edge: Q⁺ = Q + 4

**Implementation:**
- 32-bit register
- 32-bit adder
- Constant 4

---

## ROM (Read-Only Memory)

### 16×3 ROM Example (Exercise 5.51)
- 4 address inputs (A,B,C,D) since 2⁴=16
- 3 data outputs (X,Y,Z)

**Dot Notation:** Place dot at intersection of address row and output column where ROM stores 1.

**ROM Contents (Example):**
```
Address | X | Y | Z | Data
0  0000 | 1 | 0 | 0 | 100
1  0001 | 1 | 0 | 1 | 101
2  0010 | 1 | 0 | 1 | 101
...
15 1111 | 1 | 1 | 1 | 111
```

---

## Key Formulas (Memorize)

```
Register File:  N registers × W bits, R read ports, W write ports
SRAM:           6T cell, no refresh, fast
DRAM:           1T1C cell, refresh required, dense
Up/Down Counter: Q⁺ = Q + (2·Up - 1)  [Up=1→+1, Up=0→-1]
ROM:            2ᴺ addresses × M bits
```

---

## MCQ Patterns

1. **Register file ports** — MIPS: 32×32, 2 read, 1 write
2. **SRAM vs DRAM** — SRAM=6T static, DRAM=1T1C dynamic+refresh
3. **Enabled FF** — MUX at D-input (not clock gating)
3. **Counter equations** — Up/Down: Q⁺ = Q + (2·Up-1)
4. **ROM addressing** — 2ᴺ addresses for N address lines
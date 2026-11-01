# 25. Classwork Problems — Worked Exercises (Counters, ROM, Memory, FSM)

> **Source:** Unit 3 Slides 3.17.1 | Textbook: Harris & Harris Ch. 5, 6

---

## Exercise 5.43: 32-bit Up/Down Counter

### Problem
Build a 32-bit synchronous Up/Down counter with Reset and Up inputs.
- Reset=1 → Q=0
- Reset=0, Up=1 → Count up
- Reset=0, Up=0 → Count down

### Design
**Components:**
- 32-bit register
- 32-bit adder/subtractor (or adder + MUX)
- MUX
- Constant 1

### Next-State Equation
```
Q⁺ = { 0       if Reset=1
     { Q + 1   if Reset=0, Up=1
     { Q - 1   if Reset=0, Up=0
```

**Convenient Form:**
```
Q⁺ = Q + (2·Up - 1)
```
- Up=1 → 2×1-1 = +1 (count up)
- Up=0 → 2×0-1 = -1 (count down)

**Implementation:**
- Reset is **synchronous** (overrides D on clock edge, not async clear)
- Use adder with control input `Up` (1=add, 0=subtract) or MUX selecting Q+1 vs Q-1

---

## Exercise 5.44: 32-bit Counter Adding 4

### Problem
32-bit counter with Reset and CLK. On reset: Q=0. Every clock: Q⁺ = Q + 4.

### Design
**Components:**
- 32-bit register
- 32-bit adder
- Constant 4

### Next-State Equation
```
Q⁺ = Q + 4
```

**Implementation:** Feed adder output (Q+4) back to register D-input. Reset clears register synchronously.

---

## Exercise 5.51: 16×3 ROM Implementation

### Problem
Implement functions using single 16×3 ROM. Use dot notation for contents.

**Given:**
- 16×3 ROM = 4 address inputs (A,B,C,D), 3 data outputs (X,Y,Z)

### ROM Contents Table

| Address | A B C D | X | Y | Z | Data (XYZ) |
|---------|---------|---|---|---|------------|
| 0  | 0000 | 1 | 0 | 0 | 100 |
| 1  | 0001 | 1 | 0 | 1 | 101 |
| 2  | 0010 | 1 | 0 | 1 | 101 |
| 3  | 0011 | 1 | 0 | 1 | 101 |
| 4  | 0100 | 0 | 0 | 1 | 001 |
| 5  | 0101 | 0 | 1 | 1 | 011 |
| 6  | 0110 | 0 | 0 | 1 | 001 |
| 7  | 0111 | 0 | 1 | 1 | 011 |
| 8  | 1000 | 0 | 0 | 1 | 001 |
| 9  | 1001 | 0 | 0 | 1 | 001 |
| 10 | 1010 | 1 | 0 | 1 | 101 |
| 11 | 1011 | 0 | 0 | 1 | 001 |
| 12 | 1100 | 1 | 1 | 1 | 111 |
| 13 | 1101 | 1 | 1 | 1 | 111 |
| 14 | 1110 | 1 | 1 | 1 | 111 |
| 15 | 1111 | 1 | 1 | 1 | 111 |

**ROM Stores:** 100, 101, 101, 101, 001, 011, 001, 011, 001, 001, 101, 001, 111, 111, 111, 111

### Dot Notation
Place dot (●) at intersection of address row and output column where ROM stores 1.

| Addr | X | Y | Z |
|------|---|---|---|
| 0000 | ● |   |   |
| 0001 | ● |   | ● |
| 0010 | ● |   | ● |
| 0011 | ● |   | ● |
| 0100 |   |   | ● |
| 0101 |   | ● | ● |
| 0110 |   |   | ● |
| 0111 |   | ● | ● |
| 1000 |   |   | ● |
| 1001 |   |   | ● |
| 1010 | ● |   | ● |
| 1011 |   |   | ● |
| 1100 | ● | ● | ● |
| 1101 | ● | ● | ● |
| 1110 | ● | ● | ● |
| 1111 | ● | ● | ● |

---

## Exercise 6.3: Memory Word Storage (Word 42, Data 0xFF223344)

### Given
- Memory word = 42
- Word size = 32 bits = 4 bytes
- Byte-addressable memory
- Data = 0xFF223344

### (a) Byte Address of Word 42
```
Byte Address = Word Number × 4 = 42 × 4 = 168 = 0xA8
```
Word 42 starts at byte address **0xA8**.

### (b) Byte Addresses Spanned
| Byte | Address |
|------|---------|
| 0 (MSB) | 0xA8 |
| 1 | 0xA9 |
| 2 | 0xAA |
| 3 (LSB) | 0xAB |

Spans: **0xA8, 0xA9, 0xAA, 0xAB**

### (c) Store 0xFF223344 (Bytes: FF, 22, 33, 44)

**Big-Endian** (MSB at lowest address):
| Address | Data |
|---------|------|
| 0xA8 | FF |
| 0xA9 | 22 |
| 0xAA | 33 |
| 0xAB | 44 |

**Little-Endian** (LSB at lowest address):
| Address | Data |
|---------|------|
| 0xA8 | 44 |
| 0xA9 | 33 |
| 0xAA | 22 |
| 0xAB | FF |

---

## Exercise 6.4: Memory Word Storage (Word 15, Data 0xFF223344)

### (a) Byte Address of Word 15
```
Byte Address = 15 × 4 = 60 = 0x3C
```

### (b) Byte Addresses Spanned
**0x3C, 0x3D, 0x3E, 0x3F**

### (c) Store 0xFF223344

**Big-Endian:**
| Address | Data |
|---------|------|
| 0x3C | FF |
| 0x3D | 22 |
| 0x3E | 33 |
| 0x3F | 44 |

**Little-Endian:**
| Address | Data |
|---------|------|
| 0x3C | 44 |
| 0x3D | 33 |
| 0x3E | 22 |
| 0x3F | FF |

---

## Key Concepts Summary

| Concept | Formula/Rule |
|---------|--------------|
| **Byte address from word** | `ByteAddr = WordNum × 4` |
| **Word spans** | `ByteAddr, ByteAddr+1, ByteAddr+2, ByteAddr+3` |
| **Big-Endian** | MSB → lowest address |
| **Little-Endian** | LSB → lowest address |
| **Up/Down Counter** | `Q⁺ = Q + (2·Up - 1)` |
| **Counter +4** | `Q⁺ = Q + 4` |
| **ROM Size** | 2ᴺ addresses × M bits |
| **Dot Notation** | Dot = 1 at (address, output) |

---

## MCQ Patterns

1. **Byte address calc** — Word N → byte address = 4N
2. **Endianness** — Big=MSB@low, Little=LSB@low
3. **Counter equations** — Up/Down: Q+(2·Up-1); +4 counter: Q+4
4. **ROM addressing** — 16×3 = 4 address lines, 3 data lines
5. **Dot notation** — Dot at (row, col) where ROM=1
6. **Synchronous reset** — On clock edge, not immediate
7. **Adder/subtractor control** — Up=1 → add, Up=0 → subtract
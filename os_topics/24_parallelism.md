# 24. Parallelism — Spatial vs Temporal, Pipelining, Hazards, Performance

> **Source:** Unit 3 Slides 3.15.1 | Textbook: Harris & Harris Ch. 7

---

## What is Parallelism?

**Parallelism** = Simultaneous execution of multiple tasks to increase work completed per unit time.

**Goal:** Improve **throughput** (tasks/second) without relying solely on faster clocks.

**Why Parallelism?**
- Increasing clock frequency → higher power + heat (hits physical limits)
- Parallelism = better hardware utilization
- Used in: Multicore CPUs, GPUs, Supercomputers, DSPs, ML accelerators

---

## Performance Metrics

### Latency
- Time for **one task** from input to output
- `Latency = Time for one task`
- Lower = faster individual response

### Throughput
- Number of tasks completed per unit time
- `Throughput = Completed Tasks / Unit Time`
- Higher = more total work done

### Key Relationship (Non-Parallel):
```
Throughput = 1 / Latency
```

### Critical Insight:
> **Parallelism improves throughput, NOT latency.**
> A system can have high throughput (many tasks simultaneously) while individual task latency stays the same or increases.

---

## Types of Parallelism

### 1. Spatial Parallelism
**Add multiple hardware copies** — each performs a different task simultaneously.

| Examples | Advantages | Disadvantage |
|----------|------------|--------------|
| Multiple processors | True simultaneous execution | Higher hardware cost |
| Multiple ALUs | Higher throughput | More area/power |
| Multicore CPUs | — | — |
| GPUs (thousands of cores) | — | — |

### 2. Temporal Parallelism (Pipelining)
**Divide one task into stages** — different tasks occupy different stages simultaneously (assembly line).

**Example:** 5-Stage Pipeline
```
IF → ID → EX → MEM → WB
```

| Advantages | Disadvantage |
|------------|--------------|
| Better hardware utilization | Pipeline registers + control complexity |
| Lower cost than spatial | Unequal stages reduce efficiency |
| Enables higher clock frequency | Data/Control/Structural hazards |

---

## Parallelism Comparison

| Aspect | Spatial Parallelism | Temporal Parallelism (Pipelining) |
|--------|---------------------|-----------------------------------|
| **Method** | Duplicate hardware | Overlap stages of execution |
| **Hardware** | Multiple copies (more area) | Reuse same hardware over time |
| **Execution** | Truly simultaneous | Overlapped (not simultaneous per stage) |
| **Cost** | Higher | Lower |
| **Best For** | Independent tasks | Sequential dependent tasks |

**Key Point:** Modern processors combine **both** — multicore (spatial) + pipelined cores (temporal).

---

## Cookie Analogy (Textbook Numerical)

### Sequential (No Parallelism)
- Roll: 5 min, Bake: 15 min
- Next tray starts only after previous finishes
- **Latency** = 5 + 15 = 20 minutes
- **Throughput** = 60 / 20 = 3 trays per hour

### Spatial Parallelism (Two Chefs)
- Ben + Alyssa bake simultaneously
- Latency = 20 min (unchanged)
- Throughput = 3 + 3 = 6 trays/hour (2×)

### Temporal Parallelism (Two Trays)
- While Tray 1 bakes, Ben prepares Tray 2
- New tray enters oven every 15 min (baking time)
- **Throughput** = 60/15 = 4 trays/hour
- Latency = 20 min

### Spatial + Temporal (Two Chefs + Two Trays)
- **Throughput** = 8 trays/hour
- Latency = 20 min

**Conclusion:** Parallelism ↑ throughput, latency unchanged.

---

## Mathematical Model

### Without Parallelism
```
Throughput = 1 / L
```
where L = latency

### Spatial Parallelism (N units)
```
Throughput = N / L
```

### Temporal Parallelism (N equal stages)
```
Throughput = N / L
Clock period = L / N
```

### Unequal Pipeline Stages
- Stage delays: L₁, L₂, ..., Lₙ
- **Clock period = max(L₁, L₂, ..., Lₙ)**
- **Throughput = 1 / max(stage delays)**
- **Key:** Balanced stages maximize throughput.

---

## Pipeline Numerical Examples (Textbook)

### Non-Pipelined Circuit
Given: `t_cq = 0.3 ns`, Logic blocks: 3 ns, 2 ns, 4 ns, `t_setup = 0.2 ns`

**Cycle Time:** `T_c = 0.3 + 3 + 2 + 4 + 0.2 = 9.5 ns`
**Latency:** 9.5 ns
**Throughput:** `1/9.5 ns ≈ 105 MHz`

### Two-Stage Pipeline (Register after block 2)
| Stage | Components | Delay |
|-------|------------|-------|
| 1 | t_cq + 3 + 2 + t_setup | 0.3 + 3 + 2 + 0.2 = 5.5 ns |
| 2 | t_cq + 4 + t_setup | 0.3 + 4 + 0.2 = 4.5 ns |

**Clock Period:** `T_c = max(5.5, 4.5) = 5.5 ns`
**Throughput:** `1/5.5 ns ≈ 182 MHz`
**Latency:** `2 × 5.5 = 11 ns` — about the same, so pipelining raises throughput, not latency.

### Three-Stage Pipeline (Exercise)
Stage delays: 3.5 ns, 2.5 ns, 4.5 ns

**Clock Period:** `T_c = max = 4.5 ns`
**Latency:** `3 × 4.5 = 13.5 ns`
`Tc = max(3.5, 2.5, 4.5) = 4.5 ns`
**Latency:** `3 x Tc = 13.5 ns`

---

## Pipeline Hazards

Hazards prevent smooth pipeline flow → introduce **stalls (bubbles)** → reduce throughput.

### 1. Data Hazard (RAW — Read After Write)
**Cause:** Instruction needs data still being produced by earlier instruction.
```
add $s0, $t1, $t2
sub $t3, $s0, $t4    # $s0 not ready until add writes back
```
**Solutions:**
- **Forwarding (Bypassing):** Route result from EX/MEM or MEM/WB directly to EX
- **Stalls:** Insert NOPs if forwarding insufficient (e.g., load-use hazard)

### 2. Control Hazard
**Cause:** Branch/jump — next instruction unknown until decision made.
```
beq $t0, $0, label
# Next instruction fetched before branch resolved
```
**Solutions:**
- **Branch Prediction:** Predict taken/not taken
- **Delay Slots:** Execute instruction after branch unconditionally (MIPS I)
- **Speculative Execution:** Execute predicted path, squash if wrong

### 3. Structural Hazard
**Cause:** Multiple instructions need same hardware resource.
```
# Single memory port
lw $t0, 0($s1)    # MEM stage reads memory
sw $t1, 4($s2)    # MEM stage writes memory → conflict!
```
**Solutions:**
- Duplicate resource (e.g., separate I-cache and D-cache)
- Pipeline stall

---

## Forwarding Paths (MIPS 5-Stage)

```
EX/MEM → EX    (ALU result from previous instruction)
MEM/WB → EX    (ALU result from instruction before that)
```

**Load-Use Hazard:** `lw` followed by instruction using loaded value
- Load data available end of MEM stage
- Next instruction needs it in EX stage
- **Minimum 1-cycle stall** even with forwarding

---

## Advantages & Limitations of Pipelining

| Advantages | Limitations |
|------------|-------------|
| No duplicate hardware | Pipeline registers + control logic |
| Divides long combinational paths | Unequal stages → wasted time |
| Shorter clock period | Data hazards → stalls |
| Higher throughput | Control hazards → mispredictions |
| Basis of modern CPUs/GPUs | Structural hazards → resource conflicts |

---

## Key Formulas (Memorize)

```
Latency = Time per task
Throughput = Tasks / Time
Non-parallel: TP = 1 / Latency

Spatial (N units):    TP = N / Latency
Temporal (N stages):  TP = N / Latency  (if balanced)
Clock period:         T_c = max(stage_delays)
Throughput:           1 / T_c
Latency (pipelined):  N × T_c

Pipeline speedup:     T_c(non-pipe) / T_c(pipelined)
Unequal stages:       T_c = max(L₁, L₂, ..., Lₙ)

Hazards:
  Data (RAW):     Forwarding (EX/MEM→EX, MEM/WB→EX) + Stalls
  Control:        Prediction, Delay slots, Speculation
  Structural:     Resource duplication or stalls
```

---

## MCQ Patterns

1. **Parallelism goal** — Improve throughput (not latency)
2. **Spatial vs Temporal** — Spatial=more hardware, Temporal=pipelining
3. **Cookie analogy** — Spatial=more chefs, Temporal=overlap prep/bake
4. **Pipeline clock** — Determined by **slowest stage**
5. **Unbalanced stages** — Clock = max(stage delays); throughput limited by bottleneck
6. **Latency in pipeline** — N × T_c (increases slightly)
7. **Data hazard** — RAW; solved by forwarding (EX/MEM→EX, MEM/WB→EX)
8. **Load-use hazard** — Requires 1-cycle stall even with forwarding
9. **Control hazard** — Branch misprediction; solved by prediction
10. **Structural hazard** — Resource conflict; solved by duplication
11. **Amdahl's Law** — Speedup = 1/[(1-f)+f/s]; diminishing returns
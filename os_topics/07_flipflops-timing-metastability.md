# 07. Flip-Flops — D FF, Master-Slave, Timing, Metastability

> **Source:** Harris & Harris Ch. 3, Unit 1 Slides 187–210, 360–420

---

## D Flip-Flop (Positive-Edge Triggered)

### Master-Slave Construction

```
D ──┐                    ┌── Q
    │  Master Latch      │
CLK─┤ (CLK)              │
    │  Slave Latch       │
CLK'┤ (CLK')             │
    └────────────────────┘
```

- **Master:** Transparent when CLK=0 (samples D)
- **Slave:** Transparent when CLK=1 (outputs master's value)
- **Result:** Q changes only at **rising edge** (0→1)

### Symbol

```
     D ──┐
         │▷
    CLK ─┤
         │
         └── Q
```

---

## Timing Parameters

| Parameter | Symbol | Definition |
|-----------|--------|------------|
| **Clock-to-Q (max)** | tₚcq | Max delay from CLK↑ to Q stable |
| **Clock-to-Q (min)** | t_ccq | Min delay (contamination) |
| **Setup time** | t_setup | D stable **before** CLK↑ |
| **Hold time** | t_hold | D stable **after** CLK↑ |
| **Aperture** | t_setup + t_hold | Total window around edge |

---

## Setup & Hold Constraints

### Setup Constraint (Max Frequency)

```
T_c ≥ tₚcq + tₚd,comb + t_setup
f_max = 1 / T_c,min
```

**Example:** tₚcq=1.0ns, tₚd=3.5ns, t_setup=0.5ns
→ T_c,min = 5.0ns → **f_max = 200 MHz** (Q53)

### Hold Constraint (Min Delay)

```
t_ccq + t_cd ≥ t_hold
```

- **Violation:** New data races through too fast, corrupts capture
- **Fix:** Add buffers (increase contamination delay)

---

## Metastability

- **Cause:** D changes within setup-hold aperture
- **Effect:** Q hovers between 0/1, resolves unpredictably
- **MTBF:** Mean Time Between Failures (exponential with clock period)
- **Fix:** Synchronizers (2-FF chain), wider aperture FFs

---

## Enabled Flip-Flop (No Clock Gating!)

```
     D ──┐
         │ MUX ──── D_FF
    EN ──┤     (EN'·Q)
         └───────────┘
```

- **Clock always runs** — avoids skew/glitches
- **EN=1:** Load D | **EN=0:** Recirculate Q (hold)

---

## Resettable Flip-Flop

| Type | Behavior |
|------|----------|
| **Synchronous** | Reset sampled at CLK↑ (Q=0 next cycle) |
| **Asynchronous** | Reset immediate (Q=0 now, no clock wait) |

---

## T & JK Flip-Flops from D FF

| FF Type | Characteristic Eq | D Input Logic |
|---------|-------------------|---------------|
| **T (Toggle)** | Q⁺ = T ⊕ Q | D = T ⊕ Q |
| **JK** | Q⁺ = JQ' + K'Q | D = JQ' + K'Q |

---

## Ring Oscillator (Review)

- N inverters in loop (N odd)
- **Period:** T = 2·N·tₚd
- **Frequency:** f = 1/(2·N·tₚd)
- **3 inv, 2ns each:** T=12ns, f≈83.3MHz
- **5 inv, 1ns each:** T=10ns, f=100MHz

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| tₚcq vs t_ccq? | Max vs min clock-to-Q delay |
| Setup constraint formula? | T_c ≥ tₚcq + tₚd + t_setup |
| Hold constraint formula? | t_ccq + t_cd ≥ t_hold |
| Metastability cause? | D changes in setup-hold window |
| Enabled FF without clock gating? | MUX at D input (D or Q) |
| Sync vs Async reset? | Sync at edge, async immediate |
| T FF from D FF? | D = T ⊕ Q |

---

## Exam-Relevant MCQ Patterns

1. **Setup constraint** — T_c ≥ tₚcq + tₚd + t_setup (Q52, Q53)
2. **Hold constraint** — t_ccq + t_cd ≥ t_hold (Q54)
3. **Metastability** — D change in aperture → unstable Q (Q55)
4. **Enabled FF** — MUX feedback, not clock gating (Q57)
5. **Sync vs Async reset** — Sync at edge, async immediate (Q58)
6. **T FF construction** — D = T ⊕ Q (Q56)
7. **Ring oscillator** — f = 1/(2Ntₚd) (Q46, Q59, Q60)
8. **Max frequency calc** — f_max = 1/(tₚcq+tₚd+t_setup) (Q53)

---

## Key Formulas (Memorize)

```
Setup:     T_c ≥ tₚcq + tₚd,comb + t_setup
Hold:      t_ccq + t_cd ≥ t_hold
f_max:     1 / (tₚcq + tₚd + t_setup)
Ring osc:  f = 1 / (2 × N × tₚd)
T FF:      D = T ⊕ Q
JK FF:     D = J·Q' + K'·Q
Enabled:   D_mux = EN·D + EN'·Q
```
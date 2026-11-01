# Unit 2: Finite State Machines & Digital Building Blocks - Clean Lecture Notes

> Cleaned and condensed from original slides. Diagram artifacts, watermark overlaps, and animation duplicates removed.

### Slide 2: Finite State Machine (FSM):
- A Finite State Machine (FSM) is a model used to design synchronous sequential
- circuits.
- It works by moving between a limited (finite) number of states based on the current
- inputs and the present state of the circuit.
- A circuit containing k registers can have 2ᵏ different states because each register
- stores one bit of information. The FSM can be in only one state at a time.
- KEY POINT
- Finite State Machine (FSM)
- A digital circuit that stores its
- current state and changes to
- the next state on every clock
- edge. "Finite" means the
- machine has only a limited
- number of possible states.

### Slide 3: FINITE STATE MACHINE
- **An FSM consists of:** 
- M Inputs – Signals received from the external
- system.
- N Outputs – Signals produced by the circuit.
- k-bit State Register – Stores the current state
- of the FSM.
- Clock Signal (CLK) – Controls when the state
- changes.
- Optional Reset Signal – Returns the FSM to its
- initial state.

### Slide 4: BASIC STRUCTURE OF FSM
- A Finite State Machine consists of three main components
- that work together to determine the circuit's behavior.

**1. Next State Logic**

**2. State Register (Memory)**

**3. Output Logic**

**1.Next State Logic:**
- Computes the next state of the FSM.

**2. State Register (Memory)**
- Stores the present state of the FSM. Updates the stored state on every clock edge (CLK).

**3. Output Logic**
- Generates the output signals of the FSM.

### Slide 5: BASIC STRUCTURE OF FSM
- The outputs are determined based on the type of FSM:
- **Moore Machine:** Output depends only on the current
- state.
- **Mealy Machine:** Output depends on the current state
- and current inputs.
- **Working Principle:** 
- On every clock edge, the FSM:

**1.Reads the current state.**

**2.Accepts the current inputs.**

**3.Computes the next state.**

**4.Updates the state register.**

**5.Produces the required outputs.**

### Slide 6: TYPES OF FSM
- **Moore Machine:** 
- Output depends only on the current state. Changes in input do not immediately
- affect the output. Output changes only after the state changes.
- Output = f(Current State)

### Slide 7: TYPES OF FSM
- Mealy Machine
- Output depends on both the current state and the current inputs. Output can change
- immediately when the input changes. Generally requires fewer states than a Moore
- machine.
- Output = f(Current State, Current Input)

### Slide 8: FSM DESIGN EXAMPLE
- One day, while walking across campus, Ben notices
- the busy intersection between Academic Avenue and
- Bravado Boulevard.
- Students are moving between the Dormitories and
- the Labs on Academic Ave.
- Football players are traveling between the Athletic
- Fields and the Dining Hall on Bravado Blvd.
- Since many people are busy and not paying
- attention, several accidents have already occurred at
- the intersection.
- The Dean of Students asks Ben to design an

### Slide 9: FSM DESIGN EXAMPLE
- Design an FSM-based traffic light controller
- that uses traffic sensors to control the traffic
- lights and ensure safe, smooth traffic flow at
- the campus intersection.
- **Solution:** 
- Ben decides to solve the problem using a Finite
- State Machine (FSM) that can monitor traffic
- and control the signals automatically.

### Slide 10: FSM DESIGN EXAMPLE
- **2 Outputs:** LA, LB
- Sensor Location
- Function
- Traffic Light
- Controls
- Tₐ
- Academic Detects vehicles on Academic
- Avenue
- Avenue.
- Lₐ
- Academic Avenue
- Lᵦ
- Bravado Boulevard
- Tᵦ
- Bravado
- Boulevar
- Detects vehicles on Bravado
- Boulevard.
- **Clock (CLK):** The controller checks traffic and updates
- the signals every 5 seconds.
- **Reset:** Initializes the FSM to its starting state when
- the controller is turned on.

### Slide 11: STATE TRANSITION DIAGRAM
- **Overview:** 
- Each circle represents a state, and the directed
- arrows represent the transitions between states
- based on the traffic sensor inputs.
- **Moore FSM:** outputs labeled in each state
- **States:** Circles
- **Transitions:** Arcs
- **STATES:** 

### Slide 16: STATE TRANSITION DIAGRAM

### Slide 17: STATE TRANSITION TABLE
- The State Transition Table is a bridge between
- the graphical FSM representation and the
- digital hardware implementation.

### Slide 18: STATE AND OUTPUT ENCODING
- Before implementing the FSM using digital hardware, the states and outputs must be
- represented in binary form. This process is called Encoding.

**1. State Encoding**

**2. Output Encoding**
- Each state is assigned a unique
- Each traffic light color is also represented using
- binary code.
- binary values.

### Slide 19: STATE AND OUTPUT ENCODING
- Why Encoding?
- Converts symbolic states into binary values.
- Makes the FSM compatible with digital circuits.
- Simplifies the derivation of Boolean equations.
- Key Observation
- Every state and output now has a unique binary representation
- Encoding transforms the FSM from a conceptual model into a form that can
- be implemented using digital hardware.

### Slide 20: STATE AND OUTPUT ENCODING
- After assigning binary codes to each state, the State Transition Table is updated
- using these binary encodings.

### Slide 21: NEXT STATE LOGIC
- The Next-State Equations determine which state the FSM should move to based on
- the current state and the sensor inputs.
- The Boolean equations obtained from the state transition table can be simplified
- using Karnaugh Maps (K-Maps) or by inspection.
- This reduces the number of logic gates, makes the circuit simpler and improves
- hardware efficiency.

### Slide 22: OUTPUT LOGIC
- Similarly the output table using the binary
- encoding is Table 3.5

### Slide 23: COMPLETE FSM LOGIC CIRCUIT

### Slide 24: STATE ENCODING
- State Encoding is the process of assigning binary codes to the states of a Finite State
- Machine (FSM).
- The choice of encoding directly affects the hardware implementation, including the
- number of logic gates, propagation delay, and overall circuit complexity.
- Different state encodings can produce different:
- circuit implementations
- numbers of logic gates
- propagation delays
- hardware complexity
- Therefore, selecting an appropriate encoding helps in designing an efficient FSM.

### Slide 25: STATE ENCODING
- Finding the optimal encoding is difficult because it requires checking all possible
- encoding combinations, which becomes impractical as the number of states increases.
- Instead, designers usually choose a suitable encoding based on the application or use
- Computer-Aided Design (CAD) tools to help select an efficient encoding.
- The choice of state encoding influences the speed, size, and complexity of the final
- digital circuit.

### Slide 26: BINARY ENCODING
- State
- Binary Code
- Advantages
- Uses fewer state bits and requires fewer flip-flops
- Efficient hardware utilization

### Slide 27: ONE HOT ENCODING
- In One-Hot Encoding, each state is assigned a separate bit.
- Only one bit is HIGH (1) at any given time, while all other bits remain LOW (0).
- For K states, K bits are required.

**Example:For 3 states**
- State
- Encoding
- Advantages
- Simpler combinational logic and faster implementation
- Disadvantages
- Requires more flip-flops and higher hardware cost

### Slide 28: DESIGNING A DIVIDE-BY-3-COUNTER
- To understand how different state encoding techniques are applied, consider the
- design of a Divide-by-3 Counter.
- A Divide-by-3 Counter is a sequential circuit that reduces the frequency of the
- input clock by a factor of 3.
- **System Description:** 
- The FSM has one output (Y) and three states
- S0, S1, and S2 .
- The output Y becomes HIGH (1) for one clock
- cycle out of every three clock cycles.

### Slide 29: DESIGNING A DIVIDE-BY-3-COUNTER
- **Operation:** 
- The counter continuously cycles through the following sequence:
- S0 → S1 → S2 → S0 → ...
- This repeating sequence divides the clock frequency by 3.

### Slide 30: STATE TRANSITION TABLE

**1. State Transition Table:**
- The State Transition Table defines the next state for every current state.

### Slide 31: OUTPUT TABLE

**2. Output Table:**
- The Output Table specifies the output value associated with each state.

### Slide 32: BINARY VS ONE HOT ENCODING
- To implement the Divide-by-3 Counter in hardware, each state must be assigned
- a binary code. Two commonly used encoding techniques are Binary Encoding and
- One-Hot Encoding.

### Slide 33: STATE TRANSITION TABLE USING BINARY ENCODING
- Binary State Transition Table
- The Binary State Transition Table uses the 2-bit binary codes assigned to each state.
- States are represented using 2 bits.

### Slide 34: STATE TRANSITION TABLE USING ONE-HOT ENCODING
- One-Hot State Transition Table
- The One-Hot State Transition Table uses one flip-flop for each state
- Each state is represented by a unique active bit. Only one bit is HIGH at any time.

### Slide 35: FSM IMPLEMENTATION
- Binary Encoding Implementation:
- One-Hot Encoding Implementation:

### Slide 37: TYPES OF FSM
- **Moore Machine:** 
- Output depends only on the current state. Changes in input do not immediately
- affect the output. Output changes only after the state changes. Outputs are written
- inside the state circles.
- Formula
- Output = f(Current State)
- KEY POINT
- Moore machines
- usually require more
- states than Mealy
- machines for the same
- problem.

### Slide 38: TYPES OF FSM
- Mealy Machine
- Output depends on both the current state and the current inputs. Output can change
- immediately when the input changes. Generally requires fewer states than a Moore
- machine. Outputs are written on the transition arrows.
- Formula
- Output = f(Current State, Current Input)

### Slide 39: MOORE VS MEALY MACHINES
- **Scenario:** 
- Alyssa P. Hacker owns a pet robotic snail controlled by a Finite State
- Machine (FSM).The snail moves over a paper tape containing a
- sequence of 1s and 0s.
- **At every clock cycle:** 
- The snail moves one position forward.
- It remembers the last two bits it has read.
- The snail smiles when a specific bit pattern is detected.
- **Input:** [A] Current bit read by the snail.
- **Output:** [Y]
- Y = 1 → Snail smiles.
- Y = 0 → Snail does not smile.

### Slide 40: MOORE VS MEALY MACHINES
- Objective
- Design both Moore Machine and Mealy Machine .Compare both implementations.
- **Moore FSM Design:** 
- The Moore Machine requires three states. Each state represents the
- previous input history.The output depends only on the current state.

### Slide 41: MOORE VS MEALY MACHINES
- **Mealy Machine Design:** 
- The Mealy Machine requires only two states. Outputs are generated during state
- transitions.
- Each transition is labelled as Input / Output

### Slide 42: MOORE TRANSITION AND OUTPUT TABLE

### Slide 43: MOORE TRANSITION AND OUTPUT TABLE WITH BINARY ENCODING
- To implement the Moore Machine in digital hardware,each state is assigned a binary
- code.Using these binary encodings,the transition table and output table are rewritten.

### Slide 44: MOORE FSM
- **Equations:** 
- Equation 3.3.1

### Slide 45: MEALY TRANSITION AND OUTPUT TABLE
- The Mealy Machine requires only one state bit.

### Slide 46: MOORE VS MEALY MACHINES
- **Comparison:** 
- Moore Machine
- Mealy Machine
- More states
- Fewer states
- Stable output
- Faster response
- Output depends only on state
- Output depends on state and input
- One clock delay
- Immediate output
- Choose a Moore Machine when stable outputs are important.
- Choose a Mealy Machine when faster output response is required.

### Slide 48: FACTORING STATE MACHINES
- As the complexity of a Finite State Machine (FSM) increases, designing and maintaining it
- becomes difficult.
- Instead of designing one large FSM, the system can be divided into multiple smaller FSMs
- that work together.
- This design approach is called Factoring of State Machines.
- How Does It Work?
- A complex FSM is split into smaller interacting FSMs.
- The output of one FSM can be used as the input to another FSM.
- This creates a hierarchical and modular design.

### Slide 49: FACTORED AND UNFACTORED STATE MACHINES
- To understand the concept of factoring, consider the traffic light controller introduced
- earlier.
- The controller is now modified to include a Parade Mode, which keeps the Bravado
- Boulevard traffic light green while a parade is in progress.
- **Additional Inputs:** 
- Two new control inputs are introduced:
- P (Parade) – Enables Parade Mode.
- R (Resume) – Exits Parade Mode.

### Slide 50: FACTORED AND UNFACTORED STATE MACHINES
- **Controller Behaviour:** 
- When P = 1, the controller enters Parade Mode.
- During Parade Mode, the controller follows its normal sequence
- until LB becomes green.
- Once LB is green, it remains green throughout the parade.
- When R = 1, the controller exits Parade Mode and resumes normal
- traffic operation.
- **Objective:** 
- **Design the controller using:** 
- A single FSM (Unfactored).
- Multiple interacting FSMs (Factored).

### Slide 51: UNFACTORED FSM
- **Single FSM Approach:** 
- In the unfactored design, a single FSM controls both:
- Normal traffic operation.
- Parade mode.
- State Organization
- S0 – S3 → Normal Mode.
- S4 – S7 → Parade Mode.
- The two halves of the state diagram are almost identical, except that during
- Parade Mode the controller remains in State S6 while LB remains green.
- Characteristics
- One large FSM.
- More states.
- Complex transitions.
- Difficult to modify and debug.

### Slide 52: UNFACTORED FSM

### Slide 53: FACTORED FSM
- Breaking the FSM into Modules:
- Instead of using one large FSM, the controller is divided into two smaller FSMs.
- **Mode FSM:** 
- Tracks whether the controller is operating in:
- Normal Mode
- Parade Mode
- **Produces output:** M
- Lights FSM
- Controls the traffic lights using:
- Traffic Sensors (TA, TB)
- Mode Signal (M)

### Slide 54: FACTORED VS UNFACTORED FSM
- Unfactored FSM
- Single large FSM
- More states
- Complex transitions
- Factored FSM
- Multiple smaller FSMs
- Fewer states per FSM
- Simpler transitions
- Difficult to debug
- Less modular
- Harder to modify
- Easier to debug
- Highly modular
- Easy to extend

### Slide 55: DERIVING AN FSM FROM SCHEMATIC
- **STEPS FOR DERIVING FSM:** 

**1.Examine the circuit and identify Inputs,Outputs ,State bits.**

**2.Write the next-state and output equations.**

**3.Create the next-state and output tables.**

**4.Remove unreachable states.**

**5.Assign symbolic names to valid states.**

**6.Draw the state transition diagram.**

**7.Describe the overall function of the FSM.**

### Slide 56: EXAMPLE
- **Scenario:** 
- Alyssa P. Hacker discovers that the keypad lock in her house has been rewired, and the
- original unlock code no longer works.She finds a circuit diagram attached to the keypad
- and suspects it is controlled by a Finite State Machine (FSM).To determine the correct
- unlock sequence, she decides to derive the FSM from the circuit.

### Slide 57: STEP1: IDENTIFICATION
- Objective
- Determine the FSM states ,State transitions ,Output behaviour
- function of the circuit

**Step 1 – Identify Inputs, Outputs & State Equations:**
- **From the circuit:** 
- **Inputs:** A₁ ,A₀
- **Output:** Unlock
- **State Bits:** S₁ ,S₀
- **Next-State Equations:** 
- S₁' = S₀A₁A₀
- S₀' = S̅₁S₀A₁A₀
- Unlock = S₁
- Equation (3.12)
- and Overall

### Slide 58: STEP2-CREATE TABLES

**Step 2 – Create State Tables:**

### Slide 59: STEP3-REDUCTION

**Step 3 – Reduce the State Tables:**
- Some state combinations are never reached during operation.These are called
- Unreachable States.Removing these states simplifies the FSM.

### Slide 60: STEP4-STATE ASSIGNMENT

**Step 4 – Assign Symbolic State Names:**
- After removing unreachable states, each valid state is assigned a symbolic name.
- Binary State
- Symbolic Name

### Slide 61: STEP4-STATE ASSIGNMENT

**Step 4 – Assign Symbolic State Names:**

### Slide 62: STEP5-STATE TRANSITION TABLE

**Step 5 – Draw the State Transition Diagram:**
- Using the symbolic tables, the final State Transition
- Diagram is constructed.
- **Overall Behaviour:** 
- The FSM unlocks the door only after detecting the
- correct input sequence.
- After unlocking, it returns to the initial state,
- ready for the next input sequence

### Slide 63: FSM REVIEW
- FSM Design Procedure
- General Steps

**1.Identify the inputs and outputs.**

**1.Draw the State Transition Diagram.**

**1.Create:**
- State Transition Table
- Output Table

**4.Select a suitable State Encoding.**

**4.Write:**
- Next-State Equations
- Output Equations

**6.Design the circuit schematic.**

### Slide 64: QUIZ
- **Answer:** B

### Slide 65: QUIZ

**2.An FSM is implemented using 5 flip-flops with Binary Encoding.**
- What is the maximum number of states that can be represented?
- A) 5
- B) 25
- C) 31
- D) 32
- Answer
- **Explanation:** 
- In Binary Encoding, each flip-flop stores 1 bit.
- Number of flip-flops = 5
- Number of possible states = 2⁵ = 32

### Slide 66: QUIZ

**3.An FSM has 8 states. Using Binary Encoding, how many flip-flops are required?**
- A) 2
- B) 3
- C) 4
- D) 8

### Slide 68: Introduction and Arithmetic Circuits

### Slide 69: Topics of Discussion
- Introduction
- Arithmetic Circuits
- Number Systems
- Sequential Building Blocks
- Memory Arrays
- Logic Arrays

### Slide 70: Introduction
- **Digital building blocks:** 
- – Gates, multiplexers, decoders, registers, arithmetic circuits,
- counters, memory arrays, logic arrays
- Building blocks demonstrate hierarchy, modularity, and regularity:
- – Hierarchy of simpler components
- – Well-defined interfaces and functions
- – Regular structure easily extends to different sizes
- Will use these building blocks in Chapter 7 to build microprocessor

### Slide 73: 1-Bit Adders

### Slide 74: Multibit Adders (CPAs)
- Types of carry propagate adders (CPAs):
- – Ripple-carry
- – Carry-lookahead
- – Prefix
- (slow)
- (fast)
- (faster)
- Carry-lookahead and prefix adders faster for large
- adders but require more hardware
- Symbol

### Slide 75: Ripple-Carry Adder
- Chain 1-bit adders together
- Carry ripples through entire chain
- **Disadvantage:** slow

### Slide 76: Ripple-Carry Adder Delay
- tripple = NtFA
- where tFA is the delay of a 1-bit full adder

### Slide 77: Carry-Lookahead Adder
- Compute carry out (Cout) for k-bit blocks using generate and
- propagate signals
- **Some definitions:** 
- – Column i produces a carry out by either generating a carry out or
- propagating a carry in to the carry out
- – Generate (Gi) and propagate (Pi) signals for each column:
- Column i will generate a carry out if Ai AND Bi are both 1.
- Gi = Ai Bi
- Column i will propagate a carry in to the carry out if Ai OR Bi is 1.
- Pi = Ai + Bi
- The carry out of column i (Ci) is:
- Ci = Ai Bi + (Ai + Bi )Ci-1 = Gi + Pi Ci-1

### Slide 78: Carry-Lookahead Addition

**Step 1: Compute Gi and Pi for all columns**

**Step 2: Compute G and P for k-bit blocks**

**Step 3: Cin propagates through each k-bit**
- propagate/generate block

### Slide 79: Carry-Lookahead Adder

**Example: 4-bit blocks (G3:0 and P3:0) :**
- **G3:** 0 = G3 + P3 (G2 + P2 (G1 + P1G0 )
- **P3:** 0 = P3P2 P1P0
- Generally,
- **Gi:** j = Gi + Pi (Gi-1 + Pi-1 (Gi-2 + Pi-2Gj )
- **Pi:** j = PiPi-1 Pi-2Pj
- **Ci = Gi:** j + Pi:j Cj-1

### Slide 80: 32-bit CLA with 4-bit Blocks

### Slide 81: Carry-Lookahead Adder Delay
- For N-bit CLA with k-bit blocks:
- tCLA = tpg + tpg_block + (N/k – 1)tAND_OR + ktFA
- **– tpg:** 
- **– tpg_block:** 
- **– tAND_OR:** 
- delay to generate all Pi, Gi
- **delay to generate all Pi:** j, Gi:j
- delay from Cin to Cout of final AND/OR gate in k-bit CLA
- block
- An N-bit carry-lookahead adder is generally much faster than a
- ripple-carry adder for N > 16

### Slide 82: Prefix Adder
- Computes carry in (Ci-1) for each column, then
- **computes sum:** 
- Si = (Ai ⊕ Bi) ⊕ Ci
- Computes G and P for 1-, 2-, 4-, 8-bit blocks, etc.
- until all Gi (carry in) known
- log2N stages

### Slide 83: Prefix Adder
- Carry in either generated in a column or propagated from a
- previous column.
- Column -1 holds Cin, so
- G-1 = Cin, P-1 = 0
- Carry in to column i = carry out of column i-1:
- **Ci-1 = Gi-1:** -1
- **Gi-1:** -1: generate signal spanning columns i-1 to -1
- **Sum equation:** 
- **Si = (Ai ⊕ Bi) ⊕ Gi-1:** -1
- **Goal:** Quickly compute G0:-1, G1:-1, G2:-1, G3:-1, G4:-1, G5:-1, …
- (called prefixes)

### Slide 84: Prefix Adder
- Generate and propagate signals for a block spanning bits
- **i:** j:
- **Gi:** j = Gi:k + Pi:k Gk-1:j
- **Pi:** j = Pi:kPk-1:j
- **In words:** 
- **– Generate:** block i:j will generate a carry if:
- **upper part (i:** k) generates a carry or
- upper part propagates a carry generated in lower
- **part (k-1:** j)
- **– Propagate:** block i:j will propagate a carry if both the
- upper and lower parts propagate the carry

### Slide 85: Prefix Adder Schematic

### Slide 86: Prefix Adder Delay
- tPA = tpg + log2N(tpg_prefix ) + tXOR
- **– tpg:** delay to produce Pi Gi (AND or OR gate)
- **– tpg_prefix:** delay of black prefix cell (AND-OR gate)

### Slide 89: Subtracter

### Slide 90: Comparator: Equality

### Slide 91: Comparator: Less Than

### Slide 92: Arithmetic Logic Unit (ALU)
- **F2:** 0
- Function
- A&B
- A|B
- A+B
- not used
- A & ~B
- A | ~B
- A-B
- SLT

### Slide 93: ALU Design
- **F2:** 0
- Function
- A&B
- A|B
- A+B
- not used
- A & ~B
- A | ~B
- A-B
- SLT

### Slide 94: Adder Delay Comparisons
- **Compare delay of:** 32-bit ripple-carry, carry-lookahead, and
- prefix adders
- CLA has 4-bit blocks
- 2-input gate delay = 100 ps; full adder delay = 300 ps
- tripple
- tCLA
- tPA
- = NtFA = 32(300 ps)
- = 9.6 ns
- = tpg + tpg_block + (N/k – 1)tAND_OR + ktFA
- = [100 + 600 + (7)200 + 4(300)] ps
- = 3.3 ns
- = tpg + log2N(tpg_prefix ) + tXOR
- = [100 + log232(200) + 100] ps
- = 1.2 ns

### Slide 96: Set Less Than (SLT) Example
- Configure 32-bit ALU for SLT
- **operation:** A = 25 and B = 32
- – A < B, so Y should be 32-bit
- representation of 1 (0x00000001)
- **– F2:** 0 = 111
- – F2 = 1 (adder acts as
- subtracter), so 25 - 32 = -7
- – -7 has 1 in the most significant
- bit (S31 = 1)
- **– F1:** 0 = 11 multiplexer selects Y
- = S31 (zero extended) =
- 0x00000001.

### Slide 97: Shifters
- **Logical shifter:** shifts value to left or right and fills empty spaces with
- 0’s
- **– Ex:** 11001 >> 2 =
- **– Ex:** 11001 << 2 =
- **Arithmetic shifter:** same as logical shifter, but on right shift, fills empty
- spaces with the old most significant bit (msb).
- **– Ex:** 11001 >>> 2 =
- **– Ex:** 11001 <<< 2 =
- **Rotator:** rotates bits in a circle, such that bits shifted off one end are
- shifted into the other end
- **– Ex:** 11001 ROR 2 =
- **– Ex:** 11001 ROL 2 =

### Slide 98: Shifters
- **Logical shifter:** 
- **– Ex:** 11001 >> 2 = 00110
- **– Ex:** 11001 << 2 = 00100
- **Arithmetic shifter:** 
- **– Ex:** 11001 >>> 2 = 11110
- **– Ex:** 11001 <<< 2 = 00100
- **Rotator:** 
- **– Ex:** 11001 ROR 2 = 01110
- **– Ex:** 11001 ROL 2 = 00111

### Slide 99: Shifter Design

### Slide 100: Shifters as Multipliers,Dividers
- A << N = A × 2N
- **– Example:** 00001 << 2 = 00100 (1 × 22 = 4)
- **– Example:** 11101 << 2 = 10100 (-3 × 22 = -12)
- A >>> N = A ÷ 2N
- **– Example:** 01000 >>> 2 = 00010 (8 ÷ 22 = 2)
- **– Example:** 10000 >>> 2 = 11100 (-16 ÷ 22 = -4)

### Slide 101: Multipliers
- Partial products formed by multiplying a single digit
- of the multiplier with multiplicand
- Shifted partial products summed to form result

### Slide 102: 4 x 4 Multiplier

### Slide 103: 4 x 4 Divider
- A/B = Q + R/B
- **Algorithm:** 
- R’ = 0
- for i = N-1 to 0
- R = {R’ << 1. Ai}
- D=R-B
- if D < 0, Qi=0, R’=R
- else
- Qi=1, R’=D
- R’=R

### Slide 105: MCQs
- Q1. What are the different types of Carry
- propagator adders?
- a)Ripple carry adders
- b)Carry lookahead adders
- c) Prefix adders
- d)Skip ahead adders

### Slide 107: MCQs
- **Q2. A comparator is used to:** 

**a. Add two numbers**

**b. Multiply two numbers**

**c. Determine relative magnitude of two numbers**

**d. Shift a number**

### Slide 109: MCQs
- Q3. Which circuit performs arithmetic and logical
- operations?

**a. Decoder**

**b. Multiplexer**

**c. ALU**

**d. Counter**

### Slide 111: DIGITAL LOGIC AND
- COMPUTER DESIGN
- Number Systems

### Slide 113: Number Systems
- Numbers we can represent using binary representations
- Positive numbers
- Unsigned binary
- Negative numbers
- Two’s complement
- Sign/magnitude numbers
- What about fractions?

### Slide 114: Numbers with Fractions
- **Two common notations:** 
- **– Fixed-point:** binary point fixed
- **– Floating-point:** binary point floats to
- the right of the most significant 1

### Slide 115: Fixed-Point Numbers

**6.75 using 4 integer bits and 4 fraction bits:**
- Binary point is implied
- The number of integer and fraction bits must be agreed upon
- beforehand

### Slide 117: Fixed-Point Number Example
- Represent 7.510 using 4 integer bits
- and 4 fraction bits.
- **Answer:** 01111000

### Slide 119: Signed Fixed-Point Numbers
- **Representations:** 
- – Sign/magnitude
- – Two’s complement

**Example: Represent -7.510 using 4 integer and 4 fraction bits**
- **– Sign/magnitude:** 
- **– Two’s complement:** 

**1. +7.5:**

**2. Invert bits:**

**3. Add 1 to LSB:**
- +

### Slide 120: Floating-Point Numbers
- Binary point floats to the right of the most significant 1
- Similar to decimal scientific notation

**Example: write 27310 in scientific notation:**
- 273 = 2.73 × 102
- In general, a number is written in scientific notation as:
- ± M × BE
- – M = mantissa
- – B = base
- – E = exponent
- – In the example, M = 2.73, B = 10, and E = 2

### Slide 121: Floating-Point Numbers
- We show three versions –final version is called the IEEE 754 floating-point standard

**Example: represent the value 22810 using a 32-bit floating point representation**

### Slide 122: Floating-Point Representation 1

**Example: represent the value 22810 using a 32-bit floating point representation**

**1. Convert decimal to binary (don’t reverse steps 1 & 2!): 22810 = 111001002**

**2. Write the number in “binary scientific notation”: 111001002 = 1.110012 × 27**

**3. Fill in each field of the 32-bit floating point number:**
- The sign bit is positive (0)
- The 8 exponent bits represent the value 7
- The remaining 23 bits are the mantissa

### Slide 123: Floating-Point Representation 2
- First bit of the mantissa is always 1:
- 22810 = 111001002 = 1.11001 × 27
- **So, no need to store it:** implicit leading 1
- Store just fraction bits in 23-bit field

### Slide 124: Floating-Point Representation 3
- **Biased exponent:** bias = 127 (011111112)
- – Biased exponent = bias + exponent
- – Exponent of 7 is stored as: 127 + 7 = 134 = 0x10000110
- The IEEE 754 32-bit floating-point representation of 22810
- **In hexadecimal:** 0x43640000

### Slide 126: Floating-Point Example
- Write -58.2510 in floating point (IEEE 754)

**1. Convert decimal to binary: 58.2510 = 111010.012**

**2. Write in binary scientific notation: 1.1101001 × 25**

**3. Fill in fields:**
- **Sign bit:** 1 (negative)
- **8 exponent bits:** (127 + 5) = 132 = 100001002
- **23 fraction bits:** 110 1001 0000 0000 0000 0000
- **In hexadecimal:** 0xC2690000

### Slide 127: Floating-Point: Special Cases

### Slide 128: Floating-Point Precision
- **Single-Precision:** 
- 32-bit
- 1 sign bit, 8 exponent bits, 23 fraction bits
- bias = 127
- **Double-Precision:** 
- 64-bit
- 1 sign bit, 11 exponent bits, 52 fraction bits
- bias = 1023

### Slide 129: Floating-Point: Rounding
- **Overflow:** number too large to be represented
- **Rounding modes:** 
- **Underflow:** number too small to be represented
- Down
- Toward zero
- To nearest

### Slide 130: Floating-Point: Rounding

**Example: Round 1.100101 (1.578125) to only 3 fraction bits**
- **Down:** 1.100
- **Up:** 1.101
- **Toward zero:** 1.100
- **To nearest:** 1.101 (1.625 is closer to 1.578125 than 1.5 is)

### Slide 131: Floating-Point Addition

**1. Extract exponent and fraction bits**

**2. Prepend leading 1 to form mantissa**

**3. Compare exponents**

**4. Shift smaller mantissa if necessary**

**5. Add mantissas**

**6. Normalize mantissa and adjust exponent if necessary**

**7. Round result**

**8. Assemble exponent and fraction back into floating-point format**

### Slide 132: Floating-Point Addition Example
- Add the following floating-point numbers:
- 0x3FC00000
- 0x40500000

### Slide 133: Floating-Point Addition Example

**1. Extract exponent and fraction bits**
- **For first number (N1):** 
- S = 0, E = 127, F = .1
- **For second number (N2):** 
- S = 0, E = 128, F = .101

**2. Prepend leading 1 to form mantissa**
- **N1:** 

**1.1**
- **N2:** 

**1.101**

### Slide 134: Floating-Point Addition Example

**3. Compare exponents**
- 127 – 128 = -1, so shift N1 right by 1 bit

**4. Shift smaller mantissa if necessary**
- **shift N1’s mantissa:** 1.1 >> 1 = 0.11 (× 21)

**5. Add mantissas**

**0.11 × 21**
- + 1.101 × 21

**10.011 × 21**

### Slide 135: Floating-Point Addition Example

**6. Normalize mantissa and adjust exponent if necessary**

**10.011 × 21 = 1.0011 × 22**

**7. Round result**
- No need (fits in 23 bits)

**8. Assemble exponent and fraction back into floating-point format**
- S = 0, E = 2 + 127 = 129 = 100000012, F = 001100..
- **In hexadecimal:** 0x40980000

### Slide 136: MCQs

**1. Which of the following is NOT a representation for signed fixedpoint numbers?**

**A. Two's Complement**

**B. Sign/Magnitude**

**C. Excess-127**

**D. Both A and B**

**2. In IEEE 754 single-precision floating-point format, how many bits**
- are allocated for the exponent?

**A. 1**

**B. 8**

**C. 11**

**D. 23**

### Slide 137: MCQs

**3. Which IEEE 754 representation corresponds to NaN (Not a Number)?**

**A. Exponent = 00000000, Fraction = 000...0**

**B. Exponent = 11111111, Fraction = 000...0**

**C. Exponent = 11111111, Fraction ≠ 0**

**D. Exponent = 00000000, Fraction ≠ 0**

**4. During floating-point addition, what is the first operation performed after**
- extracting the exponent and fraction bits?

**A. Normalize the mantissa**

**B. Round the result**

**C. Prepend the implicit leading 1 to form the mantissa**

**D. Compare the exponents**

### Slide 138: MCQs

**1. Answer: C. Excess-127**
- **Explanation:** The PPT lists Sign/Magnitude and Two's Complement as signed fixedpoint representations.

**2. Answer: B. 8**
- **Explanation:** Single-precision uses 1 sign bit, 8 exponent bits, and 23 fraction
- (mantissa) bits.

**3. Answer: C. Exponent = 11111111, Fraction ≠ 0**
- **Explanation:** NaN is represented by an all-ones exponent with a non-zero fraction
- field.

**4. Answer: C. Prepend the implicit leading 1 to form the mantissa**
- **Explanation:** After extracting the fields, the hidden leading 1 is restored before
- comparing exponents and performing the addition.

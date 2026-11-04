# UNIT 3: COMPUTER ARCHITECTURE & PROCESSOR DESIGN
**Generated**: 2026-11-04 14:14:16
**Course**: Digital Logic and Computer Design (DLCD) — UE25CS242A / UE25CS251A

---

## TABLE OF CONTENTS

### PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS
1. [Slide Deck 3.1.1: Sequential Building Blocks (48 Pages)](#doc-1) — *Source: `resources/u3/3/Slides/3.1.1_Sequential_Building_Block.pptx`*
2. [Slide Deck 3.3.1: Memory Arrays - RAM, ROM, PLA (41 Pages)](#doc-2) — *Source: `resources/u3/3/Slides/3.3.1_Memory_Arrays.pptx`*
3. [Slide Deck 3.6.1: Computer Architecture Introduction (14 Pages)](#doc-3) — *Source: `resources/u3/3/Slides/3.6.1_Introduction.pptx`*
4. [Slide Deck 3.7.1: Assembly Language & MIPS Architecture (56 Pages)](#doc-4) — *Source: `resources/u3/3/Slides/3.7.1_Assembly_Language.pptx`*
5. [Slide Deck 3.9.1: Machine Language & Instruction Encoding (34 Pages)](#doc-5) — *Source: `resources/u3/3/Slides/3.9.1_Machine_Language.pptx`*
6. [Slide Deck 3.11.1: Programming & Procedures in Assembly (85 Pages)](#doc-6) — *Source: `resources/u3/3/Slides/3.11.1_Programming.pptx`*
7. [Slide Deck 3.14.1: Addressing Modes (29 Pages)](#doc-7) — *Source: `resources/u3/3/Slides/3.14.1_Addressing_Mode.pptx`*
8. [Slide Deck 3.14.2: Compiling, Assembling, and Loading (26 Pages)](#doc-8) — *Source: `resources/u3/3/Slides/3.14.2_COM-ASS-LOAD.pptx`*
9. [Slide Deck 3.15.1: Parallelism - ILP, Multi-threading & Multi-core (37 Pages)](#doc-9) — *Source: `resources/u3/3/Slides/3.15.1_Parallelism.pptx`*
10. [Slide Deck 3.17.1: Classwork Practice Problems (16 Pages)](#doc-10) — *Source: `resources/u3/3/Slides/3.17.1_Classwork_problems.pptx`*
11. [Assignment 3.1.1: Sequential Building Blocks Assignment (2 Pages)](#doc-11) — *Source: `resources/u3/3/Assignments/3.1.1_ASSIGNMENT.docx`*
12. [Question-Answer Bank: 5, 8, 10 Mark Solved Questions (24 Pages)](#doc-12) — *Source: `resources/u3/QA/3.1.1_QA.pdf`*
13. [Comprehensive Descriptive Question Bank (14 Pages)](#doc-13) — *Source: `resources/u3/QB/3.1.1_QB.pdf`*

### PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS
1. [18_sequential-building-blocks.md](#topic-1)
2. [19_computer-architecture-intro.md](#topic-2)
3. [20_assembly-language.md](#topic-3)
4. [21_machine-language.md](#topic-4)
5. [22_addressing-modes.md](#topic-5)
6. [23_compiling-assembling-loading.md](#topic-6)
7. [24_parallelism.md](#topic-7)
8. [25_classwork-problems.md](#topic-8)
9. [26_unit3-mcq-practice.md](#topic-9)

---

# PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS

<a id="doc-1"></a>
## Document 1: Slide Deck 3.1.1: Sequential Building Blocks (48 Pages)
**Source Document**: `resources/u3/3/Slides/3.1.1_Sequential_Building_Block.pptx`
**OCR Extraction File**: `U3_Slides_3.1.1_Sequential_Building_Block.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.1.1_Sequential_Building_Block.pptx
OCR PDF FILE      : U3_Slides_3.1.1_Sequential_Building_Block_ocr.pdf
TOTAL PAGES       : 48
WORD COUNT        : 4306
CHARACTER COUNT   : 25363
DATE EXTRACTED    : 2026-11-04 14:08:34
================================================================================

--- [Page 1 of 48] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 48] ---
PES 
UNIVERSITY 
Sequential Building Blocks
TEAM DLCD
Department of CSE and CSE (AI & ML)
  
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 48] ---
PES 
UNIVERSITY 
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 4 
architecture < 
Digital 
Circuits 
Analog 
Circuits 
»- 
o 
b3 
Physics 
DIGITAL LOGIC & COMPUTER DESIGN
• Counters
• Shift Registers 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
TOPICS

--- [Page 4 of 48] ---
PES 
UNIVERSITY 
Sequential building blocks are digital circuits that store information and change their state in response to a clock.
Unlike combinational circuits, whose outputs depend only on their current inputs, sequential circuits have memory. This 
memory is generally implemented using flip-flops.
Two important sequential building blocks discussed in this section are:
1. Counters 
A counter stores a binary value and changes that value according to a fixed counting sequence. A binary counter normally 
increments its stored value by 1 on every rising edge of the clock.
2. Shift Registers
A shift register stores multiple bits and moves the stored bits from one flip-flop to another on every clock edge.
Applications
●
Counters → timing, event counting, frequency division
●
Shift registers → serial/parallel data conversion and digital testing
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Sequential Building Blocks

--- [Page 5 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
N-bit Binary Counter
What is a Counter?
An N-bit binary counter is a sequential arithmetic circuit with:
●
A clock input
●
A reset input
●
An N-bit output Q
When reset is asserted, the counter is initialized to zero. After reset is released, the counter increments by 1 at every 
rising edge of the clock.
General operation: Qnext=Q+1
Therefore, if the current value is: Q=0101, then at the next rising clock edge: Q=0110
The counter continues this process until it reaches its maximum value and then wraps around to zero.

--- [Page 6 of 48] ---
- 
QS:D 
& PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
N-bit Binary Counter
Figure here, shows an N-bit counter composed of an adder and a resettable register.
On each cycle, the counter adds 1 to the value stored in the register.

--- [Page 7 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Number of States in an N-bit Counter
How many values can an N-bit counter represent?
An N-bit binary number can represent: 2^N different combinations.
Therefore, an N-bit counter has: 2^N possible states
The values range from: 0 to 2^(N−1)
Example: 3-bit counter
Since: 2^3=8
the counter has 8 states:
000 → 001 → 010 → 011
 ↑                                     ↓
111 ← 110 ← 101 ← 100
After 111, the next value is: 000  because the counter has exhausted all 8 possible 3-bit combinations.

--- [Page 8 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Number of States in an N-bit Counter
Example: 8-bit counter
2^8=256
So an 8-bit counter counts from: 0 to 255, before returning to 0.

--- [Page 9 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Reset and Clock
The N-bit binary counter has:
●
Clock input
●
Reset input
●
N-bit output Q
Reset
Reset initializes the output to 0.
Clock
The counter increments on the:
rising edge/falling edge of the clock
Thus: Reset→Q=0 and subsequently, on each rising edge: Q→Q+1

--- [Page 10 of 48] ---
Counter Type 
Asynchronous 
Synchronous 
Up 
Down 
Up/Down 
Decade (MOD-10) 
MOD-N 
Ring 
Johnson 
Clocking Method 
Ripple (chained) 
Global clock 
Increment only 
Decrement only 
Bidirectional 
Reset at10 
Reset at N 
Circulating 1 
Inverted feedback 
2N 
Speed 
Slower 
Faster 
Normal 
Mormal 
Flexible 
Normal 
Mormal 
Fast 
Fast 
PES 
UNIVERSITY 
Applications 
Simple event counting 
High-speed systems 
Timers, counters 
Countdown timers 
Digital clocks 
Frequency division 
Custom sequences 
Sequence confrol 
Pattern generation 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Types of counters
⮚
Asynchronous Counter(Ripple Counter) 
⮚
Synchronous Counter

--- [Page 11 of 48] ---
Clocking 
Speed 
Propagatior 
Comple) 
Power 
Consumption 
Reliability 
Cost 
Applications 
All flip-flops receive the clock signal 
simultaneously 
Faster due to simultaneous switching 
Higher due to additional gates 
More reliable and stable 
Higher due to extra hardware 
Used in high-speed operations 
Flip-flops receive clock from the previous stage 
(ripple effect) 
Slower due to propagation delay 
Lower due to fewer components 
Prone to glitches and timing issues 
Lower as it requires fewer components 
Suitable for low-speed applications 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Types of counters-Differences
⮚Asynchronous Counter(Ripple Counter) 
⮚Synchronous Counter

--- [Page 12 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Types of counters-Differences
Why T and JK Flip-Flops Are Preferred
•
T Flip-Flop (Toggle Flip-Flop)
• Has a single input (T).
• When T = 1, the output toggles on each clock edge.
• This directly divides the clock frequency by 2, making it ideal for 
counters and frequency dividers.
• Simple design, minimal logic required.
•
JK Flip-Flop
• More versatile: can perform Set, Reset, Hold, and Toggle depending 
on J and K inputs.
• When J = K = 1, it behaves exactly like a T flip-flop (toggle mode).
• Eliminates the invalid state problem of SR flip-flops.
• Widely used in counters because of flexibility and reliability.

--- [Page 13 of 48] ---
High 
PES 
UNIVERSITY 
J 
J 
Q 
J 
Q 
J 
Q 
Clock ——|>ck 
.>Ck 
N>Ck 
.>Ck 
K 
K 
Q 
K 
Q 
K 
Q 
Qq 
Qq 
Q2 
Qg 
Clock 
Qo 
Qo 
Q3 
(a) Asynchronous counter 
(b) Timing Diagram 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Types of counters-Asynchronous Counter
Asynchronous Counter (4 BIT RIPPLE / MOD 4 COUNTER)
In an asynchronous counter, there is no common 
(universal) clock for all flip-flops; only the first flip-flop is 
driven by the main clock, and each subsequent flip-flop is 
triggered by the output of the previous one, causing the 
count to ripple through the circuit.
From the timing diagram, 
Q0 changes immediately at the falling edge of the clock, 
Q1 changes at the falling edge of Q0, and the same pattern continues 
for Q2 and Q3. 
This step-by-step change creates a ripple effect through the flip-flops, 
which is why it is called a ripple counter or serial counter. A ripple 
counter is a cascade of flip-flops where the output of one flip-flop acts 
as the clock input for the next.

--- [Page 14 of 48] ---
PES 
UNIVERSITY 
Key Observations: 
* 
This is a MOD-16 counter (because 2* = 16states). 
* 
It’s asynchronous, so changes ripple through flip-flops 
with slight delays. 
* 
Useful for frequency division: 
* 
Qp=clock=+2 
* 
Qi=clock +4 
* 
Qy=clock=+8 
* 
Qz=clock +16 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Asynchronous Counter-MOD-4
Clock 
Pulse
Q₃
Q₂
Q₁
Q₀
Decimal 
Value
Reset
0
0
0
0
0
1
0
0
0
1
1
2
0
0
1
0
2
3
0
0
1
1
3
4
0
1
0
0
4
5
0
1
0
1
5
6
0
1
1
0
6
7
0
1
1
1
7
8
1
0
0
0
8
…
…
…
…
…
…
15
1
1
1
1
15
16
0
0
0
0
0 (wraps)
Timing Diagram (as in the image)
•
Clock: square wave pulses.
•
Q₀: toggles every pulse.
•
Q₁: toggles every 2 pulses.
•
Q₂: toggles every 4 pulses.
•
Q₃: toggles every 8 pulses.
•
Together, they form a binary count sequence from 0 → 15.

--- [Page 15 of 48] ---
Q, 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Asynchronous Counters -Examples
MOD-2 COUNTER(1-BIT)
When -ve edge clock pulse is applied and input is given to FF 
logic 1 then the output state of FF will toggle for every falling 
edge. The output frequency will be f/2 (If f is clock frequency). 
It is known as binary or mod -2 counter or bit ripple counter.
It has 2 unique output states (0 and 1).
MOD 4 COUNTER(2-BIT)
When two FFs are connected in series and output of one FF is act as clock 
for 2nd FF. So the state of 2nd FF will change only when output and 1st FF is 
logic 1 and falling edge occur. The output frequency of Q1 is f/4(if f is clock 
frequency). 
It can generate 4 different unique states. This is known as divide by 4 
circuits or mod 4 ripple counter. 
Here output is taken as Q1(MSB) Q0(LSB).

--- [Page 16 of 48] ---
PES 
UNIVERSITY 
Counter Outputs 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Asynchronous Counters - Examples
       3 Bit-UP COUNTER
3 Bit-DOWN COUNTER
Counter State
Q’C
Q’B
Q’A
7
1
1
1
6
1
1
0
5
1
0
1
4
1
0
0
3
0
1
1
2
0
1
0
1
0
0
1
0
0
0
0
Counter 
State
QC
QB
QA
0
0
0
0
1
0
0
1
2
0
1
0
3
0
1
1
4
1
0
0
5
1
0
1
6
1
1
0
7
1
1
1

--- [Page 17 of 48] ---
PES 
UNIVERSITY 
Combinational 
circuit 
Q * 
QOutput of 
{ 
Previous Flip Flop | Q' * 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Asynchronous Counters -Examples
Design of 3 Bit Asynchronous UP/DOWN Counter 
It is used more than separate up or down counter.
1.
In this a mode control input (say M) is used for selecting up and down mode.
2.
A combinational circuit is required between each pair of flip-flop to decide whether to do up or 
do down counting.
Step 1 : Decision for Mode control input -
Decision for mode control input
When M = 0, then Y= Q, therefore it will perform Up counting (As 
discussed above).
When M = 1, then Y= Q' therefore it will perform Down counting (As 
discussed above).
Combinational circuit is required for deciding mode control(i.e., whether 
counter will perform Up counting or Down counting).
So the all possible combinations are -

--- [Page 18 of 48] ---
Y=QwhenM=0 
Y = Q"' when M=1 
PES 
UNIVERSITY 
Here Y is the output function 
A 
Q 
Q’ 
Y 
QQ’ 
0 
0 
. 
00 
01 
11 
10 
1 
' 
: 
[ 
o 
< 
0 
1 
1 
1 
0 
0 
0 
0 
1 
1 
B 
Y=A+B 
1 
0 
0 
Y=M'Q +MQ’ 
1 
1 
1 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Asynchronous Counters -Examples

--- [Page 19 of 48] ---
PES 
UNIVERSITY 
M 
Logic 1 
Jy 
Qs 
Clock ——> 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Asynchronous Counters -Examples
Insertion of Combinational logic between every pair of FFs -

--- [Page 20 of 48] ---
Qg 
Q4 
Qo 
| 
V 
CLR 
0 
| 
V 
CLR 
| 
V 
CLR 
| 
| 
V 
CLR 
Qa3 
| 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Asynchronous Counters -Examples
Decade Counter
Counts ten states and then resets to its initial state. The most common decade counter counts from 0 to 9, but it can also be 
designed to count any ten states within 0 to 15 in a 4-bit counter before resetting. 
Clock 
pulse
Q3
Q2
Q1
Q0
0
0
0
0
0
1
0
0
0
1
2
0
0
1
0
3
0
0
1
1
4
0
1
0
0
5
0
1
0
1
6
0
1
1
0
7
0
1
1
1
8
1
0
0
0
9
1
0
0
1
10
0
0
0
0
From the circuit diagram, a NAND gate is connected to Q3 and Q1 and its output is fed to the 
clear input because the binary representation of 10 is 1010. When Q3 and Q1 both become 1, 
the NAND gate output goes low, activating the clear input, so the counter resets at 10 and 
starts counting again from 0.

--- [Page 21 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Synchronous Counters 
Synchronous Counter 
Unlike an asynchronous counter, a synchronous 
counter uses a single global clock that drives all flip-
flops simultaneously, so all outputs change in parallel. 
Its main advantage is that it can operate at higher 
frequencies because it does not suffer from 
cumulative delay, as the same clock is applied to 
every flip-flop. Hence, it is also called a parallel 
counter.

--- [Page 22 of 48] ---
PES 
UNIVERSITY 
Step 1: 
Decide the number of flip Tlops. 
Step 2: Excitation table of FF. 
Step 3: State diagram and circuit excitation table 
Step 4: Obtain simplified equations using K' map. 
Step 5: 
Draw the logic diagram. 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Synchronous Counters -Examples
Steps to design Synchronous Counters

--- [Page 23 of 48] ---
OUTPUT 
State Diagram: 2-Bit Gray Code Counter (Sequential) 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Synchronous Counters -Examples
Design 2 bit Synchronous Up Counter
Step1: Decide the number of Flipflops – 2 (JK)
Step2: Excitation table of JK FF
Step3: State Diagram & Circuit ET

--- [Page 24 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Synchronous Counters -Examples
Step 4: Solve for J1 K1 J2 K2 USING K MAPS
Step 5: Draw the logic diagram

--- [Page 25 of 48] ---
PES 
UNIVERSITY 
3-Bit Up-Counter State Diagram 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Synchronous Counters -Examples
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Design 3 bit Synchronous Up Counter using T FF
Step1: Decide the number of Flipflops – 3 (T FF)
Step2: Excitation table of T FF
Step3: State Diagram & Circuit ET
INPUT
OUTPUT
Qn
Qn+1
T
0
0
0
0
1
1
1
0
1
1
1
0

--- [Page 26 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Synchronous Counters -Examples
Step 4: Solve for T1 T2 T3 USING K MAPS
Step 5: Draw the logic diagram

--- [Page 27 of 48] ---
PES 
UNIVERSITY 
£;h1 Eiaut 
CLK 
Q 
Q@ 
& 
Qn_1 
Load 
CLK 
Sin —Ho 
0 
0 
o 
S 
1 
1 
1 
Ly 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
What Is a Shift Register?
●A chain of flip-flops sharing one clock.
●On each clock edge, a new bit enters at Sin; every stored bit moves forward one position.
●The oldest bit exits at Sout.
●After N cycles, all N bits sit together on parallel outputs Q0...QN-1.
●Function: converts a serial (one-bit-at-a-time) stream into a parallel N-bit word.
Shift register symbol
Shift register schematic
Shift register with parallel load

--- [Page 28 of 48] ---
Test 
D —o 
S, —1 
CLK 
CLK 
CLK 
< 
ip b 
©n 
= Sin Snut — 
TJest 
Test 
| 
(b) 
(c) 
DN—1 
<~ 
<~ 
<~ 
<~ 
D 
Q- 
D 
Q- 
D 
QH 
D 
Q 
L NN 
Sin Snut 
Sin Snut 
Sin Snut 
Sin Snut 
Test 
Test 
Test 
Test 
I 
I 
| 
| 
PES 
UNIVERSITY 
B S+::uut 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Shift Registers
Scannable flip-flop: (a) schematic, (b) symbol, and (c) N-bit scannable register

--- [Page 29 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Shift Register
Internal structure:
●Built from N flip-flops connected in series.
●Each flip-flop's output feeds the next flip-flop's input.
●All flip-flops share the same clock signal.
●Some designs add a reset signal to clear all flip-flops to 0.
Adding Parallel Load:
●Basic shift register only does serial-to-parallel.
●Add a parallel data input D(N-1:0) and a control signal Load to also support 
parallel-to-serial.
●When Load = 1: all flip-flops load directly from D (parallel load, one cycle).
●When Load = 0: register shifts normally (Sin feeds in, bits move forward).

--- [Page 30 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
HDL Description
always @(posedge clk or posedge rst)
  if (rst)        q <= 0;
  else if (load)  q <= data_in;         // parallel load
  else            q <= {q[N-2:0], sin}; // shift in sin
assign sout = q[N-1];
●
rst clears everything, highest priority.
●
load loads the full word from data_in in one cycle.
●
Otherwise, bits shift up and sin fills the empty slot.
●
sout is always the top bit of the register.

--- [Page 31 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Why Test Sequential Circuits Differently ?
●Combinational circuits: easy to test, apply input, check output.
●Sequential circuits: hard since the output depends on internal state.
●Example: to verify bit 31 of a 32-bit counter flips 0→1, naively need to reset then apply ~2 billion clock 
pulses.
●Problem: too many flip-flops to give each one its own test pin.
Scan Chains: The Solution
●Connect all flip-flops in the system into one long shift register called a scan chain.
●Normal mode: each flip-flop loads from its regular D input; scan connections ignored.
●Test mode: flip-flops shift data serially in/out via Sin/Sout — internal state can be read out or 
overwritten directly.
●The mux for switching modes is usually built into the flip-flop itself, forming a "scannable flip-flop."

--- [Page 32 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Type of counters - Ring counters
Definition
●
A ring counter is a shift-register-based 
counter in which the output of the last flip-
flop is fed back to the first.
●
It consists of n flip-flops connected in a 
circular manner.
●
A single 1 circulates through the flip-flops 
with each clock pulse.
Example: 4-bit Ring Counter
1000 → 0100 → 0010 → 0001 → 1000 → …
Key Point:
 For n flip-flops → n valid states → MOD-n 
counter
ORI means overriding input:   If PR(preset) = 0 then Q=1
                                                      If Clr = 0 then Q=0   
It is used to initialize counters as 1 0 0 0  
It is used to initialize (preset) the ring counter to a valid starting 
state.

--- [Page 33 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Type of counters - Ring counters
Circuit & Working
4-Bit Ring Counter
●
Four flip-flops are connected as a shift register.
●
All flip-flops receive a common clock.
●
The output of the last flip-flop is connected back to 
the input of the first.
●
The counter must be initialized with a single 1.
Working: Q0 → Q1 → Q2 → Q3 → Q0
At every clock pulse, the 1 shifts to the next flip-flop.
ORI is an initialization/reset-type control signal. It forces the 
ring counter into its starting state, usually 1000, before normal 
counting begins.
So remember:
ORI = Overriding Input
ORI = 0 → initialize the counter
ORI = 1 → normal ring-counter operation
One important point: ORI is not the clock. It is an overriding 
control used to establish the initial 1 in the ring.

--- [Page 34 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Type of counters - Ring counters
Ring Counter Timing/State Table

--- [Page 35 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Type of counters - Ring counters
Advantages
●
Simple circuit design
●
Fast operation
●
Directly provides decoded outputs
●
No additional decoding logic required
Limitations
●
Requires n flip-flops for n states
●
More hardware compared with binary counters
●
Requires proper initialization
●
0000 is an invalid/stuck state
Applications
●
Sequence generation
●
Timing and control circuits
●
Stepper motor control
●
Digital control systems
●
Timing signal generation
A ring counter circulates a single HIGH bit through 
a series of flip-flops to generate a repeating 
sequence of states.

--- [Page 36 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Type of counters - Johnson counters
●A Johnson counter is a modified shift-
register counter.
●It is also called a Twisted Ring Counter or 
Switch-Tail Ring Counter.
●The complement of the last flip-flop output 
is fed back to the input of the first flip-flop.
●For n flip-flops, a Johnson counter has 2n 
valid states.
Example:
 4-bit Johnson Counter → 8 states

--- [Page 37 of 48] ---
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Type of counters - Johnson counters
4-Bit Johnson Counter
The complemented output of the last flip-flop is fed 
back to the first.
Feedback:
D₀ = Q₃^(-)
At every clock pulse, the contents shift by one position.
Starting from 0000:
0000 → 1000 → 1100 → 1110 → 1111 → 0111 → 0011 
→ 0001 → 0000
Thus, the sequence repeats after 8 clock pulses.

--- [Page 38 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Type of counters - Johnson counters
Timing Waveforms of a 4-Bit Johnson (Twisted Ring) Counter

--- [Page 39 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Worked Example: Testing a 32-bit Counter
●Goal: confirm the counter correctly increments.
●Step 1: Shift in test pattern 0111...111 (32 bits) - 32 cycles.
●Step 2: Switch to normal mode, run 1 clock cycle (counter increments).
●Step 3: Shift the result out - 32 cycles ,  verify it reads 1000...000.
●Total: 65 cycles, instead of ~2 billion.

--- [Page 40 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
1. An N-bit binary counter with reset advances through how many distinct output values before repeating?
 A) N
 B) N²
 C) 2N
 D) 2^N
2. In the counter design built from an adder and a resettable register, what value is added to the register's contents on 
every clock cycle?
 A) 0
 B) 1
 C) N
 D) Reset value

--- [Page 41 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
1. An N-bit binary counter with reset advances through how many distinct output values before repeating?
 A) N
 B) N²
 C) 2N
 D) 2^N
 Answer: D
2. In the counter design built from an adder and a resettable register, what value is added to the register's contents on 
every clock cycle?
 A) 0
 B) 1
 C) N
 D) Reset value
 Answer: B

--- [Page 42 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
3. In the counter HDL, what has priority when both reset and the clock edge occur?
 A) The increment (q <= q + 1)
 B) Reset (q <= 0)
 C) Neither - output is undefined
 D) Load
4. What is the key structural difference between a plain shift register and a shift register with parallel load?
 A) The plain version has no clock input
 B) The parallel-load version adds a D input and Load control with a mux before each flip-flop
 C) The plain version uses combinational logic only
 D) The parallel-load version removes Sout

--- [Page 43 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
3. In the counter HDL, what has priority when both reset and the clock edge occur?
 A) The increment (q <= q + 1)
 B) Reset (q <= 0)
 C) Neither - output is undefined
 D) Load
 Answer: B
4. What is the key structural difference between a plain shift register and a shift register with parallel load?
 A) The plain version has no clock input
 B) The parallel-load version adds a D input and Load control with a mux before each flip-flop
 C) The plain version uses combinational logic only
 D) The parallel-load version removes Sout
 Answer: B

--- [Page 44 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
5. Why is testing sequential circuits harder than testing combinational circuits?
 A) Sequential circuits have no outputs
 B) Sequential circuits' outputs depend on internal state reached over many cycles, not just current inputs
 C) Sequential circuits cannot be clocked
 D) Sequential circuits use more transistors
6. In a scan chain, how does a flip-flop behave in normal (non-test) mode?
 A) It loads from its usual D input; scan connections are ignored
 B) It always loads from Sin
 C) It shifts one position per cycle regardless of mode
 D) It resets every cycle

--- [Page 45 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
5. Why is testing sequential circuits harder than testing combinational circuits?
 A) Sequential circuits have no outputs
 B) Sequential circuits' outputs depend on internal state reached over many cycles, not just current inputs
 C) Sequential circuits cannot be clocked
 D) Sequential circuits use more transistors
 Answer: B
6. In a scan chain, how does a flip-flop behave in normal (non-test) mode?
 A) It loads from its usual D input; scan connections are ignored
 B) It always loads from Sin
 C) It shifts one position per cycle regardless of mode
 D) It resets every cycle
 Answer: A

--- [Page 46 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
7. For the 32-bit counter scan-chain test example, what is the total number of cycles needed (shift in + 1 count cycle + 
shift out)?
 A) 32
 B) 33
 C) 64
 D) 65

--- [Page 47 of 48] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Questions
7. For the 32-bit counter scan-chain test example, what is the total number of cycles needed (shift in + 1 count cycle + 
shift out)?
 A) 32
 B) 33
 C) 64
 D) 65
 Answer: D

--- [Page 48 of 48] ---
PES 
UNIVERSITY 
CELEBRATING SO YEARS 
Team DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-2"></a>
## Document 2: Slide Deck 3.3.1: Memory Arrays - RAM, ROM, PLA (41 Pages)
**Source Document**: `resources/u3/3/Slides/3.3.1_Memory_Arrays.pptx`
**OCR Extraction File**: `U3_Slides_3.3.1_Memory_Arrays.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.3.1_Memory_Arrays.pptx
OCR PDF FILE      : U3_Slides_3.3.1_Memory_Arrays_ocr.pdf
TOTAL PAGES       : 41
WORD COUNT        : 4384
CHARACTER COUNT   : 25283
DATE EXTRACTED    : 2026-11-04 14:08:10
================================================================================

--- [Page 1 of 41] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 41] ---
PES 
UNIVERSITY 
 Memory Arrays
TEAM DLCD
Department of CSE and CSE (AI & ML)
  
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 41] ---
PES 
UNIVERSITY 
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 4 
architecture < 
Digital 
Circuits 
Analog 
Circuits 
»- 
o 
b3 
Physics 
DIGITAL LOGIC & COMPUTER DESIGN
5.5 Memory Arrays
 5.5.1 Overview
 5.5.2 Dynamic Random Access Memory (DRAM)
 5.5.3 Static Random Access Memory (SRAM)
 5.5.4 Area and Delay
 5.5.5 Register Files
 5.5.6 Read Only Memory
 5.5.7 Logic Using Memory Arrays
 5.5.8 Memory HDL
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
TOPICS

--- [Page 4 of 41] ---
PES 
UNIVERSITY 
Address ——| Array 
I 
Data 
Figure 5.38 Generic memory 
array symbol 
" 
1024-word x 
Address 2% 
32-bit 
Array 
$32 
Data 
Figure 5.40 32 Kb array: depth = 
2'° = 1024 words, width = 32 bits 
DIGITAL LOGIC & COMPUTER DESIGN
5.5 Memory Arrays — Overview
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A memory array stores many words using a 2-D array of 1-bit cells.
• N address bits select one of 2^N words.
• Each word contains M data bits.
• Size = depth × width = 2^N × M bits.
• Memories are specified by size and by the number/type of ports.
Example: 10 address bits + 32-bit data
→ 2^10 = 1024 words
→ 1024 × 32 = 32 Kb
Each bit cell connects to a wordline and a bitline. A decoder activates one wordline 
for the selected address.

--- [Page 5 of 41] ---
Word @ 
Word 1 
Word 2 
Word 3 
Bit 3 
Bit 2 
Bit 1 
Bit © 
| 
| 
1 
1 
1 
| 
e 
| 
1 
[ 
e 
| 
| 
| 
| 
| 
| 
| 
| 
| 
1 
1 
| 
|1 
| 
e 
[ 
1 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
e 
[ 
e 
| 
1 
| 
| 
| 
| 
| 
| 
| 
| 
| 
1 
1 
| 
|1 
|1 
[ 
e 
| 
| 
L 
| 
| 
| 
| 
PES 
UNIVERSITY 
What does N address bits mean? 
Suppose we have N address bits. 
Each address bit can be either O or 1. 
Therefore, the number of different addresses is: 
2N 
So, N address bits can select 2" different words. 
For example: 
« 
2 address bits — 22 = 4words 
« 
3 address bits — 23 = 8words 
« 
10 address bits — 21° = 1024words 
So: 
10 address bits mean the memory has 1024 words. 
What does M data bits mean? 
If each word contains M bits, then each selected row has M bits. 
For example: 
32-bit data means: 
One word = 32 bits 
Therefore, if we have 1024 words: 
1024 x 32 = 32768 bits 
Since: 
32768 = 32 X 1024 = 32K 
the memory size is: 
132 Kbits| 
Important: This is 32 Kb (kilobits), not 32 KB (kilobytes). 
DIGITAL LOGIC & COMPUTER DESIGN
5.5 Memory Arrays — Overview
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
What is a memory array?
A memory is made up of many tiny 1-bit storage cells 
arranged in rows and columns.
Think of it like a spreadsheet:
•
Each row = one word 
•
Each column = one bit 
•
A collection of bits in one row forms a word 
For example, if each word is 4 bits:

--- [Page 6 of 41] ---
Address —2+ 
2:4 
Decoder 
1 
10 
01 
00 
PES 
UNIVERSITY 
Figure 5.42 4 x 3 memory array 
bitline, 
bitline, 
bitline, 
wordline, 
| 
| 
| 
stored 
stored 
stored 
. 
bit=0 
bit=1 
bit=0 
wordline, 
| 
| 
| 
stored 
stored 
stored 
wordline, 
bit=1 
bit=0 
bit=0 
| 
| 
| 
stored 
stored 
stored 
. 
bit =1 
bit=1 
bit=0 
wordline, 
| 
| 
| 
stored 
stored 
stored 
bit=0 
bit= 1 
bit =1 
Data, 
Data; 
Data, 
Address —2~{ Array 
Data 
(a) 
Address 
Data 
11 
(o|1]o]| 
4 
10 
|1/0|0 
depth 
01 
1110 
00 
|01 
¥ 
- 
width 
(b) 
Figure 5.39 4 x 3 memory 
array: (a) symbol, (b) function 
DIGITAL LOGIC & COMPUTER DESIGN
5.5 Memory Arrays — Overview
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 7 of 41] ---
PES 
UNIVERSITY 
bitline 
wordline 
, 
stored 
bit 
Figure 5.41 Bit cell 
DIGITAL LOGIC & COMPUTER DESIGN
Memory Array: Bit Cell Organization
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Memory Bit Cell
●
A memory array is built as an array of bit cells, where each bit cell stores 1 bit.
●
Each bit cell is connected to:
○
Wordline – selects the bit cell.
○
Bitline – transfers data to or from the bit cell.
●
For each combination of address bits, one wordline is activated.
●
When the wordline is HIGH, the selected bit cells are connected to their bitlines.
●
When the wordline is LOW, the bitline is disconnected from the bit cell.
●
The circuitry used to store the bit depends on the type of memory.
Wordline = Selects the row
Bitline = Carries the data

--- [Page 8 of 41] ---
PES 
UNIVERSITY 
bitline 
wordline 
] 
stored 
bit 
Figure 5.41 Bit cell 
DIGITAL LOGIC & COMPUTER DESIGN
Reading and Writing a Bit Cell
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Read Operation
1. Bitline is initially left floating (Z).
2. The wordline is turned ON.
3. The stored bit drives the bitline to 0 or 1.
Bit Cell→Bitline
Write Operation
1. Bitline is strongly driven to the desired value.
2. The wordline is turned ON.
3. The strongly driven bitline overpowers the existing bit.
4. The desired value is stored in the bit cell.
Bitline→Bit Cell​

--- [Page 9 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Memory Array Organization
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Internal Organization of a 4 × 3 Memory Array
●
A 4 × 3 memory array contains:
○
4 words (rows)
○
3 bits per word
●
Practical memories are much larger, but their operation can be understood using this smaller array.
●
A decoder selects one wordline based on the given address.
●
The selected row of bit cells is connected to the Data bitlines.
Read Operation
●
Wordline is asserted.
●
The selected row of bit cells drives the bitlines HIGH or LOW.
●
The resulting values appear on the Data bitlines.
Write Operation
●
Data bitlines are first driven to the required values.
●
The appropriate wordline is then asserted.
●
The bitline values are stored in the selected row.

--- [Page 10 of 41] ---
Address 2 
2:4 
Decoder 
11 
10 
01 
00 
PES 
UNIVERSITY 
bitline, 
bitline, 
bitline, 
wordlines 
| 
| 
| 
stored | || stored | ||stored | | 
) 
bit=0 
bit =1 
bit=0 
wordline, 
| 
| 
| 
stored | stored | 
stored | 
wordiine, 
bit=1 
bit=0 
bit=0 
| 
| 
| 
stored | || 
stored | || 
stored | | 
: 
bit=1 
bit=1 
bit=0 
wordline, 
| 
| 
| 
stored | || 
stored - stored ) 
bit=0 
bit=1 
bit=1 
Data, 
Data, 
Data, 
Figure 5.42 4 x 3 memory array 
DIGITAL LOGIC & COMPUTER DESIGN
Memory Array Organization
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Reading Address 10
1.
Address = 10
2.
Decoder asserts wordline₂.
3.
Bitlines are initially left floating.
4.
The selected row contains 100.
5.
Therefore, 100 appears on the Data bitlines.
10→Wordline2→100
Writing 001 to Address 11
1.
Address = 11
2.
Data bitlines are driven to 001.
3.
Decoder asserts wordline₃.
4.
The value 001 is stored in that row.
11+001→Wordline3→001 stored
READ: Wordline ON→Stored data drives bitlines
WRITE: Drive bitlines→Wordline ON→Store data

--- [Page 11 of 41] ---
Address —2«| 
(a) 
Address 
11 
10 
o1 
00 
(b) 
PES 
UNIVERSITY 
Array 
Data 
Data 
ol1 o 
i 
110 
|0 
depth 
1(1 
|0 
o|l1 
|1 
w 
= 
e 
width 
Figure 5.39 4 >< 3 memory 
array: (a) symbol, (b) function 
DIGITAL LOGIC & COMPUTER DESIGN
Memory Array: Depth, Width(Word size) 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Depth, width and bit cells
• Depth = number of words (rows).
• Width = number of bits per word (columns).
Example: 4 × 3 memory
• 2 address bits select 1 of 4 words.
• Each word contains 3 bits.
• Total storage = 4 × 3 = 12 bits.

--- [Page 12 of 41] ---
CLK 
| 
PES 
UNIVERSITY 
N 
Al 
A2 
A3 
WwD3 
g 
=4 
WE3 RO 
RD2 
Array 
2 
M 
Figure 5.43 Three-ported 
memory 
DIGITAL LOGIC & COMPUTER DESIGN
Memory Ports & Read/Write Example
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A memory port provides access to one memory address. Memories may be single-
ported or multiported.
Example: three-port memory
• Two read ports can read addresses A1 and A2 simultaneously.
• One write port writes WD3 to address A3 when WD3 is asserted on the rising clock 
edge.
Practical example — register file:
A processor may read two source registers while writing one destination register in 
the same cycle.

--- [Page 13 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Memory Array Classification
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Memory arrays are specified by:
●
Size: Depth × Width
●
Number of ports
●
Type of ports
All memory arrays store data using an array of bit cells, but they differ in how the bits are 
stored.
RAM vs ROM: The broadest classification of memory is:
RAM
ROM
Random Access Memory
Read Only Memory
Volatile
Nonvolatile
Loses data when power is turned OFF
Retains data without power
Historically associated with read/write memory
Historically associated with read-only memory
Both RAM and ROM can be randomly accessed. Modern ROMs can also be written in various ways.

--- [Page 14 of 41] ---
PES 
UNIVERSITY 
bitline 
wordline 
1 
stored 
| 
bit 
g 
Figure 5.44 DRAM bit cell 
stored 
— 
bit 
- 
bitline 
| 
bitline 
I 
ine— 
wordline 
T 
T 
Figure 5.46 SRAM bit cell 
DIGITAL LOGIC & COMPUTER DESIGN
DRAM vs SRAM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
There are two major types of RAM:
1. DRAM (Dynamic RAM)
• Stores each bit as charge on a capacitor.
• Charge leaks away, so periodic refresh is required.
• Reading disturbs/destroys the capacitor value, so the data is restored after a read.
• The simplified cell uses about 1 transistor per bit → very dense.
1. SRAM (Static RAM)
• Stores the bit using cross-coupled inverters.
• No periodic refresh is required while power is applied.
• The cross-coupled inverters restore the value if noise disturbs it.
• A typical SRAM bit cell uses 6 transistors → larger than DRAM but faster.
Book comparison: flip-flop ≈ 20 transistors/bit, SRAM ≈ 6, DRAM ≈ 1.

--- [Page 15 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
DRAM vs SRAM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
1. Why is DRAM called "Dynamic"?
A DRAM cell stores a bit as electrical charge on a capacitor.
Charged capacitor → 1 
Discharged capacitor → 0 
But the capacitor gradually leaks its charge.
So:
Stored charge → leaks with time → data may be lost → refresh is 
required
That's why it is Dynamic: the stored value needs to be periodically 
refreshed.
2. Why is SRAM called "Static"?
SRAM uses cross-coupled inverters.
The two inverters continuously reinforce each other's state:
        ┌──────────┐
   Q ──│ Inverter │── Q̅
►
►
        └──────────┘
                    │
▲
             │       ▼
        ┌──────────┐
   Q̅ ──│ Inverter │── Q
►
►
        └──────────┘
If Q = 1, the feedback keeps Q = 1 and Q̅ = 0.
If Q = 0, the feedback keeps Q = 0 and Q̅ = 1.
Therefore, as long as power is supplied, SRAM does not need 
periodic refresh.
3. Why is SRAM faster than DRAM?
The important difference is:
DRAM → charge must be sensed from a capacitor
SRAM → logic state is already maintained by the transistor circuit
So SRAM can generally be accessed faster, but its cell requires more 
transistors and therefore occupies more chip area.

--- [Page 16 of 41] ---
DRAM vs SRAM vs Flip-Flop 
Feature 
DRAM 
Basic storage 
Capacitor charge 
Typical transistors/bit 
1T + capacitor 
Refresh required? 
Yes 
Read operation 
Destructive — restore 
needed 
Speed 
Slower 
Density 
Highest 
Main use 
Main memory 
SRAM 
Cross-coupled inverters 
6T 
No 
MNon-destructive 
Faster 
Lower 
Cache 
Flip-Flop 
Feedback logic 
~20T 
No 
MNon-destructive 
Very fast 
Lowest 
Registers/sequential logic 
PES 
UNIVERSITY 
COMPUTER 
SRAM 
CPU Cache 
STORAGE 
l 
| 
| 
| 
SSD 
HDD 
MAND Flash 
Magnetic disk 
DIGITAL LOGIC & COMPUTER DESIGN
DRAM vs SRAM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 17 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Volatile Memory - Area & Delay
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Flip-flops, SRAM, and DRAM are all volatile memories, but they differ in area, latency, and throughput.
Memory
Transistors/Bit
Relative Latency
Key characteristic
Flip-flop
~20
Fast
Output available immediately
SRAM
6
Medium
Faster access than DRAM
DRAM
1
Slow
High density
Why?
●
More transistors generally mean more area, power, and cost.
●
Flip-flops: data is immediately available at the output, but require at least ~20 transistors.
●
SRAM: uses 6 transistors per bit.
●
DRAM: uses only 1 transistor per bit, making it more area-efficient.

--- [Page 18 of 41] ---
hifline 
wordine 
stored +‘+ 
bit=1 l 
1 
wordine 
stored | 
=0 T 
[ 
bifling 
1 
o 
V 
PES 
UNIVERSITY 
& 
Figure 5,45 DRAM stored values 
DIGITAL LOGIC & COMPUTER DESIGN
Why is DRAM Slower?
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DRAM stores a bit as charge on a capacitor.
As shown in Figure 5.45(a), when the capacitor is charged to VDD, the stored bit is 1; when it is discharged to GND 
(Figure 5.45(b)), the stored bit is 0. 
During a read:
1. Charge moves from the capacitor → bitline.
2. The bitline is not actively driven by a transistor.
3. Charge movement is relatively slow.
4. Therefore, DRAM has higher latency than SRAM.
DRAM also has lower throughput
DRAM must:
●
Periodically refresh its stored data.
●
Refresh the data after a read.
Therefore, its throughput is fundamentally lower than SRAM.

--- [Page 19 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
SDRAM & DDR SDRAM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Technologies were developed to improve DRAM throughput:
SDRAM - Synchronous DRAM
●
Uses a clock
●
Pipelines memory accesses
DDR SDRAM - Double Data Rate SDRAM
●
Transfers/accesses data on both rising and falling edges of the clock.
●
Therefore, it can double the throughput for a given clock speed.
It should be noted that DDR was first standardized in 2000, initially operating at 100–200 MHz. Later standards such as DDR2, DDR3, 
and DDR4 increased clock speeds.
Important take away DRAM → lower area per bit, but higher latency and lower throughput.
 SRAM → faster, but uses more transistors.
 Flip-flop → fastest, but largest per-bit implementation.
Also remember: Larger memories tend to be slower than smaller memories, assuming other factors are the same. The appropriate 
memory type depends on the design's speed, cost, and power constraints.

--- [Page 20 of 41] ---
PES 
UNIVERSITY 
CLK 
| 
| 
o 
—/SL Al 
WES RN flé? 
—;‘é— A2 
RD?2 wfi 
—<— A3 
o 
Register 
32 
WD3 
File 
Figure 5.47 32 x 32 register 
file with two read ports and one 
write port 
DIGITAL LOGIC & COMPUTER DESIGN
Register Files
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Register file = a group of registers used to store temporary variables in a digital system.
●
Usually implemented as a small, multi-ported SRAM array
●
More compact than building the same registers using an array of flip-flops
●
A register file can allow multiple registers to be accessed simultaneously.
Example: 32 × 32 Three-Ported Register File
The textbook's Figure 5.47 shows a 32-register × 32-bit register file with:
●
2 read ports:
○
A1 → RD1
○
A2 → RD2
●
1 write port:
○
A3 → WD3
●
CLK controls the write operation.
●
Each address is 5 bits, because:      2^5 = 32

--- [Page 21 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Register Files
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Therefore:
Two registers can be read and one register can be written simultaneously.
Numerical 
For a 32 × 32 register file:
Number of registers=32
 
Bits per register=32
 
Address bits=log⁡2(32)=5
Total storage:
32×32=1024 bits
Register File → Small multi-ported SRAM → Temporary storage → Multiple simultaneous accesses

--- [Page 22 of 41] ---
PES 
UNIVERSITY 
bitline 
wordline 
T 
| p— 
7 
bit cell 
containing O 
bitline 
wordline 
bit cell 
containing 1 
Figure 5.48 ROM bit cells 
containing 0 and 1 
DIGITAL LOGIC & COMPUTER DESIGN
Read-Only Memory (ROM)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
ROM stores each bit based on the presence or absence of a transistor.
How a ROM bit cell works
1. The bitline is weakly pulled HIGH.
2. The wordline is turned ON.
3. If a transistor is present → it pulls the bitline LOW → stored bit = 0.
4. If a transistor is absent → bitline remains HIGH → stored bit = 1.
Key point
ROM is non volatile because its bit cell is a combinational circuit and has no state that is lost 
when power is removed.

--- [Page 23 of 41] ---
PES 
UNIVERSITY 
2:4 
Decoder 
11 
i 
Address 24 
10 
- 
01 
® 
& 
00 
& 
@ 
Data, Data, Data, 
DIGITAL LOGIC & COMPUTER DESIGN
ROM Dot Notation
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
ROM contents can be represented using dot notation.
●
Rows → Wordlines / Addresses
●
Columns → Bitlines / Data bits
●
Dot at an intersection → stored bit = 1
●
No dot → stored bit = 0
Example: 4 × 3 ROM
A 4-word × 3-bit ROM has: 2^2=4 words
and each word contains:3 bits
So the total storage is:
4×3=12 bits
For the example shown in Figure 5.49, the top wordline has a dot only on Data1, so the 
corresponding stored word is 010.

--- [Page 24 of 41] ---
2:4 
Address 
-3« 
Decoder 
11 
10 
01 
00 
Figure 5.50 4 x 3 ROM implementation using gates 
Data, Data, Data 
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
ROM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 25 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
ROM as Logic
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A ROM can also be viewed as a two-level logic circuit:
AND gates → OR gates
First level: AND gates
●
Generate all possible minterms
●
Therefore, they function as a decoder
Second level: OR gates
●
Combine selected minterms
●
Produce the required output functions
So conceptually: Address → Decoder → OR gates → Data
Important point: A ROM can implement any two-level logic function.
In practice, ROMs use transistors instead of logic gates to reduce size and cost.

--- [Page 26 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Types of ROM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
ROMs differ mainly in how their contents are programmed and erased.
1. Mask ROM
●
Contents are specified during manufacturing
●
A transistor is either present or absent in each bit cell.
●
Cannot be changed by the user.
2. PROM - Programmable ROM
●
Transistors are initially present.
●
User can program the memory.
●
In the fuse-programmable version, programming selectively blows fuses.
●
Once programmed, it cannot be reversed.
PROM = One-Time Programmable ROM (OTP)

--- [Page 27 of 41] ---
PES 
UNIVERSITY 
bitline 
wordline 
T 
intact 
fuse 
bit cell containing O 
bitline 
wordline 
T 
blown | 5 
fuse 
bit cell containing 1 
Figure 5.51 Fuse-programmable 
ROM bit cell 
DIGITAL LOGIC & COMPUTER DESIGN
Fuse-Programmable ROM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Programming operation
Fuse intact:
●
Transistor connected to GND
●
Cell stores 0
Fuse blown:
●
Transistor disconnected from GND
●
Cell stores 1
A high voltage is applied to selectively blow the required fuses.
Because a blown fuse cannot be repaired:
PROM is one-time programmable​

--- [Page 28 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Reprogrammable ROM
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
EPROM — Erasable Programmable ROM
Uses a floating-gate transistor.
Programming:
●
High voltage causes electrons to move onto the floating gate.
●
This changes the transistor's state.
Erasing:
●
Exposed to intense UV light.
●
UV light removes the electrons from the floating gate.
So:
EPROM → Program electrically → Erase using UV light

--- [Page 29 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
EEPROM & Flash Memory
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
EEPROM
Electrically Erasable Programmable ROM
●
Can be programmed electrically.
●
Can also be erased electrically.
●
Individual bits/cells can be erased.
●
No UV light required.
Flash Memory
●
Uses similar principles to EEPROM.
●
Erases larger blocks of bits rather than individual cells.
●
Requires fewer erasing circuits.
●
Therefore, it is cheaper than EEPROM.

--- [Page 30 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Comparison
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Type
Programmable?
Erasable?
Erasing method
Mask ROM
During manufacturing
No
—
PROM
Once
No
—
EPROM
Yes
Yes
UV light
EEPROM
Yes
Yes
Electrical
Flash
Yes
Yes
Electrical, block-wise

--- [Page 31 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Memory Arrays as Logic
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Memory arrays are primarily used for data storage, but they can also implement combinational logic functions.
For a memory of: 2^N-words×M-bits
it can implement any combinational function with:
●
N inputs
●
M outputs
Why?
●
The N inputs are used as the address.
●
Each possible input combination corresponds to one memory row.
●
The M data bits stored in that row represent the outputs.
So:
Inputs → Address → Memory Array → Data Outputs

--- [Page 32 of 41] ---
Address -2+ 
2:4 
Decoder 
11 
10— 
01 —e 
00 
4 
Data, Datay Data, 
l 
¢ 
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Example — ROM as Combinational Logic
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
The 4 × 3 ROM from Figure 5.49 has:
●
4 words → 2^2, so 2 inputs
●
3-bit data → 3 outputs
Therefore, it implements: 3 functions of 2 inputs
For this particular ROM:
●
Data2 = XOR of the two address inputs
●
Data0 = NOR of the two address inputs
●
Data1 is another combinational function determined by the stored ROM contents.
Key idea
The ROM contents essentially represent the truth table of the desired logic functions.

--- [Page 33 of 41] ---
PES 
UNIVERSITY 
4-word x 1-bit Array 
p 
2:4 
- 
Truth 
Decoder 
bitline 
Table 
00 
: 
A 
A 
st.ored - 
A 
BlY 
bit =0 
B 
Ao 
01 
| 
g 
(1) 
g 
stored - 
bit =0 
1 
0 
0 
10 
1 
- 
: 
. 
stored e 
bit =0 
11 
, 
stored - 
bit=1 
X 
J 
4 
Figure 5.52 4-word x 1-bit memory array used as a lookup table 
DIGITAL LOGIC & COMPUTER DESIGN
Lookup Tables (LUTs)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A memory array used to perform logic is called a:
Lookup Table (LUT)
Instead of constructing a function using individual logic gates, we store the output values in memory.
How a LUT works
1. Inputs are applied as an address.
2. The address selects a particular row.
3. The stored data in that row gives the output.
Input combination → Address → Selected row → Output

--- [Page 34 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
Example — LUT for Y=AB
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Lets uses a 4-word × 1-bit memory to implement: Y=AB
Since there are 2 inputs:2^2=4 possible input combinations
A
B
Address
Y = AB
0
0
00
0
0
1
01
0
1
0
10
0
1
1
11
1
The LUT simply stores: 0, 0, 0, 1
For N inputs and M outputs: LUT size=2N×M

--- [Page 35 of 41] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Q1. An N-bit binary counter has how many possible states?
A. N
B. 2N
C. N²
D. 2^N
Q2. What happens to a binary counter on each rising clock edge after reset is released?
A. Q remains constant
B. Q decreases by 1
C. Q increases by 1
D. Q becomes all 1s

--- [Page 36 of 41] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Q3. A shift register with N flip-flops can act as which converter?
A. Serial-to-parallel
B. Analog-to-digital only
C. Frequency-to-voltage
D. Decimal-to-BCD only
Q4. In a shift register with parallel load, what happens when Load = 1?
A. The register is cleared
B. D inputs are loaded into the flip-flops
C. The clock is disabled permanently
D. The register shifts without loading D

--- [Page 37 of 41] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Q5. A memory has 10 address bits and 8 data bits. What is its organization?
A. 10 × 8 bits
B. 100 × 8 bits
C. 1024 × 8 bits
D. 2048 × 10 bits
Q6. During a memory read, what does the decoder primarily do?
A. Adds two data words
B. Activates the wordline for the selected address
C. Refreshes every bit cell
D. Converts binary to decimal

--- [Page 38 of 41] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Q7. Which statement about DRAM is correct?
A. It stores data in cross-coupled inverters and never needs refresh
B. It stores charge on a capacitor and requires refresh
C. It is nonvolatile
D. It uses more transistors per bit than a flip-flop
Q8. Which statement about SRAM is correct?
A. It requires periodic refresh like DRAM
B. It stores the bit using cross-coupled inverters
C. A read always destroys the stored bit
D. It is nonvolatile

--- [Page 39 of 41] ---
PES 
UNIVERSITY 
DIGITAL LOGIC & COMPUTER DESIGN
MCQ
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Q9. A typical processor register file in the textbook has which port arrangement?
A. One read port and no write port
B. Two read ports and one write port
C. Three write ports and no read ports
D. One read/write port only
Q10. A 2^N-word × M-bit memory used as a LUT has:
A. N input/address bits and M output bits
B. M input bits and N output bits
C. N output bits only
D. One fixed output bit

--- [Page 40 of 41] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Answer Key:
Q1: D    Q2: C     Q3: A    Q4: B      Q5: C    Q6: B
Q7: B    Q8: B      Q9: B    Q10: A

--- [Page 41 of 41] ---
PES 
UNIVERSITY 
CELEBRATING SO YEARS 
Team DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-3"></a>
## Document 3: Slide Deck 3.6.1: Computer Architecture Introduction (14 Pages)
**Source Document**: `resources/u3/3/Slides/3.6.1_Introduction.pptx`
**OCR Extraction File**: `U3_Slides_3.6.1_Introduction.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.6.1_Introduction.pptx
OCR PDF FILE      : U3_Slides_3.6.1_Introduction_ocr.pdf
TOTAL PAGES       : 14
WORD COUNT        : 822
CHARACTER COUNT   : 5626
DATE EXTRACTED    : 2026-11-04 14:04:36
================================================================================

--- [Page 1 of 14] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 14] ---
PES 
UNIVERSITY 
ARCHITECTURE-Introduction
TEAM DLCD
Department of CSE and CSE (AI & ML)
  DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 14] ---
PES 
UNIVERSITY 
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 4 
architecture < 
Digital 
Circuits 
Analog 
Circuits 
»- 
o 
b3 
Physics 
DIGITAL LOGIC & COMPUTER DESIGN
• Introduction
• Assembly Language
• Machine Language
• Programming
• Addressing modes
• Parallelism
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
TOPICS

--- [Page 4 of 14] ---
PES 
UNIVERSITY 
What is Computer Architecture
    Computer Architecture is the programmer's view of a computer. It defines how software 
communicates with hardware by specifying:
• Instruction Set Architecture (ISA)
• Operand locations (Registers and Memory)
• Data representation and instruction formats
Why Study Computer Architecture?
• Bridges the gap between hardware and software.
• Determines how programs are executed by the processor.
• Helps design efficient, compatible, and high-performance computer systems.
• Provides a foundation for understanding processor organization and programming.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Introduction

--- [Page 5 of 14] ---
PES 
UNIVERSITY 
Architecture vs. Microarchitecture 
Computer Architecture 
Microarchitecture 
Defines how the processor is 
Defines what the processor does 
implemented 
Visible to programmers 
Internal hardware organization 
Includes ALU, datapath, control unit, 
Includes ISA, registers and memory 
pipeline, cache 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Introduction

--- [Page 6 of 14] ---
ARCHITECTURE vs MICROARCHITECTURE 
[ 
Another Real-World Analogy: 
A RESTAURANT 
| 
F 
ARCHITECTURE 
| 
MICROARCHITECTURE 
Similar to the menu and services 
- 
Similar to the kitchen operations and 
offered to the customer. 
' 
processes that make the service possible. 
INGREDIENT 
MANAGEMENT 
COOKING 
KITCHEN 
PROCESS 
EQUIPMENT 
(CPUL) 
i 
(Hardware Units) 
@ APPETIZERS 
) 
MAIN COURSE 
\ 
| 
N—" 
A ome-in 
= ;’i 
BEVERAGES 
[‘j TAKEAWAY 
- 
E 
DESSERTS 
SLL HOME DELIVERY 
Focuses on what the customer sees 
Focuses on how the service is delivered 
and interacts with. 
behind the scenes. 
It defines the interface and experience. 
It defines the internal implementation 
and hardware details. 
COORDINATION 
& TIMING 
(Control Unit) 
\II 
‘Q: In Short: 
Architecture is WHAT the customer gets. 
| 
Microarchitecture is HOW it is made possible. 
” 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Introduction

--- [Page 7 of 14] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Introduction
• Many Architectures Exist: e.g. x86, MIPS, SPARC, and PowerPC
⚬Each architecture defines its own instruction set
• Instruction Sets Are Like Dialects: once you learn one, learning another is fairly 
straightforward
• Instructions: the words of a computer’s language; even complex applications 
compile down to simple instructions like add, subtract, and jump

--- [Page 8 of 14] ---
PES 
UNIVERSITY 
Real-World Processor Architectures 
Many architectures exist, such as x86, MIPS, SPARC and PowerPC. 
Each architecture defines its own instruction set. 
Used in most PCs and 
Used in gaming consoles, 
desktop computers 
m networking and embedded systems 
Examples: Intel, AMD 
Examples: Nintendo, Cisco, Silicon Graphics 
C 
* 
[ =] 
Used in workstations 
Used in computers 
T 
and servers 
D 
and systems 
== 
Examples: Sun Microsystems 
. 
— 
Examples: IBM, Apple 
)& 
Instruction sets are like different dialects. 
'.Q.» 
Once you learn one, learning another is fairly straightforward! 
[ %) 
Real-World Analog 
= e 
. 
is the internal 
_— 
engine design 
'0 
used to implement 
those controls. 
Architecture 
is similar to the 
controls available 
to a car driver. 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Introduction

--- [Page 9 of 14] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
• Q1. What is “architecture” as defined in this chapter?
a.The programmer’s view of a computer, defined by the instruction set and 
operand locations
b.The physical arrangement of transistors on a chip
c.The way registers are wired to the ALU
d.A hardware description language

--- [Page 10 of 14] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
•
Q2. Which of the following is the human-readable form of instructions?
a. Machine language
b. Assembly language
c. Binary code
d. Microcode

--- [Page 11 of 14] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
•
Q3. Machine language instructions are ultimately encoded as:
a. Decimal numbers
b. ASCII characters
c. Binary (1’s and 0’s)
d. Hexadecimal strings only

--- [Page 12 of 14] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
• Q4. Who developed the MIPS architecture, and where?
a.John Hennessy and colleagues at Stanford
b.Dennis Ritchie at Bell Labs
c.Gordon Moore at Intel
d.Alan Turing at Cambridge

--- [Page 13 of 14] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
• Answer Key
Q1: A     Q2: B     Q3: C     Q4: A

--- [Page 14 of 14] ---
PES 
UNIVERSITY 
CELEBRATING SO YEARS 
Team DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-4"></a>
## Document 4: Slide Deck 3.7.1: Assembly Language & MIPS Architecture (56 Pages)
**Source Document**: `resources/u3/3/Slides/3.7.1_Assembly_Language.pptx`
**OCR Extraction File**: `U3_Slides_3.7.1_Assembly_Language.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.7.1_Assembly_Language.pptx
OCR PDF FILE      : U3_Slides_3.7.1_Assembly_Language_ocr.pdf
TOTAL PAGES       : 56
WORD COUNT        : 5078
CHARACTER COUNT   : 32484
DATE EXTRACTED    : 2026-11-04 14:09:00
================================================================================

--- [Page 1 of 56] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 56] ---
PES 
UNIVERSITY 
ARCHITECTURE-Assembly Language
TEAM DLCD
Department of CSE and CSE (AI & ML)
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 56] ---
PES 
UNIVERSITY 
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 4 
architecture < 
Digital 
Circuits 
Analog 
Circuits 
»- 
o 
b3 
Physics 
DIGITAL LOGIC & COMPUTER DESIGN
• Instructions
• Operands: Registers, Memory, and 
Constants 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
TOPICS

--- [Page 4 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Assembly language
• Instructions: commands in a computer’s language
⚬Assembly language: human–readable format of  instructions
⚬Machine language: computer–readable format (1’s  and 0’s)
• MIPS architecture:
⚬MIPS (Microprocessor without Interlocked Pipelined Stages) is a family of 
reduced instruction set computer (RISC), instruction set architectures (ISA) 
developed by MIPS Computer Systems, now MIPS Technologies, based in 
United States.
⚬Developed by John Hennessy and his colleagues at  Stanford, in 1980’s.
⚬Used in many commercial systems, including Silicon Graphics, Nintendo and 
Cisco
⚬Once you’ve learnt one architecture, it’s easy to learn others

--- [Page 5 of 56] ---
PES 
UNIVERSITY 
Code Example 6.4 REGISTER OPERANDS 
High-Level Code 
MIPS Assembly Code 
a=b+c: 
$3$s0=a, $sl="h, $52=c¢ 
add $s0, $s1, $s?2 
ffa=b+c 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
MIPS Instruction: Addition 
C Code
a = b + c;
MIPS assembly code
add a, b, c
add: mnemonic indicates operation to perform (here it is addition).
b, c: source operands (on which the operation is performed).
a: destination operand (to which the result is written).

--- [Page 6 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
MIPS Instruction: Subtraction 
C Code
a = b - c;
MIPS assembly code
sub  a, b, c
sub: mnemonic indicates operation to perform (here it is subtraction).
b, c: source operands (on which the operation is performed).
a: destination operand (to which the result is written).

--- [Page 7 of 56] ---
PES 
UNIVERSITY 
Computer architectures are designed using a set of fundamental principles that improve 
performance, simplicity, and efficiency.
1. Simplicity Favors Regularity
• Simple and uniform instruction formats simplify hardware design.
• Regular structures are easier to implement, test, and optimize.
2. Make the Common Case Fast
• Frequently executed operations should be optimized.
• Improves overall system performance since common tasks dominate execution time.
3. Smaller is Faster
• Smaller hardware structures, such as registers and caches, have lower access time.
• Faster access leads to improved processor performance.
4. Good Design Demands Good Compromises
• Every design involves trade-offs between performance, cost, power, and complexity.
• An efficient architecture balances these factors instead of optimizing only one.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Architecture Design Principles

--- [Page 8 of 56] ---
PES 
UNIVERSITY 
Simplicity Favors Regularity
• MIPS uses a consistent and uniform instruction format for most instructions.
• Arithmetic instructions follow the format:
⚬Two source operands
⚬One destination operand
• Uniform instruction formats simplify instruction encoding, decoding, and hardware 
implementation.
• Regular designs reduce hardware complexity, making processors faster, more reliable, and 
easier to design.
        Example: add $s0, $s1, $s2
                          sub $t0, $t1, $t2
        Both instructions follow the same format:
        Destination = Source1 OP Source2
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Design Principle – 1

--- [Page 9 of 56] ---
PES 
UNIVERSITY 
 Make the Common Case Fast
• Processor performance is improved by optimizing the operations that are 
executed most frequently.
• MIPS includes a small set of simple, commonly used instructions that can be 
decoded and executed quickly.
• Simple instructions enable smaller, faster, and more efficient hardware.
• Complex operations are implemented by combining multiple simple instructions, 
rather than using a single complex instruction.
• MIPS follows the Reduced Instruction Set Computer (RISC) philosophy, 
emphasizing simplicity and speed.
• In contrast, architectures such as Intel x86 follow the Complex Instruction Set 
Computer (CISC) approach, where individual instructions perform more complex 
tasks.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Design Principle – 2

--- [Page 10 of 56] ---
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Design Principle – 2
Feature
RISC (e.g., MIPS, ARM, RISC-V)
CISC (e.g., x86, VAX)
Instruction Set Size
Small, simple set (≈ 30–100 instructions)
Large, complex set (hundreds to thousands)
Instruction Length
Fixed (commonly 32 bits)
Variable (1–15 bytes in x86)
Execution Time
Most instructions complete in 1 clock cycle
Instructions may take multiple cycles
Complexity Location
Complexity shifted to compiler/software
Complexity handled by hardware/microcode
Memory Access
Load/Store architecture (only load/store access 
memory; ALU ops use registers)
ALU operations can directly access memory 
(read-modify-write)
Registers
Many general-purpose registers (e.g., 32 in 
ARM/RISC-V)
Fewer registers (e.g., 16 in x86-64)
Pipelining
Easy and efficient due to uniform instruction size Harder due to variable-length instructions
Code Density
Larger program size (more instructions for 
complex tasks)
Smaller program size (complex tasks in fewer 
instructions)
Instruction Decoding
Simple, fast decoding
Complex, slower decoding
Hardware Complexity
Low — simpler control logic, fewer transistors
High — microcode, wide decoders, more 
transistors
Performance Strategy
Reduce cycles per instruction (CPI)
Reduce instructions per program
Power Consumption
Lower (efficient per watt, common in 
mobile/embedded systems)
Higher (desktop/server CPUs with more power 
budget)
Examples
ARM, RISC-V, MIPS, SPARC
Intel x86, AMD64, VAX

--- [Page 11 of 56] ---
PES 
UNIVERSITY 
Code Example 6.5 TEMPORARY REGISTERS 
High-Level Code 
MIPS Assembly Code 
a=b+c-d; 
f#$s0=a, 
$sl=b, $s2=c, $s3=d 
sub $t0, $s2, $s3 
#ft=c~-d 
add $s0, $s1, $tO 
ffa=b+t 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Multiple Instructions
• More complex code is handled by multiple MIPS  instructions.
C Code
a = b + c - d;
add t, b, c 
 sub a, t, 
d
# t = b + c 
  # a = t - 
d
MIPS assembly code
A RISC architecture minimizes the hardware complexity and the necessary instruction encoding by 
keeping the set of distinct instructions small. 
For example, an instruction set with 64 simple instructions would need log264 = 6 bits to encode the 
operation. 
An instruction set with 256 complex instructions would need log2256 = 8 bits of encoding per 
instruction. 
In a CISC machine, even though the complex instructions may be used only rarely, they add overhead 
to all instructions, even the simple ones.

--- [Page 12 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Every instruction performs an operation on one or more operands. An operand is the 
data used by an instruction, and it can be stored in different locations within a 
computer.
The three operand locations in the MIPS architecture are:
• Registers – High-speed storage locations inside the CPU used for frequently 
accessed data.
• Memory – Stores large amounts of program instructions and data that cannot fit 
in registers.
• Constants (Immediates) – Fixed values encoded directly within the instruction.
Example: addi $t0, $t1, 10.                 
$t0 → Destination Register
$t1 → Source Register
10 → Immediate (Constant)
DIGITAL LOGIC & COMPUTER DESIGN
Operands: Locations

--- [Page 13 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
• Registers are small, high-speed storage locations inside the CPU used to hold 
operands and intermediate results.
• MIPS provides 32 general-purpose registers, each 32 bits wide.
• Registers can be accessed much faster than main memory, reducing instruction 
execution time.
• MIPS is called a 32-bit architecture because its registers and ALU operate on 32-
bit data.
• Frequently used variables are stored in registers, while less frequently used data 
is stored in memory.
DIGITAL LOGIC & COMPUTER DESIGN
Operands: Registers

--- [Page 14 of 56] ---
PES 
UNIVERSITY 
Smaller is Faster
• Smaller hardware structures generally have lower access time and can operate at higher 
speeds.
• MIPS includes 32 general-purpose registers, providing a balance between performance and 
hardware complexity.
• A smaller register file allows faster access, reducing instruction execution time.
• Frequently accessed data is stored in registers, while larger amounts of data are kept in main 
memory.
• This design improves overall processor performance by minimizing slower memory accesses.
Example:
• Accessing data from a register takes significantly less time than accessing the same data from 
main memory.
• Therefore, compilers try to keep frequently used variables in registers whenever possible.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Design Principle – 3

--- [Page 15 of 56] ---
PES 
UNIVERSITY 
Name
Register Number
Usage
$0
0
the constant value 0
$at
1
assembler temporary
$v0–$v1
2–3
function return values
$a0–$a3
4–7
function arguments
$t0–$t7
8–15
temporaries
$s0–$s7
16–23
saved variables
$t8–$t9
24–25
more temporaries
$k0–$k1
26–27
OS temporaries
$gp
28
global pointer
$sp
29
stack pointer
$fp
30
frame pointer
$ra
31
function return address
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
MIPS Register Set

--- [Page 16 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Operands: Registers
MIPS Register Naming Convention
‒
    In MIPS, every register name is prefixed with a '$' symbol.
‒
    Example: $0 (read as register zero or dollar zero).
‒
Registers are assigned specific roles to simplify programming and improve code 
organization.
Commonly Used Registers
‒
$0 (Register Zero): Always stores the constant value 0.
‒
$s0 – $s7 (Saved Registers): Used to store variables whose values must be preserved 
across function calls.
‒
$t0 – $t9 (Temporary Registers): Used to store intermediate results during 
calculations; their contents need not be preserved.
‒
$a0 – $a3 (Argument Registers): Used to pass arguments to functions.
‒
$v0 – $v1 (Value Registers): Used to store function return values.

--- [Page 17 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Operands: Registers
Example:
                 add $t0, $s1, $s2
• $s1, $s2 → Source operands (saved registers)
• $t0 → Destination operand (temporary register)
Note: Other special-purpose registers such as $sp (Stack Pointer), $fp (Frame Pointer), 
and $ra (Return Address) will be discussed later during function calls and stack 
management.

--- [Page 18 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Operands: Memory
•
The 32 registers in MIPS are insufficient to store all program data. 
•
Main memory is used to store additional data and program instructions.
•
Memory provides large storage capacity, but it is slower to access than registers.
•
Frequently accessed variables are kept in registers, while less frequently used data 
is stored in memory.
•
Data is transferred between memory and registers using load (lw) and store (sw) 
instructions.
Key Point:
    Registers provide fast access for frequently used data, while memory provides large 
storage for the rest of the program.

--- [Page 19 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Memory organization
Memories are organized as an array of data words. 
The MIPS architecture uses 32-bit memory addresses and 32-bit data words.
MIPS uses a byte-addressable memory. 
That is, each byte in memory has a unique address. 
However, for explanation purposes only, we first introduce a word-addressable 
memory, and afterward describe the MIPS byte-addressable memory.

--- [Page 20 of 56] ---
PES 
UNIVERSITY 
A 32-bit address means an address itself contains 32 bits (N). 
Therefore, theoretically, MIPS can identify: 
232 
different addresses. 
That is: 
232 = 4,294,967,296 
different byte locations. 
Since each location is 1 byte, this corresponds to: 
4 GB 
of byte-addressable memory. 
Data 
32-bit data word 
= 4 bytes 
Address 
32-bit address 
= identifies one byte location 
So: 
32-bit address - one BYTE 
32-bit data word - four BYTES 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Memory organization

--- [Page 21 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Memory organization
Let's take a real example
Suppose memory contains:
Address     Data
-------          ----
1000          AA
1001          BB
1002          CC
1003          DD
These four bytes together form one 32-bit word:
AA BB CC DD
Therefore:
Address 1000 ─┐
Address 1001  │
Address 1002  ──→ one 32-bit word
├
Address 1003 ─┘
The next 32-bit word starts at address:
1004
This is why MIPS addresses often increase by 4
Suppose you have an array of 32-bit integers:
int A[0]
int A[1]
int A[2]
int A[3]……..int A[31]
Each integer is 4 bytes.
Therefore:
A[0] → address 0
A[1] → address 4
A[2] → address 8
A[3] → address 12
Notice:
0 → 4 → 8 → 12
not
0 → 1 → 2 → 3
because each integer occupies 4 bytes.

--- [Page 22 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Memory organization: Word-Addressable Memory
Word-Addressable Memory: A word-addressable memory is a memory organization in 
which each memory address refers to one complete word. A word is the natural unit 
of data processed by the processor.
For a 32-bit processor:
●1 Word = 32 bits = 4 Bytes
●Each address stores one complete 32-bit word.
●Memory addresses increase by 1 word.
Characteristics
●One address points to one entire word.
●Efficient for processors that mainly operate on full words.
●Individual bytes cannot be directly addressed.

--- [Page 23 of 56] ---
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Memory organization: Word-Addressable Memory
Example:
Address
Stored data
0
Word 0
1
Word 1
2
Word 2
Key Point: In word-addressable memory, Address 2 means the third word, not the third 
byte.

--- [Page 24 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Reading Word-Addressable Memory
Reading data from memory is called a Load operation.
MIPS uses the instruction:
    lw destination, offset(base)
where:
●lw → Load Word
●destination → Register that receives the data
●base → Starting memory address
●offset → Displacement added to the base address
Address Calculation:
Effective Address=Base Register+Offset

--- [Page 25 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Reading Word-Addressable Memory
Example:
              lw $s0, 5($t1)
If, $t1 = 20
Then, Address = 20 + 5 = 25
The word stored at address 25 is loaded into $s0.

--- [Page 26 of 56] ---
Word 
Address 
00000003 
00000002 
00000001 
00000000 
Data 
4 
O 
F 307 
88 
O1 EE2 
8 42 
2 FE 1A LD T 
ABCDEFT7BS8 
PES 
UNIVERSITY 
Word 3 
Word 2 
Word 1 
Word O 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Reading Word-Addressable Memory: Example
Example:
lw $s3, 1($0)
Step 1: Base Register, $0 = 0
Step 2: Offset: 1
Step 3: Effective Address, 0 + 1 = 1
Step 4: The processor reads the contents of Memory Word 1.
$s3 = 0xF2F1AC07
Observation:
Only one instruction is needed to transfer an entire 32-bit word from memory to a 
register.

--- [Page 27 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Writing Word-Addressable Memory
Writing data into memory is called a Store operation.
MIPS uses the instruction:
sw source, offset(base)
where:
●sw → Store Word
●source → Register containing data
●base → Base memory address
●offset → Address displacement
Address Calculation:
Effective Address=Base Register+Offset
The value from the register is copied into the calculated memory location.

--- [Page 28 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Writing Word-Addressable Memory: Example
Example:
sw $t4, 0x7($0)   #write the value in $t4 to memory word 7
Step 1: Base Address, $0 = 0
Step 2: Offset, 0x7 = 7
Step 3: Effective Address, 0 + 7 = 7
Result:
The value stored in $t4 is written into Memory Word 7.

--- [Page 29 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Memory Organization: Byte-Addressable Memory
Byte-Addressable Memory: A byte-addressable memory is a memory organization in 
which each memory address refers to one byte (8 bits) of data.
For a 32-bit processor:
1 Byte = 8 bits
1 Word = 32 bits = 4 Bytes
Therefore, one 32-bit word occupies four consecutive byte addresses.
Characteristics:
• Each address identifies exactly one byte.
• Memory addresses increase by 1 byte at a time.
• MIPS uses byte-addressable memory.

--- [Page 30 of 56] ---
PES 
UNIVERSITY 
Word 
Address 
| 
Data 
. 
O0000000C 
4 O|F 3|0 7|8 8| 
Word 3 
00000008 
O1|EE|2 8|4 2| 
Word 
2 
00000004 
|F 2|F 1|A C|0 7| 
Word 1 
00000000 
ABICDHEVF| 7 8| 
Word O 
- 
L 
width = 4 bytes 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Memory Organization: Byte-Addressable Memory
A 32-bit word consists of four 8-bit bytes. So each word address is 
a multiple of 4, as shown in Figure 6.2. Again, both the 32-bit word 
address and the data value are given in hexadecimal.

--- [Page 31 of 56] ---
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Byte-Addressable Memory: Example
Example:
Suppose one 32-bit word contains 0xF2F1AC07.
In byte-addressable memory, this word occupies four consecutive byte addresses.
Byte Address
Meaning
0x04 – 0x07
Four bytes belonging to one 32-bit word
(0xF2F1AC07)
0x08
Starting byte address of the next word
0x0C
Starting byte address of the following word
Key Point: The next 32-bit word begins at address 0x08, because each word occupies 4 bytes.

--- [Page 32 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Reading Byte-Addressable Memory
Example:
lw $s3, 4($0)
Step 1: Base register, $0 = 0
Step 2: Offset = 4
Step 3: Effective address = 0 + 4 = 4
Step 4: The processor reads the four bytes stored at addresses 4, 5, 6, and 7.
Result: The four bytes are combined to form one 32-bit word and loaded into $s3.
Observation: In MIPS, the offset in lw and sw is measured in bytes, not in words.

--- [Page 33 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Word-Addressable vs Byte-Addressable Memory
Comparison:
• In word-addressable memory, one address refers to one complete word.
• In byte-addressable memory, one address refers to exactly one byte.
• In a 32-bit system, one word occupies 1 address in word-addressable memory but 4 
consecutive addresses in byte-addressable memory.
• Word addresses increase by 1 word, whereas byte addresses increase by 1 byte.
• Byte-addressable memory is more flexible because individual bytes can also be 
accessed independently.
Key Point: MIPS uses byte-addressable memory, so consecutive 32-bit words begin at 
addresses such as 0, 4, 8, 12.
"A MIPS word is 32 bits or 4 bytes, but MIPS assigns an address to every 
byte, not every word. Therefore, one 32-bit word occupies four 
consecutive memory addresses."

--- [Page 34 of 56] ---
Big-Endian 
Address 
<(thfo|Q 
MEaIP-dlu 
Nw~| @ 
g?l‘;nnmn 
Word 
Address 
<IN 
NORLL 
PES 
UNIVERSITY 
Little-Endian 
Little-Endian 
Address 
N(D| 
2| M 
=100 
Niolk(e|0 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Big–Endian & Little–Endian Example
• How to number bytes within a word?
• Little-endian: byte numbers start at the little (least significant) end
• Big-endian: byte numbers start at the big (most significant) end
• Word address is the same for big- or little-endian
           Big-Endian

--- [Page 35 of 56] ---
Byte 
Address 
ClDIE[F 
8 
9 
A 
B 
4 
5 
6 
7 
MsB- 2 Lk 
Word 
Address 
_c_ 
3 
4 
@) 
Little-Endian 
Byte 
Address 
FlED 
C 
B 
A 
9 
8 
/ 
6 
5 
4 
I\;I;SE‘-2 
1 LS% 
& PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Big–Endian & Little–Endian Example
• Jonathan Swift’s Gulliver’s Travels: the Little-Endians broke their eggs on the little 
end of the egg and the Big-Endians broke their eggs on the big end.
• It doesn’t really matter which addressing type is used – except when the two 
systems need to share data!
           Big-Endian

--- [Page 36 of 56] ---
PES 
UNIVERSITY 
Big-Endian 
Little-Endian 
Word 
Byte Address 
0,1,2,3 
Address 
3(2|1|0 
Byte Address 
Data Value 
|23|45|67(89 
0 
23|45|67(89| 
Data Value 
MSB 
LSB 
MSB 
LSB 
Figure 6.4 Big-endian and little-endian data storage 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Big–Endian & Little–Endian Example
• Suppose $t0 initially contains 0x23456789
• After following code runs on big–endian system, what value is in $s0?
• In a little–endian system?
sw $t0, 0($0)  // It stores the entire 32-bit value 0x23456789 starting at byte address 0.
lb $s0, 1($0)
• Big–endian:       0x00000045
• Little–endian:   0x00000067

--- [Page 37 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Design principle - 4
Good Design Demands Good Compromises
• Processor design involves balancing performance, cost, power consumption, 
and hardware complexity.
• Improving one aspect of a system often requires sacrificing another; therefore, 
practical designs rely on carefully chosen trade-offs.
• MIPS adopts a Reduced Instruction Set Computer (RISC) architecture by using a 
small set of simple instructions instead of many complex ones.
• This simplifies hardware implementation, improves execution speed, and 
reduces power consumption.
• An effective computer architecture achieves the best overall balance rather 
than optimizing a single parameter.

--- [Page 38 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Design principle - 4
Example
RISC (MIPS): 
⚬Simple instructions
⚬Faster execution
⚬Simpler hardware
        
 CISC (x86):
■Complex instructions
■More hardware complexity
■Fewer instructions per program

--- [Page 39 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Operands: Constant (Immediate)
Immediate Operands
●Constants are values embedded directly within the instruction, so they are 
immediately available during execution.
●MIPS uses a 16-bit signed (two's complement) field to represent immediate 
values.
●Immediate operands eliminate the need to load small constants from memory, 
reducing the number of instructions.
Immediate Instructions
●addi (Add Immediate): Adds a constant directly to the value in a register.
●andi, ori, xori: Perform bitwise operations using immediate constants.

--- [Page 40 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC &COMPUTER DESIGN
Operands: Constant (Immediate)
Why is there no subi instruction?
MIPS does not require a separate subi instruction because subtraction can be 
performed by adding a negative immediate.
Example:
addi $s1, $s0, -12
This instruction is equivalent to:
b = a - 12;
Key Point
Immediate instructions improve efficiency by encoding small constants directly 
in the instruction, avoiding an extra memory access or register for the constant.

--- [Page 41 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Operands: Constant (Immediate)
C Code:                                          
MIPS Assembly code:
                                                         
# $s0 = a,  $s1 = b
a = a + 4;                                          
addi $s0, $s0, 4
b = a – 12;                                        
addi $s1, $s0, –12 
Instruction Explanation:
●addi $s0, $s0, 4
#Adds the immediate value 4 to $s0.
○Result: $s0 = $s0 + 4 (a = a + 4)
●addi $s1, $s0, -12
#Adds −12 to $s0 and stores the result in $s1.
○Result: $s1 = $s0 - 12 (b = a - 12)
Note: addi uses a 16-bit signed immediate, so subtraction is 
performed by adding a negative value.

--- [Page 42 of 56] ---
PES 
UNIVERSITY 
Example 6.1 TRANSLATING HIGH-LEVEL CODE TO ASSEMBLY LANGUAGE 
Translate the following high-level code into assembly language. Assume variables a
–c are held in registers $s0–$s2 and f–j are in $s3–$s7.
a = b – c; 
f = (g + h) − (i + j);
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Think About It - 1
DIGITAL LOGIC & COMPUTER DESIGN

--- [Page 43 of 56] ---
Solution: The program uses four assembly language instructions. 
# MIPS assembly code 
#$s0=a, $sl=b, $s2=c, $s3 =", $s4 =g, $s6=h 
#$s6=1, $s7 =] 
sub $s0, 
add $t0, 
add $tl, 
sub $s3, 
$sl, $s2 
$s4, $sb5 
$s6, $s/ 
$t0, $tl 
fa=Db-c 
Fotl=1 
+ j 
#f=(g+h)-(i+]) 
& PES 
UNIVERSITY 
Example 6.1 TRANSLATING HIGH-LEVEL CODE TO ASSEMBLY LANGUAGE 
Translate the following high-level code into assembly language. Assume variables a
–c are held in registers $s0–$s2 and f–j are in $s3–$s7.
a = b – c; 
f = (g + h) − (i + j);
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Think About It - 1
DIGITAL LOGIC & COMPUTER DESIGN

--- [Page 44 of 56] ---
Code Example 6.8 ACCESSING BYTE-ADDRESSABLE MEMORY 
MIPS Assembly Code 
Tw $s0, 0($0) 
# read data word 0 (OxABCDEF78) into $s0 
lw $s1, 8(%$0) 
# read data word 2 (OX01EE2842) into $sl 
Iw $s2, 0xC($0) 
it read data word 3 (0x40F30788) into $s? 
sw $s3, 4(30) 
fwrite $s3 todataword 1 
sw $s4, 0x20(30) 
#write $s4 to data word 8 
sw $s5, 400($0) 
fwrite $s5 to data word 100 
PES 
UNIVERSITY 
The code shows how to read and write words in the MIPS byte-addressable 
memory. The word address is four times the word number. The MIPS assembly code 
reads words 0, 2, and 3 and writes words 1, 8, and 100. The offset can be written in 
decimal or hexadecimal.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Think About It - 2
DIGITAL LOGIC & COMPUTER DESIGN

--- [Page 45 of 56] ---
PES 
UNIVERSITY 
Using the instructions learnt so far (add and sub), can you write a program (sequence of 
instructions) that would left shift a number (stored in some register) by three bit 
positions? How many registers do you need?
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Think About It - 3
DIGITAL LOGIC & COMPUTER DESIGN

--- [Page 46 of 56] ---
PES 
UNIVERSITY 
Using the instructions learnt so far (add and sub), can you write a program 
(sequence of instructions) that would left shift 
a number (stored in some 
register) by three bit positions? How many registers do you need? 
& solution: 
- 
et 
N RSN 
Sequence of Instructions (MIPS) 
Left shifting a number by 1 bit is equivalent to multiplying 
Step 
Instruction 
Comment 
it by 2. 
| 
1 
add $t1, 
$tO, 
$tO 
$t1 =$t0 + $t0 
—> 2 x N 
cgas 
fader 
§ 
o 
x 
' 
' 
~ 
So, left shifting by 3 bits = multiplying by 2= 8. 
We can do this using only add and sub. 
2 
add $t2, S$t1, $t1 
$t2 = $t1 + $t1 - 4xN 
B 
ol T 
- 
3 
add $t3, $t2, $t2 
$t3 = $t2 + $t2 — 8 x N (left shift by 3) 
| 
Let the number in $t0 be N = 13 (0000 1101), 
i 
e 
s e 
= 
= 
~ 
Step 
| 
Register 
7 
Binary Value 
= Decimal Value | 
| 
. 
) 
| 
t 
* 
5 
Registers Used: $t0O, St1, $t2, $t3 
1 
| 
St 
0001 1010 
26 
| 
! 
1 
s 
| 
=T 
o 
N 
- 
i il e 
N 
Total Registers Needed: 4 
3 
l 
St3 
0110 1000 
104 
: 
T o 
— 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Think About It - 3
DIGITAL LOGIC & COMPUTER DESIGN

--- [Page 47 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Think about it - 4
• By writing just an assembly language  program, can you determine if the processor  
it is running on is Big–Endian or Little–Endian?
• What if the processor has no load byte and  store byte instructions?

--- [Page 48 of 56] ---
Can an Assembly Program Determine Endianness? 
& YEs. 
If the processor provides byte-level 
memory access instructions (e.g., 1b / sb), 
an assembly program can determine 
whether it is Big—Endian or Little-Endian. 
Method: 
1. Store the 32-bit value 0x12345678 at 
memory address 1000. 
2. Load the first byte from address 1000. 
« 
|If it reads Ox12 — 
Big—Endian 
« 
|If it reads Ox78 — 
Little—-Endian 
Example: Store O0x12345678 starting at address 1000 
Big—Endian 
Address 
Byte Stored 
1000 
12 
1001 
34 
1002 
56 
1003 
78 
Little—Endian 
Address 
Byte Stored 
1000 
78 
1001 
56 
1002 
34 
1003 
12 
Program executes: 1lb $tO, O($tl) 
# load byte from address 1000 
e 
If $t0 = Ox12 — 
Big—Endian 
e 
If $t0 = Ox78 — 
Little—Endian 
X No. 
If the processor has no instructions for 
accessing individual bytes (only word 
load/store, e.g., 1w / sw), an assembly 
program generally cannot determine 
endianness. 
Why? 
Endianness only affects the order of bytes 
within a multi-byte word in memory. 
If we can only store and retrieve complete 
.~ 
words, the internal byte ordering is not 
' 
observable. 
Example (both Big—-Endian and Little—-Endian): 
1i 
sw 
1w 
Program 
$tO, ©6x12345678 
$te, o(s$tl) 
$t2, o(s$tl) 
# store word 
| 
# load word 
Result: $t2 = 0x12345678 
Big—Endian Memory 
Addr 
Byte 
A 
12 
A+1 
34 
A+2 
56 
A+3 
78 
Little-Endian Memory 
Addr 
Byte 
A 
78 
A+1 
56 
A+2 
34 
A+3 
12 
9 Conclusion: 
With byte-level access (1b / sb): 
Without byte—level access: 
No, 
Yes, endianness can be determined. 
the difference is invisible to the program. 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Think about it - 4

--- [Page 49 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
• Q1.An operand stored in memory is accessed using which instructions in MIPS?
A) add and sub
B) lw and sw
C) beq and j
D) and and or

--- [Page 50 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
•
Q2. Memory is primarily used to store:
A) Frequently used temporary values only
B) Large amounts of data and programs
C) CPU clock signals
D) ALU outputs only

--- [Page 51 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
•
Q3. In byte-addressable memory, each memory address represents:
A) One bit
B) One byte
C) One word
D) Eight bytes

--- [Page 52 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
• Q4. In word-addressable memory, each memory address represents:
A) One bit
B) One byte
C) One word
D) Eight bytes

--- [Page 53 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
• Q5. An operand that is directly specified within an instruction is called a:
A) Memory operand
B) Register operand
C) Constant (Immediate) operand
D) Address operand

--- [Page 54 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
• Q6. Which statement correctly distinguishes word-addressable and 
byte-addressable memory?
A) Both assign one address per word.
B) Both assign one address per byte.
C) Word-addressable memory assigns one address per word, while 
byte-addressable memory assigns one address per byte.
D) Byte-addressable memory cannot store words.

--- [Page 55 of 56] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Answer Key
Q1: B  Q2: B  Q3: B  Q4: C  Q5: C  Q6: C

--- [Page 56 of 56] ---
PES 
UNIVERSITY 
CELEBRATING SO YEARS 
Team DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-5"></a>
## Document 5: Slide Deck 3.9.1: Machine Language & Instruction Encoding (34 Pages)
**Source Document**: `resources/u3/3/Slides/3.9.1_Machine_Language.pptx`
**OCR Extraction File**: `U3_Slides_3.9.1_Machine_Language.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.9.1_Machine_Language.pptx
OCR PDF FILE      : U3_Slides_3.9.1_Machine_Language_ocr.pdf
TOTAL PAGES       : 34
WORD COUNT        : 2829
CHARACTER COUNT   : 17151
DATE EXTRACTED    : 2026-11-04 14:07:36
================================================================================

--- [Page 1 of 34] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 34] ---
ARCHITECTURE-Machine Language
TEAM DLCD
Department of CSE and CSE (AI & ML)
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 34] ---
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 
architecture 
Logic 
Digital 
Circuits 
Analog 
Circuits 
Devices 
Physics 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC AND COMPUTER DESIGN
• Machine Language
R, I & J-Type Instructions
Instruction Formats
Logical Instructions
Shift Instructions
Stored Program
Machine Code Interpretation
Programming
TOPICS

--- [Page 4 of 34] ---
PES 
UNIVERSITY 
• Binary representation of instructions
• Computers only understand 1’s and 0’s
• 32–bit instructions
‒ Simplicity favors regularity: 32–bit data &  instructions
• 3 instruction formats:
• R – Type: register operands
• I – Type: immediate operands
• J – Type: for jumping (discuss later)
DIGITAL LOGIC AND COMPUTER DESIGN
Machine Language
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 5 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Machine Language: Big Picture
• A MIPS instruction is a 32-bit binary pattern 
stored in memory.
• The processor does not see add or lw; it 
only sees fields inside those 32 bits.
• Always read the opcode first, then decide 
whether the instruction is R-type, I-type, or J-
type.
• The remaining fields tell the CPU which 
registers, constant, or address to use.
• TA shortcut: format first, meaning next.
32-bit
instruction
Split into
fields
CPU
acts
Example: 001000 ... → opcode = addi →
interpret remaining bits as rs, rt, imm c
(I-type) instruction
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 6 of 34] ---
DIGITAL LOGIC AND COMPUTER DESIGN
Instruction Formats at a Glance
Format
Used for
Important fields
Quick memory rule
R-type
Register-register ALU ops
rs, rt, rd, funct
No immediate; funct decides exact op
I-type
Immediate, load/store, 
branch
rs, rt, imm
16-bit immediate/offset is present
J-type
Jump instructions
addr
26-bit jump target
Fast decoding order: opcode → format → field meaning → final assembly instruction
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 7 of 34] ---
. 
DIGITAL LOGIC AND COMPUTER DESIGN
R-Type: Decode in 4 Steps
• R-type is used when the operands are 
mainly registers.
• If opcode = 000000, the instruction is R-
type.
• rs and rt are usually the source registers; 
rd is the destination.
• funct chooses the exact ALU action such 
as add, sub, and, or, or shift.
op
rs
rt
rd
shamt
funct
Example: add $s0, $s1, $s2
rs = $s1, rt = $s2, rd = $s0, funct = 100000
Memory tip: destination comes first in assembly, but is 
stored in rd.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 8 of 34] ---
PES 
UNIVERSITY 
• Register – type
• 3 register operands
‒ rs, rt: source registers
‒ rd: destination register
• Other fields:
‒ op: the operation code or the opcode (0 for R–type instructions)
‒ funct: the function with opcode tells computer what operation to perform
‒ shamt: the shift amount for shift instructions, otherwise 0.
‒ Eg:For example, the opcode and funct fields for the add instruction are 0 (0000002) and 
32 (1000002), respectively. Similarly, the sub instruction has an opcode and funct field of 
0 and 34.
DIGITAL LOGIC AND COMPUTER DESIGN
R – Type
op
rs
rt
rd
 
shamt
funct
6 bits
5 bits
5 bits
5 bits
5 bits
6 bits
R–Type
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 9 of 34] ---
Assembly Code 
add S$s0, 
sub s5t0, 
$s1, 
St3, 
Ss2 
Sth 
op 
Machine Code 
rs 
rt 
rd 
shamt 
funct 
000000 10001 10010 10000 00000 100000 
Field Values 
op 
rs 
rt 
rd 
shamt 
funct 
0 
17 
18 
16 
0 
32 
0 
11 
13 
8 
0 
34 
6 bits 
5Sbits 
5bits 
5bits 
5bits 
6 bits 
000000 01011 01101 01000 00000 100010 
6 bits 
5 bits 
5 bits 
5bits 
5 bits 
6 bits 
PES 
UNIVERSITY 
(0x02328020) 
(0x016D4022) 
DIGITAL LOGIC AND COMPUTER DESIGN
R – Type Examples
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
The machine code for the R-type instructions add and sub. 
Notice that the destination is the first register in an assembly language instruction, 
but it is the third register field (rd) in the machine language instruction. 
For example, the assembly instruction add $s0, $s1, $s2 has 
rs = $s1 (17), 
rt = $s2 (18), 
rd = $s0 (16).

--- [Page 10 of 34] ---
PES 
UNIVERSITY 
Table 6.1 MIPS register set 
$0 
0 
the constant value 0 
fat 
1 
assembler temporary 
fvi-$vl 
2-3 
function return value 
$al-%$a3 
4-7 
function arguments 
$L0-$t7 
8-15 
temporary variables 
$s0-$s7 
16-23 
saved variables 
$t8-$t9 
24-25 
temporary variables 
$k0-$k1 
26-27 
operating system (OS) temporaries 
tgp 
28 
global pointer 
$sp 
29 
stack pointer 
$fp 
30 
frame pointer 
$ra 
31 
function return address 
DIGITAL LOGIC AND COMPUTER DESIGN
R – Type Examples
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Example 6.3 TRANSLATING ASSEMBLY LANGUAGE TO MACHINE LANGUAGE 
Translate the following assembly language statement into machine language. \
add $t0, $s4, $s5
Solution: According to Table 6.1, $t0, $s4, and $s5 are 
registers 8, 20, and 21. 
According to Tables B.1 and B.2, add has an opcode of 0 
and a funct code of 32. 
The easiest way to write the machine language in 
hexadecimal is to first write it in binary, then look at 
consecutive groups of four bits, which correspond to 
hexadecimal digits (indicated in blue). Hence, the machine 
language instruction is 0x02954020.

--- [Page 11 of 34] ---
Assembly Code 
add 5cl, 5=4, 585 
Field Values 
op 
rs 
i 
rd 
shamt 
funct 
0 
20 | 2 
8 
0 
32 
Ghits 
5bits 
S5hits 
5hits 
Sbits 
& bits 
Machine Code 
op 
s 
rt 
rd 
shamt 
funct 
000000 110100(10101)01000{00000| 100000 
| 
| 
I 
L1l 
i 
i i 
| 
0 
2 
Y 
5 
4 
0 
2 
0 
Figure 6.7 Machine code for the R-type instruction of Example 6.3 
(0x02954020) 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
R – Type Examples
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Example 6.3 TRANSLATING ASSEMBLY LANGUAGE TO MACHINE LANGUAGE 
Translate the following assembly language statement into machine language. 
add $t0, $s4, $s5

--- [Page 12 of 34] ---
PES 
UNIVERSITY 
I-Type
op
rs
rt
imm
6 bits
5 bits
5 bits
16 bits
DIGITAL LOGIC AND COMPUTER DESIGN
I – Type
• Immediate – type
• 2 register & 1 immediate (constant) operands
‒ rs, rt: register operands
‒ imm: 16–bit immediate for +ve number and 2’s complement  for –ve number
• Other fields:
‒ op: the operation code or the opcode
‒ Simplicity favors regularity: all instructions have opcode.
‒ Operation is completely determined by opcode.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
rs and imm are always used as source operands. 
rt is used as a destination for some instructions (such as addi 
and lw)   but as another source for others (such as sw).

--- [Page 13 of 34] ---
PES 
UNIVERSITY 
Figure 6.8 I-type instruction 
-type 
op 
rs 
rt 
imm 
format 
Gbits 
5bits 
5 bits 
16 bits 
Assembly Code 
Field Values 
Machine Code 
addi $s0, 
S$sl1, 
5 
8 
17 
16 
5 
001000 {10001 |10000) 
0000 0000 0000 0101 
addi $t0, $s3, -12| 
8 
19 
8 
-12 
001000 (10011)01000| 
1111 1111 1111 0100 
1w 
sc2, 32(s50) 
35 
0 
10 
32 
100011 {00000[01010) 0000 0000 0010 0000 
EW 
$81, 
4(stl) 
43 
9 
17 
4 
101011 (0100110001 
0000 0000 OOO0 0100 
Gbits 
5bits 
5 bits 
16 bits 
Bbits 
S5bits 
5 bits 
16 bits 
Figure 6.9 Machine code for |-type instructions 
(0%22300005) 
(0% 2268FFF4) 
(0x8COAD020) 
(0xAD310004) 
DIGITAL LOGIC AND COMPUTER DESIGN
I – Type Examples
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 14 of 34] ---
Assembly Code 
1w 553, 
—24 (5s4) 
Field Values 
PES 
UNIVERSITY 
Table 6.1 MIPS register set 
Name 
Number 
Machine Code 
$0 
0 
the constant value 0 
$at 
1 
assembler temporary 
$v0—$vi 
2-3 
function return value 
10-$a3 
4-7 
function arguments 
0-$t7 
8-15 
temporary variables 
i0-$s7 
16-23 
saved variables 
8-$t9 
24-25 
temporary variables 
(0-$k1 
26-27 
operating system (OS) temporaries 
$gp 
28 
global pointer 
$sp 
29 
stack pointer 
$fp 
30 
frame pointer 
$ra 
31 
function return address 
1111 
1111 1110 
1000 (0x8E93FFES) 
op 
rs 
rt 
imm 
3D 
20 
19 
—24 
6 bits 
5 bits 
5 bits 
16 bits 
Figure 6.10 Machine code for an I-type instruction 
op 
rs 
ri 
imm 
IH}DDJ 1 
1DI;IHD 1|Pfl1 1I 
8 
E 
9 
3 
F 
F 
E 
8 
DIGITAL LOGIC AND COMPUTER DESIGN
I – Type Examples
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Translate the following I-type instruction into machine code.
 lw $s3, −24($s4)
Solution: According to Table 6.1, $s3 and $s4 are registers 19 and 20, respectively. Table 
B.1 indicates that lw has an opcode of 35. 
rs specifies the base address, $s4, 
and rt specifies the destination register, $s3. 
The immediate, imm, encodes the 16-bit offset, −24. The fields and machine code are 
given in Figure 6.10.

--- [Page 15 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
I – Type Examples
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
NOTE: I-type instructions have a 16-bit immediate field, but the 
immediates are used in 32-bit operations. For example, lw adds a 
16-bit offset to a 32-bit base register. 
What should go in the upper half of the 32 bits? 
For positive immediates, the upper half should be all 0’s, 
but for negative immediates, the upper half should be all 1’s.

--- [Page 16 of 34] ---
PES 
UNIVERSITY 
High-Level Code 
MIPS Assembly Code 
#3s0=a 
int a =0xb6d5edf3c: 
Tui $s0, Oxb6d5e 
# a = 0x6d5e 0000 
ori $s0, $s0, 0x4f3c 
# a=0x6d5e4f3c 
DIGITAL LOGIC AND COMPUTER DESIGN
I – Type Examples
• The addi instruction is helpful for assigning 16–bit constants.
• To assign 32–bit constants, use a load upper immediate instruction (lui) followed by 
an or immediate (ori) instruction as shown in code.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 17 of 34] ---
DIGITAL LOGIC AND COMPUTER DESIGN
I-Type: Immediate, Load/Store, and Branch
• Format: op | rs | rt | imm
• imm is a 16-bit constant or address offset.
• For addi and lw, rt is usually the destination 
register.
• For sw, rt is the value that will be stored to 
memory.
• addi/lw/sw use sign extension; 
andi/ori/xori use zero extension.
Instruction
Read it as
addi $s0, $s1, 5
$s0 = $s1 + 5
lw $t2, 32($0)
$t2 = Memory[$0 + 32]
sw $s1, 4($t1)
Memory[$t1 + 4] = $s1
Exam check: in load/store, rs = base register, imm = 
offset.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 18 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
J – Type
• Jump – type
• 26–bit address operand (addr) 
• Used for jump instructions (j)
J -Type
op
addr
6 
bits
26 
bits
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 19 of 34] ---
PES 
UNIVERSITY 
R-Type
op
rs
rt
rd
shamt
funct
6 bits
5 bits
6 bits
5 bits
5 bits
5 
bits
I-Type
op
rs
rt
imm
6 bits
5 bits
5 bits
16 bits
op
addr
6 
bits
26 
bits
J -Type
DIGITAL LOGIC AND COMPUTER DESIGN
Review: Instruction Formats 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 20 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Interpreting Machine Code
• To interpret machine language, one must decipher the fields of 
each 32-bit instruction word. 
• Different instructions use different formats, but all formats start with 
a 6-bit opcode field. 
• Thus, the best place to begin is to look at the opcode. If it is 0, the 
instruction is R-type.
• otherwise it is I-type or J-type.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 21 of 34] ---
Example 6.5 TRANSLATING MACHINE LANGUAGE TO ASSEMBLY 
LANGUAGE 
Translate the following machine language code into assembly language. 
Ox2237FFF1 
0x02F34022 
Solution: First, we represent each instruction in binary and look at the six most sig- 
nificant bits to find the opcode for each instruction, as shown in Figure 6.12. The 
opcode determines how to interpret the rest of the bits. The opcodes are 001000, 
(810) and 000000, (04p), indicating an addi and R-type instruction, respectively. 
The funct field of the R-type instruction is 100010, (34,¢), indicating that it is 
a sub instruction. Figure 6.12 shows the assembly code equivalent of the two 
machine instructions. 
& PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Interpreting Machine Code
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 22 of 34] ---
DIGITAL LOGIC AND COMPUTER DESIGN
Machine Code Decoding Strategy
• Step 1: Read the opcode.
• Step 2: If opcode = 0, treat it as R-type and 
inspect funct.
• Step 3: Otherwise, use the opcode itself to 
identify the I-type or J-type instruction.
• Step 4: Convert register numbers carefully 
to register names.
• Step 5: Interpret the immediate as signed 
or unsigned based on the instruction.
Worked example: 001000 10001 10111 
1111111111110001
Field
Value
Meaning
opcode
001000
addi
rs
10001
$s1
rt
10111
$s7
imm
1111...0001
-15
Final answer: addi $s7, $s1, -15
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 23 of 34] ---
(Ox2237FFF1) | 
(0x02F34022) 
| 
Machine Code 
Field Values 
op 
s 
it 
imm 
s 
it 
imm 
001000 | 1000110111 1111 1111 1111 0001 
17 | 23 
-15 
2 
3 
7 
F 
F 
F 
f 
op 
s 
it 
rd 
shamt 
funct 
s 
f 
rd 
shamt 
000000 |10111|10011 /01000| 00000 | 100010 
23 | 19 
0 
Il 
I 
Il 
| 
Il 
IL 
Il 
| 
0 
F 
3 
4 
0 
2 
2 
PES 
UNIVERSITY 
Assembly Code 
addi $s7, Ssl, -15 
sub $t0, $s7, $s3 
DIGITAL LOGIC AND COMPUTER DESIGN
Interpreting Machine Code
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 24 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Review: The Stored Program Concept
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
What is a Stored Program?
●A program is stored in main memory as machine code (binary instructions).
●Each instruction occupies a unique memory address.
●The processor executes instructions one at a time in sequence.
Machine Code:
●Executed directly by the CPU.
●Represented in binary or hexadecimal format.
●Difficult for humans to read and write.
●Example: 0x8C0A0020

--- [Page 25 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Review: The Stored Program Concept
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Assembly Code:
●Human-readable representation of machine instructions.
●Uses mnemonics (e.g., lw, add, sub) instead of binary.
●Easier to write, understand, and debug.
●Example: lw $t2, 32($0)
Program Counter (PC):
●The Program Counter (PC) is a special register that stores the address of the next instruction to be 
executed.
●After an instruction is fetched, the PC is normally incremented by 4 bytes (for MIPS 32-bit instructions).
●Branch and jump instructions modify the PC to execute instructions from a different location.
Key point: A stored-program computer keeps both instructions and data in memory. The CPU uses the 
Program Counter (PC) to fetch and execute instructions sequentially unless a branch or jump changes the 
execution flow.

--- [Page 26 of 34] ---
Assembly Code 
1w 
2 et 
add 
$s0, 
addi s$to0, 
sub 
Sth, 
32(50) 
$s81, 
583, 
2 o 
Ss2 
-12 
GES 
Machine Code 
O0x8COAQ0020 
0x02328020 
Ox2268FFF4 
Ox016D4022 
& 
Stored Program 
a Address 
Instructions 
I 
| 
| 
| 
0040000C 
016 D40 22 
00400008 
2268FF 
4 
00400004 
02328020 
00400000 
8C0OAQ020 
: 
| 
: 
| 
| 
| 
. 
| 
1 
N 
_/ 
Main Memory 
~ 
— PC 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Review: The Stored Program Concept
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Main 
M

--- [Page 27 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
• Q1. An operand stored in memory is accessed using which instructions in MIPS?
    A) add and sub
    B) lw and sw
    C) beq and j
    D) and and or
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 28 of 34] ---
PES 
UNIVERSITY 
MCQ
• Q2. In an R-type instruction, which field identifies the exact ALU operation when 
opcode = 0?
    A) imm
    B) funct
    C) shamt
    D) addr
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 29 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
• Q3. Which set of immediate instructions uses zero extension?
    A) addi, lw, sw
    B) andi, ori, xori
    C) beq, bne
    D) j
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 30 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
• Q4. In sra, the new most significant bits are filled using:
    A) 0s
    B) sign bit
    C) funct bits
    D) shamt bits
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 31 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
• Q5. In sllv rd, rt, rs, the shift amount comes from:
    A) shamt field
    B) lower 5 bits of rs
    C) lower 5 bits of rt
    D) opcode
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 32 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
• Q6. Which instruction format is used by j?
    A) R-type
    B) I-type
    C) J-type
    D) depends on funct
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 33 of 34] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Answer Key
Q1: B    Q2: B    Q3: B    Q4: B    Q5: B    Q6: C
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 34 of 34] ---
PES 
UNIVERSITY 
THANK YOU
Team DLCD
Department of CSE and CSE(AI & ML)

```

---

<a id="doc-6"></a>
## Document 6: Slide Deck 3.11.1: Programming & Procedures in Assembly (85 Pages)
**Source Document**: `resources/u3/3/Slides/3.11.1_Programming.pptx`
**OCR Extraction File**: `U3_Slides_3.11.1_Programming.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.11.1_Programming.pptx
OCR PDF FILE      : U3_Slides_3.11.1_Programming_ocr.pdf
TOTAL PAGES       : 85
WORD COUNT        : 7307
CHARACTER COUNT   : 44423
DATE EXTRACTED    : 2026-11-04 14:09:44
================================================================================

--- [Page 1 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND
COMPUTER DESIGN
TEAM DLCD
Department of CSE and CSE (AI & ML)

--- [Page 2 of 85] ---
ARCHITECTURE-Programming
TEAM DDCO
Department of CSE and CSE (AI & ML)
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 85] ---
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 
architecture 
Logic 
Digital 
Circuits 
Analog 
Circuits 
Devices 
Physics 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC AND COMPUTER DESIGN
• Arithmetic/Logical Instructions
• Branching
• Conditional Statements.
• Getting Loopy
• Arrays
• Function Calls.
TOPICS

--- [Page 4 of 85] ---
PES 
UNIVERSITY 
• High–level languages:
‒ e.g., C, Java, Python
‒ Written at higher level of abstraction
• Common high–level software  constructs:
‒ if/else statements  for loops
‒ while loops
‒ Arrays, function calls
‒ In this section, we explore how to translate these high-level 
constructs into MIPS assembly code.
DIGITAL LOGIC AND COMPUTER DESIGN
Programming
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 5 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Arithmetic/Logical Instructions
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MIPS provides a variety of arithmetic and logical instructions that are used to implement higher-level 
programming constructs. Most arithmetic instructions operate on values stored in registers.
Arithmetic instructions
add  $t0, $s1, $s2      # $t0 = $s1 + $s2
sub  $t0, $t3, $t5      # $t0 = $t3 - $t5
addi $t0, $s3, -12      # $t0 = $s3 - 12
For example, if $s1 = 25 and $s2 = 10:
add $t0,$s1,$s2 
 $t0=35
⇒
MIPS also provides separate instructions for multiplication and division, which use the special hi and lo 
registers.

--- [Page 6 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Arithmetic/Logical Instructions
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MIPS provides four basic logical operations: AND, OR, XOR and NOR. These are R-type instructions and operate bit-
by-bit on two source registers.
For example, consider:
$s1 = 0xFFFF0000
$s2 = 0x46A1F0B7
The results are:
and $s3, $s1, $s2    # $s3 = 0x46A10000
or  $s4, $s1, $s2    # $s4 = 0xFFFFF0B7
xor $s5, $s1, $s2    # $s5 = 0xB95EF0B7
nor $s6, $s1, $s2    # $s6 = 0x00000F48
AND is useful for masking bits because it can force selected bits to 0. OR can combine bits from two values.
MIPS does not provide a separate NOT instruction. Instead,
NOT A=A NOR $0

--- [Page 7 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Logical Instructions: What to Remember
AND
Mask bits
(keep only selected 
1s)
OR
Set / combine bits
XOR
Show differences
between bits
NOR
OR first, then invert
(NOR with $0 = 
NOT)
• andi, ori, and xori zero-extend the 16-bit immediate before the operation.
• Use and for masking, 
           or for merging fields,
           xor for bit comparison, 
           nor for inversion tricks.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 8 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Logical Instructions: Example 1
1111 1111 1111 1111 0000 0000 0000 0000
$s1
$s2 0100 0110 1010 0001 1111 0000 1011 0111
Assembly Code
and $s3, $s1, $s2   $s3
or $s4, $s1, $s2 $s4  xor 
$s5, $s1, $s2 $s5  nor 
$s6, $s1, $s2   $s6
Source Registers
Result
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 9 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
1111 1111 1111 1111 0000 0000 0000 0000
$s1
$s2 0100 0110 1010 0001 1111 0000 1011 0111
0100 0110 1010 0001 0000 0000 0000 0000
1111 1111 1111 1111 1111 0000 1011 0111
1011 1001 0101 1110 1111 0000 1011 0111
0000 0000 0000 0000 0000 1111 0100 1000
Assembly Code
and $s3, $s1, $s2   $s3
or $s4, $s1, $s2 $s4  xor 
$s5, $s1, $s2 $s5  nor 
$s6, $s1, $s2   $s6
Source Registers
Result
Logical Instructions: Example 1
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 10 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Logical Instructions: Example 2
0000 0000 0000 0000 0000 0000 1111 1111
$s1
imm
Assembly Code
andi $s2, $s1, 0xFA34  
ori  $s3, $s1, 0xFA34
xori $s4, $s1, 0xFA34
0000 0000 0000 0000 1111 1010 0011 0100
$s2
$s3
$s4
Source Values
Result
zero-extended
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
• Logical operations can also 
operate 
on 
immediates. 
These I-type instructions 
are andi, ori, and xori. 
• nori 
is 
not 
provided, 
because 
the 
same 
functionality can be easily 
implemented 
using 
the 
other instructions. 
• Because these instructions 
operate on a 32-bit value 
from a register and a 16-bit 
immediate, they first zero-
extend the immediate to 32 
bits.

--- [Page 11 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Logical Instructions: Example 2
0000 0000 0000 0000 0000 0000 1111 1111
$s1
imm
Assembly Code
andi $s2, $s1, 0xFA34  
ori  $s3, $s1, 0xFA34
xori $s4, $s1, 0xFA34
0000 0000 0000 0000 1111 1010 0011 0100
0000 0000 0000 0000 0000 0000 0011 0100
0000 0000 0000 0000 1111 1010 1111 1111
0000 0000 0000 0000 1111 1010 1100 1011
$s2
$s3
$s4
Source Values
Result
zero-extended
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 12 of 85] ---
PES 
UNIVERSITY 
• MIPS instruction set has an or instruction as well as a nor instruction, and also 
an ori instruction, but no nori instruction.
‒ Why?
‒ How can nori functionality be implemented?
DIGITAL LOGIC AND COMPUTER DESIGN
Think About It
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 13 of 85] ---
DIGITAL LOGIC AND COMPUTER DESIGN
Think About It: Why is there no nori?
• MIPS avoids adding instructions whose 
behavior can already be built using existing 
ones.
• nori would mean: destination = NOT(rs OR 
immediate).
• That behavior is already easy to create in two 
instructions.
ori  $t0, $s1, 0x00FF
nor  $t0, $t0, $zero
Result:
$t0 = ~( $s1 | 0x00FF )
Key idea: nor with $zero works like bitwise NOT, so a dedicated nori instruction is unnecessary.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 14 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Shift Instructions
• Shift instructions shift the value in a register left or right by up to 31 bits.
• Shift operations multiply or divide by powers of two.
• MIPS shift operations are sll (shift left logical), srl (shift right logical), and sra (shift 
right arithmetic).
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 15 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Shift Instructions
• Left shifts always fill the least significant bits with 0’s.
• However, right shifts can be either logical (0’s shift into the most significant bits) or 
arithmetic (the sign bit shifts into the most significant bits).
• Figure shows the machine code for the R–type instructions sll, srl, and sra.
• rt (i.e., $s1) holds the 32–bit value to be shifted, and shamt gives the amount by 
which to shift (4).
• The shifted result is placed in rd.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 16 of 85] ---
Assembly Code 
s1l1l $t0, $s1, 4 
srl $s2, $sl1, 4 
sra 5s3, S$sl1, 
4 
Field Values 
Machine Code 
op 
rs 
rt 
rd 
shamt 
funct 
op 
rs 
rt 
rd 
shamt 
funct 
0 
0 
17 
8 
4 
0 
000000 (0000010001 |fl1unn 00100| 000000| (0x00114100) 
0 
0 
17 
18 
4 
2 
000000 [00000{10001|10010/00100| 000010| (0x00119102) 
0 
0 
17 
10 
4 
3 
000000 |00000({10001 (10011|00100| 000011 | (0x00119903) 
Gbits 
GSbits 
5hits 
5bits 
5bits 
6 bits 
Ebits 
Shits 
Sbits 
5bits 
5bits 
& bits 
Figure Shift instruction machine code 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Shift Instructions: Example
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 17 of 85] ---
$s1 
shamt 
Assembly Code 
s11 S$t0, 
S$s1, 
4 
$t0 
srl S$s2, Ssl1, 
4 
$s2 
sra 5s3, Ssl1, 
4 
$s3 
Source Values 
1111 0011 0000 0000 0000 0010 1010 1000 
Result 
00100 
0011 0000 0000 0000 0010 1010 1000 0000 
0000 1111 0011 0000 0000 
0010 1010 
1111 1111 0011 0000 0000 0000 0010 1010 
Figure Shift operations 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
•Figure shows the register values for the shift instructions sll, srl, and sra.
•Shifting a value left by N is equivalent to multiplying it by 2N.
•Likewise, arithmetically shifting a value right by N is equivalent to dividing it by 2N,
Shift Instructions: Example
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 18 of 85] ---
DIGITAL LOGIC AND COMPUTER DESIGN
Shift Instructions: sll vs srl vs sra
Instruction
What it does
Bits filled in
Typical use
sll
Shift left logical
0s on the right
Multiply by 2^n (if 
no overflow)
srl
Shift right logical
0s on the left
Unsigned values / 
bit extraction
sra
Shift right arithmetic
Copies sign bit
Signed divide by 
2^n
Example value:
10010000
srl by 2 → 00100100
sra by 2 → 11100100
shamt stores the fixed shift 
amount (0–31).
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 19 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Variable Shift Instructions
• MIPS also has variable–shift instructions: sllv (shift left logical variable), srlv (shift 
right logical variable), and srav (shift right arithmetic variable).
• Figure shows the machine code for these instructions.
• Variable–shift assembly instructions are of the form sllv rd, rt, rs.
• The order of rt and rs is reversed from most R–type instructions.
• rt ($s1) holds the value to be shifted, and the five least significant bits of rs ($s2) 
give the amount to shift.
• The shifted result is placed in rd, as before.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 20 of 85] ---
Assembly Code 
Field Values 
op 
rs 
rt 
rd 
shamt 
funct 
sllv £s3, 
8s1, 
Ss2 
0 
18 
17 
19 
0 
4 
srlv Ss4, 
8§81, 
5s2 
0 
18 
17 
20 
0 
6 
srav 5s5, 
&sl1, 
5s2 
0 
18 
17 
21 
0 
7 
Bbits 
5Sbits 
5bits 
5bits 
5bits 
& bits 
Machine Code 
op 
rs 
rt 
rd 
shamt 
funct 
000000 10010 [ 10001 10011 | OOO0O0 | OO0100 
000000 10010 [ 10001 10100 | 00000 | 000110 
000000 10010 
(10001 (10101 | 00000 | 000111 
Gbits 
5bits 
Sbits 
5bits 
Sbits 
6 bits 
Figure Variable-shift instruction machine code 
(0x02519804) 
(00251 ADOE) 
(0x0251A807) 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Variable Shift Instructions: Example
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 21 of 85] ---
Assembly Code 
sllv 5s3, Ssl, ss2 
srlv 5sd, Ssl1, Ss2 
srav 5sk, Ssl, s5s2 
$s1 
$s2 
88 
Source Values 
1111 0011 0000 0100 0000 0010 1010 1000 
0000 0000 0000 0000 0000 0000 
1000 
Result 
0000 0100 0000 0010 1010 1000 0000 0000 
0000 0000 1111 0011 0000 0100 0000 0010 
1111 1111 1111 0011 0000 0100 0000 0010 
Figure Variable-shift operations 
& PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
• The shamt field is ignored and should be all 0’s.
• Figure shows register values for each type of variable–shift instruction.
Variable Shift Instructions: Example
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 22 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Variable Shift: Why rs and rt seem reversed
• Syntax is sllv rd, rt, rs (and similarly srlv, 
srav).
• rt contains the value that will be shifted.
• The lower 5 bits of rs give the shift amount.
• rd stores the final result.
• shamt is ignored because the amount now 
comes from a register.
rs
shift amount
rt
value to shift
rd
result
Easy memory tip: the variable amount comes from 
a register, not from the instruction bits.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 23 of 85] ---
PES 
UNIVERSITY 
:ode Example 6.10 16-BIT CONSTANT 
High-Level Code 
MIPS Assembly 
Code 
{ff §s0 =2 
int a =0x4f3c; 
addi $s0, $0, Oxdf3c 
§f a = 0xdf3c 
DIGITAL LOGIC AND COMPUTER DESIGN
Generating Constants
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
The addi instruction can be used to assign a 16-bit constant to a register.
For example, to implement:
int a = 0x4F3C;
MIPS uses:
addi $s0, $0, 0x4F3C
Since $0 always contains zero:
$s0=0+0x4F3C
Therefore:
$s0 = 0x00004F3C
For a 32-bit constant, a single immediate instruction is not sufficient. MIPS uses lui followed by ori.

--- [Page 24 of 85] ---
PES 
UNIVERSITY 
Code Example 6.11 32-BIT CONSTANT 
High-Level Code 
MIPS Assembly Code 
# §=0=2 
int a = 0xod5ed fic; 
Tui §s0, OxGdSe 
# a = 0xbd5e0000 
ori §s0, §s0, Oxdfic 
¥ a = OnbdSedfic 
DIGITAL LOGIC AND COMPUTER DESIGN
Generating a 32-bit Constant
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
To implement:
int a = 0x6D5E4F3C;
MIPS divides the constant into two 16-bit parts:
Upper 16 bits = 0x6D5E
Lower 16 bits = 0x4F3C
First, lui loads the upper half: lui $s0, 0x6D5E
giving: $s0 = 0x6D5E0000
Then ori inserts the lower half: ori $s0, $s0, 0x4F3C
giving: $s0 = 0x6D5E4F3C
Thus:
lui+ori
32-bit constant
⇒

--- [Page 25 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Multiplication and Division
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Multiplication and division differ from the other arithmetic operations because they can produce more 
than one 32-bit result.
Multiplying two 32-bit numbers produces a 64-bit product. MIPS stores this result in two special-purpose 
registers:
●hi → upper 32 bits
●lo → lower 32 bits
mult $s0, $s1
For division: div $s0, $s1
the results are:
●lo → quotient
●hi → remainder
The results can be moved to general-purpose registers using: mflo $t0; mfhi $t1

--- [Page 26 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Multiplication and Division: Numerical
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MIPS uses the special HI and LO registers for multiplication and division. For division, LO stores the quotient and HI stores 
the remainder. For example, if: $s0=20,$s1=6
div  $s0, $s1
mflo $t0        # $t0 = 3 (quotient)
mfhi $t1        # $t1 = 2 (remainder)
because: 20÷6=3 remainder 2
For multiplication, two 32-bit numbers produce a 64-bit product. HI stores the upper 32 bits and LO stores the lower 32 
bits.
mult $s0, $s1
mflo $t0        # lower 32 bits
mfhi $t1        # upper 32 bits
MIPS also provides mul, which produces a 32-bit result directly in a general-purpose register:
mul $s1, $s2, $s3       # $s1 = $s2 × $s3
Remember: div → LO = quotient, HI = remainder; mult → HI:LO = 64-bit product.

--- [Page 27 of 85] ---
PES 
UNIVERSITY 
Executing Instructions Out of Sequence
Modern processors improve performance by changing the normal order of execution 
when a branch instruction occurs.
Types of Branch Instructions:
Conditional Branches
Execution jumps only if a specified condition is true.
●beq (Branch if Equal): Branches when two registers contain the same value.
●bne (Branch if Not Equal): Branches when two registers contain different values.
DIGITAL LOGIC AND COMPUTER DESIGN
Branching
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 28 of 85] ---
PES 
UNIVERSITY 
Unconditional Branches
Execution always transfers control to another location.
●j (Jump): Unconditionally jumps to a specified target address.
●jr (Jump Register): Jumps to the address stored in a register (commonly used for 
function returns).
●jal (Jump and Link): Jumps to a function and saves the return address in the $ra 
(return address) register.
DIGITAL LOGIC AND COMPUTER DESIGN
Branching
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 29 of 85] ---
PES 
UNIVERSITY 
# MIPS assembly 
addi 
$s0, %0, 4 
# $s0 =0 + 4 =4 
addi $s1, $0, 2 
# $s1 =0+ 2 =2 
add 
$s1, $s1, $s1 
#8581 =2%2=§ 
beq 
$s0, $s1, target 
# branch is taken 
addi $s1, $s1, 
1 
# not executed 
sub 
$s1, $s1, $s0 
# not executed 
target: 
# label 
add 
$s1, $sl1, 
$sO0 
# $s1 =4 + 4 = 8 
ILabels indicate instruction location. They can’t be 
reserved words and must be followed by colon (:) 
DIGITAL LOGIC AND COMPUTER DESIGN
Conditional branching (BEQ):
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Branch if Equal (beq):
●Compares the values stored in two registers.
●If the values are equal, control transfers to the specified label.
●If the values are not equal, execution continues with the next sequential instruction.
Syntax:
beq $rs, $rt, label
Example Explanation:
●
$s0 is initialized to 4.
●
$s1 is initialized to 2, then doubled to become 4.
●
Since $s0 == $s1, the condition is true.
●
The processor branches to the label target.
●
The instructions between beq and target are skipped.
●
Execution resumes at target, where $s1 becomes 8 (4 + 4).

--- [Page 30 of 85] ---
PES 
UNIVERSITY 
# MIPS assembly 
addi 
$s0, %0, 4 
# $s0 =0 + 4 =4 
addi $s1, $0, 2 
# $s1 =0+ 2 =2 
add 
$s1, $sl1, $sl1 
# $s1l =2+ 2 =4 
beq 
$s0, $sl1, target 
# branch is taken 
addi $s1, $s1, 
1 
# not executed 
sub 
$s1, $sl1, $s0 
# not executed 
target: 
# label 
add 
$s1, $sl1, 
$sO0 
# $s1 =4 + 4 = 8 
Labels indicate instruction location. They can’t be 
reserved words and must be followed by colon (:) 
DIGITAL LOGIC AND COMPUTER DESIGN
Conditional branching (BEQ):
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Labels:
●A label identifies the address of an instruction.
●It acts as the branch destination.
●Labels must end with a colon (:) and cannot be reserved keywords.
Key Takeaway: beq changes the program flow only when the two register values are equal; otherwise, 
execution proceeds with the next instruction.

--- [Page 31 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
The branch not take (BNE)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Branch if Not Equal (bne):
●Compares the values stored in two registers.
●Branches to the specified label only if the register values are not equal.
●If the values are equal, execution continues with the next sequential instruction.
Syntax:
bne $rs, $rt, label
Example Explanation
●
$s0 is initialized to 4.
●
$s1 is initialized to 2, then doubled to become 4.
●
Since $s0 == $s1, the condition for bne (not equal) is false.
●
The branch is not taken, so execution continues with the next instructions.
●
addi updates $s1 from **4 → 5, and subupdates$s1 from **5 → 1.
●
Execution eventually reaches the target label, where $s1 becomes 5 (1 + 4).

--- [Page 32 of 85] ---
# MIPS assembly 
addi 
addi 
add 
bne 
addi 
sub 
target: 
add 
$s0, 
$s1, 
$sl, 
$s0, 
54 
$s1, 
$s1, 
$0, 4 
$0, 
2 
$sl1, 
$s1 
$sl1l, target 
$s1, 
1 
$sl, 
$s0O 
$sl1l, 
$s0O 
# $sO0 = 0 + 4 = 4 
F BEL = 
g 3 
== 
3 
FS$s) = 2+ 2 = 4 
# branch not taken 
# $s1 =4 + 1 =5 
# $s1 =5 -4 =1 
sl =1L 
=5 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
The branch not take (BNE)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Key Takeaway: bne transfers control only when the compared register values are different. If they are 
equal, execution continues sequentially with the next instruction.
This matches the beq slide in style while clearly highlighting the difference:
●beq → Branch when Equal.
●bne → Branch when Not Equal.

--- [Page 33 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Unconditional Branching (J)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Jump (j)
●An unconditional branch transfers control to another instruction without checking any condition.
●The processor always jumps to the specified target label.
●Instructions between the j instruction and the target label are skipped.
Syntax:
j label
Example Explanation
●$s0 is initialized to 4.
●$s1 is initialized to 1.
●The instruction j target immediately transfers control to the label target.
●The instructions sra, addi, and sub are not executed.
●Execution resumes at target, where $s1 becomes 5 (1 + 4).

--- [Page 34 of 85] ---
PES 
& UNIVERSITY 
# MIPS assembly 
add1 $s0, $0, 4 
# 950 = 4 
addl $s1, $0, 1 
# 951 =1 
] 
target 
# jump to target 
sra 
$s1, $s1, 2 
# not executed 
addi 
$s1, $s1, 1 
# not executed 
sub 
$s1, $s1, $s0 
# not executed 
target: 
add 
$s1, $s1, $s0 
# 9$sl =1+4=25 
DIGITAL LOGIC AND COMPUTER DESIGN
Unconditional Branching (J)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Applications of j
●Skipping a block of instructions.
●Implementing loops.
●Transferring control to another section of a 
program.
Key Takeaway: The j instruction always transfers 
execution to the specified label, regardless of any 
condition, causing all intermediate instructions to be 
skipped.

--- [Page 35 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Unconditional Branching (Jr)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Jump Register (jr)
●Transfers control to the address stored in a register.
●The target address is determined at run time, not encoded in the instruction.
●Unlike j, jr uses a register operand instead of a label.
●jr is an R-type instruction in the MIPS instruction set.
Syntax:
jr $rs
Example Explanation
●addi $s0, $0, 0x2010 loads the address 0x00002010 into register $s0.
●jr $s0 immediately jumps to the address stored in $s0.
●The instructions at 0x00002008 and 0x0000200C are skipped.
●Execution resumes at 0x00002010, where lw $s3, 44($s1) is executed.

--- [Page 36 of 85] ---
# MIPS assembly 
0x00002000 
0x00002004 
0x00002008 
0x0000200C 
0x00002010 
addi $s0, $0, 0x2010 
jr 
$s0 
addi $sl1, $0, 
1 
sra 
%$sl, $sl1, 
2 
lw 
$s3, 44(%$sl) 
jris an R-type instruction. 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Unconditional Branching (Jr)
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Applications of jr
●Returning from functions using jr $ra.
●Jumping to addresses computed during program execution.
●Supporting indirect control transfer.
Key Takeaway: jr transfers control to the address contained in a register, enabling indirect jumps and 
function returns in MIPS programs.

--- [Page 37 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Conditional statements
Conditional statements such as if, if/else, and switch/case execute a block of code only when a 
specified condition is satisfied. 
In MIPS, these high-level constructs are implemented using conditional branch instructions and 
labels.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 38 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
IF statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
How an if Statement Works
●An if statement executes a block of code only when a specified condition is true.
●In MIPS, this is implemented using conditional branch instructions.
●The branch instruction checks the opposite condition to skip the if block when the 
condition is false.
Example Explanation
C Code:
if (i == j)
    f = g + h;
f = f - i;

--- [Page 39 of 85] ---
C Code: 
if (i ==]) 
f=g+h; 
f 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
IF statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Equivalent MIPS Code:
bne $s3, $s4, L1
add $s0, $s1, $s2
L1: sub $s0, $s0, $s3
●bne checks whether i and j are not equal.
●If i != j, control jumps to L1, skipping f = g + h.
●If i == j, the branch is not taken, and f = g + h is executed.
●After the if block, execution continues with f = f - i.
Why use bne instead of beq?
Assembly often tests the opposite condition so that it can skip the if block when the condition is false, 
resulting in simpler and more efficient code.

--- [Page 40 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
IF/ELSE statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
How an if-else Statement Works
●An if-else statement executes one of two blocks based on a condition.
●In MIPS, this is implemented using a conditional branch and an unconditional jump.
●The conditional branch selects the appropriate block, while the unconditional jump skips the other 
block after execution.
Example Explanation
C Code:
if (i == j)
    f = g + h;
else
    f = f - i;

--- [Page 41 of 85] ---
C Code: 
if (i == j) 
f=g+h; 
else 
f=1-i 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
IF/ELSE statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Equivalent MIPS Code:
bne $s3, $s4, L1
add $s0, $s1, $s2
j done
L1: sub $s0, $s0, $s3
done:
●bne checks whether i and j are not equal.
●If i == j, the branch is not taken, and f = g + h is executed.
●The j done instruction skips the else block.
●If i != j, control branches directly to L1, where f = f - i is executed.
●Execution continues from the label done after either block.
Key Takeaway: An if-else statement is implemented using a conditional branch to choose the correct 
block and an unconditional jump to avoid executing the alternate block.

--- [Page 42 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Switch/Case statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A switch/case selects one of several blocks based on a value. 
In MIPS, it can be implemented as a series of conditional tests, equivalent to nested if/else statements.
 If none of the cases match, the default block is executed.

--- [Page 43 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Getting Loopy
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Loops repeatedly execute a block of code as long as a condition is satisfied. 
Common high-level loop constructs are while and for loops. 
In MIPS, loops are implemented using comparison, branch, and jump instructions.

--- [Page 44 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
While statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
How a while Loop Works
●A while loop repeatedly executes a block of code as long as the specified condition is true.
●In MIPS, the loop is implemented using a conditional branch to exit the loop and an unconditional 
jump to repeat it.
●The loop condition is evaluated before each iteration.
Example Explanation
C Code
while (pow != 128) {
    pow = pow * 2;
    x = x + 1;  }

--- [Page 45 of 85] ---
PES 
UNIVERSITY 
C Code 
while (pow !=128) { 
pow = pow * 2; 
X=Xx+1; 
} 
DIGITAL LOGIC AND COMPUTER DESIGN
While statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Equivalent MIPS Code
while:  beq  
$s0, $t0, done
        
sll  
$s0, $s0, 1
        
addi 
$s1, $s1, 1
        
j   
while
done:
●beq checks whether pow == 128.
●If the condition is true, control branches to done, terminating the loop.
●If the condition is false, the loop body executes:
○sll $s0, $s0, 1 multiplies pow by 2 (left shift by 1 bit).
○addi $s1, $s1, 1 increments x.
●j while returns control to the beginning of the loop to evaluate the condition again.

--- [Page 46 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
While statement
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
●Why use beq?
●The original C condition is pow != 128, but the assembly tests the opposite condition 
(pow == 128) to determine when to exit the loop. This simplifies the loop control.
Key Takeaway: A while loop in MIPS uses a conditional branch to exit the loop and an 
unconditional jump to repeat the loop until the termination condition is met.

--- [Page 47 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
For loop
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A for loop is used to repeatedly execute a block of code when the number of 
iterations is known or controlled by a loop variable.
Syntax
for (initialization; condition; loop operation)
    
statement;
Components of a for Loop
●Initialization: Executes once before the loop begins.
●Condition: Evaluated at the start of each iteration. The loop continues while 
the condition is true.
●Statement: The block of code executed during each iteration.
●Loop Operation (Update): Executes at the end of each iteration before the 
condition is checked again.

--- [Page 48 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
For loop
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Execution Flow
●Initialization → Condition → Statement → Loop Operation → Condition → … → 
Exit
Key Takeaway: A for loop combines initialization, condition checking, and update 
into a single statement, making it ideal for count-controlled iterations.

--- [Page 49 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
For loop in MIPS
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
How a for Loop Works
●A for loop performs initialization, checks a condition, executes the loop body, 
updates the loop variable, and repeats until the condition becomes false.
●In MIPS, it is implemented using initialization instructions, a conditional branch, an 
update instruction, and an unconditional jump.
Example Explanation
C Code:
for (i = 0; i != 10; i++) {
    sum = sum + i;
}

--- [Page 50 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
For loop in MIPS
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Equivalent MIPS Code:
addi $s1, $0, 0      # sum = 0
add  $s0, $0, $0     # i = 0
addi $t0, $0, 10     # loop limit
for:  beq  $s0, $t0, done
      add  $s1, $s1, $s0
      addi $s0, $s0, 1
      j    for
done:
●addi instructions initialize sum, i, and the loop limit (10).
●beq checks whether i == 10.
●If the condition is true, control branches to done, terminating the loop.
●Otherwise, the loop body adds the current value of i to sum.
●addi $s0, $s0, 1 increments the loop variable.

--- [Page 51 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
For loop in MIPS
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
●j for returns control to the beginning of the loop for the next iteration.
Key Takeaway: A for loop in MIPS consists of initialization, condition checking, loop 
body execution, loop variable update, and an unconditional jump to repeat the loop 
until the termination condition is met.

--- [Page 52 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Magnitude Comparison Using slt
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
The beq and bne instructions compare whether two values are equal or unequal. For magnitude comparisons, 
MIPS provides the Set Less Than (slt) instruction.
slt $t1, $s0, $s1
The instruction sets $t1 to 1 when $s0 < $s1, otherwise it sets $t1 to 0.
For example:
$s0 = 5
$s1 = 8
slt $t1, $s0, $s1
gives:
5<8
$t1=1
⇒
This can then be combined with beq or bne to implement conditions such as less than, greater than, less than or 
equal to, and greater than or equal to.

--- [Page 53 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Loop Using slt : Numerical
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
The textbook example adds powers of 2 from 1 to 100:
C code:
int sum = 0;
for (i = 1; i < 101; i = i * 2)
    sum = sum + i;
MIPS equivalent: 
addi $s1, $0, 0       # sum = 0
addi $s0, $0, 1       # i = 1
addi $t0, $0, 101
loop:
slt  $t1, $s0, $t0    # $t1 = 1 if i < 101
beq  $t1, $0, done    # if i >= 101, exit
add  $s1, $s1, $s0    # sum = sum + i

--- [Page 54 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Loop Using slt : Numerical
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
sll  $s0, $s0, 1      # i = i * 2
j    loop
done:
The values added are:
1+2+4+8+16+32+64=1271+2+4+8+16+32+64=127
Therefore:
sum=127
Key idea: slt converts a magnitude comparison into a 1/0 result, which can then be tested using a branch 
instruction.

--- [Page 55 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Arrays and Array Indexing
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
An array stores multiple elements of the same type in sequential memory locations. Each element is 
identified by an index, starting from 0. The address of the first element, array[0], is called the base 
address.
For a 32-bit integer array, each element occupies 4 bytes. Therefore:
Address of array[i]=Base Address+4i
For example, if the base address is 0x10007000:
array[0] → 0x10007000
array[1] → 0x10007004
array[2] → 0x10007008
To access an element, MIPS uses the base address and an offset:
lw $t1, 4($s0)     # loads array[1];  where $s0 contains the base address.

--- [Page 56 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Accessing an Array in MIPS
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Consider: int array[5];
array[0] = array[0] * 8;
array[1] = array[1] * 8;
If the base address is 0x10007000, MIPS first loads this address into $s0:
lui $s0, 0x1000
ori $s0, $s0, 0x7000
Then the elements are accessed using their byte offsets:
lw  $t1, 0($s0)       # array[0]
sll $t1, $t1, 3       # multiply by 8
sw  $t1, 0($s0)
lw  $t1, 4($s0)       # array[1]
sll $t1, $t1, 3       # multiply by 8
sw  $t1, 4($s0)
Since each integer occupies 4 bytes, array[1] is located 4 bytes after array[0].

--- [Page 57 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Array Access Using a for Loop
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
For a large array, the same instructions should not be repeated for every element. The index can be used to calculate the address 
of each element.
For a 1000-element integer array:
for (i = 0; i < 1000; i++)
    array[i] = array[i] * 8;
MIPS calculates the address using:
sll $t0, $s1, 2       # $t0 = i × 4
add $t0, $t0, $s0     # address of array[i]
lw  $t1, 0($t0)
sll $t1, $t1, 3       # array[i] × 8
sw  $t1, 0($t0)
Here, $s0 contains the base address and $s1 contains i.
Byte offset=i×4
The shift sll $t0,$s1,2 is used because: i×4=i×2^2

--- [Page 58 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Byte Arrays and Characters
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Characters can be stored in a single byte instead of a 32-bit word. MIPS provides special instructions 
for accessing byte data:
lbu    # Load Byte Unsigned
lb     # Load Byte
sb     # Store Byte
lbu zero-extends the loaded byte to 32 bits, while lb sign-extends it. sb stores only the least significant 
byte of a register into memory.
For byte arrays, consecutive elements are only 1 byte apart:
Address of chararray[i]=Base Address+i
This differs from an integer array, where the offset is 4i.

--- [Page 59 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Character Array: Lowercase to Uppercase Numerical
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Question:
Convert the following C code into MIPS assembly language:
char chararray[10];
int i;
for (i = 0; i != 10; i = i + 1)
    chararray[i] = chararray[i] - 32;
Assume that $s0 already contains the base address of chararray.
Solution
addi $s1, $0, 0          # i = 0
addi $t0, $0, 10         # $t0 = 10

--- [Page 60 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Character Array Numerical
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
loop:
beq  $t0, $s1, done      # if i == 10, exit
add  $t1, $s1, $s0       # address of chararray[i]
lb   $t2, 0($t1)         # load chararray[i]
addi $t2, $t2, -32       # convert lowercase to uppercase
sb   $t2, 0($t1)         # store result
addi $s1, $s1, 1         # i = i + 1
j    loop
done:

--- [Page 61 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Character Array Numerical
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Why add $t1, $s1, $s0?
Each character occupies 1 byte, so the address of chararray[i] is:
Base Address+i
For ASCII characters:
a =0x61, 0x61−0x20=0x41= A
′ ′
′ ′
Thus, subtracting 32 (0x20) converts a lowercase English letter to its corresponding uppercase letter.

--- [Page 62 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Function Calls and Returns
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Functions allow frequently used code to be reused, making programs more modular and readable. A function 
receives arguments and produces a return value.
MIPS follows a convention for communication between the caller and callee:
$a0−$a3→input arguments;  $v0−$v1→return value
The function is called using jal, which stores the return address in $ra and jumps to the function. The function returns 
using jr $ra.
jal simple       # call function
...
simple:
jr $ra           # return to caller
For example, if jal is at 0x00400200, the next instruction is at 0x00400204. Therefore: $ra=0x00400204\boxed{\
$ra=0x00400204}

--- [Page 63 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Function Call with Arguments
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
Consider the function:
int diffofsums(int f, int g, int h, int i) {
    int result;
    result = (f + g) - (h + i);
    return result;
}
The caller places the four arguments in $a0–$a3:
addi $a0, $0, 2
addi $a1, $0, 3
addi $a2, $0, 4
addi $a3, $0, 5

--- [Page 64 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Function Call with Arguments
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
jal  diffofsums
add  $s0, $v0, $0
The callee performs the calculation and places the result in $v0:
add $t0, $a0, $a1
add $t1, $a2, $a3
sub $s0, $t0, $t1
add $v0, $s0, $0
jr  $ra
Numerically:
(2+3)−(4+5)=5−9=−4(2+3)-(4+5)=5-9=\boxed{-4}
Therefore, the function returns −4 in $v0.

--- [Page 65 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Stack in Function Calls
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
The stack is a LIFO memory structure used to store temporary data and local variables during function execution. The 
MIPS stack grows toward lower memory addresses.
$sp is the stack pointer and points to the top of the stack.
If: $sp=0x7FFFFFFC and a function needs two additional words:
addi $sp, $sp, -8
then: $sp=0x7FFFFFF4
because each word occupies 4 bytes.
A function follows five basic steps when saving registers:
1. Allocate stack space.
2. Store registers on the stack.
3. Execute the function.
4. Restore the registers.
5. Deallocate the stack space.

--- [Page 66 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Saving Registers on the Stack
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A function must preserve registers that the caller depends on. The stack can temporarily store these registers while 
the function executes.
For diffofsums, three registers are saved:
addi $sp, $sp, -12     # space for 3 words
sw   $s0, 8($sp)
sw   $t0, 4($sp)
sw   $t1, 0($sp)
# function operations
lw   $t1, 0($sp)
lw   $t0, 4($sp)
lw   $s0, 8($sp)

--- [Page 67 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Saving Registers on the Stack
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
addi $sp, $sp, 12
jr   $ra
Since each register requires one word: 3×4=12 bytes
The stack space allocated by a function is called its stack frame.

--- [Page 68 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Preserved and Nonpreserved Registers
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MIPS divides registers into preserved and nonpreserved registers.
Preserved
Nonpreserved
$s0–$s7
$t0–$t9
$ra
$a0–$a3
$sp
$v0–$v1
A callee must save and restore preserved registers that it modifies. Nonpreserved registers may be changed 
by the callee.
Therefore, in the improved diffofsums, only $s0 needs to be saved:
addi $sp, $sp, -4
sw   $s0, 0($sp)
# function operations

--- [Page 69 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Preserved and Nonpreserved Registers
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
lw   $s0, 0($sp)
addi $sp, $sp, 4
jr   $ra
Thus, the stack frame requires only:
1×4=4 bytes​

--- [Page 70 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Recursive Function Calls
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
A leaf function does not call another function, whereas a nonleaf function calls another function. A recursive 
function is a nonleaf function that calls itself.
Consider factorial:
int factorial(int n) {
    if (n <= 1)
        return 1;
    else
        return n * factorial(n - 1); }
The recursive relationship is: factorial(n)=n×factorial(n−1)
with the base case: factorial(1)=1
For n=3: 3!=3×2×1=6
Each recursive call creates its own stack frame to preserve $a0 and $ra.

--- [Page 71 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Recursive Factorial in MIPS
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
The textbook implementation saves $a0 and $ra before making the recursive call:
factorial:
addi $sp, $sp, -8
sw   $a0, 4($sp)
sw   $ra, 0($sp)
addi $t0, $0, 2
slt  $t0, $a0, $t0
beq  $t0, $0, else
addi $v0, $0, 1
addi $sp, $sp, 8
jr   $ra
else:
addi $a0, $a0, -1
jal  factorial

--- [Page 72 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Recursive Factorial in MIPS
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
lw   $ra, 0($sp)
lw   $a0, 4($sp)
addi $sp, $sp, 8
mul  $v0, $a0, $v0
jr   $ra
For factorial(3):
3→2→1
Then the calls return:
1→2×1=2→3×2=6
Each invocation allocates 8 bytes for $a0 and $ra.

--- [Page 73 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
Additional Arguments and Local Variables
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
MIPS provides registers $a0–$a3 for the first four input arguments. If a function requires more than four arguments, the 
additional arguments are passed through the stack.
First 4 arguments → $a0–$a3
Additional arguments → Stack
The caller expands its stack to make room for the additional arguments. A function may also use the stack for local 
variables and local arrays.
The callee's stack frame can contain:
Local variables / arrays
$s0–$s7 (if needed)
$a0–$a3 (if needed)
Return address
Additional arguments
An important exception is that when a function has more than four arguments, the callee may access the additional 
arguments in the caller's stack frame.Key MIPS Function-Call Flow: Arguments→jal→Callee→Return value→jr $ra​

--- [Page 74 of 85] ---
PES 
UNIVERSITY 
1. Assume that register $s1 contains 7 and register $s2 contains 4. Consider  the 
following instruction sequence (the first register is the destination, and  the not 
instruction inverts each bit):
nor  $s3, $s0, $s2
addi $s3, $s2, 1
add $s3, $s1, $s2
1. What value gets stored in $s3? What arithmetic operation do above 
instructions perform on $s1 and $s2 contents?
DIGITAL LOGIC AND COMPUTER DESIGN
Think About It
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 75 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q1. What is the primary role of the Program Counter (PC)?
A) Store arithmetic results
 B) Hold the address of the next instruction to be executed
 C) Store data values temporarily
 D) Decode machine instructions
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 76 of 85] ---
PES 
UNIVERSITY 
MCQ
Q2. Which statement correctly distinguishes assembly code from machine code?
A) Assembly code is executed directly by the CPU.
 B) Machine code uses mnemonics such as add and lw.
 C) Assembly code is human-readable and must be translated into machine code.
 D) Both are identical representations of a program.
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 77 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q3. Which MIPS instruction transfers control only when two register values are equal?
A) bne
 B) j
 C) beq
 D) jr
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 78 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q4. Which instruction is commonly used to return from a function in MIPS?
A) beq
 B) j
 C) jal
 D) jr
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 79 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q5. In the MIPS implementation of an if-else statement, why is the instruction j done used?
A) To initialize variables before execution
 B) To skip the else block after executing the if block
 C) To compare two registers
 D) To terminate the program
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 80 of 85] ---
PES 
UNIVERSITY 
   DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q6. In a MIPS while loop, which instruction causes the loop to repeat?
A) beq
 B) addi
 C) j while
 D) sub
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 81 of 85] ---
PES 
UNIVERSITY 
   DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q7. Which sequence correctly represents the execution order of a for loop?
A) Statement → Initialization → Condition → Update
 B) Initialization → Condition → Statement → Update
 C) Condition → Initialization → Update → Statement
 D) Initialization → Statement → Update → Condition
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 82 of 85] ---
PES 
UNIVERSITY 
   DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q8. An integer array has base address 0x10007000. What address does the following MIPS 
code access?
Assume $s0 = 0x10007000.
A. 0x10007006
 B. 0x10007018
 C. 0x10007024
 D. 0x10007028
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 83 of 85] ---
PES 
UNIVERSITY 
   DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
Q9. Consider the following function call:
addi $a0, $0, 2
addi $a1, $0, 3
addi $a2, $0, 4
addi $a3, $0, 5
jal  diffofsums
where the function computes: result = (f + g) - (h + i);
What value should be returned in $v0?
A. -4
 B. 0
 C. 4
 D. 14
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.

--- [Page 84 of 85] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MCQ
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
ANSWER KEY:
Q1: B  Q2: C  Q3: C  Q4: D  Q5: B  Q6: C
 Q7: B
 Q8: B
 Q9: A

--- [Page 85 of 85] ---
PES 
UNIVERSITY 
THANK YOU
Team DLCD
Department of CSE and CSE(AI & ML)

```

---

<a id="doc-7"></a>
## Document 7: Slide Deck 3.14.1: Addressing Modes (29 Pages)
**Source Document**: `resources/u3/3/Slides/3.14.1_Addressing_Mode.pptx`
**OCR Extraction File**: `U3_Slides_3.14.1_Addressing_Mode.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.14.1_Addressing_Mode.pptx
OCR PDF FILE      : U3_Slides_3.14.1_Addressing_Mode_ocr.pdf
TOTAL PAGES       : 29
WORD COUNT        : 1756
CHARACTER COUNT   : 11699
DATE EXTRACTED    : 2026-11-04 14:07:09
================================================================================

--- [Page 1 of 29] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 29] ---
ARCHITECTURE-Addressing Modes
TEAM DLCD
Department of CSE and CSE (AI & ML)
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 29] ---
Application 
>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 
architecture 
Logic 
Digital 
Circuits 
Analog 
Circuits 
Devices 
Physics 
PES 
UNIVERSITY 
Addressing Modes
• Addressing Modes

--- [Page 4 of 29] ---
PES 
UNIVERSITY 
What is an Addressing Mode?
An addressing mode specifies how the CPU locates the operand(s) required to 
execute an instruction. Depending on the instruction, operands may be stored in 
registers, memory locations, or within the instruction itself.
Why are Addressing Modes Important?
●Determine where operands are located
●Influence execution speed and memory usage
●Provide flexibility for handling constants, variables, arrays, loops, and function calls
●Reduce instruction size while improving processor efficiency
Addressing Modes

--- [Page 5 of 29] ---
PES 
UNIVERSITY 
MIPS Addressing Modes:
●Register Only
○Operands are stored entirely in CPU registers.
○Used for arithmetic and logical operations.
○Example: add $s0, $t2, $t3
●Immediate
○One operand is a constant value encoded directly within the instruction.
○Eliminates the need to fetch the constant from memory.
○Example: addi $s0, $s0, 10
●Base Addressing
○The operand is stored in memory.
○The effective address is calculated using a base register and an offset.
○Example: lw $t0, 8($sp)
Addressing Modes

--- [Page 6 of 29] ---
PES 
UNIVERSITY 
MIPS Addressing Modes:
●PC-Relative Addressing
○Used by branch instructions.
○The destination address is calculated relative to the Program Counter (PC).
○Example: beq $t0, $0, Loop
●Pseudo Direct Addressing
○Used by jump instructions.
○
The instruction specifies the jump target address to transfer program control.
○Example: j main
Key Formulae:
Base Addressing:  Effective Address = Base Register + Offset
PC–Relative Addressing: Branch Target Address = PC + 4 + (Offset × 4)
Addressing Modes

--- [Page 7 of 29] ---
PES 
UNIVERSITY 
Register-Only Addressing:
●Definition: Register-only addressing uses CPU registers for both the source and 
destination operands. No memory locations are accessed during instruction execution.
●Used By: All R-type instructions in the MIPS architecture.
●Operation: The ALU reads operands directly from the register file, performs the required 
operation, and stores the result back into a register.
●Advantage: Since registers are the fastest storage elements in the processor, register-
only addressing provides high execution speed and minimizes memory access.
●Example: add $s0, $t2, $t3
○Source operands: $t2, $t3
○Destination operand: $s0
Key Point:
All operands remain within the CPU registers, making Register-Only Addressing 
the fastest addressing mode in MIPS.
Addressing Modes

--- [Page 8 of 29] ---
PES 
UNIVERSITY 
Register-Only Addressing:
●Operands are stored entirely in CPU registers.
●The instruction reads the required operands from the register file, performs the operation in the 
ALU, and stores the result back into a register.
●No memory access is required during execution, making this addressing mode fast and 
efficient.
Examples:
●add $s0, $t2, $t3
○Performs: $s0 = $t2 + $t3
●sub $t8, $s1, $0
○Performs: $t8 = $s1 − $0 (copying the value of $s1 since $0 always contains 0)
Note: Register $0 is hardwired to the value 0 in MIPS and cannot be modified.
Addressing Modes

--- [Page 9 of 29] ---
PES 
UNIVERSITY 
Immediate Addressing:
●Definition: Immediate addressing uses a 16-bit constant (immediate value) encoded directly within 
the instruction, along with a register operand.
●Instruction Format: One operand is a register, while the other is the immediate value specified in the 
instruction.
●Used By: I-type instructions such as addi (Add Immediate), ori (OR Immediate), andi (AND 
Immediate), and lui (Load Upper Immediate).
●Advantage: Since the constant is part of the instruction, the processor does not need to access 
memory, resulting in faster execution.
●Applications: Commonly used for initializing registers, updating loop counters, 
incrementing/decrementing values, and performing arithmetic or logical operations with constants.
Key Point:
Immediate addressing combines a register operand with a constant value embedded in the 
instruction, making it efficient for operations involving fixed constants.
Addressing Modes

--- [Page 10 of 29] ---
PES 
UNIVERSITY 
Addressing Modes
Immediate Addressing:
Examples: 
addi $s4, $t5, -73
●Performs: $s4 = $t5 + (-73)
●Adds the immediate value −73 to the contents of register $t5 and stores the result in $s4.
ori $t3, $t7, 0xFF
●Performs: $t3 = $t7 OR 0x00FF
●Performs a bitwise OR between the contents of $t7 and the hexadecimal constant 0xFF, storing 
the result in $t3.
Key Point:
Immediate addressing is ideal for operations involving fixed constants, as the operand is 
embedded directly within the instruction, resulting in faster execution.

--- [Page 11 of 29] ---
PES 
UNIVERSITY 
Base Addressing:
●Definition: Base addressing is used to access data stored in memory. The memory address is calculated 
by adding a base address stored in a register to a 16-bit signed offset (immediate value).
●Used By: Memory access instructions such as lw (Load Word) and sw (Store Word).
●Effective Address Calculation:
 
Effective Address = Base Register + Sign-Extended Offset
●Operation: The processor first computes the effective address, then reads data from memory (lw) or 
writes data to memory (sw).
●Applications: Commonly used for accessing arrays, stack variables, structures, and dynamically 
allocated memory.
Key Point:
Base addressing enables efficient memory access by combining a register-based base address with a signed 
offset, allowing programs to access different memory locations using the same instruction format.
Addressing Modes

--- [Page 12 of 29] ---
PES 
UNIVERSITY 
Addressing Modes
Base Addressing:
●The memory address is obtained by adding the base register to the sign-extended 16-bit offset.
●The calculated value is called the Effective Address (EA).
Examples:
 lw $s4, 72($0)
●Effective Address = $0 + 72
●Since $0 = 0, the address becomes 72.
●Loads the word stored at memory address 72 into register $s4.
sw $t2, -25($t1)
●Effective Address = $t1 + (-25)
●Stores the contents of register $t2 into the memory location 25 bytes before the address contained in $t1.
Note: The offset may be positive or negative, allowing access to memory locations before or after the base 
address. This addressing mode is widely used for arrays, stack frames, and structures.

--- [Page 13 of 29] ---
PES 
UNIVERSITY 
PC-Relative Addressing:
●Definition: PC-relative addressing is used by conditional branch instructions to determine 
the next instruction to execute when a branch condition is satisfied.
●Instead of storing the complete destination address, the instruction stores a 16-bit signed 
offset relative to the current Program Counter (PC).
●The processor computes the Branch Target Address (BTA) using the formula:
BTA=(PC+4)+(Sign-Extended Offset×4)
●Used By: Branch instructions such as beq (Branch if Equal) and bne (Branch if Not Equal).
●Advantage: Reduces instruction size while allowing both forward and backward branching 
within a program.
Key Point: PC-relative addressing specifies the destination relative to the current 
instruction rather than storing the complete address.
Addressing Modes

--- [Page 14 of 29] ---
PES 
UNIVERSITY 
PC-Relative Addressing – Example
Assembly Code:
0x10   beq  $t0, $0, else
0x14   addi $v0, $0, 1
0x18   addi $sp, $sp, 8
0x1C   jr   $ra
0x20 else: addi $a0, $a0, -1
0x24       j    factorial
Machine Code Fields:
●Opcode (op) = 4 (beq)
●Source Register (rs) = $t0 = 8
●Target Register (rt) = $0 = 0
●Immediate (offset) = 3
Thus, the instruction is encoded as: beq $t0, $0, 3
Addressing Modes

--- [Page 15 of 29] ---
PES 
UNIVERSITY 
Offset Calculation:
●Current PC = 0x10
●Next instruction = PC + 4 = 0x14
●Branch target (else) = 0x20
●Distance = 3 instructions
Therefore, Immediate Offset = 3
Key Observation:
●The immediate field stores the number of instructions to jump, not the actual memory address.
●During execution, the processor sign-extends the offset, multiplies it by 4 (word addressing), and adds 
it to PC + 4 to compute the branch target address.
Addressing Modes

--- [Page 16 of 29] ---
PES 
UNIVERSITY 
Pseudo- Direct Addressing:
●Definition: Pseudo-direct addressing is used by jump instructions to transfer program 
control to another location in the program.
●The jump instructions j (Jump) and jal (Jump and Link) use a 26-bit address field 
instead of storing the complete 32-bit target address.
●The processor constructs the 32-bit Jump Target Address (JTA) by combining:
○The upper 4 bits of PC + 4, and
○The 26-bit address field shifted left by 2 bits.
●This addressing mode is called pseudo-direct because only part of the destination address 
is stored in the instruction.
Jump Target Address Formula
JTA={(PC+4)31:28,  Address25:0,  00}
Addressing Modes

--- [Page 17 of 29] ---
PES 
UNIVERSITY 
Pseudo-Direct Addressing:
Used By
●j (Jump)
●jal (Jump and Link)
Key Point: Pseudo-direct addressing stores only a 26-bit target field, reducing 
instruction size while allowing efficient jumps within the same 256 MB memory region.
Addressing Modes

--- [Page 18 of 29] ---
PES 
UNIVERSITY 
Pseudo-Direct Addressing – Example
Assembly Code
0x0040005C      j   sum
...
0x004000A0  sum:
              
add  $v0, $a0, $a1
Address Calculation
●Jump Target Address (JTA) = 0x004000A0
●26-bit Address Field = 0x0100028
●Opcode for j = 000010
Addressing Modes

--- [Page 19 of 29] ---
PES 
UNIVERSITY 
During execution, the processor:
1. Takes the upper 4 bits of PC + 4
2. Appends the 26-bit address field
3. Adds two trailing 0 bits (word alignment)
4. Forms the complete 32-bit Jump Target Address
Machine Code Format
Opcode (6 bits) | Address (26 bits)
000010              | 00000100000000000000101000
Machine Code: 
0x08100028
Addressing Modes

--- [Page 20 of 29] ---
PES 
UNIVERSITY 
Why Shift Left by 2?
●Every MIPS instruction is 4 bytes (32 bits) long.
●Instruction addresses are therefore word-aligned, so the last 2 bits are always 00.
●These bits are omitted from the instruction and restored by the processor during 
execution.
Key Observation:
Unlike PC-relative addressing, pseudo-direct addressing does not store an offset. 
Instead, it stores part of the destination address, which the processor combines 
with the upper bits of the Program Counter to obtain the full jump target.
Addressing Modes

--- [Page 21 of 29] ---
PES 
UNIVERSITY 
MCQ
Q1. Register-only addressing is primarily used by which type of MIPS 
instructions?
A) I-type instructions
 B) J-type instructions
 C) R-type instructions
 D) Memory access instructions

--- [Page 22 of 29] ---
PES 
UNIVERSITY 
MCQ
Q2. In immediate addressing, the constant operand is:
A) Stored in memory
 B) Stored in a register
 C) Encoded within the instruction itself
 D) Retrieved from the stack

--- [Page 23 of 29] ---
PES 
UNIVERSITY 
MCQ
Q3. Which MIPS instructions use base addressing?
A) add and sub
 B) beq and bne
 C) lw and sw
 D) j and jal

--- [Page 24 of 29] ---
PES 
UNIVERSITY 
MCQ
Q4. In base addressing, the effective memory address is calculated as:
A) PC + Immediate
 B) Base Register + Sign-Extended Offset
 C) Register + Register
 D) PC + Jump Target Address

--- [Page 25 of 29] ---
PES 
UNIVERSITY 
MCQ
Q5. PC-relative addressing is mainly used by:
A) Arithmetic instructions
 B) Load and store instructions
 C) Conditional branch instructions
 D) Jump instructions

--- [Page 26 of 29] ---
PES 
UNIVERSITY 
MCQ
Q6. In PC-relative addressing, the branch target address is calculated relative to:
A) Current PC
 B) PC + 4
 C) Stack Pointer ($sp)
 D) Global Pointer ($gp)

--- [Page 27 of 29] ---
PES 
UNIVERSITY 
MCQ
Q7. Which addressing mode is used by the j and jal instructions?
A) Register-only Addressing
 B) Immediate Addressing
 C) Base Addressing
 D) Pseudo-direct Addressing

--- [Page 28 of 29] ---
PES 
UNIVERSITY 
MCQ
Answer Key
Q1: C  Q2: C  Q3: C  Q4: B  Q5: C  Q6: B  Q7: D

--- [Page 29 of 29] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-8"></a>
## Document 8: Slide Deck 3.14.2: Compiling, Assembling, and Loading (26 Pages)
**Source Document**: `resources/u3/3/Slides/3.14.2_COM-ASS-LOAD.pptx`
**OCR Extraction File**: `U3_Slides_3.14.2_COM-ASS-LOAD.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.14.2_COM-ASS-LOAD.pptx
OCR PDF FILE      : U3_Slides_3.14.2_COM-ASS-LOAD_ocr.pdf
TOTAL PAGES       : 26
WORD COUNT        : 2531
CHARACTER COUNT   : 16047
DATE EXTRACTED    : 2026-11-04 14:06:56
================================================================================

--- [Page 1 of 26] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 26] ---
Lights, Camera, Action: Compiling, Assembling, 
and Loading
TEAM DLCD
Department of CSE and CSE (AI & ML)
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 26] ---
PES 
UNIVERSITY 
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 4 
architecture < 
Digital 
Circuits 
Analog 
Circuits 
»- 
o 
b3 
Physics 
DIGITAL LOGIC & COMPUTER DESIGN
• Lights, Camera, Action: Compiling, 
Assembling, and Loading
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
TOPICS

--- [Page 4 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
●Until now: translating short high-level snippets into assembly and machine code.
●This section: compiling and assembling a complete program, and loading it into 
memory for execution.
●We will study about the MIPS memory map (where code, data and stack live) and the 
steps of code execution for a sample program in this section.
DIGITAL LOGIC & COMPUTER DESIGN
Lights, Camera, Action: Compiling, Assembling, and Loading

--- [Page 5 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
●32-bit addresses → address space = 2³² bytes = 4 GB.
●Word addresses are divisible by 4, ranging from 0 to 0xFFFFFFFC.
●Four segments: text, global data, dynamic data, reserved.
DIGITAL LOGIC & COMPUTER DESIGN
The MIPS Memory Map
Address range
Segment
0x00000000 – 0x003FFFFC
Reserved
0x00400000 – 0x0FFFFFFC
Text (PC starts at 0x00400000)
0x10000000 – 0x1000FFFC
Global data ($gp = 0x10008000)
0x10010000 – 0x7FFFFFFC
Dynamic data: heap (bottom) and stack (top, $sp = 0x7FFFFFFC)
0x80000000 – 0xFFFFFFFC
Reserved

--- [Page 6 of 26] ---
Address 
OxFFFFFFFC 
0x80000000 
Ox7FFFFFFC 
0x10010000 
0x1000FFFC 
0x10000000 
OXOFFFFFFC 
0x00400000 
O0x003FFFFC 
0x00000000 
Segment 
Reserved 
Stack 
Dynamic Data 
Heap 
Global Data 
Text 
Reserved 
«— $sp =0x7FFFFFFC 
<«—$gp =0x10008000 
<«—PC =0x00400000 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
The MIPS Memory Map
MIPS memory map

--- [Page 7 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
●Stores the machine language program.
●Large enough for almost 256 MB of code.
●The top 4 bits of every text address are all 0, so the j instruction can jump directly to 
any address in the program.
Analogy: The text segment is the recipe book. The PC is your finger on the line you are 
currently following. The book is read-only reference material that tells the CPU what to do.
DIGITAL LOGIC & COMPUTER DESIGN
Text Segment

--- [Page 8 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Global Data Segment
●Stores global variables, which, unlike local variables, can be seen by all functions.
●These are defined at start-up, before the program begins executing.
●These variables are declared outside main in C and accessible by any function.
●Large enough for 64 KB of globals.
●Accessing Globals with $gp: Global variables are accessed using the global pointer ($gp), 
which is initialized to 0x100080000. Unlike the stack pointer ($sp), $gp does not change 
during program execution. Any global variable can be accessed with a 16-bit positive or 
negative offset from $gp. The offset is known at assembly time, so the variables can be 
efficiently accessed using base addressing mode with constant offsets.
Analogy: Global variables are the noticeboard in a shared office, readable and writable by 
everyone. Local variables are notes on your own desk.

--- [Page 9 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Dynamic Data Segment (Stack and Heap)
●Holds the stack and the heap.
●Data is not known at start-up; it is allocated and deallocated during execution.
●This is the largest segment, spanning almost 2 GB.
Stack
Heap
Use
Save/restore registers used by functions; 
hold local variables such as arrays 
Data allocated at runtime
Allocation
LIFO stack frames
malloc in C; new in C++ and Java
Direction
Grows downward from the top (0x7FFFFFFC)
Grows upward from the bottom
Order
Last-in-first-out
Used and discarded in any order
●If stack and heap grow into each other, program data can be corrupted. The memory allocator 
prevents this by returning an out-of-memory error when space is insufficient.

--- [Page 10 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Reserved Segments
●Used by the operating system; cannot be used directly by the program.
●Part of the reserved memory is used for interrupts and memory-mapped I/O (to 
be discussed in depth in future lectures).

--- [Page 11 of 26] ---
PES 
UNIVERSITY 
High-Level Code 
[ 
Compiler 
] 
v 
Assembly Code 
v 
[ 
Assembler 
] 
Object Files 
Oblei‘ File | ibrary Files 
[ 
Linker 
v 
Executable 
v 
[ 
Loader 
] 
v 
Memory 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program (Overview)
High-level code → Compiler → Assembly code → Assembler → Object file → Linker (+ 
object files and library files) → Executable → Loader → Memory
1. Compile: high-level code → assembly code.
2. Assemble: assembly → machine code in an object file.
3. Link: combine machine code with library/other object code → complete 
executable.
4. Load: loader puts the program in memory and starts execution.
In practice, most compilers perform compiling, assembling and linking together.
Steps for translating and starting a program

--- [Page 12 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 1 - Compilation
A compiler translates high-level code into assembly. 
Example:
High-Level Code (C language):
int f, g, y; // global variables 
int main(void) { 
f = 2; 
g = 3; 
y = sum(f, g); 
return y; } 
int sum(int a, int b) { 
return (a + b); }
MIPS assembly:
.data
f:
g:
y:
.text
main:
  addi $sp, $sp, -4   # make stack frame
  sw   $ra, 0($sp)    # store $ra on stack
  addi $a0, $0, 2     # $a0 = 2
  sw   $a0, f         # f = 2
  addi $a1, $0, 3     # $a1 = 3
  sw   $a1, g         # g = 3
  jal  sum            # call sum function
  sw   $v0, y         # y = sum(f, g)
  lw   $ra, 0($sp)    # restore $ra from stack
  addi $sp, $sp, 4    # restore stack pointer
  jr   $ra            # return to operating system
sum:
  add  $v0, $a0, $a1  # $v0 = a+b
  jr   $ra            # return to caller

--- [Page 13 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 1 - Compilation
●.data and .text are assembler directives marking where the data and text segments begin.
●Labels f, g, y name the globals. Their storage locations are decided by the assembler; for now they stay 
as symbols.

--- [Page 14 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 2 - Assembling (Pass 1)
●The assembler converts assembly into an object file containing machine code.
●It makes two passes.
●Pass 1: assign instruction addresses and find all symbols (labels, global variable names).
Address
Instruction
0x00400000
main: addi $sp, $sp, -4
0x00400004
sw $ra, 0($sp)
0x00400008
addi $a0, $0, 2
0x0040000C
sw $a0, f
0x00400010
addi $a1, $0, 3
0x00400014
sw $a1, g
0x00400018
jal sum

--- [Page 15 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 2 - Assembling (Pass 1)
0x0040001C
sw $v0, y
0x00400020
lw $ra, 0($sp)
0x00400024
addi $sp, $sp, 4
0x00400028
jr $ra
0x0040002C
sum: add $v0, $a0, $a1
0x00400030
jr $ra

--- [Page 16 of 26] ---
PES 
UNIVERSITY 
Address 
f 
0x10000000 
g 
0x10000004 
y 
0x10000008 
main 
0x00400000 
sum 
0x0040002C 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 2 - Assembling (Symbol 
Table and Pass 2)
Symbol table
●Names and addresses of symbols are kept in the symbol table 
as shown in the table; addresses are filled in after Pass 1, when 
label addresses are known.
●Global variables are assigned storage in the global data 
segment starting at 0x10000000.
●Pass 2: the assembler produces machine code, taking 
addresses of globals and labels from the symbol table.
●The machine code and symbol table are stored in the object 
file.

--- [Page 17 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 3 - Linking
Why link?
●Large programs have many files. If only one changes, recompiling and reassembling the others 
is wasteful.
●Library files almost never change.
●If a high-level file is unchanged, its object file need not be updated.
What the linker does
●Combines all object files into one machine-language file: the executable.
●Relocates data and instructions so they are not all on top of each other.
●Uses the symbol tables to adjust addresses of relocated globals and labels.
●In our example there is one object file, so no relocation is needed.

--- [Page 18 of 26] ---
Executable file header 
Text Size 
Data Size 
0x34 (52 bytes) 
0xC (12 bytes) 
Text segment 
Address 
Instruction 
0x00400000 
0x23BDFFFC 
0x00400004 
OxAFBF0000 
0x00400008 
0x20040002 
0x0040000C 
OxAF848000 
0x00400010 
0x20050003 
0x00400014 
OxAF858004 
0x00400018 
0x0C10000B 
0x0040001C 
OxAF828008 
0x00400020 
0x8FBF0000 
0x00400024 
0x23BD0004 
0x00400028 
0x03E00008 
0x0040002C 
0x00851020 
0x00400030 
0x03E00008 
Data segment 
Address 
Data 
0x10000000 
0x10000004 
9 
0x10000008 
y 
PES 
UNIVERSITY 
addi $sp, $sp, —4 
sw 
$ra, 0($sp) 
addi $a0, $0, 2 
sw 
$a0, 0x8000($gp) 
addi $a1, $0, 3 
sw 
$al, 0x8004($gp) 
jal 
0x0040002C 
sw 
$v0, 0x8008($gp) 
lw 
$ra, O($sp) 
addi $sp, $sp, 4 
jr 
$ra 
add $v0, $a0, $at 
jr 
$ra 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: The Executable
Executable has three sections: header, text 
segment, data segment.
●Header: text size = 0x34 (52 bytes) (13 
instructions × 4), data size = 0xC (12 
bytes) (3 words).
●Text segment: instructions in the order 
stored in memory.
●Data segment: address of each global 
variable.
●The figure shows readable instructions 
beside the machine code for 
convenience; the real file has only 
machine instructions.

--- [Page 19 of 26] ---
Executable file header 
Text Size 
Data Size 
0x34 (52 bytes) 
0xC (12 bytes) 
Text segment 
Address 
Instruction 
0x00400000 
0x23BDFFFC 
0x00400004 
OxAFBF0000 
0x00400008 
0x20040002 
0x0040000C 
OxAF848000 
0x00400010 
0x20050003 
0x00400014 
OxAF858004 
0x00400018 
0x0C10000B 
0x0040001C 
OxAF828008 
0x00400020 
0x8FBF0000 
0x00400024 
0x23BD0004 
0x00400028 
0x03E00008 
0x0040002C 
0x00851020 
0x00400030 
0x03E00008 
Data segment 
Address 
Data 
0x10000000 
0x10000004 
9 
0x10000008 
y 
PES 
UNIVERSITY 
addi $sp, $sp, —4 
sw 
$ra, 0($sp) 
addi $a0, $0, 2 
sw 
$a0, 0x8000($gp) 
addi $a1, $0, 3 
sw 
$al, 0x8004($gp) 
jal 
0x0040002C 
sw 
$v0, 0x8008($gp) 
lw 
$ra, O($sp) 
addi $sp, $sp, 4 
jr 
$ra 
add $v0, $a0, $at 
jr 
$ra 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: The Executable
Example (first store): sw $a0, 0x8000($gp) 
stores 2 into global f at 0x10000000.
●0x8000 is a 16-bit signed offset, sign-
extended to 0xFFFF8000, then added to 
$gp:
●$gp + 0x8000 = 0x10008000 + 
0xFFFF8000 = 0x10000000  (address of f)

--- [Page 20 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 4 - Loading
The OS loads the program by:
1. Reading the text segment of the executable from storage (usually the hard disk) into the text 
segment of memory.
2. Setting $gp = 0x10008000 (middle of the global data segment).
3. Setting $sp = 0x7FFFFFFC (top of the dynamic data segment).
4. Performing jal 0x00400000 to jump to the start of the program.
Memory at start of execution (Figure 6.34):
●Text segment from 0x00400000 holds the 13 instructions (0x23BDFFFC … 0x03E00008).
●f, g, y at 0x10000000–0x10000008 (global data).
●Stack at the top (0x7FFFFFFC), heap at the bottom of the dynamic segment (0x10010000).
●PC = 0x00400000.

--- [Page 21 of 26] ---
Address 
Ox7FFFFFFC 
0x10010000 
0x10000000 
0x00400000 
Memory 
Reserved 
Stack 
Heap 
e 1 
0x03E00008 
0x00851020 
0x03E00008 
0x23BD0004 
0x8FBF0000 
OxAF828008 
0x0C10000B 
0xAF858004 
0x20050003 
O0xAF848000 
0x20040002 
O0xAFBF0000 
0x23BDFFFC 
Reserved 
<«—$sp = Ox7FFFFFFC 
<«— $gp = 0x10008000 
<«—PC = 0x00400000 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Translating and Starting a Program: Step 4 - Loading
Executable loaded in memory

--- [Page 22 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
MCQ
Q1. Which segment does the MIPS j instruction rely on being addressable directly, and why?
 A. Stack, because it starts at 0x7FFFFFFC
 B. Text, because the top 4 bits of its addresses are all 0
 C. Heap, because it grows upward
 D. Global data, because $gp is fixed
Q2. What is the value of $gp at program start, and what does it point to?
 A. 0x10000000, the start of global data
 B. 0x7FFFFFFC, the top of the stack
 C. 0x10008000, the middle of the global data segment
 D. 0x00400000, the start of the text segment

--- [Page 23 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
MCQ
Q3. Why can any global variable be reached efficiently using $gp?
 A. Globals are always stored in registers
 B. The 16-bit signed offset from $gp is known at assembly time, so base addressing with a constant offset 
works
 C. $gp changes with each function call to track the current variable
 D. The linker converts all globals into immediate values
Q4. Which statement about the dynamic data segment is correct?
 A. The heap grows downward from 0x7FFFFFFC and the stack grows upward
 B. The stack grows downward from 0x7FFFFFFC and the heap grows upward from the bottom
 C. Both grow downward, with the heap above the stack
 D. It is reserved for the OS and the program cannot use it

--- [Page 24 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
MCQ
Q5. What does the assembler do on its first pass?
 A. Produces the final machine code
 B. Relocates instructions from library files
 C. Assigns instruction addresses and finds all symbols (labels and global variable names)
 D. Loads the program into memory
Q6. In the example, sw $a0, 0x8000($gp) stores to which address?
 A. 0x10008000 + 0x8000 = 0x10010000
 B. 0x10008000 + 0xFFFF8000 = 0x10000000
 C. 0x00008000
 D. 0x7FFF8000
Q7. Which is the correct order of the steps that translate and start a program?
 A. Assemble → Compile → Link → Load
 B. Compile → Link → Assemble → Load
 C. Compile → Assemble → Link → Load
 D. Link → Compile → Assemble → Load

--- [Page 25 of 26] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Answer key
Q
Ans
Why
1
B
Top 4 bits of text addresses are 0, so j can jump to any program address.
2
C
The OS sets $gp to 0x10008000, the middle of the global data segment.
3
B
The offset is a signed 16-bit constant known at assembly time, so globals are accessed with 
base addressing.
4
B
The stack grows down from 0x7FFFFFFC, and the heap grows up from the bottom.
5
C
Pass 1 builds the symbol table. Pass 2 produces machine code.
6
B
The 0x8000 offset is sign-extended to 0xFFFF8000. Adding it to $gp gives 0x10000000, the 
address of f.
7
C
The pipeline is compiler → assembler → linker → loader.

--- [Page 26 of 26] ---
PES 
UNIVERSITY 
CELEBRATING SO YEARS 
Team DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-9"></a>
## Document 9: Slide Deck 3.15.1: Parallelism - ILP, Multi-threading & Multi-core (37 Pages)
**Source Document**: `resources/u3/3/Slides/3.15.1_Parallelism.pptx`
**OCR Extraction File**: `U3_Slides_3.15.1_Parallelism.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.15.1_Parallelism.pptx
OCR PDF FILE      : U3_Slides_3.15.1_Parallelism_ocr.pdf
TOTAL PAGES       : 37
WORD COUNT        : 2572
CHARACTER COUNT   : 17648
DATE EXTRACTED    : 2026-11-04 14:07:50
================================================================================

--- [Page 1 of 37] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
UE25CS251A
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 37] ---
ARCHITECTURE-Parallelism
TEAM DLCD
Department of CSE and CSE (AI & ML)
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 37] ---
PES 
UNIVERSITY 
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Micro- 4 
architecture < 
Digital 
Circuits 
Analog 
Circuits 
»- 
o 
b3 
Physics 
DIGITAL LOGIC & COMPUTER DESIGN
• Parallelism
© Elsevier, Digital Design and Computer Architecture, 2nd 
TOPICS

--- [Page 4 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
Parallelism is the technique of performing multiple operations simultaneously to 
improve the overall performance of a computer system. Instead of processing one task 
completely before starting the next, several tasks are executed at the same time using 
additional hardware resources or by overlapping different stages of execution.
The primary objective of parallelism is to increase system throughput without significantly 
affecting the latency of an individual task.
●Executes multiple tasks simultaneously.
●Improves processor performance.
●Makes better use of available hardware resources.
●Widely used in modern processors, GPUs, and multicore systems.
Definition: Parallelism is the simultaneous execution of multiple tasks to increase 
the amount of work completed in a given period.
DIGITAL LOGIC & COMPUTER DESIGN
Parallelism

--- [Page 5 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
Modern computer systems must process a large number of tasks efficiently. Simply 
increasing the processor clock frequency is no longer sufficient because it leads to higher 
power consumption and heat generation.
Parallelism improves performance by executing multiple tasks simultaneously or by 
overlapping their execution.
Benefits
●Increases overall system throughput.
●Makes efficient use of available hardware.
●Enables higher performance without relying only on faster clocks.
●Widely used in multicore processors and GPUs.
Key Point: Parallelism mainly improves throughput rather than reducing latency.
DIGITAL LOGIC & COMPUTER DESIGN
Why Parallelism?

--- [Page 6 of 37] ---
REAL-LIFE EXAMPLE: RESTAURANT KITCHEN 
WITHOUT PARALLELISM 
(One Chef Does Everything) 
The chef first cuts the vegetables. 
Only after that does he start cooking. 
WITH PARALLELISM 
(Two Chefs Work Simultaneously) 
One chef prepares the vegetables 
while the other cooks the food at the same time. 
Step 1: 
» \ u 
Prepare 
; 
. 
Vegetables 
Step 2: 
Cook the Food 
Prepares 
' 
; 
o 
Vegetables 
I 
\ 
Cooks the Food 
Time Taken: Longer 
Time Taken: Shorter 
Meals served one after another 
More meals served in the same time 
[* Conclusion: When tasks are done in parallel, the overall work is completed faster. ] 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
Example: Imagine a restaurant kitchen where one chef prepares vegetables while 
another cooks food. Since both tasks occur simultaneously, meals are prepared faster 
than if only one chef performed every task.
DIGITAL LOGIC & COMPUTER DESIGN
Parallelism

--- [Page 7 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Performance Metrics – Latency and Throughput
Before studying parallelism, it is important to understand two performance metrics used to 
evaluate a computer system.
1. Latency
Latency is the time required for a single task (token) to travel from input to output.
It measures how long one operation takes to complete.
Formula
Latency=Time required for one task
​2. Throughput
Throughput is the number of tasks completed per unit time.
Higher throughput means the processor finishes more work every second.

--- [Page 8 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Performance Metrics – Latency and Throughput
Formula
Throughput=Number of completed tasks / Unit Time
For a non-parallel system,
Throughput=1 / Latency
Latency vs Throughput
●Latency is the time taken to complete a single task from start to finish. Lower latency means faster 
response for an individual task.
●Throughput is the number of tasks completed in a given amount of time. Higher throughput means 
the system can process more work overall.
Key Point: A system can achieve high throughput by processing many tasks simultaneously, but the time 
taken for each individual task (latency) may still remain the same, or even increase. Therefore, improving 
throughput does not always reduce latency.

--- [Page 9 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Example – Cookie Throughput and Latency (Textbook Numerical)
Problem: Ben is baking cookies.
●Rolling cookies = 5 minutes
●Baking cookies = 15 minutes
After one tray finishes baking, only then does he start preparing the next tray. Find 
latency and throughput
Solution: Step 1: Latency
Total time for one tray
5+15=20 minutes =1/3 hour
Therefore, Latency=20 minutes​

--- [Page 10 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Example – Cookie Throughput and Latency (Textbook Numerical)
Step 2: Throughput
One tray is completed every 20 minutes.
In one hour,
60/20=3
Hence,
Throughput=3 trays / hour
Observation:
Although each tray requires 20 minutes, only three trays can be produced every 
hour because no tasks overlap.

--- [Page 11 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Types of Parallelism
Parallelism is broadly classified into two categories.
1. Spatial Parallelism
Spatial parallelism improves performance by adding multiple copies of hardware. Each hardware unit 
performs a different task simultaneously.
Examples:
●Multiple processors
●Multiple ALUs
●Multicore CPUs
Advantages:
●Higher throughput
●True simultaneous execution
Disadvantage:
●Higher hardware cost

--- [Page 12 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Types of Parallelism
2. Temporal Parallelism (Pipelining)
Temporal parallelism divides one task into multiple stages.
Different tasks occupy different stages simultaneously, just like an assembly line.
Example
Instruction Fetch -> Instruction Decode -> Execute -> Memory -> Write Back
Advantages
●Better hardware utilization
●Lower hardware cost than spatial parallelism

--- [Page 13 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Types of Parallelism
Spatial Parallelism
●Executes multiple operations simultaneously by duplicating hardware resources.
●Requires additional hardware, such as multiple processors or multiple functional units.
●Provides high performance but comes with higher implementation cost.
Temporal Parallelism
●Improves performance by dividing a task into sequential pipeline stages.
●Reuses the same hardware across different stages over time.
●Requires less additional hardware, making it more cost-effective.
●Commonly implemented using pipelining in processors.
Key Point: Spatial parallelism increases performance by adding more hardware, whereas temporal 
parallelism increases performance by overlapping different stages of execution using the same 
hardware.

--- [Page 14 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Cookie Parallelism (Textbook Numerical)
Ben wants to bake cookies faster.
Case 1: Spatial Parallelism
Ben asks Alyssa to help. Now, Both bake simultaneously.
Latency = 20 minutes
Each person produces : 3 trays/hour
Therefore, Throughput = 3+3 = 6 = 6 trays/hour
Case 2: Temporal Parallelism
Ben buys another tray. While Tray 1 is baking, he prepares Tray 2. Still, latency = 20 minutes
One tray enters oven every 15 minutes
Therefore, Throughput = 60 / 15=4 trays/hour​

--- [Page 15 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Cookie Parallelism (Textbook Numerical)
Case 3: Spatial + Temporal
Two people. Two trays. Result,
Latency = 20 minutes
Throughput = 8 trays/hour
Conclusion:
Parallelism improves throughput but does not reduce latency.

--- [Page 16 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Mathematical Model of Parallelism
Consider a task having latency L.
Without Parallelism
Throughput=1 / L
Spatial Parallelism
Suppose N hardware units exist. Then
Throughput=N / L​
Temporal Parallelism
Suppose, Task divided into N equal stages. Then
Throughput=N / L

--- [Page 17 of 37] ---
PES 
UNIVERSITY 
Real Processor Examples 
Multiple operations occur at the same time 
Multiple operations of the same task are 
using multiple hardware units. 
overlapped in time. 
1. Multicore CPUs 
1. Instruction Pipelining 
e Multiple cores execute 
IF 
ID 
EX 
MEM 
wB 
CORE | CORE 
e Example: Intel Core i7, 
Instr2 
‘Il 
EX 
| 
AMD Ryzen 
Instr 3 
[ F ] o [[Ex ][ mem ][ ws 
] 
[ CONTROL UNIT ] 
. Severa‘I ALL‘Js perform 
| | 
operations in parallel. 
« Different instructions are at different stages of execution 
e Used in superscalar 
simultaneously. 
I'A':UJ I AL_U I 
A"U 
I ALU I 
processors. 
v 
2. Arithmetic Pipelines 
3. GPU Cores 
Stage 
1 
Stage 
2 
Stage 
3 
e Thousands of small cores 
Input —» 
9 
> 
g‘ 
> 
p g 
— Output 
: 
(Add) 
(Multiply) 
(Divide) 
work in parallel on large 
data sets. 
e Example: NVIDIA RTX 
e Long arithmetic operations are divided into pipeline stages 
series 
to increase throughput. 
Modern processors combine both spatial and temporal parallelism } 
to maximize performance and efficiency. 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Mathematical Model of Parallelism

--- [Page 18 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Mathematical Model of Parallelism
If stages are unequal, the longest stage determines speed. If longest stage latency is L1, then
Throughput=1 / L1​
Key Observation:
Increasing the number of stages increases throughput only if the workload is evenly balanced.

--- [Page 19 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Pipelining Example (Textbook Numerical)
Circuit Without Pipeline
Given Clock-to-Q delay is  0.3 ns, Logic blocks are 3 ns, 2 ns, 4 ns, Setup time is 0.2 ns
Step 1: Cycle Time, TC=0.3+3+2+4+0.2=9.5ns
Step 2: Latency = 9.5ns
Step 3: Throughput = 1 / 9.5ns = 105MHz

--- [Page 20 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Two-Stage Pipeline (Textbook Numerical)
Now insert one register after Block 3.
Stage 1: 0.3+3+2+0.2 = 5.5ns
Stage 2: 0.3+4+0.2 = 4.5ns
Clock period equals longest stage.
Therefore, TC = 5.5ns
Throughput = 1 / 5.5ns = 182MHz
Performance Comparison
Without Pipelining
●
Clock Cycle Time: 9.5 ns
●
Maximum Throughput: 105 MHz
●
The entire task is completed in a single long cycle, resulting in a lower operating frequency.

--- [Page 21 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Two-Stage Pipeline (Textbook Numerical)
With Two-Stage Pipelining
●Clock Cycle Time: 5.5 ns
●Maximum Throughput: 182 MHz
●Dividing the circuit into two stages reduces the critical path delay, allowing the 
processor to run at a higher clock frequency.
Observation:
 By introducing pipelining, the clock cycle time decreases from 9.5 ns to 5.5 ns, 
increasing the maximum operating frequency from 105 MHz to 182 MHz. This 
significantly improves throughput, while the latency of an individual task remains 
nearly unchanged.

--- [Page 22 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Why Pipeline is Attractive
Pipelining is one of the most effective forms of temporal parallelism.
Advantages
●Does not require duplicate hardware.
●Divides long combinational logic into shorter stages.
●Enables a shorter clock period.
●Improves throughput significantly.
●Makes efficient use of hardware resources.
Important Note
Pipeline registers isolate consecutive stages, preventing one token from interfering with another.

--- [Page 23 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Advantages, Limitations & Applications
Advantages
●Increases throughput.
●Improves processor utilization.
●Enables higher clock frequencies.
●Forms the basis of modern pipelined processors.
●Essential in multicore CPUs and GPUs.
Limitations
●Spatial parallelism requires additional hardware.
●Pipelining introduces pipeline registers and control complexity.
●Unequal pipeline stages reduce efficiency.
●Data hazards and control hazards may reduce performance.

--- [Page 24 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Advantages, Limitations & Applications
Applications
●Multicore processors
●Graphics Processing Units (GPUs)
●Supercomputers
●Digital Signal Processors (DSPs)
●Machine Learning accelerators
Key Takeaways
●Latency measures the time taken to complete one task.
●Throughput measures the number of tasks completed per unit time.
●Spatial Parallelism uses multiple hardware units.
●Temporal Parallelism overlaps task execution through pipelining.
●Parallelism mainly improves throughput, while latency often remains unchanged.
●Pipelining is one of the most effective and widely used forms of temporal parallelism in modern 
computer architecture.

--- [Page 25 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Advantages, Limitations & Applications
Pipeline Hazards
Pipeline hazards are conditions that prevent instructions from executing smoothly through the pipeline. They introduce 
stalls (bubbles), reducing the overall throughput.
1. Data Hazard
●
Occurs when an instruction requires data that is still being produced by a previous instruction.
●
The dependent instruction must wait until the data is available.
2. Control Hazard
●
Caused by branch or jump instructions.
●
The processor may fetch incorrect instructions until the branch decision is known.
3. Structural Hazard
●
Occurs when multiple instructions need the same hardware resource simultaneously.
●
One instruction must wait until the resource becomes available.

--- [Page 26 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Advantages, Limitations & Applications
Question:
 The circuit in the textbook is divided into a three-stage pipeline. The three pipeline stages have delays of 3.5 ns, 2.5 ns, and 
4.5 ns, respectively. Determine:
1.
The clock cycle time
2.
The latency of the circuit
3.
The throughput
Answer
The clock must be slow enough for the slowest pipeline stage.
Tc=max⁡(3.5,2.5,4.5);  Tc=4.5 ns
Latency:
There are 3 pipeline stages.
Latency = 3Tc = 3(4.5)=13.5 ns

--- [Page 27 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
DIGITAL LOGIC & COMPUTER DESIGN
Advantages, Limitations & Applications
Throughput:
Throughput
= 1/Tc
= 14.5×10^-9
≈ 222 MHz
Final Answer:
●
Cycle time = 4.5 ns
●
Latency = 13.5 ns
●
Throughput = 222 MHz

--- [Page 28 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Parallelism primarily aims to improve:
A) Memory capacity
 B) Throughput
 C) Register size
 D) Cache size

--- [Page 29 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
A token in a parallel system refers to:
A) A processor core
 B) A unit of work moving through the system
 C) A clock pulse
 D) A memory address

--- [Page 30 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Which type of parallelism increases performance by using multiple hardware units?
A) Temporal Parallelism
 B) Spatial Parallelism
 C) Instruction Parallelism
 D) Data Compression

--- [Page 31 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Pipeline registers are inserted to:
A) Increase memory size
 B) Divide combinational logic into stages
 C) Reduce cache misses
 D) Store operating system data

--- [Page 32 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Modern processors achieve high performance by combining:
A) Only higher clock frequencies
 B) Only larger memories
 C) Spatial and temporal parallelism
 D) Only single-cycle execution

--- [Page 33 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Increasing the number of pipeline stages generally:
A) Improves throughput but may increase latency
 B) Reduces throughput significantly
 C) Eliminates pipeline hazards completely
 D) Makes the processor slower in all cases

--- [Page 34 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Which metric indicates how much useful work a system completes over time?
A) Latency
 B) Throughput
 C) Clock Period
 D) Register Width

--- [Page 35 of 37] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Which of the following is a real-world example of temporal parallelism?
A) Two cashiers serving customers simultaneously
 B) An assembly line where different workers perform different stages on different 
products
 C) Two printers printing the same document
 D) Two CPUs installed on a motherboard without coordination

--- [Page 36 of 37] ---
PES 
UNIVERSITY 
MCQ
DIGITAL LOGIC & COMPUTER DESIGN
Answer Key
Q1: B  Q2: B  Q3: B  Q4: B  Q5: C  Q6: B    Q7: B     Q8: B

--- [Page 37 of 37] ---
PES 
UNIVERSITY 
CELEBRATING SO YEARS 
Team DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-10"></a>
## Document 10: Slide Deck 3.17.1: Classwork Practice Problems (16 Pages)
**Source Document**: `resources/u3/3/Slides/3.17.1_Classwork_problems.pptx`
**OCR Extraction File**: `U3_Slides_3.17.1_Classwork_problems.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.17.1_Classwork_problems.pptx
OCR PDF FILE      : U3_Slides_3.17.1_Classwork_problems_ocr.pdf
TOTAL PAGES       : 16
WORD COUNT        : 1182
CHARACTER COUNT   : 6530
DATE EXTRACTED    : 2026-11-04 14:04:59
================================================================================

--- [Page 1 of 16] ---
PES 
UNIVERSITY 
TEAM DLCD
Department of CSE and CSE (AI & ML)
DIGITAL LOGIC AND 
COMPUTER DESIGN

--- [Page 2 of 16] ---
PES 
UNIVERSITY 
Sequential Building Blocks
TEAM DLCD
Department of CSE and CSE (AI & ML)
  
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 3 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.43
Exercise 5.43: Build a 32-bit synchronous Up/Down counter. The inputs are Reset and Up. When Reset is 1, the outputs are all 0. 
Otherwise, when Up = 1, the circuit counts up, and when Up = 0, the circuit counts down.
Given
●
Inputs: Reset, Up, CLK
●
Output: Q[31:0]
●
If Reset = 1 → Q = 0
●
If Reset = 0 and Up = 1 → count up
●
If Reset = 0 and Up = 0 → count down
Design
Use:
●
32-bit register
●
32-bit adder/subtractor
●
MUX
●
Constant 1

--- [Page 4 of 16] ---
Up 
32'h0000_0001 — 
(+1) 
32'hFFFF_FFFF — 
=1 
CLK 
Reset 
2:1 
MUX 
Q[31:0] 
32-bit 
Adder 
(Q+A) 
D[31:0] 
' 
32-bit Register 
Q[31:0] 
> 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.43
The next-state equation is:
Q+= {
0 
Reset=1
Q+1
Reset=0, Up=1
Q−1
Reset=0, Up=0}
A convenient implementation is: Q^(+) = Q + (2Up-1)
or, more practically, use an adder/subtractor controlled by Up.
Reset here is synchronous - it overrides D on the clock edge, not an immediate async clear.

--- [Page 5 of 16] ---
Q[31:0] 
32-bit 
32'h0000_0004 
— ! 
adder 
- 
(+4) 
(Q+4) 
D[31:0] 
Y 
CLK —» 
Reset —» 
32-bit Register 
Q[31:0] 
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.44
Exercise 5.44 Design a 32-bit counter that adds 4 at each clock edge. The counter has reset and clock inputs. Upon reset, the counter 
output is all 0.
Given
●
Inputs: Reset, CLK
●
Output: Q[31:0]
●
Reset → Q = 0
●
Every clock edge:
Q^(+) = Q+4
Design
Use:
●
32-bit register
●
32-bit adder
●
Constant 4

--- [Page 6 of 16] ---
PES 
UNIVERSITY 
& 
(a) X=AB+BCD+AB 
(b) Y=AB+BD 
(c) Z=A+B+C+D 
(a) X=AB+BCD+AB 
(b) Y=AB+BD 
(c) Z=A+B+C+D 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.51
Implement the following functions using a single 16 × 3 ROM. Use dot notation to indicate the ROM contents.
Given:
A 16 × 3 ROM has:
●
4 address inputs: A,B,C,D since 2^(4)=16 addresses
●
3 data outputs: X,Y,Z
Step 1: Determine the ROM contents

--- [Page 7 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.51
Address
A B C D
X
Y
Z
ROM Data (XYZ)
0
0000
1
0
0
100
1
0001
1
0
1
101
2
0010
1
0
1
101
3
0011
1
0
1
101
4
0100
0
0
1
001
5
0101
0
1
1
011
6
0110
0
0
1
001
7
0111
0
1
1
011
8
1000
0
0
1
001
9
1001
0
0
1
001
10
1010
1
0
1
101

--- [Page 8 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.51
11
1011
0
0
1
001
12
1100
1
1
1
111
13
1101
1
1
1
111
14
1110
1
1
1
111
15
1111
1
1
1
111
Step 2: ROM contents
Therefore, the 16 × 3 ROM stores:
100, 101, 101, 101, 001, 011, 001, 011, 001, 001, 101, 001, 111, 111, 111, 111​

--- [Page 9 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.51
Dot Notation
In dot notation, place a dot at the intersection of an address row and output column wherever the ROM stores a 1.
Address ABCDABCD
X
Y
Z
0000
●
0001
●
●
0010
●
●
0011
●
●
0100
●
0101
●
●
0110
●
0111
●
●

--- [Page 10 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 5.51
1000
●
1001
●
1010
●
●
1011
●
1100
●
●
●
1101
●
●
●
1110
●
●
●
1111
●
●
●

--- [Page 11 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 6.3
Exercise 6.3: Consider memory storage of a 32-bit word stored at memory word 42 in a byte-addressable memory. (a) 
What is the byte address of memory word 42? (b) What are the byte addresses that memory word 42 spans? (c) Draw 
the number 0xFF223344 stored at word 42 in both big-endian and little-endian machines. Your drawing should be 
similar to Figure 6.4. Clearly label the byte address corresponding to each data byte value.
Given
●
Memory word = 42
●
Word size = 32 bits = 4 bytes
●
Memory is byte-addressable
●
Data = 0xFF223344
(a) Byte address of memory word 42
Since each word occupies 4 bytes: Byte address=Word number×4=42×4=168
Convert 168 to hexadecimal: 0xA8
Answer:0xA8. So, word 42 starts at byte address 0xA8.

--- [Page 12 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 6.3
(b) Byte addresses that word 42 spans
A 32-bit word contains 4 bytes.
Starting at 0xA8, the four bytes occupy consecutive addresses:
Byte
Address
Byte 0
0xA8
Byte 1
0xA9
Byte 2
0xAA
Byte 3
0xAB
Answer: 0xA8, 0xA9, 0xAA, 0xAB​

--- [Page 13 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 6.3
(c) Store 0xFF223344
First divide the 32-bit number into its four bytes: FF
22
33
44, where:
●
FF = Most Significant Byte (MSB)
●
44 = Least Significant Byte (LSB)
The textbook explains that in big-endian, the MSB is stored at the lower byte address, while in little-endian, the LSB is 
stored at the lower byte address.
Big-Endian
MSB goes to the lowest address. Therefore:
●
FF → 0xA8
●
22 → 0xA9
●
33 → 0xAA
●
44 → 0xAB

--- [Page 14 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 6.3
Little-Endian
LSB goes to the lowest address.
Therefore:
●
44 → 0xA8
●
33 → 0xA9
●
22 → 0xAA
●
FF → 0xAB
Finally, 
Big-endian
A8:FF, A9:22, AA:33, AB:44
Little-endian
A8:44, A9:33, AA:22, AB:FF

--- [Page 15 of 16] ---
PES 
UNIVERSITY 
© Elsevier, Digital Design and Computer Architecture, 2nd Ed., 2012.
DIGITAL LOGIC & COMPUTER DESIGN
Exercise problems: 6.4
Exercise 6.4: Repeat Exercise 6.3 for memory storage of a 32-bit word stored at memory word 15 in a byte-
addressable memory.
(a) Byte address of memory word 15
Byte Address=15×4=60= 0x3C (in hexadecimal)
(b) Byte addresses that memory word 15 spans
A 32-bit word = 4 bytes, so it spans:
0x3C, 0x3D, 0x3E, 0x3F
(c) Store 0xFF223344
Endian Type
Byte Address : Data
Big-endian
3C:FF, 3D:22, 3E:33, 3F:44
Little-endian
3C:44, 3D:33, 3E:22, 3F:FF

--- [Page 16 of 16] ---
PES 
UNIVERSITY 
CELEBRATING SO YEARS 
Team DLCD
Department of CSE and CSE(AI & ML)
THANK YOU

```

---

<a id="doc-11"></a>
## Document 11: Assignment 3.1.1: Sequential Building Blocks Assignment (2 Pages)
**Source Document**: `resources/u3/3/Assignments/3.1.1_ASSIGNMENT.docx`
**OCR Extraction File**: `U3_Assignment_3.1.1_ASSIGNMENT.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.1.1_ASSIGNMENT.docx
OCR PDF FILE      : U3_Assignment_3.1.1_ASSIGNMENT_ocr.pdf
TOTAL PAGES       : 2
WORD COUNT        : 591
CHARACTER COUNT   : 3476
DATE EXTRACTED    : 2026-11-04 14:03:58
================================================================================

--- [Page 1 of 2] ---
DLCD LEVEL-2 PROBLEM STATEMENTS
Instructions: 
1. Level-2 problem will be solved by 4 members team. The team is same as the project 
team of the Lab project.
2. Solution to be submitted to the respective lab instructor on the day of the lab project 
presentation.
3. Expected outcome of this exercise is working Verilog code, Test bench and output.
4. Team should demo the Verilog code to the respective lab instructor, and answer any 
questions asked related to the level-2 problem statement and Verilog syntax.
5. Lab instructor will assign Problem 1 for Half of the project team of respective section, 
Problem2 for the rest of the teams.
Problem Statement:
Problem1: Traffic Light Controller Built from K-map-Derived Flip-Flop Equations
Design a traffic light controller with 3 states, RED, GREEN, and YELLOW, cycling forever in 
that order, one clock tick per state. The requirement is to derive the actual next-state 
equations for the flip-flops directly from a K-map, and implement the FSM using those 
equations, rather than writing a behavioral case statement for the state transitions.
Interface:
●
Inputs: clk, reset (synchronous, active high; goes to RED)
●
Outputs: red, green, yellow (one-hot, only one high at a time)
State encoding: RED = 00, GREEN = 01, YELLOW = 10 (state bits S1 S0). The code 11 is 
unused.
Tasks:
1. Write the state transition truth table: current state S1 S0 to next state D1 D0, for 
RED to GREEN to YELLOW to RED. Treat the unused code 11 as a don't care.
2. Use a K-map to derive minimized Boolean equations for D1 and D0 directly from 
that truth table.
3. Derive the Moore output equations for red, green, and yellow directly from the 
state bits (each is a single minterm, no grouping needed).
4. Implement the FSM in Verilog using only the derived equations for D1, D0, red, 
green, and yellow, connected to a plain 2-bit register. Do not use a case statement 
anywhere in the design. Write a testbench that runs the FSM through at least 2 full 
RED-GREEN-YELLOW cycles and confirms the output sequence is correct.

--- [Page 2 of 2] ---
Problem2: 4-Bit Counter FSM with Run/Hold Control and 7-Segment Output
Design a 4-bit counter controlled by a simple 2-state Moore FSM, with its value shown on a 
7-segment display.
Interface:
●
Inputs: clk, reset (synchronous, active high), run
●
Outputs: count[3:0], seg[6:0] (common-cathode 7-segment pattern, active high)
Behavior: two states, RUN and HOLD. While run = 1, the FSM is in RUN and count 
increases by 1 every clock edge, wrapping from 1111 back to 0000. While run = 0, the 
FSM is in HOLD and count keeps its current value. seg is generated combinationally 
from count, showing the hexadecimal digit 0 through F.
Tasks:
1. Draw the 2-state state diagram for RUN and HOLD, labeling the transition 
condition on every arrow, including the self-loops.
2. Write the next-count logic as a truth table style description: in RUN, next count = 
count + 1 (mod 16); in HOLD, next count = count. Show how a 2-to-1 MUX selecting 
between (count + 1) and count, controlled by run, feeds the D inputs of four flip-
flops.
3. Design the 7-segment decoder as a combinational module with a full truth table 
covering all 16 hex digits (0 through F), each mapped to its 7-segment pattern.
4. Implement the whole design in Verilog (the run-controlled counter plus the 
decoder) and write a testbench that checks: count increases while run = 1, count 
holds while run = 0, and count wraps from 1111 to 0000 correctly.

```

---

<a id="doc-12"></a>
## Document 12: Question-Answer Bank: 5, 8, 10 Mark Solved Questions (24 Pages)
**Source Document**: `resources/u3/QA/3.1.1_QA.pdf`
**OCR Extraction File**: `U3_QA_3.1.1_QA.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.1.1_QA.pdf
OCR PDF FILE      : U3_QA_3.1.1_QA_ocr.pdf
TOTAL PAGES       : 24
WORD COUNT        : 8643
CHARACTER COUNT   : 49057
DATE EXTRACTED    : 2026-11-04 14:06:43
================================================================================

--- [Page 1 of 24] ---
Digital Logic and Computer Design (DLCD)
Question Bank – 5, 8 and 10 Mark Questions with Answers
Based on the Unit PPTs: Introduction, Assembly Language, Machine Language, Programming, Addressing 
Modes, Parallelism, Sequential Building Blocks, Memory Arrays
How to use: every answer has exactly as many numbered points as marks – 5 marks = 5 
points, 8 marks = 8 points, 10 marks = 10 points (1 point = 1 mark). Each deck has 2 
questions of 5 marks, 2 of 8 marks and 2 of 10 marks.
1. Introduction (Computer Architecture)
Q1. [5 Marks]  Define computer architecture. State what it specifies and why it is important 
to study it.
Answer (5 points):
1.
Definition: Computer architecture is the programmer's view of a computer; it defines how 
software communicates with hardware.
2.
Instruction Set Architecture (ISA): it specifies the set of instructions the processor 
understands.
3.
Operand locations: it specifies where operands are kept – registers and memory.
4.
Data representation and instruction formats: it specifies how data and instructions are 
encoded in bits.
5.
Importance: it bridges the gap between hardware and software, decides how programs are 
executed, helps design efficient, compatible, high-performance systems and is the foundation 
of processor organisation and programming.
Q2. [5 Marks]  Differentiate between assembly language and machine language with an 
example. Who developed MIPS?
Answer (5 points):
1.
Instructions are the "words" of a computer's language; the collection of instructions is the 
instruction set.
2.
Assembly language is the human-readable form of instructions using mnemonics, e.g. add 
$s0, $s1, $s2.
3.
Machine language is the computer-readable form made of 1's and 0's (32-bit in MIPS), e.g. 
the same instruction is 0x02328020.
add $s0, $s1, $s2
000000 10001 10010 10000 00000 100000  = 0x02328020
4.
Translation: assembly is translated into machine code by an assembler; the processor 
executes only machine code, while assembly is easier to write, read and debug.
5.
MIPS was developed by John Hennessy and colleagues at Stanford in the 1980s.
Q3. [8 Marks]  Explain the statement "Instruction sets are like dialects of a language". 
Name some architectures and explain how complex applications finally run on the 
processor.
Answer (8 points):
1.
Many architectures exist, e.g. x86, MIPS, SPARC and PowerPC.
2.
Each architecture defines its own instruction set.
3.
Dialect analogy: dialects of one language share the same structure but differ in vocabulary; 
likewise instruction sets share the same basic ideas (arithmetic, logic, load/store, branch) but 
differ in names and formats.
4.
Hence, once one architecture is learnt, learning another is fairly straightforward.
5.
Instructions are the words of the computer's language.
DLCD Question Bank – Page 1

--- [Page 2 of 24] ---
6.
Even complex applications are compiled down to simple instructions such as add, 
subtract and jump.
7.
The processor fetches and executes these simple instructions one after another.
8.
The ISA is therefore the interface between software and hardware: a program must be 
compiled for the ISA of the machine on which it runs.
Q4. [8 Marks]  Describe the MIPS architecture – its full form, origin, philosophy and 
applications.
Answer (8 points):
1.
Full form: Microprocessor without Interlocked Pipelined Stages.
2.
MIPS is a family of Reduced Instruction Set Computer (RISC) instruction set architectures.
3.
It was developed by John Hennessy and colleagues at Stanford in the 1980s.
4.
It was commercialised by MIPS Computer Systems (now MIPS Technologies), United States.
5.
It is used in commercial systems such as Silicon Graphics, Nintendo and Cisco.
6.
Philosophy: a small set of simple, regular instructions with 32-bit data and 32-bit instructions 
that can be decoded and executed quickly.
7.
It contrasts with CISC architectures like Intel x86, where one instruction performs a more 
complex task.
8.
Once MIPS is learnt, other architectures are easy to learn.
Q5. [10 Marks]  Explain how a high-level language statement is finally executed by the 
hardware. Illustrate the levels of abstraction using a = b + c.
Answer (10 points):
1.
High-level language (C, Java, Python) works at a high abstraction level using if/else, loops, 
arrays and function calls.
2.
A compiler converts high-level code into simple instructions of the target ISA.
3.
Assembly language represents each instruction with a human-readable mnemonic.
4.
An assembler converts assembly into machine language, a 32-bit binary pattern stored in 
memory.
5.
Example in C: a = b + c;  → MIPS assembly: add a, b, c.
C:    a = b + c;
MIPS: add a, b, c
6.
In the assembly instruction, add is the mnemonic (operation), b and c are the source 
operands and a is the destination operand.
7.
With real registers (a=$s0, b=$s1, c=$s2) the instruction becomes add $s0, $s1, $s2.
8.
Its machine code is 000000 10001 10010 10000 00000 100000 = 0x02328020.
op=000000 rs=10001($s1) rt=10010($s2) rd=10000($s0) shamt=00000 
funct=100000(add)
9.
The CPU fetches this 32-bit word from memory and decodes the opcode/funct fields.
10. It reads $s1 and $s2, the ALU adds them and the result is written back to $s0.
Q6. [10 Marks]  Explain the role of the Instruction Set Architecture as the interface between 
software and hardware. Compare RISC (MIPS) and CISC (x86) architectures.
Answer (10 points):
1.
ISA is the set of instructions, operand locations, data representation and instruction formats 
that a processor supports.
2.
It is the programmer's view of the computer and hides how the hardware is built internally.
3.
Software compiled for an ISA can run on any hardware that implements that ISA, which 
gives compatibility.
DLCD Question Bank – Page 2

--- [Page 3 of 24] ---
4.
Hardware designers may implement the same ISA in different ways to trade off performance, 
cost and power.
5.
Examples of ISAs: x86, MIPS, SPARC, PowerPC; each has its own instruction set.
6.
RISC (MIPS): a small set of simple, regular instructions that are decoded and executed 
quickly.
7.
In RISC, complex operations are built by combining several simple instructions.
8.
RISC gives simpler hardware, faster execution and lower power consumption.
9.
CISC (x86): individual instructions perform more complex tasks, so fewer instructions are 
needed per program but hardware is more complex.
10. This is the design principle "Good design demands good compromises" – no design 
optimises everything.
Feature
RISC (MIPS)
CISC (x86)
Instructions
Simple
Complex
Hardware
Simpler
More complex
Instructions per program
More
Fewer
Execution speed
Faster per instruction
Slower per instruction
DLCD Question Bank – Page 3

--- [Page 4 of 24] ---
2. Assembly Language (MIPS)
Q1. [5 Marks]  State and explain the four design principles of computer architecture.
Answer (5 points):
1.
Simplicity favors regularity: uniform instruction formats (e.g. add/sub both use two sources 
and one destination) simplify encoding, decoding and hardware.
2.
Make the common case fast: frequently executed operations are optimised; MIPS has a 
small set of simple instructions (RISC) and builds complex operations from them.
3.
Smaller is faster: small structures such as the 32-register file have lower access time than 
large memory.
4.
Good design demands good compromises: performance, cost, power and complexity 
must be balanced (e.g. RISC vs CISC).
5.
Example: MIPS applies all four – regular formats, simple common instructions, only 32 
registers and a RISC compromise.
Q2. [5 Marks]  What are the three operand locations in MIPS? Explain with the example 
addi $t0, $t1, 10.
Answer (5 points):
1.
An operand is the data used by an instruction; it can be stored in different locations.
2.
Registers: high-speed storage inside the CPU for frequently used data (32 registers).
3.
Memory: large storage for programs and data that do not fit in registers; accessed using lw 
and sw.
4.
Constants (immediates): fixed values encoded directly in the instruction (16-bit signed).
5.
Example: in addi $t0, $t1, 10, $t0 is the destination register, $t1 the source register and 10 
the immediate; $t0 = $t1 + 10.
Q3. [8 Marks]  Describe the MIPS register set. Why does MIPS have only 32 registers? 
Explain the usage of the important registers.
Answer (8 points):
1.
MIPS has 32 general-purpose registers, each 32 bits wide, so it is called a 32-bit 
architecture.
2.
Every register name is prefixed with $ (e.g. $0 is read "dollar zero").
3.
Why only 32 – "Smaller is faster": a small register file has lower access time and balances 
performance and hardware complexity.
4.
$0 always holds the constant 0 and cannot be modified.
5.
$s0–$s7 (saved): variables whose values must be preserved across function calls.
6.
$t0–$t9 (temporaries): intermediate results; need not be preserved.
7.
$a0–$a3 pass function arguments and $v0–$v1 hold return values.
8.
Special registers: $at (assembler temporary), $k0–$k1 (OS), $gp (global pointer), $sp (stack 
pointer), $fp (frame pointer) and $ra (return address).
Name
No.
Usage
$0
0
constant 0
$at
1
assembler temporary
$v0–$v1
2–3
return values
$a0–$a3
4–7
arguments
$t0–$t7
8–15
temporaries
$s0–$s7
16–23
saved variables
$t8–$t9
24–25
more temporaries
$k0–$k1
26–27
OS temporaries
DLCD Question Bank – Page 4

--- [Page 5 of 24] ---
Name
No.
Usage
$gp $sp $fp $ra
28 29 30 31
global, stack, frame pointer, return address
Q4. [8 Marks]  Compare word-addressable and byte-addressable memory. Explain lw and 
sw with effective address calculation.
Answer (8 points):
1.
Word-addressable memory: each address refers to one complete word (32 bits = 4 bytes); 
individual bytes cannot be addressed directly.
2.
Byte-addressable memory: each address refers to exactly one byte (8 bits).
3.
A 32-bit word occupies 1 address in word-addressable memory but 4 consecutive 
addresses in byte-addressable memory.
4.
Word addresses increase by 1 word (0,1,2,3); byte addresses increase by 1 byte, so 
consecutive words start at 0, 4, 8, 12.
5.
Byte-addressable memory is more flexible because individual bytes can also be accessed; 
MIPS uses byte-addressable memory.
6.
lw (load word) reads memory into a register; sw (store word) writes a register to memory: 
lw dest, offset(base).
7.
Effective Address = Base Register + Offset; in MIPS the offset is in bytes, not words.
8.
Examples: lw $s3, 4($0) → EA = 0 + 4 = 4, bytes 4–7 are loaded into $s3; lw $s0, 5($t1) with 
$t1 = 20 → EA = 25; sw $t4, 0x7($0) → value of $t4 written to location 7.
lw $s3, 4($0)    # EA = 0 + 4 = 4 -> bytes 4,5,6,7
lw $s0, 5($t1)   # $t1=20 -> EA = 25
sw $t4, 0x7($0)  # write $t4 at EA = 7
Q5. [10 Marks]  Translate the following into MIPS assembly: (a) a = b – c  (b) f = (g + h) – (i 
+ j)  (c) a = a + 4; b = a – 12. Assume a–c in $s0–$s2 and f–j in $s3–$s7. Explain why there 
is no subi.
Answer (10 points):
1.
Add format: add a, b, c – add is the mnemonic, b and c are sources, a is the destination.
2.
Sub format: sub a, b, c performs a = b – c; it follows the same regular format.
3.
(a) a = b – c:
# $s0=a $s1=b $s2=c $s3=f $s4=g $s5=h $s6=i $s7=j
sub $s0, $s1, $s2     # a = b - c
4.
Each MIPS instruction has only two sources and one destination, so longer expressions 
need temporary registers for intermediate results.
5.
(b) f = (g+h) – (i+j) needs four instructions:
add $t0, $s4, $s5     # t0 = g + h
add $t1, $s6, $s7     # t1 = i + j
sub $s3, $t0, $t1     # f = t0 - t1
6.
For a = b + c – d, two instructions are used: add t, b, c then sub a, t, d (t = temporary).
7.
Immediate operands are constants embedded in the instruction (16-bit two's complement), 
avoiding a memory access or extra register.
8.
(c) a = a + 4 and b = a – 12:
addi $s0, $s0, 4      # a = a + 4
addi $s1, $s0, -12    # b = a - 12
9.
Why no subi? Subtraction of a constant is done by adding a negative immediate, so a 
separate instruction is unnecessary (regularity; make the common case fast).
10. Think-about-it: a left shift by 3 (×8) can be done with only add: add $t0,$s0,$s0 repeated 
three times, using just one register.
DLCD Question Bank – Page 5

--- [Page 6 of 24] ---
Q6. [10 Marks]  Explain big-endian and little-endian byte ordering. If $t0 = 0x23456789, find 
$s0 after sw $t0, 0($0) and lb $s0, 1($0) in both systems. How can a program detect the 
endianness of a machine?
Answer (10 points):
1.
A word has several bytes, so a rule is needed for how bytes are numbered within a word.
2.
Big-endian: numbering starts at the big (most significant) end – the MSB is stored at the 
lowest byte address.
3.
Little-endian: numbering starts at the little (least significant) end – the LSB is stored at the 
lowest byte address.
4.
The word address is the same in both systems.
5.
The names come from Gulliver's Travels (eggs broken at the big or little end); the choice 
does not matter except when two systems share data.
6.
For the word 0x23456789 stored at address 0, the byte layout is:
Byte address
0
1
2
3
Big-endian
23
45
67
89
Little-endian
89
67
45
23
7.
sw $t0, 0($0) stores the word at address 0; lb $s0, 1($0) loads the single byte at address 1.
8.
Big-endian: byte at address 1 is 0x45, so $s0 = 0x00000045.
9.
Little-endian: byte at address 1 is 0x67, so $s0 = 0x00000067.
10. Detecting endianness: store 1 as a word and read the byte at address 0 – if it is 1 the 
machine is little-endian, if 0 it is big-endian. (Without lb/sb, the bytes must be separated by 
other means such as shifts and masks.)
addi $t0, $0, 1
sw   $t0, 0($0)
lb   $s0, 0($0)    # 1 -> little-endian, 0 -> big-endian
DLCD Question Bank – Page 6

--- [Page 7 of 24] ---
3. Machine Language (MIPS)
Q1. [5 Marks]  Explain the three MIPS instruction formats (R, I and J) with their field sizes.
Answer (5 points):
1.
All MIPS instructions are 32 bits long (simplicity favors regularity) and come in three formats.
2.
R-type (register operands): op(6) | rs(5) | rt(5) | rd(5) | shamt(5) | funct(6); op = 0 and funct 
selects the exact operation.
3.
In R-type, rs and rt are sources, rd is the destination and shamt is the shift amount 
(otherwise 0).
4.
I-type (immediate): op(6) | rs(5) | rt(5) | imm(16); used for immediates, load/store and 
branches; the opcode alone decides the operation.
5.
J-type (jump): op(6) | addr(26); used for j and jal. Decode order: opcode → format → field 
meaning → assembly instruction.
Q2. [5 Marks]  Explain the logical instructions and, or, xor, nor and their immediate forms 
with applications.
Answer (5 points):
1.
and is used for masking bits, e.g. 0xF234012F AND 0x000000FF = 0x0000002F.
2.
or is used for combining bit fields, e.g. 0xF2340000 OR 0x000012BC = 0xF23412BC.
3.
xor shows differences between bits.
4.
nor is OR followed by inversion; A NOR $0 = NOT A, so MIPS has no separate NOT.
5.
andi, ori, xori use a 16-bit immediate that is zero-extended; nori is not needed because ori 
followed by nor with $0 gives the same result.
Q3. [8 Marks]  Explain the shift instructions sll, srl, sra and the variable shifts sllv, srlv, 
srav with examples.
Answer (8 points):
1.
Shift instructions move the bits of a register left or right by 0 to 31 positions.
2.
sll (shift left logical): fills the least significant bits with 0; shifting left by N multiplies by 2^N.
3.
srl (shift right logical): shifts 0s into the most significant bits; used for unsigned values.
4.
sra (shift right arithmetic): copies the sign bit into the new most significant bits; divides a 
signed value by 2^N.
5.
Shifts are R-type: the value in rt is shifted by shamt and the result is placed in rd.
6.
Example: 10010000 → srl by 2 = 00100100; sra by 2 = 11100100; sll $t0,$s1,4 on 1111 
0011 0000 0000 0000 0010 1010 1000 gives 0011 0000 0000 0000 0010 1010 1000 0000.
7.
Variable shifts take the amount from a register: sllv rd, rt, rs; rt holds the value and the 5 
least significant bits of rs give the shift amount.
8.
For variable shifts the order of rt and rs is reversed compared with most R-type instructions 
and shamt is ignored (0); e.g. $s2 = 8 shifts by 8.
Q4. [8 Marks]  Explain the stored program concept and the role of the Program Counter 
with an example.
Answer (8 points):
1.
Both 32-bit instructions and data are stored in memory.
2.
The only difference between two applications is the sequence of instructions stored.
3.
To run a new program there is no rewiring – the new program is simply stored in memory.
4.
The processor fetches instructions from memory in sequence.
5.
The processor then performs the specified operation.
6.
The Program Counter (PC) keeps track of the current instruction by holding its address.
7.
After each fetch the PC is normally incremented by 4; branch and jump instructions change it.
DLCD Question Bank – Page 7

--- [Page 8 of 24] ---
8.
Example: the program starts at 0x00400000 and the PC steps through 0x00400004, 
0x00400008, 0x0040000C.
Address      Machine code   Assembly
0x00400000   0x8C0A0020     lw   $t2, 32($0)
0x00400004   0x02328020     add  $s0, $s1, $s2
0x00400008   0x2268FFF4     addi $t0, $s3, -12
0x0040000C   0x016D4022     sub  $t0, $t3, $t5
Q5. [10 Marks]  Encode into machine code (binary and hex): add $s0,$s1,$s2; sub 
$t0,$t3,$t5; addi $s0,$s1,5; addi $t0,$s3,-12; lw $t2,32($0); sw $s1,4($t1).
Answer (10 points):
1.
Register numbers: $0=0, $t0=8, $t1=9, $t2=10, $t3=11, $t5=13, $s0=16, $s1=17, $s2=18, 
$s3=19.
2.
R-type format: op | rs | rt | rd | shamt | funct, with assembly written as op rd, rs, rt.
3.
add $s0,$s1,$s2 → 0 | 17 | 18 | 16 | 0 | 32 = 0x02328020.
000000 10001 10010 10000 00000 100000
4.
sub $t0,$t3,$t5 → 0 | 11 | 13 | 8 | 0 | 34 = 0x016D4022.
000000 01011 01101 01000 00000 100010
5.
I-type format: op(6) | rs(5) | rt(5) | imm(16).
6.
addi $s0,$s1,5 → 8 | 17 | 16 | 5 = 0x22300005.
001000 10001 10000 0000 0000 0000 0101
7.
addi $t0,$s3,-12 → 8 | 19 | 8 | -12 = 0x2268FFF4 (-12 = 0xFFF4 in 16-bit two's 
complement).
001000 10011 01000 1111 1111 1111 0100
8.
lw $t2,32($0) → 35 | 0 | 10 | 32 = 0x8C0A0020.
100011 00000 01010 0000 0000 0010 0000
9.
sw $s1,4($t1) → 43 | 9 | 17 | 4 = 0xAD310004.
101011 01001 10001 0000 0000 0000 0100
10. Register order: in R-type the destination is written first in assembly but stored in rd; in I-type 
assembly lists rt first, yet machine code places rs before rt; in lw/sw, rs is the base register 
and imm is the byte offset.
Q6. [10 Marks]  Explain the strategy for interpreting machine code. Decode 0x2237FFF1 
and 0x02F34022 and explain how a 32-bit constant is loaded into a register.
Answer (10 points):
1.
Step 1: read the opcode (top 6 bits) – it tells how to parse the remaining bits.
2.
Step 2: if the opcode is all 0's the instruction is R-type and the funct field gives the operation.
3.
Step 3: otherwise the opcode itself identifies the I-type or J-type instruction.
4.
Step 4: convert register numbers to register names.
5.
Step 5: interpret the immediate as signed or unsigned as the instruction requires (e.g. 
andi/ori/xori zero-extend).
6.
Decode 0x2237FFF1 = 001000 10001 10111 1111111111110001.
Field
Value
Meaning
op
001000
addi
rs
10001
$s1
rt
10111
$s7
DLCD Question Bank – Page 8

--- [Page 9 of 24] ---
Field
Value
Meaning
imm
1111…0001
-15
7.
Result: addi $s7, $s1, -15.
8.
Decode 0x02F34022 = 000000 10111 10011 01000 00000 100010: opcode 0 → R-type, 
funct 100010 = sub.
9.
Fields: rs = 23 ($s7), rt = 19 ($s3), rd = 8 ($t0) → sub $t0, $s7, $s3.
10. 32-bit constants: addi handles only 16 bits, so lui loads the upper 16 bits and ori inserts the 
lower 16 bits (e.g. 0x6D5E4F3C).
lui $s0, 0x6D5E          # $s0 = 0x6D5E0000
ori $s0, $s0, 0x4F3C     # $s0 = 0x6D5E4F3C
DLCD Question Bank – Page 9

--- [Page 10 of 24] ---
4. Programming (MIPS)
Q1. [5 Marks]  Explain the branch and jump instructions beq, bne, j, jr and jal.
Answer (5 points):
1.
beq rs, rt, label branches to the label if the two registers are equal; otherwise execution 
continues sequentially (a label ends with a colon).
2.
bne rs, rt, label branches only if the registers are not equal.
3.
j label is an unconditional jump; the instructions in between are skipped (used for loops and 
skipping blocks).
4.
jr rs (R-type) jumps to the address held in a register, decided at run time; used for returns (jr 
$ra).
5.
jal label jumps to a function and saves the return address (PC+4) in $ra; e.g. jal at 
0x00400200 gives $ra = 0x00400204.
Q2. [5 Marks]  How are multiplication, division and 32-bit constants handled in MIPS? Give 
examples.
Answer (5 points):
1.
Multiplying two 32-bit numbers gives a 64-bit product stored in HI (upper 32 bits) and LO 
(lower 32 bits): mult $s0,$s1.
2.
For div $s0,$s1, LO holds the quotient and HI holds the remainder.
3.
Results are moved to general registers using mflo and mfhi; mul $s1,$s2,$s3 gives a 32-bit 
result directly.
4.
Example: $s0 = 20, $s1 = 6 → div gives mflo $t0 = 3 (quotient) and mfhi $t1 = 2 (remainder).
5.
A 32-bit constant needs lui followed by ori (addi handles only 16 bits).
# int a = 0x6D5E4F3C;
lui $s0, 0x6D5E
ori $s0, $s0, 0x4F3C
Q3. [8 Marks]  Explain how if and if/else statements are implemented in MIPS. Why is the 
opposite condition tested?
Answer (8 points):
1.
An if statement executes a block only when the condition is true; it is implemented using a 
conditional branch and labels.
2.
Example: if (i == j) f = g + h; f = f – i;
bne $s3, $s4, L1     # skip if i != j
add $s0, $s1, $s2    # f = g + h
L1: sub $s0, $s0, $s3 # f = f - i
3.
If i != j the branch is taken to L1 and the if-block is skipped; if i == j it is not taken and f = g + h 
executes.
4.
Opposite condition: the assembly tests the opposite so that control can skip the block when 
the condition is false, giving simpler and more efficient code.
5.
An if/else statement needs a conditional branch to choose the block and an unconditional 
jump to skip the other block.
6.
Example: if (i == j) f = g + h; else f = f – i;
bne $s3, $s4, L1
add $s0, $s1, $s2
j   done              # skip else
L1: sub $s0, $s0, $s3
done:
7.
If i == j the if-block runs and j done skips the else block; if i != j control goes to L1; both paths 
continue at done.
DLCD Question Bank – Page 10

--- [Page 11 of 24] ---
8.
A switch/case is implemented as a series of conditional tests (nested if/else) with a default 
block.
Q4. [8 Marks]  Explain arrays in MIPS: address calculation, loop access and byte 
(character) arrays.
Answer (8 points):
1.
An array stores same-type elements in sequential memory; index starts at 0 and array[0] is at 
the base address.
2.
For an int array: Address of array[i] = Base + 4i (each element is 4 bytes).
3.
Example: with base 0x10007000, array[1] = 0x10007004 and array[2] = 0x10007008.
4.
The base is loaded with lui $s0,0x1000; ori $s0,$s0,0x7000, then elements are accessed 
as lw $t1, 4($s0).
5.
For a large array a loop computes the address: i×4 is obtained with sll by 2.
# array[i] = array[i] * 8 ; $s0=base, $s1=i
sll $t0, $s1, 2      # i*4
add $t0, $t0, $s0    # address of array[i]
lw  $t1, 0($t0)
sll $t1, $t1, 3      # x 8
sw  $t1, 0($t0)
6.
Byte arrays store characters in one byte: lb (sign-extend), lbu (zero-extend) and sb (store 
least significant byte).
7.
For a byte array, Address of chararray[i] = Base + i (offset i, not 4i).
8.
Lowercase → uppercase: subtract 32 (0x20) since 'a' = 0x61 and 'A' = 0x41.
addi $s1,$0,0 ; addi $t0,$0,10
loop: beq $t0,$s1,done
      add  $t1,$s1,$s0
      lb   $t2,0($t1)
      addi $t2,$t2,-32
      sb   $t2,0($t1)
      addi $s1,$s1,1
      j    loop
done:
Q5. [10 Marks]  Explain the implementation of while and for loops in MIPS with examples, 
and the use of slt for magnitude comparison.
Answer (10 points):
1.
A while loop repeats a block while the condition is true; the condition is tested before every 
iteration.
2.
In MIPS a conditional branch exits the loop and an unconditional jump repeats it.
# while (pow != 128) { pow = pow*2; x = x+1; }
while: beq $s0, $t0, done   # $t0=128
       sll $s0, $s0, 1      # pow = pow*2
       addi $s1, $s1, 1     # x++
       j   while
done:
3.
The C test is pow != 128, but the assembly tests the opposite (pow == 128) to leave the loop.
4.
A for loop has initialisation, condition, statement and update; flow: Initialization → Condition 
→ Statement → Update → Condition … → Exit.
5.
Example: for (i = 0; i != 10; i++) sum = sum + i;
addi $s1,$0,0       # sum = 0
add  $s0,$0,$0      # i = 0
addi $t0,$0,10      # limit
for: beq $s0,$t0,done
     add  $s1,$s1,$s0
     addi $s0,$s0,1
DLCD Question Bank – Page 11

--- [Page 12 of 24] ---
j    for
done:
6.
The loop exits when i == 10 and the final value is sum = 0+1+…+9 = 45.
7.
slt $t1,$s0,$s1 sets $t1 = 1 if $s0 < $s1, else 0 (e.g. 5 < 8 gives 1); beq/bne only test 
equality.
8.
slt combined with beq or bne implements <, >, ≤ and ≥ conditions.
9.
Example: for (i = 1; i < 101; i = i*2) sum = sum + i;
addi $s1,$0,0 ; addi $s0,$0,1 ; addi $t0,$0,101
loop: slt $t1,$s0,$t0    # i < 101 ?
      beq $t1,$0,done    # exit if i >= 101
      add $s1,$s1,$s0
      sll $s0,$s0,1      # i = i*2
      j   loop
done:
10. The values added are 1+2+4+8+16+32+64 = 127.
Q6. [10 Marks]  Explain function calls in MIPS – arguments, return values, the stack, 
preserved registers – with diffofsums, and extend it to recursive factorial.
Answer (10 points):
1.
A function receives arguments in $a0–$a3 and returns its result in $v0–$v1; more than four 
arguments go on the stack.
2.
The caller uses jal (saves PC+4 in $ra) and the callee returns with jr $ra.
3.
diffofsums(f,g,h,i) = (f+g)–(h+i) – caller code:
addi $a0,$0,2 ; addi $a1,$0,3 ; addi $a2,$0,4 ; addi $a3,$0,5
jal  diffofsums
add  $s0,$v0,$0        # result
4.
Callee code (saving only $s0 – a 4-byte frame):
diffofsums:
  addi $sp,$sp,-4
  sw   $s0,0($sp)
  add  $t0,$a0,$a1
  add  $t1,$a2,$a3
  sub  $s0,$t0,$t1
  add  $v0,$s0,$0
  lw   $s0,0($sp)
  addi $sp,$sp,4
  jr   $ra
5.
Result: (2+3) – (4+5) = 5 – 9 = –4 returned in $v0.
6.
The stack is a LIFO structure that grows toward lower addresses; $sp points to the top (addi 
$sp,$sp,-8 changes 0x7FFFFFFC to 0x7FFFFFF4).
7.
Steps: allocate stack space, store registers, execute, restore registers, deallocate space; the 
allocated space is the stack frame.
8.
Preserved: $s0–$s7, $ra, $sp (callee must save/restore); nonpreserved: $t0–$t9, $a0–$a3, 
$v0–$v1.
9.
A recursive function is a nonleaf function that calls itself; each call needs its own frame to 
preserve $a0 and $ra (8 bytes).
10. factorial(n) = n × factorial(n–1), base case factorial(1) = 1; for n = 3 the calls go 3→2→1 
and returns give 1 → 2 → 6.
factorial:
  addi $sp,$sp,-8
  sw $a0,4($sp) ; sw $ra,0($sp)
  addi $t0,$0,2
  slt  $t0,$a0,$t0
  beq  $t0,$0,else
DLCD Question Bank – Page 12

--- [Page 13 of 24] ---
addi $v0,$0,1
  addi $sp,$sp,8
  jr   $ra
else: addi $a0,$a0,-1
  jal  factorial
  lw $ra,0($sp) ; lw $a0,4($sp)
  addi $sp,$sp,8
  mul  $v0,$a0,$v0
  jr   $ra
DLCD Question Bank – Page 13

--- [Page 14 of 24] ---
5. Addressing Modes
Q1. [5 Marks]  What is an addressing mode? Why are addressing modes important? List 
the MIPS addressing modes.
Answer (5 points):
1.
An addressing mode specifies how the CPU locates the operand(s) needed to execute an 
instruction.
2.
Operands may be in registers, memory locations, or inside the instruction itself.
3.
Addressing modes determine where operands are located and influence execution speed 
and memory usage.
4.
They give flexibility for constants, variables, arrays, loops and function calls, and reduce 
instruction size.
5.
MIPS modes: register-only, immediate, base, PC-relative and pseudo-direct.
Q2. [5 Marks]  Explain register-only and immediate addressing with examples.
Answer (5 points):
1.
Register-only: all source and destination operands are CPU registers; used by all R-type 
instructions.
2.
No memory access is needed, so it is the fastest addressing mode; e.g. add $s0,$t2,$t3 → 
$s0 = $t2 + $t3.
3.
Register $0 is hard-wired to 0, so sub $t8,$s1,$0 copies $s1 into $t8.
4.
Immediate: a 16-bit constant is encoded in the instruction along with a register operand; 
used by I-type instructions addi, ori, andi, lui.
5.
No memory access is required for the constant; e.g. addi $s4,$t5,-73 → $s4 = $t5 – 73 and 
ori $t3,$t7,0xFF → $t3 = $t7 OR 0x00FF.
Q3. [8 Marks]  Explain base addressing with the effective address formula and examples.
Answer (8 points):
1.
Base addressing is used to access data in memory.
2.
It is used by the lw and sw instructions.
3.
Effective Address = Base Register + Sign-Extended 16-bit Offset.
4.
The processor first computes the effective address and then reads (lw) or writes (sw) 
memory.
5.
The offset may be positive or negative, so locations before or after the base can be 
accessed.
6.
lw $s4, 72($0): EA = $0 + 72 = 72; the word at address 72 is loaded into $s4.
7.
sw $t2, -25($t1): EA = $t1 – 25; the contents of $t2 are stored there.
8.
Applications: arrays, stack frames, structures and dynamically allocated memory, all using 
one instruction format.
Q4. [8 Marks]  Explain PC-relative addressing with the branch target formula. Compute the 
offset for beq $t0,$0,else at 0x10 when else is at 0x20.
Answer (8 points):
1.
PC-relative addressing is used by the conditional branches beq and bne.
2.
The instruction stores a 16-bit signed offset relative to the PC instead of the full destination 
address.
3.
BTA = (PC + 4) + (Sign-Extended Offset × 4).
4.
Advantage: shorter instruction and both forward and backward branches are possible.
5.
In the example, beq is at PC = 0x10, so PC + 4 = 0x14 and the target else = 0x20.
6.
Distance = (0x20 – 0x14)/4 = 3 instructions, so the immediate is 3.
7.
Encoding: op = 4 (beq), rs = $t0 = 8, rt = $0 = 0, imm = 3 → beq $t0,$0,3.
DLCD Question Bank – Page 14

--- [Page 15 of 24] ---
8.
The immediate stores the number of instructions to skip; hardware sign-extends it, 
multiplies by 4 and adds it to PC+4 (0x14 + 12 = 0x20).
Q5. [10 Marks]  Explain pseudo-direct addressing used by j and jal. Derive the target 
address and machine code for j sum located at 0x0040005C with sum at 0x004000A0.
Answer (10 points):
1.
Pseudo-direct addressing is used by the jump instructions j and jal.
2.
They are J-type and hold only a 26-bit address field instead of the full 32-bit target.
3.
JTA = { (PC+4)[31:28], Address[25:0], 00 }.
4.
It is called pseudo-direct because only part of the destination address is stored in the 
instruction.
5.
Jumps are possible anywhere within the same 256 MB region (same upper 4 bits of PC+4).
6.
Example: the JTA is 0x004000A0.
JTA = 0000 0000 0100 0000 0000 0000 1010 0000
7.
Dropping the last two bits (shift right by 2) gives the 26-bit field 0x0100028.
8.
The opcode for j is 000010.
9.
Machine code = 000010 | 00000100000000000000101000 = 0x08100028.
0000 1000 0001 0000 0000 0000 0010 1000 = 0x08100028
10. Why shift by 2: every instruction is 4 bytes and word-aligned so the last two address bits are 
always 00; they are omitted and restored by hardware. Unlike PC-relative, an address part 
(not an offset) is stored.
Q6. [10 Marks]  Compare the five MIPS addressing modes with the instruction types that 
use them, formulas and examples.
Answer (10 points):
1.
Register-only: operands are in registers; used by R-type instructions.
2.
It is the fastest mode and needs no memory access; e.g. add $s0,$t2,$t3.
3.
Immediate: one operand is a 16-bit constant in the instruction; used by addi, ori, andi, lui.
4.
It avoids fetching the constant from memory; e.g. addi $s0,$s0,10.
5.
Base: operand is in memory; used by lw and sw; EA = Base + SignExt(offset).
6.
It is ideal for arrays, stack frames and structures; e.g. lw $t0, 8($sp).
7.
PC-relative: used by beq and bne; BTA = (PC+4) + (offset × 4).
8.
It keeps branches short and allows forward and backward branching; e.g. beq $t0,$0,Loop.
9.
Pseudo-direct: used by j and jal; JTA = {(PC+4)[31:28], addr26, 00}.
10. It reaches any address within the same 256 MB region using only 26 bits; e.g. j main.
Mode
Used by
Formula / operand
Register-only
R-type
registers
Immediate
addi, ori, andi, lui
constant in instruction
Base
lw, sw
EA = Base + offset
PC-relative
beq, bne
PC+4 + offset×4
Pseudo-direct
j, jal
{(PC+4)[31:28], addr, 00}
DLCD Question Bank – Page 15

--- [Page 16 of 24] ---
6. Parallelism
Q1. [5 Marks]  Define latency and throughput. Calculate both for Ben baking cookies 
(rolling 5 min, baking 15 min, no overlap).
Answer (5 points):
1.
Latency is the time required for one task (token) to travel from input to output.
2.
Throughput is the number of tasks completed per unit time.
3.
For a non-parallel system, Throughput = 1 / Latency.
4.
Cookie latency = 5 + 15 = 20 minutes per tray.
5.
Cookie throughput = 60 / 20 = 3 trays per hour, because tasks do not overlap.
Q2. [5 Marks]  Differentiate spatial parallelism and temporal parallelism.
Answer (5 points):
1.
Spatial parallelism improves performance by adding multiple copies of hardware, each 
doing a different task simultaneously.
2.
Temporal parallelism (pipelining) divides a task into stages so that different tasks occupy 
different stages at the same time, like an assembly line.
3.
Examples: spatial – multiple processors, ALUs, multicore CPUs; temporal – Fetch → 
Decode → Execute → Memory → Write back.
4.
Cost: spatial has higher hardware cost; temporal reuses the same hardware and is more 
cost-effective.
5.
Throughput: N units give N/L in spatial parallelism and N equal stages give about N/L in 
temporal parallelism.
Point
Spatial
Temporal
Idea
Duplicate hardware
Overlap stages
Cost
High
Lower
Example
Multicore
Pipelining
Q3. [8 Marks]  Solve the cookie parallelism problem for spatial, temporal and combined 
parallelism, giving latency and throughput.
Answer (8 points):
1.
Base case: latency 20 min and throughput 3 trays/hour (no overlap).
2.
Spatial: Alyssa helps and both bake simultaneously.
3.
Spatial throughput = 3 + 3 = 6 trays/hour.
4.
Temporal: Ben buys a second tray and prepares tray 2 while tray 1 bakes.
5.
One tray enters the oven every 15 min, so temporal throughput = 60/15 = 4 trays/hour.
6.
Spatial + temporal: two people with two trays give 8 trays/hour.
7.
In all three cases latency stays 20 minutes.
8.
Conclusion: parallelism improves throughput but does not reduce latency.
Q4. [8 Marks]  What are pipeline hazards? Explain their types and the limitations of 
pipelining.
Answer (8 points):
1.
Pipeline hazards are conditions that prevent instructions from flowing smoothly through the 
pipeline.
2.
They introduce stalls (bubbles) that reduce throughput.
3.
Data hazard: an instruction needs data still being produced by an earlier instruction and 
must wait.
DLCD Question Bank – Page 16

--- [Page 17 of 24] ---
4.
Control hazard: caused by branch/jump; wrong instructions may be fetched until the branch 
decision is known.
5.
Structural hazard: two instructions need the same hardware resource at the same time.
6.
Limitation: pipeline registers and control logic add complexity.
7.
Limitation: unequal stages reduce efficiency because the longest stage sets the clock 
period.
8.
Limitation: spatial parallelism needs additional hardware, and hazards reduce performance.
Q5. [10 Marks]  A circuit has clock-to-Q delay 0.3 ns, logic blocks of 3, 2 and 4 ns and 
setup time 0.2 ns. Find cycle time, latency and throughput without pipelining and with a 
two-stage pipeline. Also solve a three-stage pipeline with stage delays 3.5, 2.5 and 4.5 ns.
Answer (10 points):
1.
Without pipeline: Tc = 0.3 + 3 + 2 + 4 + 0.2 = 9.5 ns.
2.
Latency = 9.5 ns.
3.
Throughput = 1/9.5 ns ≈ 105 MHz.
4.
Two-stage pipeline (register after block 2): Stage 1 = 0.3 + 3 + 2 + 0.2 = 5.5 ns.
5.
Stage 2 = 0.3 + 4 + 0.2 = 4.5 ns.
6.
The clock must suit the slowest stage, so Tc = max(5.5, 4.5) = 5.5 ns.
7.
Throughput = 1/5.5 ns ≈ 182 MHz.
8.
Latency = 2 × 5.5 = 11 ns – about the same, so pipelining raises throughput, not latency.
9.
Three-stage pipeline (3.5, 2.5, 4.5 ns): Tc = max = 4.5 ns; latency = 3 × 4.5 = 13.5 ns.
Tc = max(3.5, 2.5, 4.5) = 4.5 ns
Latency = 3 x Tc = 13.5 ns
10. Throughput = 1/4.5 ns ≈ 222 MHz; pipeline registers isolate consecutive stages so tokens do 
not interfere.
Q6. [10 Marks]  Explain the need for parallelism and its mathematical model. Discuss its 
advantages, limitations and applications.
Answer (10 points):
1.
Need: raising clock frequency increases power consumption and heat, so performance must 
come from doing more work at once.
2.
Definition: parallelism is the simultaneous execution of multiple tasks to increase the work 
completed in a given period (like two chefs in a kitchen).
3.
Without parallelism: Throughput = 1/L for a task of latency L.
4.
Spatial parallelism with N hardware units: Throughput = N/L.
5.
Temporal parallelism with N equal stages: Throughput = N/L.
6.
Unequal stages: the longest stage latency L1 decides speed, Throughput = 1/L1, so more 
stages help only if the work is balanced.
Case
Throughput
No parallelism
1 / L
Spatial (N units)
N / L
Temporal (N equal stages)
N / L
Unequal stages
1 / L1
7.
Advantages: higher throughput, better hardware utilisation, higher clock frequency and no 
duplicate hardware for pipelining.
8.
Limitations: extra hardware (spatial), pipeline registers/control complexity, unequal stages, 
and data/control hazards.
9.
Applications: multicore processors, GPUs, supercomputers, DSPs and machine-learning 
accelerators.
DLCD Question Bank – Page 17

--- [Page 18 of 24] ---
10. Modern processors combine spatial and temporal parallelism; parallelism mainly improves 
throughput while latency often stays unchanged.
DLCD Question Bank – Page 18

--- [Page 19 of 24] ---
7. Sequential Building Blocks (Counters and Shift Registers)
Q1. [5 Marks]  Explain the N-bit binary counter. How many states does it have? Show the 
3-bit sequence.
Answer (5 points):
1.
An N-bit binary counter is a sequential circuit with a clock input, a reset input and an N-bit 
output Q.
2.
It is built from an adder (adds 1) and a resettable register.
3.
Reset sets Q = 0; after reset is released, Q becomes Q + 1 on every rising clock edge and 
wraps to 0 after the maximum.
4.
An N-bit counter has 2^N states (0 to 2^N – 1); an 8-bit counter counts 0 to 255.
5.
3-bit sequence: 000 → 001 → 010 → 011 → 100 → 101 → 110 → 111 → 000; counters are 
used for timing, event counting and frequency division.
000 -> 001 -> 010 -> 011 -> 100 -> 101 -> 110 -> 111 -> 000
Q2. [5 Marks]  Differentiate asynchronous (ripple) and synchronous counters.
Answer (5 points):
1.
Clocking: in an asynchronous counter only the first flip-flop gets the main clock and each 
next one is clocked by the previous output; a synchronous counter uses one common clock 
for all flip-flops.
2.
Output change: asynchronous outputs change one after another (ripple); synchronous 
outputs change in parallel.
3.
Delay: asynchronous has cumulative propagation delay; synchronous has none.
4.
Speed: synchronous counters work at higher frequencies; asynchronous ones are slower.
5.
Other names and design: asynchronous = serial/ripple counter and is simple; synchronous 
= parallel counter and needs extra combinational logic.
Q3. [8 Marks]  Explain the working of a 4-bit asynchronous ripple counter with its count 
table. Describe the decade counter.
Answer (8 points):
1.
In a ripple counter only the first flip-flop gets the clock; the output of each flip-flop clocks 
the next.
2.
Q0 toggles on every clock pulse.
3.
Q1 toggles every 2 pulses, Q2 every 4 and Q3 every 8, giving the binary sequence 0 to 
15.
4.
Each stage divides frequency by 2 (Q0 = f/2, Q1 = f/4); one FF is a MOD-2 and two FFs form 
a MOD-4 counter.
5.
Count table: reset 0000, pulse 1 → 0001, 2 → 0010, 7 → 0111, 8 → 1000, 15 → 1111 and 
pulse 16 wraps to 0000.
Clock
Q3 Q2 Q1 Q0
Decimal
Reset
0000
0
1
0001
1
2
0010
2
7
0111
7
8
1000
8
15
1111
15
16
0000
0 (wraps)
6.
The 4-bit ripple counter has 16 states (MOD-16).
DLCD Question Bank – Page 19

--- [Page 20 of 24] ---
7.
Decade counter: counts ten states (0–9) and then resets.
8.
A NAND gate on Q3 and Q1 (binary 1010 = 10) drives the clear input, so the counter resets 
at 10 and restarts from 0.
Q4. [8 Marks]  Explain ring counter and Johnson counter with their sequences. Compare 
them.
Answer (8 points):
1.
A ring counter is a shift-register counter whose last flip-flop output is fed back to the first.
2.
A single 1 circulates: 1000 → 0100 → 0010 → 0001 → 1000; n flip-flops give n states (MOD-
n).
3.
It must be initialised with a single 1; 0000 is an invalid/stuck state.
4.
Ring counters are simple and fast and give decoded outputs directly, but need n flip-flops for 
n states; used for timing, sequence generation and stepper motor control.
5.
A Johnson (twisted-ring/switch-tail) counter feeds the complement of the last flip-flop 
back to the first (D0 = Q3').
6.
4-bit sequence: 0000 → 1000 → 1100 → 1110 → 1111 → 0111 → 0011 → 0001 → 0000.
7.
For n flip-flops a Johnson counter has 2n states (8 states for 4 bits).
8.
Comparison: ring – n states, direct decoding; Johnson – 2n states for the same number of 
flip-flops, needs simple decoding.
Point
Ring
Johnson
Feedback
Q of last FF
Q' of last FF
States (n FFs)
n
2n
Q5. [10 Marks]  Explain the shift register, shift register with parallel load and its HDL. 
Describe scan chains and how a 32-bit counter is tested in 65 cycles.
Answer (10 points):
1.
A shift register is a chain of N flip-flops sharing one clock.
2.
Each flip-flop's output feeds the next flip-flop's input; a reset may clear all of them.
3.
On each clock edge a new bit enters at Sin and every stored bit moves forward; the oldest bit 
leaves at Sout.
4.
After N cycles the N bits are available on the parallel outputs, so it converts serial to 
parallel.
5.
Parallel load: a D input and a Load control with a mux before each flip-flop; Load = 1 loads 
D in one cycle, Load = 0 shifts normally.
6.
HDL: reset has highest priority, then load, otherwise shift.
always @(posedge clk or posedge rst)
  if (rst)       q <= 0;
  else if (load) q <= data_in;
  else           q <= {q[N-2:0], sin};
assign sout = q[N-1];
7.
Testing problem: sequential circuits depend on internal state; checking bit 31 of a 32-bit 
counter would need ~2 billion clocks and there are too many flip-flops for individual test pins.
8.
Scan chain: all flip-flops are connected into one long shift register using scannable flip-
flops (a mux built into each FF).
9.
In normal mode each FF loads from its regular D input; in test mode data is shifted serially 
in/out so internal state can be set or read.
10. 32-bit counter test: shift in 0111…1 (32 cycles), run 1 normal clock (1 cycle), shift out and 
check 1000…0 (32 cycles) – total 65 cycles.
32 (shift in) + 1 (count) + 32 (shift out) = 65 cycles
DLCD Question Bank – Page 20

--- [Page 21 of 24] ---
Q6. [10 Marks]  Design a 3-bit synchronous up counter using T flip-flops and a 2-bit 
synchronous up counter using JK flip-flops. Also design the 32-bit counters of Exercises 
5.43 and 5.44.
Answer (10 points):
1.
Design steps: decide the number of flip-flops, write the excitation table, draw the state 
diagram and circuit excitation table, solve using K-maps, draw the logic diagram.
2.
T flip-flop excitation: Qn→Qn+1: 0→0: T=0; 0→1: T=1; 1→0: T=1; 1→1: T=0 (T=1 toggles 
the FF).
3.
3-bit up counter uses 3 T flip-flops with one common clock and states 000→001→…
→111→000.
4.
K-maps give T0 = 1, T1 = Q0, T2 = Q1·Q0.
T0 = 1
T1 = Q0
T2 = Q1 . Q0
5.
A bit toggles only when all lower bits are 1.
6.
2-bit up counter with JK FFs uses 2 flip-flops and the JK excitation table.
7.
K-maps give J0 = K0 = 1 and J1 = K1 = Q0.
J0 = K0 = 1
J1 = K1 = Q0
8.
Exercise 5.43 (32-bit up/down counter): Q+ = 0 if Reset, Q+1 if Up = 1, Q–1 if Up = 0; use 
a 32-bit register, adder/subtractor and mux controlled by Up.
9.
Exercise 5.44 (adds 4 each clock): Q+ = Q + 4 with Reset → 0; use a 32-bit register, a 32-
bit adder and constant 4.
10. In both exercises Reset is synchronous – it overrides the next-state value at the clock 
edge.
DLCD Question Bank – Page 21

--- [Page 22 of 24] ---
8. Memory Arrays
Q1. [5 Marks]  Explain the organisation of a memory array. Find the size of a memory with 
10 address bits and 32-bit data.
Answer (5 points):
1.
A memory array is a 2-D array of 1-bit cells; each row is a word and each column is a bit.
2.
N address bits select one of 2^N words, each of M bits, so size = 2^N × M bits.
3.
Each bit cell connects to a wordline (selects the row) and a bitline (carries data).
4.
A decoder asserts one wordline for each address; memories are specified by size and by 
number/type of ports.
5.
Example: 10 address bits and 32-bit data → 2^10 = 1024 words → 1024 × 32 = 32 Kb.
N = 10 -> 2^10 = 1024 words
Size = 1024 x 32 = 32768 bits = 32 Kb
Q2. [5 Marks]  Differentiate RAM and ROM.
Answer (5 points):
1.
Full form: RAM = Random Access Memory; ROM = Read Only Memory.
2.
Volatility: RAM is volatile (loses data when power is off); ROM is nonvolatile.
3.
Operations: RAM is read/write memory; ROM is historically read-only (modern ROMs can 
be written in various ways).
4.
Types: RAM – DRAM and SRAM; ROM – Mask ROM, PROM, EPROM, EEPROM and 
Flash.
5.
Access: both can be accessed randomly.
Q3. [8 Marks]  Compare DRAM, SRAM and flip-flop memories. Why is DRAM slower? 
Explain SDRAM and DDR SDRAM.
Answer (8 points):
1.
DRAM stores each bit as charge on a capacitor (about 1 transistor per bit), so it is very 
dense.
2.
DRAM charge leaks, so periodic refresh is needed, and a read destroys the value so it is 
restored.
3.
SRAM stores a bit in cross-coupled inverters; no refresh is needed and noise is corrected.
4.
Area: flip-flop ≈ 20 transistors/bit, SRAM = 6, DRAM = 1.
5.
Latency: flip-flop fastest, SRAM medium, DRAM slowest.
Memory
Transistors/bit
Latency
Flip-flop
~20
Fast
SRAM
6
Medium
DRAM
1
Slow
6.
Why DRAM is slower: charge moves from the capacitor to a bitline that is not actively 
driven, and refresh lowers throughput.
7.
SDRAM (Synchronous DRAM) uses a clock and pipelines memory accesses.
8.
DDR SDRAM transfers data on both rising and falling clock edges, doubling throughput for a 
given clock speed.
Q4. [8 Marks]  Explain the register file with the 32 × 32 three-ported example.
Answer (8 points):
1.
A register file is a group of registers storing temporary variables in a digital system.
2.
It is usually a small multi-ported SRAM array, more compact than flip-flop registers.
DLCD Question Bank – Page 22

--- [Page 23 of 24] ---
3.
The 32 × 32 register file has 32 registers of 32 bits each.
4.
It has two read ports (A1 → RD1, A2 → RD2).
5.
It has one write port (A3, WD3), controlled by CLK and the write enable.
6.
Each address is 5 bits because 2^5 = 32.
7.
Two registers can be read and one written in the same cycle (e.g. two source registers 
and one destination of an instruction).
8.
Total storage = 32 × 32 = 1024 bits.
Q5. [10 Marks]  Explain ROM: bit-cell working, dot notation and the types of ROM (Mask, 
PROM, EPROM, EEPROM, Flash). Why is ROM nonvolatile?
Answer (10 points):
1.
A ROM stores each bit by the presence or absence of a transistor.
2.
The bitline is weakly pulled HIGH and the wordline is turned ON.
3.
If a transistor is present it pulls the bitline LOW, so the stored bit is 0; if absent the bitline 
stays HIGH and the bit is 1.
4.
ROM is nonvolatile because its bit cell is combinational and has no state that is lost when 
power is removed.
5.
Dot notation: rows are wordlines (addresses), columns are bitlines; a dot at an intersection 
means stored 1 (e.g. a 4×3 ROM stores 12 bits).
6.
Mask ROM: contents fixed during manufacturing; cannot be changed.
7.
PROM: transistors initially present; programming blows fuses with high voltage, so it is one-
time programmable.
8.
EPROM: uses a floating-gate transistor; programmed with high voltage and erased with 
intense UV light.
9.
EEPROM: programmed and erased electrically, individual cells can be erased.
10. Flash: like EEPROM but erases larger blocks, needing fewer erase circuits and so cheaper.
Type
Programmable
Erasable
Method
Mask ROM
At manufacture
No
—
PROM
Once
No
—
EPROM
Yes
Yes
UV light
EEPROM
Yes
Yes
Electrical
Flash
Yes
Yes
Electrical, block-wise
Q6. [10 Marks]  Explain how memory arrays implement combinational logic (LUT). 
Implement Y = AB using a LUT and explain the RAM and ROM HDL descriptions.
Answer (10 points):
1.
A 2^N-word × M-bit memory can implement any combinational function with N inputs and 
M outputs.
2.
The N inputs form the address; the data stored in the selected row gives the M outputs.
3.
The size of the memory is 2^N × M; the contents are the truth table.
4.
A ROM can be seen as two-level logic: the address passes through a decoder (AND gates 
giving all minterms) and then OR gates.
5.
A memory array used to perform logic is called a Lookup Table (LUT).
6.
Y = AB needs a 4 × 1 memory because there are 2^2 = 4 input combinations; it stores 0, 0, 
0, 1.
A
B
Address
Y = AB
0
0
00
0
0
1
01
0
DLCD Question Bank – Page 23

--- [Page 24 of 24] ---
A
B
Address
Y = AB
1
0
10
0
1
1
11
1
7.
RAM HDL: a 2^N × M RAM is declared as an array of M-bit words (N = 6, M = 32 gives 64 × 
32).
logic [M-1:0] mem [2**N-1:0];
8.
RAM write is synchronous: it occurs on the rising clock edge when we = 1 (mem[adr] <= 
din).
9.
RAM read is immediate/asynchronous (assign dout = mem[adr]); RAM contents are 
unpredictable at power-up.
10. ROM HDL: contents are fixed using a case statement on the address.
always_comb case(adr)
  2'b00: dout <= 3'b011;  2'b01: dout <= 3'b110;
  2'b10: dout <= 3'b100;  2'b11: dout <= 3'b010;
endcase
DLCD Question Bank – Page 24

```

---

<a id="doc-13"></a>
## Document 13: Comprehensive Descriptive Question Bank (14 Pages)
**Source Document**: `resources/u3/QB/3.1.1_QB.pdf`
**OCR Extraction File**: `U3_QB_3.1.1_QB.txt`

```
================================================================================
ORIGINAL DOCUMENT : 3.1.1_QB.pdf
OCR PDF FILE      : U3_QB_3.1.1_QB_ocr.pdf
TOTAL PAGES       : 14
WORD COUNT        : 5177
CHARACTER COUNT   : 32638
DATE EXTRACTED    : 2026-11-04 14:04:42
================================================================================

--- [Page 1 of 14] ---
DIGITAL LOGIC & COMPUTER DESIGN
DETAILED QUESTION BANK
5 MARKS • 8 MARKS • 10 MARKS
8 Uploaded PPTs • Exam-Oriented Answers + Numericals
Each PPT contains 2 × 5-mark, 2 × 8-mark and 2 × 10-mark questions. Answers are expanded according to marks
and include numerical problems where supported by the slides.
PPT
5M
8M
10M
1. Introduction
2
2
2
2. Assembly Language
2
2
2
3. Machine Language
2
2
2
4. Programming
2
2
2
5. Addressing Modes
2
2
2
6. Parallelism
2
2
2
7. Memory Arrays
2
2
2
8. Sequential Building Blocks
2
2
2

--- [Page 2 of 14] ---
1. Introduction
Q1. [5 Marks] Define Computer Architecture and explain what it specifies.
Answer:
Computer Architecture is the programmer's view of a computer. It describes the interface through which software
communicates with hardware.
The PPT identifies the following major specifications:
1. Instruction Set Architecture (ISA) – the instructions understood by the processor.
2. Operand locations – where operands are stored, such as registers and memory.
3. Data representation – how data values are represented.
4. Instruction formats – how instructions are organized/encoded.
Thus, architecture provides the interface that determines how a program is executed by the processor.
Q2. [5 Marks] Why is Computer Architecture studied? Explain its importance.
Answer:
Computer Architecture is important because it:
1. Bridges the gap between hardware and software.
2. Explains how programs are executed by a processor.
3. Helps in designing efficient and high-performance computer systems.
4. Helps maintain compatibility between software and hardware.
5. Provides a foundation for understanding processor organization and programming.
Therefore, it connects what a programmer writes with what the hardware actually executes.
Q3. [8 Marks] Explain Instruction Set Architecture (ISA) and the idea that instruction sets are like
computer 'dialects'.
Answer:
Instruction Set Architecture is the programmer-visible interface of a processor. It defines the operations/instructions that
the processor understands, operand locations, data representation and instruction formats.
The PPT points out that many architectures exist, such as x86, MIPS, SPARC and PowerPC. Each architecture defines
its own instruction set.
Instruction sets can be compared to different dialects of a language: the basic purpose is similar, but the exact words
and rules differ. Once one instruction set is understood, learning another is easier because many basic
operations—such as addition, subtraction and jumps—are common in concept.
Hence, ISA is the key boundary between software and processor hardware.
Q4. [8 Marks] Explain the role of instructions in the execution of computer programs.
Answer:
Instructions are the basic words of a computer's language. Even complex applications are ultimately translated into
simple machine-level operations.
The execution process can be understood as:
1. A programmer writes an application.
2. The program is translated/compiled into instructions supported by the target architecture.
3. The processor fetches and interprets these instructions.
4. Instructions perform operations such as arithmetic, logical operations, memory access and control flow.
5. The processor updates registers/memory and continues with the next instruction.
Thus, instructions provide the mechanism through which software controls the hardware.
Q5. [10 Marks] Explain the major layers from software to hardware and how Computer Architecture
connects them.
Answer:
A computer system can be viewed as a set of layers. At the top is application software, which expresses the user's task.
The operating system manages resources and provides services. Computer architecture provides the
programmer-visible interface, including the ISA, operand locations, data representation and instruction formats. Below
architecture are lower hardware implementation levels such as microarchitecture, logic and digital circuits.
Computer architecture is therefore the important boundary between software and hardware. A program does not directly
manipulate transistors; instead, it uses the instructions and data conventions defined by the architecture. The

--- [Page 3 of 14] ---
processor's implementation then carries out those instructions.
This layered view is useful because it separates what software expects from how the hardware implements it. Different
architectures can implement similar software goals using different instruction sets and hardware organizations.
Q6. [10 Marks] Discuss why many computer architectures exist and compare their instruction-set
concept using examples from the PPT.
Answer:
Different architectures exist because processors can be designed with different instruction sets and design goals. The
PPT gives examples including x86, MIPS, SPARC and PowerPC.
An architecture defines:
1. The instruction set available to programs.
2. The locations from which operands can be obtained.
3. Data representation.
4. Instruction formats.
5. The programmer-visible behavior of the processor.
For example, a program targeting MIPS uses MIPS instructions, while an x86 program uses the x86 instruction set.
Although the exact instructions differ, many basic operations have the same purpose, such as add, subtract and jump.
Therefore, architectures can be thought of as different computer-language dialects: different instruction vocabularies
and formats, but common computational concepts.
2. Assembly Language
Q1. [5 Marks] What is an operand? Explain the three operand locations in MIPS with an example.
Answer:
An operand is the data used by an instruction. The PPT identifies three operand locations in MIPS:
1. Registers – high-speed storage inside the CPU.
2. Memory – large storage for program instructions and data.
3. Constants/immediates – fixed values encoded directly in the instruction.
Example:
addi $t0, $t1, 10
Here $t0 is the destination register, $t1 is the source register, and 10 is the immediate constant.
Thus, an instruction can obtain its data from registers, memory or directly from an encoded constant.
Q2. [5 Marks] Explain immediate operands and immediate instructions in MIPS.
Answer:
An immediate operand is a constant embedded directly in an instruction. MIPS uses a 16-bit signed two's-complement
field for immediate values.
Advantages:
1. The constant is immediately available.
2. A separate memory access is not needed for a small constant.
3. It can reduce the number of instructions required.
Examples include:
addi – add an immediate constant.
andi – AND with an immediate.
ori – OR with an immediate.
xori – XOR with an immediate.
Therefore, immediate operands are useful for small fixed values.
Q3. [8 Marks] Compare registers, memory and constants/immediates as operand locations.
Answer:
Registers are high-speed storage locations inside the CPU. They are useful for frequently accessed data and
intermediate results, but their number is limited.
Memory provides much larger storage and contains program instructions and data that cannot fit in registers. However,
memory access is slower than register access.
Constants/immediates are fixed values encoded directly within an instruction. They are convenient for small constants
because the processor does not need to load them from memory.

--- [Page 4 of 14] ---
For example, addi $t0,$t1,10 uses an immediate. If a value is stored in memory, lw is used to load it into a register. If
two values are already in registers, an instruction such as add can operate directly on them.
Thus, registers emphasize speed, memory capacity, and immediates convenient constant access.
Q4. [8 Marks] Explain the role of lw and sw instructions in MIPS memory access.
Answer:
MIPS has only a limited number of registers, so program data and instructions are also stored in main memory. The
PPT emphasizes that memory is larger but slower than registers.
The two basic data-transfer instructions are:
• lw (load word): transfers a word from memory into a register.
• sw (store word): transfers a word from a register into memory.
A memory address is formed using a base address and an offset. A typical sequence is:
1. Keep the base address in a register.
2. Calculate the required effective address.
3. Use lw to bring the value into a register.
4. Perform arithmetic/logic operations on registers.
5. Use sw if the result must be written back to memory.
This is central to the MIPS load/store architecture.
Q5. [10 Marks] Explain how an arithmetic expression involving registers, constants and memory can be
implemented in MIPS.
Answer:
MIPS performs arithmetic primarily on register operands. Suppose values are needed from memory and a constant
must be added.
Step 1: Load the memory value into a register using lw.
Step 2: If another operand is already in a register, use it directly.
Step 3: Use add or sub for register-register arithmetic.
Step 4: Use addi when one operand is a suitable constant.
Step 5: Store the result using sw if it must be written to memory.
For example, the operation result = memory_value + register_value + 10 can conceptually be implemented as:
lw $t0, offset($s0)
add $t1, $t0, $s1
addi $t1, $t1, 10
sw $t1, offset2($s0)
The important principle is that memory values are moved into registers before arithmetic is performed.
Q6. [10 Marks] Explain why both registers and memory are necessary in MIPS.
Answer:
Registers and memory serve different purposes.
Registers:
• Are located inside the CPU.
• Provide very fast access.
• Hold frequently used operands, addresses and intermediate results.
• Are limited in number.
Memory:
• Has much larger capacity.
• Stores program instructions and large amounts of data.
• Is slower to access than registers.
• Is accessed using load/store instructions.
Because registers cannot contain all program data, memory is necessary for capacity. Because memory is slower,
registers are necessary for efficient execution of frequently used values.
MIPS therefore follows a register-based approach: data is brought from memory into registers with lw, processed using
arithmetic/logic instructions, and written back with sw when necessary.
3. Machine Language

--- [Page 5 of 14] ---
Q1. [5 Marks] Explain R-type, I-type and J-type instruction formats.
Answer:
MIPS instructions are 32-bit binary patterns. The three main formats are:
1. R-type – mainly register-register operations.
2. I-type – immediate operations, load/store operations and branches.
3. J-type – jump instructions.
The processor first examines the opcode and then interprets the remaining fields according to the selected format.
Q2. [5 Marks] Explain the fields of an R-type instruction.
Answer:
An R-type instruction contains:
• op – opcode; for R-type it is 000000.
• rs – first source register.
• rt – second source register.
• rd – destination register.
• shamt – shift amount; normally 0 except for shift instructions.
• funct – selects the exact operation.
For example, in add $s0,$s1,$s2, $s1 and $s2 are sources and $s0 is the destination.
Q3. [8 Marks] Explain the three MIPS instruction formats with their important fields.
Answer:
R-type:
Used mainly for register-register ALU operations. It contains rs, rt, rd, shamt and funct fields in addition to the opcode.
I-type:
Used for immediate operations, loads/stores and branches. It contains rs, rt and a 16-bit immediate/offset field.
J-type:
Used for jump instructions. It contains a 26-bit address field.
A useful decoding order is:
opcode → determine format → interpret fields → determine the final assembly instruction.
All three formats fit into the fixed 32-bit instruction size.
Q4. [8 Marks] Explain how a 32-bit MIPS machine instruction is interpreted by the processor.
Answer:
A MIPS instruction is stored in memory as a 32-bit binary pattern. The processor does not directly see the assembly
mnemonic such as add or lw. Instead, it sees bit fields.
The interpretation process is:
1. Fetch the 32-bit instruction.
2. Read the opcode.
3. Use the opcode to determine the instruction format and operation category.
4. Interpret the remaining bits as register numbers, an immediate/offset, shift amount, function code or jump address.
5. Perform the operation specified by those fields.
For example, an opcode corresponding to addi tells the processor to interpret the remaining fields as rs, rt and a 16-bit
immediate.
Q5. [10 Marks] Decode the instruction 'add $s0, $s1, $s2' and explain the function of every field.
Answer:
The instruction is an R-type instruction because it performs a register-register ALU operation.
For:
add $s0, $s1, $s2
the fields are:
• opcode = 000000, identifying R-type.
• rs = $s1, the first source register.
• rt = $s2, the second source register.
• rd = $s0, the destination register.
• shamt = 0 because add is not a shift instruction.
• funct = the function code that selects the add operation.

--- [Page 6 of 14] ---
During execution, the processor reads the values from $s1 and $s2, performs addition, and writes the result into $s0.
The important point is that assembly order and machine-field order are not identical: the destination appears first in
assembly, but is encoded in the rd field.
Q6. [10 Marks] Explain logical and shift instructions in MIPS machine language, including logical,
arithmetic and immediate shifts.
Answer:
MIPS provides logical operations such as AND, OR, XOR and NOR. These operate bit-by-bit. Logical immediate
versions include andi, ori and xori.
Shift instructions include:
• sll – shift left logical.
• srl – shift right logical.
• sra – shift right arithmetic.
The shift amount is represented by the shamt field for these R-type shift instructions.
For a left shift, zeros enter the least significant bit positions. For a logical right shift, zeros enter the most significant
positions. For an arithmetic right shift, the sign bit is copied into the most significant positions.
Thus, logical operations manipulate individual bits, while shifts move bit patterns and can preserve or change the sign
depending on the type of right shift.
4. Programming
Q1. [5 Marks] Explain MIPS arithmetic and logical instructions with examples.
Answer:
MIPS provides arithmetic instructions such as add, sub and addi.
Examples:
add $t0,$s1,$s2 → $t0 = $s1 + $s2
sub $t0,$t3,$t5 → $t0 = $t3 − $t5
addi $t0,$s3,-12 → $t0 = $s3 − 12
MIPS also provides multiplication and division instructions using the special hi and lo registers.
Logical instructions include AND, OR, XOR and NOR and operate bit-by-bit.
Q2. [5 Marks] What is the purpose of branching and conditional statements in MIPS?
Answer:
Branching changes the normal sequential flow of a program. It is required for decisions and repetition.
Conditional statements such as if and if-else are implemented using conditional branches. A branch checks a condition
and transfers control to a target label when the condition is satisfied.
Thus, branching provides control flow, while arithmetic and logical instructions perform the actual data processing.
Q3. [8 Marks] Explain the four basic logical operations in MIPS and their uses.
Answer:
MIPS provides AND, OR, XOR and NOR.
AND: operates bit-by-bit and is useful for masking selected bits. AND can force selected bits to zero.
OR: combines bits from two operands and can be used to set selected bits.
XOR: produces 1 when corresponding bits differ and can be used for bit toggling or comparison of bit patterns.
NOR: produces the complement of OR. Since $0 contains all zeros, NOT A can be implemented as A NOR $0.
The PPT also gives hexadecimal examples demonstrating the bit-by-bit results.
Q4. [8 Marks] Explain how loops are implemented using labels, updates and branch instructions.
Answer:
A loop repeatedly executes a group of instructions. In MIPS, the structure generally contains:
1. A label marking the beginning of the loop.
2. Instructions that perform the required work.
3. An update to a loop variable or counter.
4. A condition check.
5. A conditional branch back to the label when the loop must continue.

--- [Page 7 of 14] ---
For example, a counter can be incremented using addi and then compared using a branch instruction. The branch
determines whether execution returns to the loop label or continues to the next part of the program.
Thus, loops are built from ordinary instructions plus control-flow branches.
Q5. [10 Marks] Explain how an if-else statement is implemented in MIPS assembly.
Answer:
An if-else statement requires two possible paths.
General structure:
1. Evaluate the condition using registers.
2. Use a conditional branch to select the appropriate path.
3. Execute the 'then' block if the condition is true.
4. Otherwise execute the 'else' block.
5. After the selected block, jump to the common continuation point if necessary.
Conceptually:
evaluate condition
branch to ELSE if condition is false
THEN block
jump to ENDIF
ELSE:
ELSE block
ENDIF:
next statement
Labels identify branch destinations. Thus, high-level selection is converted into explicit control-flow instructions.
Q6. [10 Marks] Explain how arrays are processed in MIPS programming.
Answer:
An array occupies consecutive memory locations. To access an element, the program needs the base address of the
array and an offset corresponding to the element position.
A typical array-processing loop performs:
1. Keep the array base address in a register.
2. Maintain an index or byte offset.
3. Calculate the address of the required element.
4. Load the element using lw.
5. Perform arithmetic/logic processing in registers.
6. Store the result using sw if required.
7. Update the index/offset.
8. Branch back to the loop until the required number of elements has been processed.
For word arrays, offsets must account for the word size. Thus arrays combine memory addressing, register operations
and loops.
5. Addressing Modes
Q1. [5 Marks] What is an addressing mode? Why is it needed?
Answer:
An addressing mode specifies how the CPU locates an operand or calculates the address used by an instruction.
It is needed because instructions may obtain operands from different places: registers, immediate fields, memory or
control-flow targets.
The PPT covers register, immediate, base, PC-relative and pseudo-direct addressing. Each mode provides a compact
way to specify where the required data or target address is located.
Q2. [5 Marks] Explain base addressing with its formula and purpose.
Answer:
Base addressing is used to access data in memory. The instruction contains a base register and an offset.
Formula:
Effective Address = Base Register + Sign-Extended Offset

--- [Page 8 of 14] ---
The base register supplies the starting address, while the offset selects a location relative to that address.
It is especially useful for accessing arrays, structures and stack-relative data.
Q3. [8 Marks] Explain the major MIPS addressing modes covered in the PPT.
Answer:
1. Register addressing: the operands are located in registers.
2. Immediate addressing: a constant is contained directly in the instruction.
3. Base addressing: a memory address is calculated as Base Register + Offset.
4. PC-relative addressing: used by branch instructions; the target is calculated relative to the program counter.
5. Pseudo-direct addressing: used by j and jal instructions to specify a jump target.
The modes allow MIPS to represent different operand and control-flow locations within fixed instruction formats.
Q4. [8 Marks] A branch instruction has PC = 1000 and an offset of 5. Calculate its PC-relative branch
target using the PPT formula.
Answer:
For PC-relative addressing, the PPT gives:
Branch Target = PC + 4 + (Offset × 4)
Given:
PC = 1000
Offset = 5
Step 1:
PC + 4 = 1004
Step 2:
Offset × 4 = 5 × 4 = 20
Step 3:
Target = 1004 + 20 = 1024
Therefore, the branch target address is 1024.
The multiplication by 4 accounts for the word-aligned MIPS instruction addresses.
Q5. [10 Marks] Compare base addressing, PC-relative addressing and pseudo-direct addressing with
examples.
Answer:
Base addressing is used for memory operands. The effective address is:
EA = Base Register + Sign-Extended Offset.
Example form: lw $t0, offset($s0).
PC-relative addressing is used by branch instructions. Its target is:
Target = PC + 4 + (Offset × 4).
It is suitable for branches because the target is specified relative to the current code location.
Pseudo-direct addressing is used by jump instructions such as j and jal. Instead of calculating a memory data address,
the instruction supplies a jump target field for transferring control.
Therefore:
• Base → memory/data address.
• PC-relative → branch target.
• Pseudo-direct → jump target.
These addressing modes make instruction encoding compact while supporting common processor operations.
Q6. [10 Marks] Solve an effective-address problem and explain the steps used in base addressing.

--- [Page 9 of 14] ---
Answer:
Suppose a load instruction uses a base register containing 5000 and an offset of 24. Using:
Effective Address = Base Register + Sign-Extended Offset
Step 1: Base register = 5000.
Step 2: Offset = 24. It is sign-extended before addition; since it is positive, its value remains 24.
Step 3: Add:
EA = 5000 + 24 = 5024.
Therefore, the memory location accessed is address 5024.
If the offset were negative, it would represent a location before the base address. The important point is that the offset is
combined with the base register to produce the effective memory address.
6. Parallelism
Q1. [5 Marks] Define latency, throughput and parallelism.
Answer:
Latency is the time required to complete one individual task from start to finish.
Throughput is the number of tasks completed per unit time.
Parallelism means executing multiple tasks simultaneously or overlapping their execution.
A key point from the PPT is that parallelism mainly improves throughput; it does not necessarily reduce the latency of
one individual task.
Q2. [5 Marks] State the advantages and applications of parallelism.
Answer:
Advantages:
1. Higher overall throughput.
2. Better utilization of available hardware.
3. Higher performance without depending only on increased clock frequency.
Applications listed in the PPT include multicore processors, GPUs, supercomputers, digital signal processors and
machine-learning accelerators.
Q3. [8 Marks] Explain spatial and temporal parallelism using the mathematical model in the PPT.
Answer:
For a task with latency L:
Without parallelism:
Throughput = 1/L.
Spatial parallelism:
If N hardware units execute independent tasks, then ideally:
Throughput = N/L.
The improvement comes from having multiple hardware units working at the same time.
Temporal parallelism:
If the task is divided into N stages and different tasks overlap in those stages, ideal throughput is also approximately:
Throughput = N/L.
Pipelining is the major example of temporal parallelism.
Thus, spatial parallelism uses more hardware, while temporal parallelism overlaps work across time.
Q4. [8 Marks] Explain the two-stage pipeline numerical example from the PPT.
Answer:
The PPT gives a circuit with an original critical path of 9.5 ns. Without pipelining:
Clock cycle time = 9.5 ns
Throughput = 1/9.5 ns ≈ 105 MHz.
After inserting a register, the two stages are:

--- [Page 10 of 14] ---
= 182 MHz. 
= 105.26 MHz. 
AHz. 
2.7%. 
Stage 1 = 5.5 ns
Stage 2 = 4.5 ns
The clock period is determined by the longest stage:
Tc = max(5.5, 4.5) = 5.5 ns.
Therefore:
Throughput = 1/5.5 ns ≈ 182 MHz.
Thus, pipelining increases the maximum operating frequency and throughput by dividing the long critical path into
shorter stages.
Q5. [10 Marks] Explain pipeline hazards and their effect on processor performance.
Answer:
A pipeline hazard is a condition that prevents instructions from moving smoothly through the pipeline. Hazards can
introduce stalls or bubbles and therefore reduce throughput.
1. Data hazard:
An instruction needs data that is still being produced by an earlier instruction. The dependent instruction may need to
wait.
2. Control hazard:
Caused by branches or jumps. The processor may fetch instructions before the branch decision is known and may have
to discard incorrect instructions.
3. Structural hazard:
Two or more instructions require the same hardware resource at the same time. One instruction must wait.
Therefore, although pipelining increases potential throughput, hazards prevent ideal performance. Pipeline design must
handle these conditions to maintain efficient execution.
Q6. [10 Marks] A non-pipelined circuit has a clock period of 9.5 ns. A two-stage pipeline has stage delays
of 5.5 ns and 4.5 ns. Calculate throughput and percentage throughput improvement.
Answer:
Without pipelining:
T = 9.5 ns
Throughput = 1/T = 1/9.5 ns ≈ 105.26 MHz.
With pipelining:
The clock period equals the longest stage:
T = max(5.5,4.5) = 5.5 ns.
Throughput = 1/5.5 ns ≈ 181.82 MHz.
Throughput improvement:
181.82 − 105.26 = 76.56 MHz.
Percentage improvement:
(76.56 / 105.26) × 100 ≈ 72.7%.
Therefore, the pipeline raises the maximum throughput from approximately 105 MHz to 182 MHz, an improvement of
about 72.7%. The improvement occurs because the critical path per clock cycle is reduced.
7. Memory Arrays
Q1. [5 Marks] Explain the organization and size of a memory array.
Answer:
A memory array is made from many 1-bit storage cells arranged in rows and columns. If there are N address bits, the
memory contains 2^N words. If each word contains M bits, the total size is:
Size = 2^N × M bits.
For example, with 10 address bits and 32-bit data:

--- [Page 11 of 14] ---
2^10 = 1024 words
Size = 1024 × 32 = 32,768 bits = 32 Kb.
A decoder activates the wordline corresponding to the selected address.
Q2. [5 Marks] Compare DRAM and SRAM.
Answer:
DRAM stores each bit as charge on a capacitor. The charge leaks, so periodic refresh is required. A simplified DRAM
cell uses about one transistor per bit, making it highly dense.
SRAM stores a bit using cross-coupled inverters. It does not need periodic refresh while power is applied and a typical
cell uses six transistors per bit.
Therefore, DRAM is denser and generally slower, while SRAM is faster but requires more area per bit.
Q3. [8 Marks] Explain the read and write operations of a memory bit cell.
Answer:
Read operation:
1. The selected wordline is activated.
2. The selected cell is connected to its bitline.
3. The stored value influences the bitline.
4. The sense circuitry detects whether the stored value represents 0 or 1.
Write operation:
1. The desired data value is driven onto the bitline.
2. The wordline is activated to select the cell.
3. The driven bitline forces the cell to store the new value.
4. The wordline is then deactivated.
Thus, the wordline selects a cell while the bitline carries the data. The exact internal mechanism differs between SRAM
and DRAM.
Q4. [8 Marks] Explain the area and delay trade-off among flip-flops, SRAM and DRAM.
Answer:
The PPT compares volatile storage technologies using transistor count and relative speed:
• Flip-flop: about 20 transistors/bit; very fast and the output is immediately available.
• SRAM: about 6 transistors/bit; faster than DRAM and does not require refresh while powered.
• DRAM: about 1 transistor/bit; very dense but slower and requires refresh.
More transistors generally mean more area, power and cost. Therefore, reducing the number of transistors improves
density, but the resulting memory cell may have slower access or additional requirements such as refresh.
Q5. [10 Marks] A memory has 12 address bits and a 16-bit word. Calculate the number of words and total
memory size. Explain the organization.
Answer:
Number of addressable words:
2^N = 2^12 = 4096 words.
Each word = 16 bits.
Total size:
4096 × 16 = 65,536 bits.
In bytes:
65,536 / 8 = 8,192 bytes = 8 KB.
Therefore, the memory organization is:
4096 words × 16 bits/word,
or 65,536 bits (8 KB).

--- [Page 12 of 14] ---
The 12 address bits select one of the 4096 rows/words. The 16 data bits represent the word width. A decoder uses the
address to activate the corresponding wordline, and the data bits are transferred through the bitlines.
Q6. [10 Marks] Explain how a 2^N-word × M-bit RAM can be described in HDL, including read and write
operations.
Answer:
A RAM of depth 2^N and width M contains 2^N memory locations, each M bits wide. Conceptually it has address, data
input, data output, clock and write-enable signals.
For a synchronous write, the write occurs on a clock edge when WE is asserted:
always_ff @(posedge clk)
if (we)
mem[adr] <= din;
This means:
1. Wait for the rising edge of the clock.
2. Check write enable.
3. If WE=1, store din at the selected address.
For an immediate/asynchronous read, the addressed location can be connected to the output:
assign dout = mem[adr];
For example, N=6 and M=32 gives 2^6 = 64 words, each 32 bits wide. Hence the RAM is 64 × 32 bits.
8. Sequential Building Blocks
Q1. [5 Marks] Define an N-bit binary counter and explain its operation.
Answer:
An N-bit binary counter is a sequential arithmetic circuit with a clock, reset and N-bit output Q.
When reset is asserted, Q is initialized to 0. After reset is released, the counter increments by 1 at every rising edge:
Q_next = Q + 1.
For example:
0101 → 0110 → 0111 → 1000.
When the counter reaches its maximum value, the next increment wraps around to zero.
Counters are used for timing, event counting and frequency division.
Q2. [5 Marks] Explain a shift register and list its applications.
Answer:
A shift register stores multiple bits using a chain of flip-flops. On each clock edge, the stored bits move from one flip-flop
to the next.
A serial input Sin introduces a new bit, while the last stored bit can leave through Sout.
Applications include:
1. Serial-to-parallel data conversion.
2. Parallel-to-serial data conversion.
3. Digital testing.
4. Data movement and temporary storage.
A parallel-load version can load multiple bits at once using additional control logic.
Q3. [8 Marks] Compare asynchronous and synchronous counters.
Answer:
Asynchronous/ripple counter:
• The first flip-flop receives the main clock.
• Subsequent flip-flops are triggered by earlier flip-flop outputs.
• Changes ripple through the counter.
• Propagation delays accumulate.
• It is simpler but limited in speed.

--- [Page 13 of 14] ---
32 cycles. 
— 1 cycle. 
Synchronous counter:
• All flip-flops receive the same global clock.
• Outputs change in parallel.
• It does not suffer from cumulative ripple delay.
• It can operate at higher frequencies.
• It is also called a parallel counter.
Therefore, synchronous counters are preferred when higher-speed counting is required.
Q4. [8 Marks] Explain ring and Johnson counters and calculate their number of states.
Answer:
Ring counter:
A ring counter is a shift-register-based counter in which the last flip-flop output is fed back to the first. A single 1
circulates through the flip-flops.
For n flip-flops:
Number of valid states = n.
Example: a 4-bit ring counter can follow:
1000 → 0100 → 0010 → 0001 → 1000.
Johnson counter:
The complemented output of the last flip-flop is fed back to the first.
For n flip-flops:
Number of valid states = 2n.
Therefore, a 4-bit Johnson counter has:
2 × 4 = 8 states.
Q5. [10 Marks] Explain the design steps for a synchronous counter using flip-flops.
Answer:
The PPT gives a systematic design procedure:
1. Determine the required counting sequence and number of states.
2. Determine the number of flip-flops required.
3. Draw the state diagram.
4. Prepare the present-state/next-state table.
5. Select the flip-flop type and use its excitation table.
6. Determine the required inputs to each flip-flop.
7. Simplify the input equations using Boolean algebra/K-maps.
8. Implement the resulting combinational logic.
9. Connect all flip-flops to the common clock.
10. Verify that the required sequence is produced.
The key feature is that all flip-flops receive the same clock, so state transitions occur synchronously.
Q6. [10 Marks] Explain scan-chain testing of sequential circuits and the 32-bit counter example.
Answer:
Sequential circuits are harder to test than combinational circuits because their outputs depend on internal state. Testing
a particular internal state directly could require an extremely large number of clock cycles.
A scan chain solves this problem by connecting the flip-flops into one long shift register.
Normal mode:
• Each flip-flop receives its normal D input.
Test mode:
• Data is shifted serially through Sin and Sout.
• Internal state can be loaded directly.
• Internal state can also be shifted out and observed.
For the 32-bit counter example in the PPT:
1. Shift a 32-bit test pattern into the scan chain → 32 cycles.
2. Allow the counter to operate for one clock cycle → 1 cycle.

--- [Page 14 of 14] ---
3. Shift the 32-bit result out → 32 cycles.
Total = 32 + 1 + 32 = 65 cycles.
This is dramatically smaller than testing by simply waiting for approximately 2 billion counter transitions.

```

---

# PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS

<a id="topic-1"></a>
## Topic Module 1: 18_sequential-building-blocks.md
**Source File**: `docs/18_sequential-building-blocks.md`

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
- **Read:** Precharge bit lines → Assert word line → Sense amp detects differential
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
Q⁺ = { 0       if Reset=1
     { Q+1    if Reset=0, Up=1
     { Q-1    if Reset=0, Up=0
```

**Convenient Form:**
```
Q⁺ = Q + (2·Up - 1)
```
- Up=1 → 2×1-1 = +1 (count up)
- Up=0 → 2×0-1 = -1 (count down)

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
3  0011 | 1 | 0 | 1 | 101
4  0100 | 0 | 0 | 1 | 001
5  0101 | 0 | 1 | 1 | 011
6  0110 | 0 | 0 | 1 | 001
7  0111 | 0 | 1 | 1 | 011
8  1000 | 0 | 0 | 1 | 001
9  1001 | 0 | 0 | 1 | 001
10 1010 | 1 | 0 | 1 | 101
11 1011 | 0 | 0 | 1 | 001
12 1100 | 1 | 1 | 1 | 111
13 1101 | 1 | 1 | 1 | 111
14 1110 | 1 | 1 | 1 | 111
15 1111 | 1 | 1 | 1 | 111
```

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

## Key Formulas (Memorize)

```
Register File:  N registers × W bits, R read ports, W write ports
SRAM:           6T cell, no refresh, fast
DRAM:           1T1C cell, refresh required, dense
Up/Down Counter: Q⁺ = Q + (2·Up - 1)
Counter +4:      Q⁺ = Q + 4
ROM:             2ᴺ addresses × M bits
```

---

## MCQ Patterns

1. **Register file ports** — MIPS: 32×32, 2 read, 1 write
2. **SRAM vs DRAM** — SRAM=6T static, DRAM=1T1C dynamic+refresh
3. **Enabled FF** — MUX at D-input (not clock gating)
3. **Counter equations** — Up/Down: Q⁺ = Q + (2·Up-1)
4. **ROM addressing** — 2ᴺ addresses for N address lines

---

<a id="topic-2"></a>
## Topic Module 2: 19_computer-architecture-intro.md
**Source File**: `docs/19_computer-architecture-intro.md`

# 19. Computer Architecture Introduction — Von Neumann, Performance, Memory Map

> **Source:** Unit 3 Slides 3.6.1, 3.14.2 | Textbook: Harris & Harris Ch. 6, 7

---

## Von Neumann vs Harvard Architecture

| Feature | Von Neumann | Harvard |
|---------|-------------|---------|
| **Memory** | Unified (Code+Data) | Separate Instruction/Data |
| **Bus** | Single shared bus | Separate I/D buses |
| **Bottleneck** | Yes (von Neumann bottleneck) | No |
| **Example** | Most general CPUs | DSPs, Microcontrollers |

---

## MIPS Memory Map (32-bit → 4 GB)

| Address Range | Segment | Description |
|---------------|---------|-------------|
| 0x00000000 – 0x003FFFFC | Reserved | — |
| **0x00400000 – 0x0FFFFFFC** | **Text** | PC starts at 0x00400000; ~256 MB for code |
| **0x10000000 – 0x1000FFFC** | **Global Data** | $gp = 0x10008000 (middle); 64 KB globals |
| **0x10010000 – 0x7FFFFFFC** | **Dynamic Data** | Heap (bottom ↑), Stack (top ↓, $sp=0x7FFFFFFC) |
| 0x80000000 – 0xFFFFFFFC | Reserved | OS, interrupts, memory-mapped I/O |

---

## Memory Segments Detail

### Text Segment
- Stores machine language program
- PC starts at 0x00400000
- Top 4 bits of all text addresses = 0 → `j` instruction can jump anywhere
- **Analogy:** Recipe book; PC = finger on current line

### Global Data Segment
- Stores global variables (declared outside functions in C)
- Accessed via `$gp` (global pointer) = 0x10008000
- `$gp` does **not** change during execution
- Any global accessed via base addressing with 16-bit offset from `$gp`

### Dynamic Data Segment (Stack & Heap)
| Property | Stack | Heap |
|----------|-------|------|
| **Use** | Save/restore registers; local variables/arrays | `malloc` (C), `new` (C++/Java) |
| **Allocation** | LIFO stack frames | Any order |
| **Direction** | Grows **down** from 0x7FFFFFFC | Grows **up** from 0x10010000 |
| **Collision** | If stack/heap meet → data corruption → OOM error |

### Reserved Segments
- Used by OS; cannot be used directly by program
- Interrupts, memory-mapped I/O

---

## Program Translation & Execution Pipeline

```
High-level code (C)
      ↓ Compiler
Assembly code (.s)
      ↓ Assembler (2 passes)
Object file (.o) — machine code + symbol table
      ↓ Linker
Executable (header + text + data)
      ↓ Loader (OS)
Memory (text + data + stack + heap)
      ↓ jal 0x00400000
Execution begins
```

### Assembler Two Passes
| Pass | Function |
|------|----------|
| **Pass 1** | Assign instruction addresses; build symbol table (labels, globals) |
| **Pass 2** | Produce machine code using symbol table for label/global addresses |

**Example:** `sw $a0, 0x8000($gp)` stores to global `f`
- 0x8000 sign-extended = 0xFFFF8000
- `$gp + 0xFFFF8000 = 0x10008000 + 0xFFFF8000 = 0x10000000` (address of `f`)

### Loader Steps
1. Read text segment from disk → memory text segment (0x00400000)
2. Set `$gp = 0x10008000` (middle of global data)
3. Set `$sp = 0x7FFFFFFC` (top of stack)
4. `jal 0x00400000` to start program

---

## Performance Metrics

### Latency
- Time required for **one task** from input to output
- `Latency = Time for one task`

### Throughput
- Number of tasks completed per unit time
- `Throughput = Completed tasks / Unit Time`
- For non-parallel: `Throughput = 1 / Latency`

### Key Distinction
- **Latency** = time per task (lower = faster response)
- **Throughput** = tasks per second (higher = more work)
- **Parallelism improves throughput, NOT latency**

---

## Amdahl's Law
```
Speedup = 1 / [(1 - f) + f/s]
```
- `f` = fraction of program that can be improved
- `s` = speedup of improved portion

**Example:** If 40% of program can be sped up 10×:
- Speedup = 1 / [0.6 + 0.4/10] = 1 / 0.64 = 1.56×

---

## Key Formulas (Memorize)

```
MIPS Memory:      2³² bytes = 4 GB
Text segment:     0x00400000–0x0FFFFFFC (PC starts at 0x00400000)
Global data:      0x10000000–0x1000FFFC ($gp=0x10008000)
Stack:            grows down from 0x7FFFFFFC
Heap:             grows up from 0x10010000
Latency:          time per task
Throughput:       tasks/second
Non-parallel TP:  1 / Latency
Amdahl's Law:     1 / [(1-f) + f/s]
```

---

## MCQ Patterns

1. **Von Neumann bottleneck** — single shared bus for code+data
2. **MIPS memory map segments** — text, global, dynamic, reserved
3. **$gp vs $sp** — $gp fixed at 0x10008000; $sp changes
4. **Stack vs Heap** — Stack grows down, Heap grows up
5. **Assembler passes** — Pass 1: symbol table; Pass 2: machine code
6. **Loader steps** — Load text, set $gp/$sp, jal to start
7. **Amdahl's Law** — diminishing returns on partial speedup

---

<a id="topic-3"></a>
## Topic Module 3: 20_assembly-language.md
**Source File**: `docs/20_assembly-language.md`

# 20. Assembly Language — MIPS Instructions, Registers, Pseudoinstructions

> **Source:** Unit 3 Slides 3.7.1, 3.11.1 | Textbook: Harris & Harris Ch. 6

---

## MIPS Registers (32 General Purpose: x0–x31 / $0–$31)

| Register | Name | Use | Preserved? |
|----------|------|-----|------------|
| $0 ($zero) | zero | Hardwired 0 | N/A |
| $1 ($at) | assembler temp | Reserved for assembler | No |
| $2–$3 ($v0–$v1) | return values | Function results | No |
| $4–$7 ($a0–$a3) | arguments | First 4 function args | No |
| $8–$15 ($t0–$t7) | temporaries | Caller-saved (non-preserved) | **No** |
| $16–$23 ($s0–$s7) | saved | Callee-saved (preserved) | **Yes** |
| $24–$25 ($t8–$t9) | temporaries | Caller-saved | No |
| $26–$27 ($k0–$k1) | kernel | Reserved for OS | No |
| $28 ($gp) | global pointer | Middle of global data | Yes |
| $29 ($sp) | stack pointer | Top of stack | Yes |
| $30 ($fp/$s8) | frame pointer | Stack frame base | Yes |
| $31 ($ra) | return address | Function return address | Yes |

**Key:** Callee must save/restore `$s0–$s7`, `$ra`, `$sp`, `$fp` if used. Caller saves `$t0–$t9`, `$a0–$a3`, `$v0–$v1`.

---

## Instruction Formats

### R-Type (Register)
```
op(6) | rs(5) | rt(5) | rd(5) | shamt(5) | funct(6)
```
- 3 register operands (rs, rt, rd)
- ALU ops: add, sub, and, or, xor, nor, slt
- Shifts: sll, srl, sra (shamt = shift amount)
- Variable shifts: sllv, srlv, srav (rs = shift amount)
- jr (jump register)

### I-Type (Immediate)
```
op(6) | rs(5) | rt(5) | imm(16)
```
- 2 registers + 16-bit immediate
- Arithmetic: addi, addiu
- Logical: andi, ori, xori (zero-extend); addi/lw/sw (sign-extend)
- Load/Store: lw, sw, lb, lbu, sb
- Branch: beq, bne (PC-relative)

### J-Type (Jump)
```
op(6) | addr(26)
```
- 26-bit address (shifted left 2)
- Jump: j, jal

---

## Arithmetic Instructions

| Instruction | Format | Operation | Notes |
|-------------|--------|-----------|-------|
| `add rd, rs, rt` | R | rd = rs + rt | Overflow trap |
| `addu rd, rs, rt` | R | rd = rs + rt | No overflow trap |
| `sub rd, rs, rt` | R | rd = rs - rt | Overflow trap |
| `subu rd, rs, rt` | R | rd = rs - rt | No overflow trap |
| `addi rt, rs, imm` | I | rt = rs + imm | Sign-extended, overflow trap |
| `addiu rt, rs, imm` | I | rt = rs + imm | Sign-extended, no overflow |

---

## Logical Instructions

| Instruction | Format | Operation | Extension |
|-------------|--------|-----------|-----------|
| `and rd, rs, rt` | R | rd = rs & rt | — |
| `or rd, rs, rt` | R | rd = rs \| rt | — |
| `xor rd, rs, rt` | R | rd = rs ^ rt | — |
| `nor rd, rs, rt` | R | rd = ~(rs \| rt) | — |
| `andi rt, rs, imm` | I | rt = rs & imm | **Zero-extend** |
| `ori rt, rs, imm` | I | rt = rs \| imm | **Zero-extend** |
| `xori rt, rs, imm` | I | rt = rs ^ imm | **Zero-extend** |

**No `nori`** — use `ori` + `nor` with `$zero`:
```
ori $t0, $s1, 0x00FF
nor $t0, $t0, $zero  # $t0 = ~($s1 | 0x00FF)
```

---

## Shift Instructions

| Instruction | Type | Operation | Fill Bits | Use |
|-------------|------|-----------|-----------|-----|
| `sll rd, rt, shamt` | R | rd = rt << shamt | 0s on right | Multiply by 2ᴺ |
| `srl rd, rt, shamt` | R | rd = rt >> shamt | 0s on left | Unsigned / bit extract |
| `sra rd, rt, shamt` | R | rd = rt >>> shamt | **Sign bit** | Signed divide by 2ᴺ |

**Variable Shifts** (amount in lower 5 bits of rs):
| Instruction | Type | Syntax | Notes |
|-------------|------|--------|-------|
| `sllv rd, rt, rs` | R | rd = rt << rs[4:0] | shamt=0 |
| `srlv rd, rt, rs` | R | rd = rt >> rs[4:0] | shamt=0 |
| `srav rd, rt, rs` | R | rd = rt >>> rs[4:0] | shamt=0 |

---

## Generating Constants

### 16-bit Constant
```
addi $s0, $0, 0x4F3C   # $s0 = 0x00004F3C
```

### 32-bit Constant (lui + ori)
```
lui  $s0, 0x6D5E       # $s0 = 0x6D5E0000
ori  $s0, $s0, 0x4F3C  # $s0 = 0x6D5E4F3C
```

---

## Multiplication & Division

| Instruction | Result Location | Notes |
|-------------|-----------------|-------|
| `mult rs, rt` | HI:LO = 64-bit product | HI=upper 32, LO=lower 32 |
| `multu rs, rt` | HI:LO = 64-bit product | Unsigned |
| `div rs, rt` | LO=quotient, HI=remainder | Signed |
| `divu rs, rt` | LO=quotient, HI=remainder | Unsigned |
| `mul rd, rs, rt` | rd = rs × rt (32-bit) | Low 32 bits only |
| `mfhi rd` | rd = HI | Move from HI |
| `mflo rd` | rd = LO | Move from LO |

**Example:** `$s0=20, $s1=6` → div gives mflo $t0 = 3 (quotient) and mfhi $t1 = 2 (remainder).

---

## Load/Store Instructions

| Instruction | Format | Operation | Notes |
|-------------|--------|-----------|-------|
| `lw rt, offset(rs)` | I | rt = Mem[rs + offset] | Sign-extend offset |
| `sw rt, offset(rs)` | I | Mem[rs + offset] = rt | Sign-extend offset |
| `lb rt, offset(rs)` | I | rt = sign-extend(Mem[rs+offset]) | Byte load |
| `lbu rt, offset(rs)` | I | rt = zero-extend(Mem[rs+offset]) | Unsigned byte |
| `sb rt, offset(rs)` | I | Mem[rs+offset] = rt[7:0] | Byte store |

---

## Branch Instructions (PC-Relative)

| Instruction | Format | Condition | Target |
|-------------|--------|-----------|--------|
| `beq rs, rt, label` | I | rs == rt | PC+4 + (imm×4) |
| `bne rs, rt, label` | I | rs != rt | PC+4 + (imm×4) |
| `slt rd, rs, rt` | R | rd = (rs < rt) ? 1 : 0 | Magnitude compare |

**Branch Target Address:**
```
BTA = (PC + 4) + (SignExtendedOffset × 4)
```

---

## Jump Instructions

| Instruction | Format | Target Calculation |
|-------------|--------|-------------------|
| `j label` | J | JTA = {PC+4[31:28], addr[25:0], 00} |
| `jal label` | J | $ra = PC+4; JTA = {PC+4[31:28], addr[25:0], 00} |
| `jr rs` | R | PC = rs |

**Pseudo-Direct Addressing:**
- 26-bit address field → shifted left 2 → combined with upper 4 bits of PC+4
- Allows jumps within 256 MB region

---

## High-Level Constructs in MIPS

### If Statement
```c
if (i == j) f = g + h;
f = f - i;
```
```mips
bne  $s3, $s4, L1      # if i != j, skip
add  $s0, $s1, $s2     # f = g + h
L1:  sub  $s0, $s0, $s3 # f = f - i
```

### If-Else Statement
```c
if (i == j) f = g + h;
else f = f - i;
```
```mips
bne  $s3, $s4, L1      # if i != j, go to else
add  $s0, $s1, $s2     # f = g + h
j    done              # skip else
L1:  sub  $s0, $s0, $s3 # f = f - i
done:
```

### While Loop
```c
while (pow != 128) {
  pow = pow * 2;
  x = x + 1;
}
```
```mips
while: beq  $s0, $t0, done   # if pow == 128, exit
       sll  $s0, $s0, 1      # pow *= 2
       addi $s1, $s1, 1      # x++
       j    while
done:
```

### For Loop
```c
for (i = 0; i != 10; i++) sum = sum + i;
```
```mips
addi $s1, $0, 0       # sum = 0
add  $s0, $0, $0      # i = 0
addi $t0, $0, 10      # limit = 10
for:  beq  $s0, $t0, done
      add  $s1, $s1, $s0
      addi $s0, $s0, 1
      j    for
done:
```

### Array Access
```c
int array[5];
array[i] = array[i] * 8;
```
```mips
sll  $t0, $s1, 2      # $t0 = i × 4
add  $t0, $t0, $s0    # address of array[i]
lw   $t1, 0($t0)      # load array[i]
sll  $t1, $t1, 3      # × 8
sw   $t1, 0($t0)      # store
```

### Character Array (bytes)
```c
for (i = 0; i != 10; i++)
  chararray[i] = chararray[i] - 32;  // lowercase to uppercase
```
```mips
addi $s1, $0, 0       # i = 0
addi $t0, $0, 10
loop:
  beq  $t0, $s1, done
  add  $t1, $s1, $s0  # address = base + i (1 byte each)
  lb   $t2, 0($t1)    # load byte
  addi $t2, $t2, -32  # 'a'(0x61) - 0x20 = 'A'(0x41)
  sb   $t2, 0($t1)    # store byte
  addi $s1, $s1, 1
  j    loop
done:
```

---

## Function Calls

### Caller/Callee Convention
| Category | Registers | Responsibility |
|----------|-----------|----------------|
| **Arguments** | $a0–$a3 | Caller places args |
| **Return** | $v0–$v1 | Callee places result |
| **Preserved** | $s0–$s7, $ra, $sp | Callee saves if used |
| **Non-preserved** | $t0–$t9, $a0–$a3, $v0–$v1 | Caller saves if needed |

### Call Sequence
```mips
# Caller
addi $a0, $0, 2     # arg1
addi $a1, $0, 3     # arg2
jal  diffofsums     # $ra = PC+4; jump
add  $s0, $v0, $0   # save return value

# Callee (diffofsums)
add  $t0, $a0, $a1
add  $t1, $a2, $a3
sub  $s0, $t0, $t1
add  $v0, $s0, $0   # return value
jr   $ra            # return
```

### Stack Frame (Callee-saved registers)
```mips
# Prologue
addi $sp, $sp, -12   # allocate 3 words
sw   $s0, 8($sp)
sw   $t0, 4($sp)
sw   $t1, 0($sp)

# ... function body ...

# Epilogue
lw   $t1, 0($sp)
lw   $t0, 4($sp)
lw   $s0, 8($sp)
addi $sp, $sp, 12    # deallocate
jr   $ra
```

### Recursive Factorial
```mips
factorial:
  addi $sp, $sp, -8
  sw   $a0, 4($sp)   # save n
  sw   $ra, 0($sp)   # save return addr
  addi $t0, $0, 2
  slt  $t0, $a0, $t0 # n < 2?
  beq  $t0, $0, else
  addi $v0, $0, 1    # base case: return 1
  addi $sp, $sp, 8
  jr   $ra
else: addi $a0, $a0, -1  # n-1
  jal  factorial     # recursive call
  lw   $ra, 0($sp)
  lw   $a0, 4($sp)   # restore n
  addi $sp, $sp, 8
  mul  $v0, $a0, $v0 # n * factorial(n-1)
  jr   $ra
```

---

## Key Formulas (Memorize)

```
R-type:     op(6)|rs(5)|rt(5)|rd(5)|shamt(5)|funct(6)
I-type:     op(6)|rs(5)|rt(5)|imm(16)
J-type:     op(6)|addr(26)
Branch:     BTA = (PC+4) + (offset×4)
Jump:       JTA = {PC+4[31:28], addr[25:0], 00}
Array addr: base + 4×i (int), base + i (char)
32-bit const: lui upper16 + ori lower16
Function:   Args→$a0-$a3, Return→$v0, Call→jal, Return→jr $ra
Stack:      $sp grows DOWN (subtract to allocate)
```

---

## MCQ Patterns

1. **Register conventions** — $s0–$s7 preserved, $t0–$t9 non-preserved
2. **Branch vs Jump** — beq/bne=PC-relative, j/jal=pseudo-direct
3. **Immediate extension** — addi/lw/sw=sign-extend, andi/ori/xori=zero-extend
4. **Shift right** — srl=0-fill, sra=sign-fill
5. **Function call** — jal saves $ra=PC+4; jr $ra returns
6. **Stack** — grows downward (subtract), $sp points to top
7. **Array indexing** — int: base+4i, char: base+i
8. **Multiplication** — mult→HI:LO (64-bit), mul→32-bit result
8. **Division** — div→LO=quotient, HI=remainder
9. **Pseudoinstructions** — lui+ori for 32-bit constants

---

<a id="topic-4"></a>
## Topic Module 4: 21_machine-language.md
**Source File**: `docs/21_machine-language.md`

# 21. Machine Language — Instruction Encoding, Decoding, Stored Program

> **Source:** Unit 3 Slides 3.9.1 | Textbook: Harris & Harris Ch. 6

---

## MIPS Machine Language Formats

All MIPS instructions are **32 bits (4 bytes)**. Word addresses divisible by 4.

### R-Type Format
```
31          25 24    20 19    15 14    10 9     5 4        0
┌─────────────┬───────┬───────┬───────┬───────┬───────────┐
│   op (6)    │ rs(5) │ rt(5) │ rd(5) │shamt(5)│ funct(6) │
└─────────────┴───────┴───────┴───────┴───────┴───────────┘
```
- **op = 0** for all R-type
- **funct** determines exact operation

### I-Type Format
```
31          25 24    20 19    15 14                0
┌─────────────┬───────┬───────┬─────────────────────┐
│   op (6)    │ rs(5) │ rt(5) │       imm(16)       │
└─────────────┴───────┴───────┴─────────────────────┘
```
- rs = source register (base for load/store)
- rt = destination (load) or source (store)
- imm = 16-bit immediate (sign-extended for arithmetic/load/store/branch, zero-extended for logical)

### J-Type Format
```
31          25 24                              0
┌─────────────┬─────────────────────────────────┐
│   op (6)    │          addr(26)               │
└─────────────┴─────────────────────────────────┘
```
- 26-bit address field
- Shifted left 2 (×4) for word alignment
- Combined with PC+4[31:28] for full 32-bit target

---

## Opcode and Funct Values (Key Subset)

| Instruction | op | funct | Format |
|-------------|-----|-------|--------|
| **add** | 0 | 32 (0x20) | R |
| **sub** | 0 | 34 (0x22) | R |
| **and** | 0 | 36 (0x24) | R |
| **or** | 0 | 37 (0x25) | R |
| **xor** | 0 | 38 (0x26) | R |
| **nor** | 0 | 39 (0x27) | R |
| **slt** | 0 | 42 (0x2A) | R |
| **sll** | 0 | 0 | R |
| **srl** | 0 | 2 | R |
| **sra** | 0 | 3 | R |
| **jr** | 0 | 8 | R |
| **addi** | 8 (0x08) | — | I |
| **addiu** | 9 (0x09) | — | I |
| **andi** | 12 (0x0C) | — | I |
| **ori** | 13 (0x0D) | — | I |
| **xori** | 14 (0x0E) | — | I |
| **lw** | 35 (0x23) | — | I |
| **sw** | 43 (0x2B) | — | I |
| **beq** | 4 | — | I |
| **bne** | 5 | — | I |
| **slti** | 10 (0x0A) | — | I |
| **lui** | 15 (0x0F) | — | I |
| **j** | 2 | — | J |
| **jal** | 3 | — | J |

---

## Encoding Examples

### Example 1: `add $t0, $s4, $s5`
- $t0 = 8, $s4 = 20, $s5 = 21
- op=0, rs=20, rt=21, rd=8, shamt=0, funct=32
- Binary: `000000 10100 10101 01000 00000 100000`
- Hex: **0x02954020**

### Example 2: `lw $s3, -24($s4)`
- $s3 = 19, $s4 = 20
- op=35 (0x23), rs=20, rt=19, imm=-24 = 0xFFE8
- Binary: `100011 10100 10011 1111111111101000`
- Hex: **0x8D93FFE8**

### Example 3: `addi $s7, $s1, -15`
- $s7 = 23, $s1 = 17
- op=8 (0x08), rs=17, rt=23, imm=-15 = 0xFFF1
- Binary: `001000 10001 10111 1111111111110001`
- Hex: **0x223FFFF1**

### Example 4: `j sum` (PC=0x0040005C, sum=0x004000A0)
- op=2, addr = 0x004000A0 >> 2 = 0x00100028
- Binary: `000010 00000100000000000000101000`
- Hex: **0x08100028**

---

## Decoding Machine Code

### Strategy
1. **Read opcode** (bits 31-26)
2. **If op = 0** → R-type → inspect **funct** (bits 5-0)
3. **If op ≠ 0** → Use opcode to identify I-type or J-type
4. **Extract register fields** → map to register names ($0-$31)
5. **Interpret immediate** → signed (addi, lw, sw, beq, bne) or unsigned (andi, ori, xori, lui)

### Worked Example: `0x223FFFF1`
```
Binary: 001000 10001 10111 1111111111110001
op = 001000₂ = 8 → addi (I-type)
rs = 10001₂ = 17 → $s1
rt = 10111₂ = 23 → $s7
imm = 1111111111110001₂ = -15 (sign-extended)
Result: addi $s7, $s1, -15
```

### Worked Example: `0x02F34022`
```
Binary: 000000 10111 10011 01000 00000 100010
op = 0 → R-type
funct = 100010₂ = 34 → sub
rs = 10111₂ = 23 → $s7
rt = 10011₂ = 19 → $s3
rd = 01000₂ = 8 → $t0
Result: sub $t0, $s7, $s3
```

---

## Stored Program Concept

### Machine Code
- Executed directly by CPU
- Binary/hex format (e.g., `0x8C0A0020`)
- Difficult for humans

### Assembly Code
- Human-readable mnemonics (e.g., `lw $t2, 32($0)`)
- Must be **assembled** into machine code

### Program Counter (PC)
- Special register holding **address of next instruction**
- Incremented by 4 after each fetch (MIPS 32-bit = 4 bytes)
- Modified by branch/jump instructions

### Memory Organization
- **Both instructions and data in same memory** (Von Neumann)
- Instructions fetched from text segment
- Data accessed from data/stack/heap segments

---

## Register Reference (for Encoding)

| Number | Name | Number | Name | Number | Name | Number | Name |
|--------|------|--------|------|--------|------|--------|------|
| 0 | $zero | 8 | $t0 | 16 | $s0 | 24 | $t8 |
| 1 | $at | 9 | $t1 | 17 | $s1 | 25 | $t9 |
| 2 | $v0 | 10 | $t2 | 18 | $s2 | 26 | $k0 |
| 3 | $v1 | 11 | $t3 | 19 | $s3 | 27 | $k1 |
| 4 | $a0 | 12 | $t4 | 20 | $s4 | 28 | $gp |
| 5 | $a1 | 13 | $t5 | 21 | $s5 | 29 | $sp |
| 6 | $a2 | 14 | $t6 | 22 | $s6 | 30 | $fp/$s8 |
| 7 | $a3 | 15 | $t7 | 23 | $s7 | 31 | $ra |

---

## Key Formulas (Memorize)

```
R-type:  op(6)|rs(5)|rt(5)|rd(5)|shamt(5)|funct(6)    op=0
I-type:  op(6)|rs(5)|rt(5)|imm(16)
J-type:  op(6)|addr(26)                               addr = target>>2

Branch target:  BTA = (PC+4) + (signExt(imm) × 4)
Jump target:    JTA = {PC+4[31:28], addr[25:0], 00}

Hex conversion:  4 bits → 1 hex digit
0x8C0A0020 = 10001100 00001010 00000000 00100000
```

---

## MCQ Patterns

1. **Opcode identification** — op=0 → R-type (check funct); op=35 → lw; op=43 → sw; op=4 → beq; op=5 → bne; op=2 → j; op=3 → jal
2. **R-type funct codes** — add=32, sub=34, and=36, or=37, slt=42, sll=0, jr=8
3. **I-type opcodes** — addi=8, andi=12, ori=13, lw=35, sw=43, beq=4, bne=5, lui=15
4. **J-type opcodes** — j=2, jal=3
5. **Immediate sign** — arithmetic/load/store/branch = sign-extend; logical = zero-extend
6. **Register mapping** — know $t0=8, $s0=16, $a0=4, $v0=2, $ra=31, $sp=29
7. **Machine code → assembly** — extract fields, interpret by format
8. **Jump address calc** — shift 26-bit addr left 2, combine with PC+4[31:28]
8. **Branch offset** — offset = (target - (PC+4)) / 4

---

<a id="topic-5"></a>
## Topic Module 5: 22_addressing-modes.md
**Source File**: `docs/22_addressing-modes.md`

# 22. Addressing Modes — MIPS Operand Location Methods

> **Source:** Unit 3 Slides 3.14.1 | Textbook: Harris & Harris Ch. 6

---

## What is an Addressing Mode?

An **addressing mode** specifies how the CPU locates the operand(s) required to execute an instruction. Operands may be in registers, memory, or within the instruction itself.

**Why Important:**
- Determine operand location
- Influence execution speed and memory usage
- Provide flexibility for constants, variables, arrays, loops, function calls
- Reduce instruction size while improving efficiency

---

## MIPS Addressing Modes (5 Types)

| Mode | Operand Location | Example Instructions |
|------|------------------|---------------------|
| **Register** | CPU Registers | `add $s0, $t2, $t3` |
| **Immediate** | Constant in Instruction | `addi $s0, $s0, 10` |
| **Base (Displacement)** | Memory (Base + Offset) | `lw $t0, 8($sp)` |
| **PC-Relative** | Memory (PC + Offset) | `beq $t0, $0, Loop` |
| **Pseudo-Direct** | Memory (Partial Address) | `j main`, `jal func` |

---

## 1. Register-Only Addressing

**Definition:** Operands stored entirely in CPU registers. No memory access.

**Used By:** All R-type instructions (add, sub, and, or, slt, shifts, jr)

**Format:** `op rd, rs, rt` or `op rd, rt, shamt`

**Example:**
```
add $s0, $t2, $t3
# $s0 = $t2 + $t3
# Source: $t2, $t3 | Destination: $s0
```

**Characteristics:**
- ALU reads operands directly from register file
- Result stored back to register
- **Fastest** addressing mode (registers = fastest storage)
- No memory access during execution

---

## 2. Immediate Addressing

**Definition:** One operand is a 16-bit constant encoded directly in the instruction.

**Used By:** I-type instructions (addi, ori, andi, lui, addiu, slti)

**Format:** `op rt, rs, imm`

**Immediate Handling:**
| Instruction Type | Extension |
|------------------|-----------|
| **Arithmetic** (addi, addiu) | **Sign-extend** to 32 bits |
| **Load/Store** (lw, sw) | **Sign-extend** to 32 bits |
| **Branch** (beq, bne) | **Sign-extend** to 32 bits |
| **Logical** (andi, ori, xori) | **Zero-extend** to 32 bits |
| **lui** | Place in upper 16 bits, lower 16 = 0 |

**Examples:**
```
addi $s4, $t5, -73       # $s4 = $t5 + (-73)  [sign-extended]
ori  $t3, $t7, 0xFF      # $t3 = $t7 | 0x00FF [zero-extended]
lui  $s0, 0x6D5E         # $s0 = 0x6D5E0000
```

**Advantage:** Constant in instruction → no memory access → faster execution

**Applications:** Initialize registers, loop counters, increment/decrement, arithmetic with constants

---

## 3. Base Addressing (Displacement/Indexed)

**Definition:** Memory access using base register + 16-bit signed offset.

**Used By:** Memory instructions — `lw`, `sw`, `lb`, `lbu`, `sb`

**Effective Address Calculation:**
```
Effective Address = Base Register + Sign-Extended 16-bit Offset
```

**Format:** `op rt, offset(rs)` — reads as "load/store rt from/to memory at rs+offset"

**Examples:**
```
lw  $s4, 72($0)     # EA = $0 + 72 = 72; word at addr 72 loaded into $s4
sw  $t2, -25($t1)   # EA = $t1 - 25; contents of $t2 stored there
lw  $t1, 4($s0)     # Load array[1] (int array: $s0=base, offset=4)
```

**Offset Properties:**
- 16-bit signed → range -32768 to +32767 bytes
- Can be positive or negative
- Allows access before/after base address

**Applications:** Arrays, stack frames, structures, dynamic memory

**Key Point:** Base addressing enables efficient memory access with constant offsets known at assembly time.

---

## 4. PC-Relative Addressing

**Definition:** Conditional branches use 16-bit signed offset relative to **PC+4**.

**Used By:** Branch instructions — `beq`, `bne`

**Branch Target Address Formula:**
```
BTA = (PC + 4) + (Sign-Extended Offset × 4)
```

**Why ×4?** MIPS instructions are 4 bytes (word-aligned). Offset counts **instructions**, not bytes.

**Example:**
```
Assembly:
0x10   beq  $t0, $0, else
0x14   addi $v0, $0, 1
0x18   addi $sp, $sp, 8
0x1C   jr   $ra
0x20 else: addi $a0, $a0, -1
0x24       j    factorial

Machine: beq $t0, $0, 3
# offset = 3 (3 instructions from 0x14 to 0x20)
# BTA = (0x10+4) + (3×4) = 0x14 + 0xC = 0x20 ✓
```

**Key Observation:** Immediate field stores **number of instructions to jump**, not byte address.

**Advantage:** Compact (16-bit offset vs 32-bit address); allows forward/backward branching.

---

## 5. Pseudo-Direct Addressing

**Definition:** Jump instructions use 26-bit address field; processor constructs full 32-bit target.

**Used By:** `j` (Jump), `jal` (Jump and Link)

**Jump Target Address Formula:**
```
JTA = { (PC+4)[31:28], Address[25:0], 00 }
```

**Construction Steps:**
1. Take upper 4 bits of PC+4
2. Append 26-bit address field from instruction
3. Add two trailing 0 bits (word alignment)

**Example:**
```
Assembly:
0x0040005C      j   sum
...
0x004000A0  sum: add $v0, $a0, $a1

Calculation:
JTA = 0x004000A0
26-bit field = 0x00100028
Opcode for j = 000010

Machine: 0x08100028
```

**Why Shift Left by 2?**
- Every MIPS instruction = 4 bytes = 32 bits
- Instruction addresses are **word-aligned** (last 2 bits always `00`)
- These bits omitted from instruction, restored by processor

**Limitation:** Can only jump within same **256 MB region** (same upper 4 bits of PC+4).

---

## Comparison Table

| Aspect | Register | Immediate | Base | PC-Relative | Pseudo-Direct |
|--------|----------|-----------|------|-------------|---------------|
| **Operand** | Register | Constant in instr | Memory | Memory | Memory |
| **Instr Type** | R-type | I-type | I-type (lw/sw) | I-type (beq/bne) | J-type (j/jal) |
| **Address Calc** | None | None | Base + Offset | (PC+4) + Offset×4 | {PC+4[31:28], addr, 00} |
| **Range** | 32 regs | ±32K (sign) / 64K (zero) | ±32K from base | ±128K instructions | 256 MB region |
| **Speed** | Fastest | Fast | Memory access | Memory access | Memory access |

---

## MIPS Instruction Categories by Addressing Mode

| Category | Instructions | Addressing Mode |
|----------|--------------|-----------------|
| **Arithmetic/Logic** | add, sub, and, or, slt, sll, srl, sra | Register |
| **Immediate Arithmetic** | addi, addiu, slti | Immediate |
| **Immediate Logical** | andi, ori, xori | Immediate (zero-extend) |
| **Load Upper** | lui | Immediate (upper 16) |
| **Memory Access** | lw, sw, lb, lbu, sb | Base (Base + Offset) |
| **Conditional Branch** | beq, bne | PC-Relative |
| **Unconditional Jump** | j, jal | Pseudo-Direct |
| **Register Jump** | jr | Register |

---

## Key Formulas (Memorize)

```
Register:        rd = rs op rt
Immediate:       rt = rs op imm
Base (lw/sw):    EA = BaseReg + SignExt(Offset)
PC-Relative:     BTA = (PC + 4) + (SignExt(Offset) × 4)
Pseudo-Direct:   JTA = {PC+4[31:28], Addr[25:0], 00}

Offset ranges:
  Immediate (sign):     -32768 to +32767
  Immediate (zero):     0 to 65535
  Base offset:          -32768 to +32767 bytes
  Branch offset:        -32768 to +32767 instructions (×4 bytes)
  Jump address:         26 bits → 256 MB region
```

---

## MCQ Patterns

1. **Register-only** — used by R-type (add, sub, jr); fastest
2. **Immediate** — constant in instruction; addi=sign-extend, andi=zero-extend
3. **Base addressing** — lw/sw; EA = Base + SignExt(Offset)
4. **PC-relative** — beq/bne; BTA = (PC+4) + Offset×4; offset counts instructions
5. **Pseudo-direct** — j/jal; 26-bit field + PC+4[31:28] + 00; 256 MB range
6. **No nori** — use ori + nor $zero
7. **lui** — loads upper 16 bits, clears lower 16
8. **Shift left 2** — word alignment (instructions=4 bytes)

---

<a id="topic-6"></a>
## Topic Module 6: 23_compiling-assembling-loading.md
**Source File**: `docs/23_compiling-assembling-loading.md`

# 23. Compiling, Assembling, Linking & Loading — Program Translation Pipeline

> **Source:** Unit 3 Slides 3.14.2 | Textbook: Harris & Harris Ch. 6, 7

---

## Translation Pipeline Overview

```
High-level Code (C)
        ↓ Compiler
Assembly Code (.s)
        ↓ Assembler (2 passes)
Object File (.o) — Machine code + Symbol Table
        ↓ Linker
Executable — Header + Text Segment + Data Segment
        ↓ Loader (OS)
Memory (Text + Data + Stack + Heap)
        ↓ jal 0x00400000
Execution Begins
```

**In practice:** Most compilers (gcc, clang) combine compile+assemble+link in one command.

---

## Step 1: Compilation (C → Assembly)

Compiler translates high-level code into assembly.

### Example: Sum Function

**C Code:**
```c
int f, g, y;              // global variables
int main(void) {
    f = 2;
    g = 3;
    y = sum(f, g);
    return y;
}
int sum(int a, int b) {
    return (a + b);
}
```

**MIPS Assembly:**
```assembly
.data
f:                      # global f
g:                      # global g
y:                      # global y

.text
main:
    addi $sp, $sp, -4       # make stack frame
    sw   $ra, 0($sp)        # store $ra on stack
    addi $a0, $0, 2         # $a0 = 2
    sw   $a0, f             # f = 2
    addi $a1, $0, 3         # $a1 = 3
    sw   $a1, g             # g = 3
    jal  sum                # call sum(f, g)
    sw   $v0, y             # y = sum(f, g)
    lw   $ra, 0($sp)        # restore $ra
    addi $sp, $sp, 4        # restore stack pointer
    jr   $ra                # return to OS

sum:
    add  $v0, $a0, $a1      # $v0 = a + b
    jr   $ra                # return to caller
```

**Directives:**
- `.data` — start of data segment (globals)
- `.text` — start of text segment (code)
- Labels `f:`, `g:`, `y:` name globals; addresses assigned by assembler

---

## Step 2: Assembling (Assembly → Object File)

Assembler converts assembly to machine code in an **object file**. Two passes:

### Pass 1: Assign Addresses & Build Symbol Table

| Address | Instruction |
|---------|-------------|
| 0x00400000 | main: addi $sp, $sp, -4 |
| 0x00400004 | sw $ra, 0($sp) |
| 0x00400008 | addi $a0, $0, 2 |
| 0x0040000C | sw $a0, f |
| 0x00400010 | addi $a1, $0, 3 |
| 0x00400014 | sw $a1, g |
| 0x00400018 | jal sum |

...continues for all instructions...

### Pass 2: Generate Machine Code Using Symbol Table

**Symbol Table (after Pass 1):**
| Symbol | Address | Type |
|--------|---------|------|
| main | 0x00400000 | Label |
| sum | 0x0040002C | Label |
| f | 0x10000000 | Global |
| g | 0x10000004 | Global |
| y | 0x10000008 | Global |

Globals assigned in global data segment starting at 0x10000000.

### Object File Contents
- Machine code (text section)
- Data section (global variable addresses)
- Symbol table (for linking)

---

## Step 3: Linking (Object Files → Executable)

### Why Link?
- Large programs = many source files
- Change one file → only recompile that file
- Library files rarely change
- Unchanged files → reuse object files

### Linker Functions
1. **Combine** all object files into one machine-language file (executable)
2. **Relocate** data/instructions so they don't overlap
3. **Resolve** addresses using symbol tables (adjust relocated globals/labels)

**In our example:** Single object file → no relocation needed.

---

## Step 4: The Executable Structure

**Three Sections:**
| Section | Content |
|---------|---------|
| **Header** | Text size, Data size |
| **Text Segment** | Instructions in memory order |
| **Data Segment** | Global variable addresses |

### Example: First Store Instruction
```
Assembly: sw $a0, f
Machine:  sw $a0, 0x8000($gp)
```
- `$gp = 0x10008000` (middle of global data)
- Offset `0x8000` = 16-bit signed → sign-extended to `0xFFFF8000`
- Effective Address = `$gp + 0xFFFF8000 = 0x10008000 + 0xFFFF8000 = 0x10000000`
- This is address of global `f` ✓

---

## Step 5: Loading (Executable → Memory)

OS loads program by:
1. **Read text segment** from disk → memory text segment (0x00400000)
2. **Set `$gp = 0x10008000`** (middle of global data segment)
3. **Set `$sp = 0x7FFFFFFC`** (top of dynamic data segment)
4. **`jal 0x00400000`** to jump to program start

### Memory at Start of Execution
| Segment | Address Range | Content |
|---------|---------------|---------|
| Text | 0x00400000–0x00400030 | 13 instructions |
| Globals (f,g,y) | 0x10000000–0x10000008 | 3 words |
| Stack | Top at 0x7FFFFFFC | Empty initially |
| Heap | Bottom at 0x10010000 | Empty initially |
| **PC** | **0x00400000** | Points to `main` |

---

## MIPS Memory Map (32-bit = 4 GB)

| Range | Segment | Notes |
|-------|---------|-------|
| 0x00000000 – 0x003FFFFC | Reserved | — |
| **0x00400000 – 0x0FFFFFFC** | **Text** | PC starts at 0x00400000 (~256 MB) |
| **0x10000000 – 0x1000FFFC** | **Global Data** | $gp = 0x10008000 (middle) |
| **0x10010000 – 0x7FFFFFFC** | **Dynamic Data** | Heap (bottom↑), Stack (top↓, $sp=0x7FFFFFFC) |
| 0x80000000 – 0xFFFFFFFC | Reserved | OS, interrupts, MMIO |

### Segment Details

**Text Segment:**
- Stores program code
- Top 4 bits of all text addresses = 0
- **Why?** So `j` instruction (26-bit addr) can reach any text address

**Global Data:**
- Variables declared outside functions in C
- Accessed via `$gp` with 16-bit offset
- `$gp` fixed at 0x10008000 (doesn't change)
- Offset known at assembly time → efficient base addressing

**Dynamic Data (Stack + Heap):**
| Property | Stack | Heap |
|----------|-------|------|
| Use | Save/restore regs; local vars/arrays | malloc/new |
| Allocation | LIFO frames | Any order |
| Direction | Grows **down** from 0x7FFFFFFC | Grows **up** from 0x10010000 |
| Collision | Stack/heap meet → corruption → OOM error | — |

**Reserved:** OS, interrupts, memory-mapped I/O

---

## Key Formulas (Memorize)

```
Pipeline:     C → Assembly → Object → Executable → Memory → Run
Assembler:    Pass 1: addresses + symbol table; Pass 2: machine code
Linker:       Combine + Relocate + Resolve symbols
Loader:       Load text, set $gp=0x10008000, $sp=0x7FFFFFFC, jal 0x00400000

MIPS Memory:  2³² = 4 GB
Text:         0x00400000– (PC starts here)
Global:       0x10000000– ($gp=0x10008000)
Stack:        Grows down from 0x7FFFFFFC
Heap:         Grows up from 0x10010000

Global access:  EA = $gp + SignExt(16-bit offset)
               Offset known at assembly time
```

---

## MCQ Patterns

1. **Translation order** — Compile → Assemble → Link → Load
2. **Assembler passes** — Pass 1: addresses + symbols; Pass 2: machine code
3. **Linker purpose** — Combine object files, relocate, resolve symbols
4. **Loader steps** — Load text, set $gp/$sp, jal to start
5. **MIPS memory map** — Text at 0x00400000, Global at 0x10000000, Stack at 0x7FFFFFFC
6. **$gp vs $sp** — $gp fixed (0x10008000); $sp changes
7. **Global access** — $gp + 16-bit offset (base addressing)
8. **Stack/Heap direction** — Stack DOWN, Heap UP
9. **Text segment top bits** — All 0 → enables `j` to reach anywhere
10. **sw $a0, 0x8000($gp)** — offset sign-extended: 0x8000 → 0xFFFF8000 → EA = 0x10000000

---

<a id="topic-7"></a>
## Topic Module 7: 24_parallelism.md
**Source File**: `docs/24_parallelism.md`

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

---

<a id="topic-8"></a>
## Topic Module 8: 25_classwork-problems.md
**Source File**: `docs/25_classwork-problems.md`

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

---

<a id="topic-9"></a>
## Topic Module 9: 26_unit3-mcq-practice.md
**Source File**: `docs/26_unit3-mcq-practice.md`

# 26. Unit 3 MCQ Practice — Architecture, Assembly, Memory, Parallelism

> **Source:** Unit 3 Slides (3.14.1, 3.14.2, 3.15.1, 3.17.1) MCQs | Textbook: Harris & Harris Ch. 6, 7

---

## Addressing Modes (3.14.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | Register-only addressing used by which MIPS instructions? | R-type |
| 2 | In immediate addressing, the constant operand is: | Encoded within the instruction itself |
| 3 | Which MIPS instructions use base addressing? | lw and sw |
| 4 | In base addressing, effective address = | Base Register + Sign-Extended Offset |
| 5 | PC-relative addressing mainly used by: | Conditional branch instructions (beq, bne) |
| 6 | In PC-relative, branch target calculated relative to: | PC + 4 |
| 7 | Which addressing mode used by j and jal? | Pseudo-direct Addressing |

**Answer Key:** Q1:C, Q2:C, Q3:C, Q4:B, Q5:C, Q6:B, Q7:D

---

## Compiling, Assembling, Loading (3.14.2)

| # | Question | Answer |
|---|----------|--------|
| 1 | Which segment does j instruction rely on? | Text — top 4 bits of addresses are 0 |
| 2 | Value of $gp at program start? | 0x10008000 (middle of global data) |
| 3 | Why can globals be reached efficiently via $gp? | 16-bit offset known at assembly time, base addressing |
| 4 | Correct statement about dynamic data segment? | Stack grows down from 0x7FFFFFFC, heap grows up |
| 5 | What does assembler do on Pass 1? | Assigns instruction addresses, finds all symbols |
| 6 | sw $a0, 0x8000($gp) stores to which address? | 0x10008000 + 0xFFFF8000 = 0x10000000 |
| 7 | Correct order of translation steps? | Compile → Assemble → Link → Load |

**Answer Key:** Q1:B, Q2:C, Q3:B, Q4:B, Q5:C, Q6:B, Q7:C

---

## Parallelism (3.15.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | Parallelism primarily aims to improve: | Throughput |
| 2 | A token in a parallel system refers to: | A unit of work moving through the system |
| 3 | Which parallelism uses multiple hardware units? | Spatial Parallelism |
| 4 | Pipeline registers are inserted to: | Divide combinational logic into stages |
| 5 | Modern processors combine: | Spatial and temporal parallelism |
| 6 | Increasing pipeline stages generally: | Improves throughput but may increase latency |
| 7 | Metric indicating useful work over time: | Throughput |
| 8 | Real-world example of temporal parallelism: | Assembly line (different stages on different products) |

**Answer Key:** Q1:B, Q2:B, Q3:B, Q4:B, Q5:C, Q6:A, Q7:B, Q8:B

---

## Assembly & Machine Language (3.7.1, 3.9.1, 3.11.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | Primary role of Program Counter (PC)? | Hold address of next instruction to execute |
| 2 | Assembly vs Machine code distinction? | Assembly is human-readable, must be translated to machine code |
| 3 | Which instruction transfers control when two registers equal? | beq |
| 4 | Instruction commonly used to return from function? | jr |
| 5 | In if-else, why is `j done` used? | To skip else block after executing if block |
| 6 | In while loop, which instruction causes repeat? | j while |
| 7 | Correct for-loop execution order? | Initialization → Condition → Statement → Update |
| 8 | Array base 0x10007000, what address accessed? | (Depends on index: base + 4×index) |
| 9 | In R-type, which field identifies ALU op when op=0? | funct |
| 10 | Which immediates use zero extension? | andi, ori, xori |
| 11 | In sra, new MSBs filled with: | Sign bit |
| 12 | In sllv, shift amount from: | Lower 5 bits of rs |
| 13 | Instruction format for j? | J-type |
| 14 | beq vs bne? | beq: branch if equal; bne: branch if not equal |

**Answer Key:** Q1:B, Q2:C, Q3:C, Q4:D, Q5:B, Q6:C, Q7:B, Q8:B, Q9:B, Q10:B, Q11:B, Q12:B, Q13:C, Q14:beq=equal, bne=not equal

---

## Classwork Problems (3.17.1)

| # | Question | Answer |
|---|----------|--------|
| 1 | 32-bit Up/Down counter: Q⁺ when Reset=0, Up=1? | Q + 1 |
| 2 | Up/Down counter convenient form: Q⁺ = Q + (2·Up - 1)? | Up=1→+1, Up=0→-1 |
| 3 | 32-bit counter adding 4: Q⁺ = ? | Q + 4 |
| 4 | 16×3 ROM address inputs? | 4 (A,B,C,D) |
| 5 | Byte address of memory word 42? | 42 × 4 = 168 = 0xA8 |
| 6 | Word 42 spans which byte addresses? | 0xA8, 0xA9, 0xAA, 0xAB |
| 7 | Big-endian stores 0xFF223344 at 0xA8: | A8:FF, A9:22, AA:33, AB:44 |
| 8 | Little-endian stores 0xFF223344 at 0xA8: | A8:44, A9:33, AA:22, AB:FF |
| 9 | Byte address of memory word 15? | 15 × 4 = 60 = 0x3C |

---

## High-Yield Unit 3 MCQ Patterns

| Topic | Pattern |
|-------|---------|
| **Addressing Modes** | Register=R-type, Immediate=constant in instr, Base=lw/sw (Base+Offset), PC-Rel=beq/bne ((PC+4)+Off×4), Pseudo-Direct=j/jal (26-bit+PC[31:28]) |
| **Memory Map** | Text@0x00400000, Global@0x10000000 ($gp=0x10008000), Stack@0x7FFFFFFC↓, Heap@0x10010000↑ |
| **Translation Pipeline** | Compile→Assemble(2 pass)→Link→Load; Pass1=addresses+symbols, Pass2=machine code |
| **Global Access** | $gp fixed, offset known at assembly, base addressing |
| **Stack/Heap** | Stack grows DOWN, Heap grows UP |
| **Function Calls** | Args→$a0-$a3, Return→$v0, Call→jal ($ra=PC+4), Return→jr $ra, Preserved=$s0-$s7,$ra,$sp |
| **Branches** | beq=branch if equal, bne=branch if not equal, offset from PC+4 |
| **Loops** | while: beq exit + j loop; for: init→beq exit→body→update→j for |
| **Arrays** | int: base+4i, char: base+i; lbu=zero-extend, lb=sign-extend, sb=store byte |
| **Endianness** | Big: MSB@low addr; Little: LSB@low addr |
| **Parallelism** | Throughput not latency; Spatial=more HW, Temporal=pipelining |
| **Pipeline** | Clock=slowest stage; TP=1/Tc; Latency=N×Tc; Hazards: Data(RAW)=forwarding, Control=prediction, Structural=duplicate HW |
| **Amdahl's Law** | Speedup = 1/[(1-f)+f/s] |
| **Machine Code** | op=0→R-type(check funct); op=35→lw; op=43→sw; op=4→beq; op=2→j; funct: add=32, sub=34, jr=8 |

---

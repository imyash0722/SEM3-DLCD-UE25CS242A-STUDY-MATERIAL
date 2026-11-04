# UNIT 2: FINITE STATE MACHINES & DIGITAL BUILDING BLOCKS
**Generated**: 2026-11-04 14:14:16
**Course**: Digital Logic and Computer Design (DLCD) — UE25CS242A / UE25CS251A

---

## TABLE OF CONTENTS

### PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS
1. [DLCD - Unit 2 Combined Lecture Slides (139 Pages)](#doc-1) — *Source: `resources/DLCD - Unit 2 Combined Slides.pdf`*
2. [Unit 2 Question Bank Solved (10 Pages)](#doc-2) — *Source: `resources/U2QB_soln.docx`*
3. [Unit 2 Descriptive Question Bank (2 Pages)](#doc-3) — *Source: `resources/U2QB.docx`*
4. [Unit 2 Multiple Choice Questions Set 1 (13 Pages)](#doc-4) — *Source: `resources/U2MCQ1.docx`*
5. [Unit 2 Multiple Choice Questions Set 2 (6 Pages)](#doc-5) — *Source: `resources/U2MCQ2.docx`*
6. [Unit 2 Multiple Choice Questions Set 3 - Number Systems (21 Pages)](#doc-6) — *Source: `resources/U2MCQ3.pdf`*
7. [Lecture Notes: Finite State Machines Comprehensive (24 Pages)](#doc-7) — *Source: `notes/FSM.pdf`*
8. [Lecture Notes: Unit 2 Topics Part 1 (15 Pages)](#doc-8) — *Source: `notes/U2N1.pdf`*
9. [Lecture Notes: Unit 2 Topics Part 2 (13 Pages)](#doc-9) — *Source: `notes/U2N2.pdf`*
10. [Lab Week 8: Prefix Adder and 4-bit Comparator Submission (6 Pages)](#doc-10) — *Source: `lab/week8/PES2UG25CS615_Yashwanth K_DLCDLab8.docx`*

### PART 2: DLCD SYNTHESIZED STUDY PACKAGE (Clean Slides, Question Banks, MCQs)
1. [DLCD_Unit_2_Clean_Slides.md](#res-1)
2. [DLCD_Unit_2_Question_Bank.md](#res-2)
3. [DLCD_Unit_2_MCQs.md](#res-3)

### PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS
1. [08_fsm-moore-mealy-design.md](#topic-1)
2. [09_state-encoding-factoring.md](#topic-2)
3. [10_arithmetic-adders.md](#topic-3)
4. [11_alu-comparator-shifter-multiplier.md](#topic-4)
5. [12_number-systems-fixedpoint.md](#topic-5)
6. [13_floating-point-ieee754.md](#topic-6)

---

# PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS

<a id="doc-1"></a>
## Document 1: DLCD - Unit 2 Combined Lecture Slides (139 Pages)
**Source Document**: `resources/DLCD - Unit 2 Combined Slides.pdf`
**OCR Extraction File**: `Resources_DLCD - Unit 2 Combined Slides.txt`

```
================================================================================
ORIGINAL DOCUMENT : DLCD - Unit 2 Combined Slides.pdf
OCR PDF FILE      : Resources_DLCD - Unit 2 Combined Slides_ocr.pdf
TOTAL PAGES       : 139
WORD COUNT        : 7849
CHARACTER COUNT   : 46073
DATE EXTRACTED    : 2026-11-04 14:10:32
================================================================================

--- [Page 1 of 139] ---
DIGITAL LOGIC AND COMPUTER DESIGN
FINITE STATE MACHINES

--- [Page 2 of 139] ---
% UNIVERSITY 
Number of 
Registers (k) 
Possible States (2%) 
Finite State Machine (FSM):
• A Finite State Machine (FSM) is a model used to design synchronous sequential
circuits.
•
It works by moving between a limited (finite) number of states based on the current
inputs and the present state of the circuit.
• A circuit containing k registers can have 2ᵏdifferent states because each register
stores one bit of information. The FSM can be in only one state at a time.
KEY POINT
Finite State Machine (FSM)
A digital circuit that stores its 
current state and changes to 
the next state on every clock 
edge. "Finite" means the 
machine has only a limited 
number of possible states. 
DIGITAL LOGIC AND COMPUTER DESIGN
FINITE STATE MACHINES

--- [Page 3 of 139] ---
PES 
UNIVERSITY 
Input =1 
Input =0 
An FSM consists of:
•M Inputs – Signals received from the external
system.
•N Outputs – Signals produced by the circuit.
•k-bit State Register – Stores the current state
of the FSM.
•Clock Signal (CLK) – Controls when the state
changes.
•Optional Reset Signal – Returns the FSM to its
initial state.
DIGITAL LOGIC AND COMPUTER DESIGN
FINITE STATE MACHINE

--- [Page 4 of 139] ---
PES 
UNIVERSITY 
Current State 
+ Inputs 
( 
) 
Next State Logic 
. 
7 
R’ 
State Register 
(CLK) 
& 
J 
, 
4 
N 
Output Logic 
- 
7 
v 
o 
DIGITAL LOGIC AND COMPUTER DESIGN
BASIC STRUCTURE OF FSM
A Finite State Machine consists of three main components
that work together to determine the circuit's behavior.
1. Next State Logic
2. State Register (Memory)
3. Output Logic
1.Next State Logic:
Computes the next state of the FSM.
2. State Register (Memory)
Stores the present state of the FSM. Updates the stored state on every clock edge (CLK).
3. Output Logic
Generates the output signals of the FSM.

--- [Page 5 of 139] ---
PES 
UNIVERSITY 
Current State 
+ Inputs 
( 
) 
Next State Logic 
. 
7 
R’ 
State Register 
(CLK) 
& 
J 
, 
4 
N 
Output Logic 
- 
7 
v 
o 
DIGITAL LOGIC AND COMPUTER DESIGN
BASIC STRUCTURE OF FSM
The outputs are determined based on the type of FSM:
Moore Machine: Output depends only on the current
state.
Mealy Machine: Output depends on the current state
and current inputs.
Working Principle:
On every clock edge, the FSM:
1.Reads the current state.
2.Accepts the current inputs.
3.Computes the next state.
4.Updates the state register.
5.Produces the required outputs.

--- [Page 6 of 139] ---
Inputs +— 
(a) Moore machine, 
- 
outputs 
CLK 
next 
| k "X %?k 
| 
stals 
slale 
; 
State 
flui[‘ful 
o0k 
’ 
’ 
logic 
____/ 
— 
__/ 
O PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
TYPES OF FSM
Moore Machine:
Output depends only on the current state. Changes in input do not immediately
affect the output. Output changes only after the state changes.
Output = f(Current State)

--- [Page 7 of 139] ---
Inputs 
—— outputs 
CLK 
next | k "X 
| 
| 
nfe 
1/ 
state 
, state | output 
——_/ 
____/ 
(b) Mealy machine 
O PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
TYPES OF FSM
Mealy Machine
Output depends on both the current state and the current inputs. Output can change
immediately when the input changes. Generally requires fewer states than a Moore
machine.
Output = f(Current State, Current Input)

--- [Page 8 of 139] ---
PES 
UNIVERSITY 
Meet Ben, a smart engineering student 
who loves solving real-world problems. 
/= = S 
| 
| ATHLETIC [ 
DIGITAL LOGIC AND COMPUTER DESIGN
FSM DESIGN EXAMPLE
One day, while walking across campus, Ben notices
the busy intersection between Academic Avenue and
Bravado Boulevard.
Students are moving between the Dormitories and
the Labs on Academic Ave.
Football players are traveling between the Athletic
Fields and the Dining Hall on Bravado Blvd.
Since many people are busy and not paying
attention, several accidents have already occurred at
the intersection.
The Dean of Students asks Ben to design an
automatic traffic light controller

--- [Page 9 of 139] ---
é@ UNIVERSITY 
Dining 
Hall 
6 
Academic ‘ . 
Ave. 
@ openelg 
Labs 
L 
Dorms 
Z | Athletic 
= | Fields 
Campus map 
DIGITAL LOGIC AND COMPUTER DESIGN
FSM DESIGN EXAMPLE
Ben decides to solve the problem using a Finite
State Machine (FSM) that can monitor traffic
and control the signals automatically.
Solution:
Design an FSM-based traffic light controller
that uses traffic sensors to control the traffic
lights and ensure safe, smooth traffic flow at
the campus intersection.

--- [Page 10 of 139] ---
The FSM has: 
*2Inputs: Ty, Ty 
O 
CLK 
T4 
Traffic 
Light 
Ts 
Controller 
PES 
UNIVERSITY 
e = 
Black box view 
| 
Reset 
e TM 
DIGITAL LOGIC AND COMPUTER DESIGN
FSM DESIGN EXAMPLE
•Clock (CLK): The controller checks traffic and updates 
the signals every 5 seconds. 
•Reset: Initializes the FSM to its starting state when 
the controller is turned on.
•2 Outputs: LA, LB
Sensor
Location
Function
Tₐ
Academic 
Avenue
Detects vehicles on Academic 
Avenue.
Tᵦ
Bravado 
Boulevar
d
Detects vehicles on Bravado 
Boulevard.
Traffic Light
Controls
Lₐ
Academic Avenue
Lᵦ
Bravado Boulevard

--- [Page 11 of 139] ---
demic Ave. (L) 
Bravado Blvd. (Lg) 
S0 
green 
red 
S1 
yellow 
red 
52 
red 
green 
83 
red 
vellow 
O PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION DIAGRAM
Each circle represents a state, and the directed
arrows represent the transitions between states
based on the traffic sensor inputs.
Overview :
STATES:
•Moore FSM: outputs labeled in each state
•States: Circles
•Transitions: Arcs

--- [Page 12 of 139] ---
% UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION DIAGRAM

--- [Page 13 of 139] ---
% UNIVERSITY 
L, yellow 
Lg: red 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION DIAGRAM

--- [Page 14 of 139] ---
% UNIVERSITY 
L, yellow 
L red 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION DIAGRAM

--- [Page 15 of 139] ---
% UNIVERSITY 
S 
L, yellow 
Lg:red 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION DIAGRAM

--- [Page 16 of 139] ---
PES 
UNIVERSITY 
State Transitions 
— 
Reset—S0 
The FSM always enters State SO whenever the 
Reset signal is activated. 
S0 — $1: If T, = 0, the controller changes from SO 
to S1. 
After 
After 
S1-5S2: 
After 
5 
seconds, 
the 
controller " 
? seconds 
automatically changes from S1 to S2. 
S2 — S3: If Ty = 0, the controller changes from 
S2 to S3. 
S3 — S0: After 5 seconds, the controller returns to 
S0, completing one traffic signal cycle. 
Conditions for Remaining in the Same State: 
S0 — S0whenT, =1 
State transition diagram 
S2 ->S2whenTz =1 
L.: Green 
Lg: Red 
La: Yellow 
Lg: Red 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION DIAGRAM

--- [Page 17 of 139] ---
é@ UNIVERSITY 
| a' After creating the State Transition Diagram, Ben converts it 
Table 3.1 State transition table 
Q into a State Transition Table. The table specifies the next state 
of the FSM for every combination of the current state and 
input conditions. 
Current 
Inputs 
MNext State 
State S 
T'a 
Ip 
8 
X (Don't Care) :means that the value of that 
input does not affect the next state. 
Sl 
X 
X 
52 
Examples: 
*|In S1, the FSM always moves to S2, regardless 
32 
A 
0 
33 
of Ty or Tp. 
) 
Y 
1 
) 
*In S3, the FSM always returns to SO, regardless 
of the sensor inputs. 
S3 
X 
X 
S0 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION TABLE
The State Transition Table is a bridge between
the graphical FSM representation and the
digital hardware implementation.

--- [Page 18 of 139] ---
% UNIVERSITY 
Table 3.2 State encoding 
Table 3.3 Output encoding 
State 
Encoding S1. 
Output 
Encoding Li.q 
- 
green 
00 
S1 
01 
< 
10 
yellow 
01 
S3 
11 
red 
10 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE AND OUTPUT ENCODING
Before implementing the FSM using digital hardware, the states and outputs must be
represented in binary form. This process is called Encoding.
1. State Encoding
Each state is assigned a unique 
binary code.
2. Output Encoding
Each traffic light color is also represented using 
binary values.

--- [Page 19 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE AND OUTPUT ENCODING
Why Encoding?
•
Converts symbolic states into binary values.
• Makes the FSM compatible with digital circuits.
• Simplifies the derivation of Boolean equations.
Key Observation
• Every state and output now has a unique binary representation
• Encoding transforms the FSM from a conceptual model into a form that can
be implemented using digital hardware.

--- [Page 20 of 139] ---
% UNIVERSITY 
Table 3.4 State transition table with binary encodings 
Table 3.5 Output table 
Current State 
Inputs 
Next State 
0 
Current State 
Outputs 
Lfllfi) 
Lfil 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE AND OUTPUT ENCODING
After assigning binary codes to each state, the State Transition Table is updated
using these binary encodings.

--- [Page 21 of 139] ---
% UNIVERSITY 
The revised table defines the next state (5;’Sy)as a function of the Current State 
(51’ Sy) and Inputs (Ty Tg) 
S; = El So +S1§.DTB + S-lggTB 
DIGITAL LOGIC AND COMPUTER DESIGN
NEXT STATE LOGIC
• The Next-State Equations determine which state the FSM should move to based on
the current state and the sensor inputs.
• The Boolean equations obtained from the state transition table can be simplified
using Karnaugh Maps (K-Maps) or by inspection.
• This reduces the number of logic gates, makes the circuit simpler and improves
hardware efficiency.

--- [Page 22 of 139] ---
E ; } UNIVERSITY 
Table 3.5 Output table 
Output Equations 
Current State 
Outputs 
Ly =5 
5 
1 
Ly 
Ly 
Lo = 51_50 
Lpy =5 
Lo = 515 
DIGITAL LOGIC AND COMPUTER DESIGN
OUTPUT LOGIC
Similarly the output table using the binary
encoding is Table 3.5

--- [Page 23 of 139] ---
(TN .4 
s, 
=P 
S'o 
So 
r 
| 
FReset 
state register 
(a) 
PES 
UNIVERSITY 
Te 
Sy 
iNnputs 
(b) 
— 
— > 
(c) 
' gD_I_‘tl—\ 
S'o 
So 
=D 
| 
So 
Nnext state logic 
| 
IL.--il.:lI 
Sy 
= 
| 
output 
outputs 
logic 
Figure 3.26 State machine circuit for traffic light controller 
DIGITAL LOGIC AND COMPUTER DESIGN
COMPLETE FSM LOGIC CIRCUIT

--- [Page 24 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE ENCODING
• State Encoding is the process of assigning binary codes to the states of a Finite State
Machine (FSM).
• The choice of encoding directly affects the hardware implementation, including the
number of logic gates, propagation delay, and overall circuit complexity.
Different state encodings can produce different:
• circuit implementations
• numbers of logic gates
• propagation delays
• hardware complexity
Therefore, selecting an appropriate encoding helps in designing an efficient FSM.

--- [Page 25 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE ENCODING
• Finding the optimal encoding is difficult because it requires checking all possible
encoding combinations, which becomes impractical as the number of states increases.
• Instead, designers usually choose a suitable encoding based on the application or use
Computer-Aided Design (CAD) tools to help select an efficient encoding.
• The choice of state encoding influences the speed, size, and complexity of the final
digital circuit.

--- [Page 26 of 139] ---
% UNIVERSITY 
In Binary Encoding, each state of the FSM is represented using a binary number. 
For an FSM with K states, the number of bits required is: 
lngK 
Only the minimum number of bits needed to represent all states is used. 
Ex:For 4 states 
DIGITAL LOGIC AND COMPUTER DESIGN
BINARY ENCODING
State
Binary Code
S0
00
S1
01
S2
10
S3
11
Advantages
• Uses fewer state bits and requires fewer flip-flops
•
Efficient hardware utilization

--- [Page 27 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
ONE HOT ENCODING
In One-Hot Encoding, each state is assigned a separate bit.
Only one bit is HIGH (1) at any given time, while all other bits remain LOW (0).
For K states, K bits are required.
Example:For 3 states
State
Encoding
S0
001
S1
010
S2
100
Advantages
Simpler combinational logic and faster implementation
Disadvantages
Requires more flip-flops and higher hardware cost

--- [Page 28 of 139] ---
PES 
UNIVERSITY 
Reset 
Figure 3.28 Divide-by-3 counter 
(a) waveform and (b) state 
transition diagram 
DIGITAL LOGIC AND COMPUTER DESIGN
DESIGNING A DIVIDE-BY-3-COUNTER
To understand how different state encoding techniques are applied, consider the
design of a Divide-by-3 Counter.
A Divide-by-3 Counter is a sequential circuit that reduces the frequency of the
input clock by a factor of 3.
System Description:
• The FSM has one output (Y) and three states
S0, S1, and S2 .
• The output Y becomes HIGH (1) for one clock
cycle out of every three clock cycles.

--- [Page 29 of 139] ---
% UNIVERSITY 
CLK 
Y / 
\ 
/ 
\ 
(a) 
Reset 
Figure 3.28 Divide-by-3 counter 
(a) waveform and (b) state 
o e e 
transition diagram 
DIGITAL LOGIC AND COMPUTER DESIGN
DESIGNING A DIVIDE-BY-3-COUNTER
Operation:
The counter continuously cycles through the following sequence:
S0 →S1 →S2 →S0 →...
This repeating sequence divides the clock frequency by 3.

--- [Page 30 of 139] ---
% UNIVERSITY 
Table 3.6 Divide-by-3 counter 
state transition table 
51 
52 
52 
S0 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION TABLE
1. State Transition Table:
The State Transition Table defines the next state for every current state.

--- [Page 31 of 139] ---
% UNIVERSITY 
Table 3.7 Divide-by-3 counter 
output table 
51 
0 
52 
0 
DIGITAL LOGIC AND COMPUTER DESIGN
OUTPUT TABLE
2. Output Table:
The Output Table specifies the output value associated with each state.

--- [Page 32 of 139] ---
% UNIVERSITY 
Table 3.8 One-hot and binary encodings for divide-by-3 counter 
, 
One-Hot Encoding 
Binary Encoding 
Stfltf 
X 
X 
1 
1 
1 
\p: 
\Y 
AR 
\} 
\f 
51 
0 
1 
0 
0 
1 
52 
1 
0 
() 
1 
0 
DIGITAL LOGIC AND COMPUTER DESIGN
BINARY VS ONE HOT ENCODING
To implement the Divide-by-3 Counter in hardware, each state must be assigned
a binary code. Two commonly used encoding techniques are Binary Encoding and
One-Hot Encoding.

--- [Page 33 of 139] ---
% UNIVERSITY 
Table 3.9 State transition table with binary encoding 
Current State 
Next State 
Ay 
So 
A 
5 
0 
0 
0 
1 
0 
1 
1 
0 
1 
0 
0 
0 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION TABLE USING BINARY ENCODING
Binary State Transition Table
• The Binary State Transition Table uses the 2-bit binary codes assigned to each state.
• States are represented using 2 bits.

--- [Page 34 of 139] ---
% UNIVERSITY 
Table 3.10 State transition table with one-hot encoding 
Current State 
Next State 
DIGITAL LOGIC AND COMPUTER DESIGN
STATE TRANSITION TABLE USING ONE-HOT ENCODING
• Each state is represented by a unique active bit. Only one bit is HIGH at any time.
One-Hot State Transition Table
• The One-Hot State Transition Table uses one flip-flop for each state

--- [Page 35 of 139] ---
S 
next state logic 
state reqister 
] 
So 
v 
—=C 
C 
Reset 
output logic 
}Y 
CLK 
Reset 
output 
O PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
FSM IMPLEMENTATION
Binary Encoding Implementation:
One-Hot Encoding Implementation:

--- [Page 36 of 139] ---
DIGITAL LOGIC AND COMPUTER DESIGN
FINITE STATE MACHINES

--- [Page 37 of 139] ---
% UNIVERSITY 
CLK 
I naxl'k““‘%?k 
| 
N 
inpuls-/—_ 
date 
| 
slale 
Sate | outpul - 
Oulpu 
. 
logic 
| —) 
Y| 
2 Finite state 
(a) Moore machine, 
DIGITAL LOGIC AND COMPUTER DESIGN
TYPES OF FSM
Moore Machine:
Output depends only on the current state. Changes in input do not immediately
affect the output. Output changes only after the state changes. Outputs are written
inside the state circles.
Formula
Output = f(Current State)
KEY POINT
Moore machines 
usually require more 
states than Mealy 
machines for the same 
problem.

--- [Page 38 of 139] ---
inputs +—— 
(b) Mealy machine 
CLK 
' 
\ 
next %7 
r 
‘ 
et | K 
K 
L 
, 
stale | 
|, state | output 
| 
state 
- 
i 
logic 
\L 
— 
—__/ 
-~ outputs 
O PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
TYPES OF FSM
Mealy Machine
Output depends on both the current state and the current inputs. Output can change
immediately when the input changes. Generally requires fewer states than a Moore
machine. Outputs are written on the transition arrows.
Formula
Output = f(Current State, Current Input)

--- [Page 39 of 139] ---
Scenario:
Alyssa P. Hacker owns a pet robotic snail controlled by a Finite State
Machine (FSM).The snail moves over a paper tape containing a
sequence of 1s and 0s.
At every clock cycle:
The snail moves one position forward.
It remembers the last two bits it has read.
The snail smiles when a specific bit pattern is detected.
DIGITAL LOGIC AND COMPUTER DESIGN
MOORE VS MEALY MACHINES
Input: [A] Current bit read by the snail.
Output:[Y]
•Y = 1 →Snail smiles.
•Y = 0 →Snail does not smile.

--- [Page 40 of 139] ---
PES 
UNIVERSITY 
FSM state transition diagrams: (a) Moore machine, 
DIGITAL LOGIC AND COMPUTER DESIGN
MOORE VS MEALY MACHINES
Objective
Design both Moore Machine and Mealy Machine .Compare both implementations.
The Moore Machine requires three states. Each state represents the 
previous input history.The output depends only on the current state.
Moore FSM Design :

--- [Page 41 of 139] ---
DIGITAL LOGIC AND COMPUTER DESIGN
MOORE VS MEALY MACHINES
Mealy Machine Design:
The Mealy Machine requires only two states. Outputs are generated during state 
transitions. 
Each transition is labelled as Input / Output

--- [Page 42 of 139] ---
% UNIVERSITY 
Table 3.11 Moore state transition table 
Table 3.12 Moore output table 
50 
1 
50 
51 
0 
51 
51 
1 
52 
51 
0 
52 
0 
51 
52 
1 
52 
1 
50 
DIGITAL LOGIC AND COMPUTER DESIGN
MOORE TRANSITION AND OUTPUT TABLE

--- [Page 43 of 139] ---
% UNIVERSITY 
Table 3.13 Moore state transition table with state 
encodings 
Table 3.14 Moore output table 
Current State 
Input 
Next State 
with state encodings 
So 
A 
3, 
\Y 
0 
0 
0 
0 
1 
0 
0 
1 
0 
0 
0 
0 
0 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
1 
1 
0 
| 
0 
| 
1 
0 
0 
0 
1 
1 
0 
1 
0 
0 
DIGITAL LOGIC AND COMPUTER DESIGN
MOORE TRANSITION AND OUTPUT TABLE WITH BINARY ENCODING
To implement the Moore Machine in digital hardware,each state is assigned a binary
code.Using these binary encodings,the transition table and output table are rewritten.

--- [Page 44 of 139] ---
PES 
UNIVERSITY 
Table 3.13 Moore state transition table with state 
encodings 
Table 3.14 Moore output table 
1 
So 
A 
1 
S 
with state encodings 
Current State 
Input 
Next State 
5 
O 
O 
0 
0 
1 
O 
0 
1 
0 
O 
O 
1 
O 
O 
1 
0 
0 
0 
O 
1 
1 
1 
O 
1 
O 
0 
O 
1 
0 
1 
0 
1 
O 
1 
O 
O 
1 
0 
1 
S 
= SpA 
b=A 
DIGITAL LOGIC AND COMPUTER DESIGN
MOORE FSM
Equations:
Equation 3.3.1

--- [Page 45 of 139] ---
% UNIVERSITY 
Table 3.15 Mealy state transition and output table 
Table 3,16 Mealy state transition and output table with state encodings 
Current State 
Input 
Next State 
Output 
Current State ~ Input ~ Next State ~ Output 
DIGITAL LOGIC AND COMPUTER DESIGN
MEALY TRANSITION AND OUTPUT TABLE
The Mealy Machine requires only one state bit.

--- [Page 46 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
MOORE VS MEALY MACHINES
Moore Machine
Mealy Machine
More states
Fewer states
Stable output
Faster response
Output depends only on state
Output depends on state and input
One clock delay
Immediate output
Comparison:
• Choose a Moore Machine when stable outputs are important.
• Choose a Mealy Machine when faster output response is required.

--- [Page 47 of 139] ---
DIGITAL LOGIC AND COMPUTER DESIGN
FINITE STATE MACHINES

--- [Page 48 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
FACTORING STATE MACHINES
As the complexity of a Finite State Machine (FSM) increases, designing and maintaining it 
becomes difficult.
Instead of designing one large FSM, the system can be divided into multiple smaller FSMs 
that work together.
This design approach is called Factoring of State Machines.
How Does It Work?
• A complex FSM is split into smaller interacting FSMs. 
• The output of one FSM can be used as the input to another FSM. 
• This creates a hierarchical and modular design.

--- [Page 49 of 139] ---
% UNIVERSITY 
P—» 
:- 
TM 
Controller 
[*” Ly 
A—» 
FSM 
p— 
L 
(a) single traffic light controller FSM 
DIGITAL LOGIC AND COMPUTER DESIGN
FACTORED AND UNFACTORED STATE MACHINES
To understand the concept of factoring, consider the traffic light controller introduced 
earlier.
The controller is now modified to include a Parade Mode, which keeps the Bravado 
Boulevard traffic light green while a parade is in progress.
Additional Inputs:
Two new control inputs are introduced:
• P (Parade) – Enables Parade Mode. 
• R (Resume) – Exits Parade Mode.

--- [Page 50 of 139] ---
Ly 
FSM 
PES 
UNIVERSITY 
> 
Mode 
TaT® 
Lights 
> 
| 
Tot» 
FSM 
: > 
| 
| 
| 
I 
I 
Controller 
I 
: 
FSM 
: 
(b) 
| 
_ 
(b) factored designs for modified 
traffic light controller FSM 
DIGITAL LOGIC AND COMPUTER DESIGN
FACTORED AND UNFACTORED STATE MACHINES
Controller Behaviour:
• When P = 1, the controller enters Parade Mode. 
•During Parade Mode, the controller follows its normal sequence 
until LB becomes green. 
• Once LB is green, it remains green throughout the parade. 
• When R = 1, the controller exits Parade Mode and resumes normal 
traffic operation. 
Objective:
Design the controller using:
• A single FSM (Unfactored). 
• Multiple interacting FSMs (Factored).

--- [Page 51 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
UNFACTORED FSM
Single FSM Approach:
In the unfactored design, a single FSM controls both:
• Normal traffic operation. 
• Parade mode. 
State Organization
• S0 – S3 → Normal Mode. 
• S4 – S7 → Parade Mode. 
The two halves of the state diagram are almost identical, except that during 
Parade Mode the controller remains in State S6 while LB remains green.
Characteristics
• One large FSM. 
• More states. 
• Complex transitions. 
•Difficult to modify and debug.

--- [Page 52 of 139] ---
PES 
UNIVERSITY 
L, yellow 
S5 
; 
L,: vellow 
L red 
(a) unfactored, 
DIGITAL LOGIC AND COMPUTER DESIGN
UNFACTORED FSM

--- [Page 53 of 139] ---
PES 
UNIVERSITY 
Mode FSM 
Lights FSM 
(b) factored 
DIGITAL LOGIC AND COMPUTER DESIGN
FACTORED FSM
Breaking the FSM into Modules:
Instead of using one large FSM, the controller is divided into two smaller FSMs.
Mode FSM:
Tracks whether the controller is operating in:
• Normal Mode 
•Parade Mode 
Produces output: M
Lights FSM
Controls the traffic lights using:
• Traffic Sensors (TA, TB) 
• Mode Signal (M)

--- [Page 54 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
FACTORED VS UNFACTORED FSM
Unfactored FSM
Factored FSM
Single large FSM
Multiple smaller FSMs
More states
Fewer states per FSM
Complex transitions
Simpler transitions
Difficult to debug
Easier to debug
Less modular
Highly modular
Harder to modify
Easy to extend

--- [Page 55 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
DERIVING AN FSM FROM SCHEMATIC
STEPS FOR DERIVING FSM:
1.Examine the circuit and identify Inputs,Outputs ,State bits.
2.Write the next-state and output equations.
3.Create the next-state and output tables.
4.Remove unreachable states.
5.Assign symbolic names to valid states.
6.Draw the state transition diagram.
7.Describe the overall function of the FSM.

--- [Page 56 of 139] ---
% UNIVERSITY 
q—/‘ 
Unlock 
—I_j'l 
Reset 
Figure 3.325 Circuit of found FSM for Example 3.9 
Scenario:
Alyssa P. Hacker discovers that the keypad lock in her house has been rewired, and the
original unlock code no longer works.She finds a circuit diagram attached to the keypad
and suspects it is controlled by a Finite State Machine (FSM).To determine the correct
unlock sequence, she decides to derive the FSM from the circuit.
DIGITAL LOGIC AND COMPUTER DESIGN
EXAMPLE

--- [Page 57 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
STEP1: IDENTIFICATION
Objective
Determine the FSM states ,State transitions ,Output behaviour
and Overall
function of the circuit
Step 1 – Identify Inputs, Outputs & State Equations:
From the circuit:
Inputs: A₁ ,A₀
Output: Unlock
State Bits: S₁ ,S₀
Next-State Equations:
S₁' = S₀A₁A₀
S₀' = S̅₁S₀A₁A₀
Unlock = S₁
Equation (3.12)

--- [Page 58 of 139] ---
PES 
Table 3.17 Next state table derived from circuit é@ UNIVERSITY 
Current State 
Input 
- Next State 
Sy 
So 
Ay 
Ag 
3 
30 
0 
0 
0 
0 
0 
0 
0 
0 
0 
1 
0 
0 
0 
0 
1 
0 
0 
0 
Table 3.18 Output table derived from circuit 
0 
0 
1 
1 
0 
1 
in Figure 3.35 
0 
1 
0 
0 
0 
0 
Current State 
Output 
0 
! 
0 
! 
! 
0 
S, 
So 
Unlock 
0 
! 
! 
0 
0 
0 
0 
1 
1 
1 
0 
0 
0 
0 
0 
1 
0 
0 
0 
0 
0 
0 
1 
0 
1 
0 
0 
1 
0 
0 
1 
0 
1 
0 
0 
0 
1 
0 
1 
1 
0 
1 
1 
0 
0 
1 
1 
1 
1 
1 
0 
0 
0 
0 
1 
0 
1 
1 
0 
1 
1 
0 
0 
0 
1 
1 
1 
0 
0 
DIGITAL LOGIC AND COMPUTER DESIGN
STEP2-CREATE TABLES
Step 2 – Create State Tables:

--- [Page 59 of 139] ---
PES 
UNIVERSITY 
Table 3.19 Reduced next state table 
Next State 
] 
1 
A 
£ 
Ag 
51 
S0 
Table 3.20 Reduced output table 
0 
0 
0 
0 
0 
0 
0 
0 
0 
1 
0 
0 
Current State 
Output 
0 
0 
1 
0 
0 
0 
' 
S0 
Unlock 
0 
0 
1 
1 
0 
1 
0 
1 
0 
0 
0 
0 
0 
1 
0 
1 
1 
0 
0 
1 
1 
0 
0 
0 
0 
1 
1 
1 
0 
0 
1 
0 
X 
X 
0 
0 
DIGITAL LOGIC AND COMPUTER DESIGN
STEP3-REDUCTION
Step 3 – Reduce the State Tables:
Some state combinations are never reached during operation.These are called
Unreachable States.Removing these states simplifies the FSM.

--- [Page 60 of 139] ---
DIGITAL LOGIC AND COMPUTER DESIGN
STEP4-STATE ASSIGNMENT
Step 4 – Assign Symbolic State Names:
After removing unreachable states, each valid state is assigned a symbolic name.
Binary State
Symbolic Name
00
S0
01
S1
10
S2

--- [Page 61 of 139] ---
% UNIVERSITY 
Table 3.21 Symbolic next state table 
Table 3.22 Symbolic output table 
Current State 
Output 
S 
Unlock 
51 
0 
52 
1 
Current State 
Input 
Next State 
) 
§' 
50 
1 
S0 
50 
2 
SO 
50 
3 
51 
51 
0 
S0 
51 
1 
S2 
51 
2 
S0 
51 
3 
S0 
52 
X 
S0 
DIGITAL LOGIC AND COMPUTER DESIGN
STEP4-STATE ASSIGNMENT
Step 4 – Assign Symbolic State Names:

--- [Page 62 of 139] ---
PES 
UNIVERSITY 
Reset 
DIGITAL LOGIC AND COMPUTER DESIGN
STEP5-STATE TRANSITION TABLE
Step 5 – Draw the State Transition Diagram:
Using the symbolic tables, the final State Transition
Diagram is constructed.
Overall Behaviour:
The FSM unlocks the door only after detecting the
correct input sequence.
After unlocking, it returns to the initial state,
ready for the next input sequence

--- [Page 63 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
FSM REVIEW
FSM Design Procedure
General Steps
1.Identify the inputs and outputs.
1.Draw the State Transition Diagram.
1.Create:
•State Transition Table
•Output Table
4.Select a suitable State Encoding.
4.Write:
•Next-State Equations
•Output Equations
6.Design the circuit schematic.

--- [Page 64 of 139] ---
% UNIVERSITY 
In Example the output Unlock is given by 
Unlock = S, 
This indicates that the output depends on 
A) Current input only 
B) Current state only 
C) Current input and current state 
D) Next state only 
DIGITAL LOGIC AND COMPUTER DESIGN
QUIZ
Answer:B

--- [Page 65 of 139] ---
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN
QUIZ
2.An FSM is implemented using 5 flip-flops with Binary Encoding.
What is the maximum number of states that can be represented?
A) 5
B) 25
C) 31
D) 32
Answer
D
Explanation:
In Binary Encoding, each flip-flop stores 1 bit.
•Number of flip-flops = 5 
•Number of possible states = 2⁵ = 32

--- [Page 66 of 139] ---
A »)LES 
Answer 
B)3 
Explanation: 
Flip—flops = [log, 
N 
[log,8] = [3] = 3 
DIGITAL LOGIC AND COMPUTER DESIGN
QUIZ
3.An FSM has 8 states. Using Binary Encoding, how many flip-flops are required?
A) 2
B) 3
C) 4
D) 8

--- [Page 67 of 139] ---
THANK YOU

--- [Page 68 of 139] ---
UNIVERSITY 
DA 
DIGITAL LOGIC AND COMPUTER DESIGN
UE25CS152B
Team DLCD
Department of CSE and CSE(AI&ML)
Introduction and Arithmetic Circuits
Unit 2
1

--- [Page 69 of 139] ---
Application 
Software 
>"hello 
Operating 
Systems 
s 
0 
R 
'_l 
Q. 
Architecture 
Micro- 
architecture 
Digital 
Circuits 
Analog 
Circuits 
Devices 
Physics 
PES 
UNIVERSITY 
JceLeanariming 
r<sns ) 
Topics of Discussion 
• Introduction
• Arithmetic Circuits
• Number Systems
• Sequential Building Blocks
• Memory Arrays
• Logic Arrays
Unit 2
2

--- [Page 70 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Introduction
• Digital building blocks:
– Gates, multiplexers, decoders, registers, arithmetic circuits, 
counters, memory arrays, logic arrays
• Building blocks demonstrate hierarchy, modularity, and regularity:
– Hierarchy of simpler components
– Well-defined interfaces and functions
– Regular structure easily extends to different sizes
• Will use these building blocks in Chapter 7 to build microprocessor
Unit 2
3

--- [Page 71 of 139] ---
UNIVERSITY 
Full 
Adder 
Half 
Adder 
Cout 
Cin 
Cout 
out 
ONO, 
out 
ORE, 
DIGITAL BUILDING BLOCKS
1-Bit Adders
Unit 2
4

--- [Page 72 of 139] ---
UNIVERSITY 
Full 
Adder 
Half 
Adder 
Cin 
Cout 
Cout 
Cout 
Cin 
Cout 
out 
wO 
DIGITAL BUILDING BLOCKS
1-Bit Adders
Unit 2
5

--- [Page 73 of 139] ---
UNIVERSITY 
Full 
Adder 
Half 
Adder 
out 
Cout 
S 
A 
B | C,, 
Cin 
Cout 
=A®B 
AB 
S 
Cout 
A®B®C, 
AB +AC,_+BC._ 
S 
Cout 
DIGITAL BUILDING BLOCKS
1-Bit Adders
Unit 2
6

--- [Page 74 of 139] ---
DIGITAL BUILDING BLOCKS
Multibit Adders (CPAs)
• Types of carry propagate adders (CPAs):
– Ripple-carry 
(slow)
– Carry-lookahead 
(fast)
– Prefix 
(faster)
• Carry-lookahead and prefix adders faster for large 
adders but require more hardware
Symbol
Unit 2
7

--- [Page 75 of 139] ---
UNIVERSITY 
VIS 
Y fe 
1 
C 
/%29 
C30 
SSO 
S31 
DIGITAL BUILDING BLOCKS
Ripple-Carry Adder
• Chain 1-bit adders together
• Carry ripples through entire chain
• Disadvantage: slow
Unit 2
8

--- [Page 76 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Ripple-Carry Adder Delay
tripple = NtFA
where tFA is the delay of a 1-bit full adder
Unit 2
9

--- [Page 77 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Carry-Lookahead Adder
•
Compute carry out (Cout) for k-bit blocks using generate and 
propagate signals
•
Some definitions:
– Column i produces a carry out by either generating a carry out or 
propagating a carry in to the carry out
– Generate (Gi) and propagate (Pi) signals for each column:
• Column i will generate a carry out if Ai AND Bi are both 1. 
Gi = Ai Bi
• Column i will propagate a carry in to the carry out if Ai OR Bi is 1.
Pi = Ai  + Bi
• The carry out of column i (Ci) is:
Ci = Ai Bi + (Ai  + Bi )Ci-1 = Gi + Pi Ci-1
Unit 2
10

--- [Page 78 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Carry-Lookahead Addition
• Step 1: Compute Gi and Pi for all columns 
• Step 2: Compute G and P for k-bit blocks
• Step 3: Cin propagates through each k-bit 
propagate/generate block
Unit 2
11

--- [Page 79 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Carry-Lookahead Adder
• Example: 4-bit blocks (G3:0 and P3:0) :
G3:0 = G3 + P3 (G2 + P2 (G1 + P1G0)
P3:0 = P3P2 P1P0
• Generally,
Gi:j = Gi + Pi (Gi-1 + Pi-1 (Gi-2 + Pi-2Gj )
Pi:j = PiPi-1 Pi-2Pj
Ci = Gi:j + Pi:j Cj-1
Unit 2
12

--- [Page 80 of 139] ---
UNIVERSITY 
+ 
¥ 
B27:24 A27:24 
+ 
¥ 
B31:23 A31:28 
A ]_ Cin 
Block 
Block 
C;|4-bit CcLA|C; [4-bit CL 
Block 
-bit CLA|Co7[4-bit CLA|C,3 
Block 
4 
Cout—[ 
N 
o 
0 
G, 
I Cin 
N 
————— 
i 
——————————————————————————————————————————————— 
i ———————————— 
DIGITAL BUILDING BLOCKS
32-bit CLA with 4-bit Blocks
Unit 2
13

--- [Page 81 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Carry-Lookahead Adder Delay
For N-bit CLA with k-bit blocks:
tCLA = tpg + tpg_block+ (N/k – 1)tAND_OR + ktFA
– tpg : 
delay to generate all Pi, Gi
– tpg_block :
delay to generate all Pi:j, Gi:j
– tAND_OR :
delay from Cin to Cout of final AND/OR gate in k-bit CLA 
block
An N-bit carry-lookahead adder is generally much faster than a 
ripple-carry adder for N > 16
Unit 2
14

--- [Page 82 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Prefix Adder
• Computes carry in (Ci-1) for each column, then 
computes sum:
Si = (Ai ⊕Bi) ⊕Ci
• Computes G and P for 1-, 2-, 4-, 8-bit blocks, etc. 
until all Gi (carry in) known
• log2N stages
Unit 2
15

--- [Page 83 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Prefix Adder
•
Carry in either generated in a column or propagated from a 
previous column.
•
Column -1 holds Cin, so 
G-1 = Cin, P-1 = 0
•
Carry in to column i = carry out of column i-1: 
Ci-1 = Gi-1:-1
Gi-1:-1: generate signal spanning columns i-1 to -1
•
Sum equation:
Si = (Ai ⊕Bi) ⊕Gi-1:-1
•
Goal: Quickly compute G0:-1, G1:-1, G2:-1, G3:-1, G4:-1, G5:-1, … 
(called prefixes)
Unit 2
16

--- [Page 84 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Prefix Adder
•
Generate and propagate signals for a block spanning bits 
i:j:
Gi:j = Gi:k + Pi:k Gk-1:j
Pi:j = Pi:kPk-1:j
•
In words:
– Generate: block i:j will generate a carry if:
•
upper part (i:k) generates a carry or 
•
upper part propagates a carry generated in lower 
part (k-1:j)
– Propagate: block i:j will propagate a carry if both the 
upper and lower parts propagate the carry
Unit 2
17

--- [Page 85 of 139] ---
& 
PES 
UNIVERSITY 
TN 5O 
15 
14 
13 
12 
11 
14:13 
12:11 
10:9 
8:7 
6:5 
4:3 
2:1 
0:-1 
DIGITAL BUILDING BLOCKS
Prefix Adder Schematic
Unit 2
18

--- [Page 86 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Prefix Adder Delay
tPA = tpg + log2N(tpg_prefix ) + tXOR
– tpg: delay to produce Pi Gi (AND or OR gate)
– tpg_prefix: delay of black prefix cell (AND-OR gate)
Unit 2
19

--- [Page 87 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Adder Delay Comparisons
Compare delay of: 32-bit ripple-carry, carry-lookahead, and 
prefix adders
•
CLA has 4-bit blocks
•
2-input gate delay = 100 ps; full adder delay = 300 ps
Unit 2
20

--- [Page 88 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Adder Delay Comparisons
Compare delay of: 32-bit ripple-carry, carry-lookahead, and 
prefix adders
•
CLA has 4-bit blocks
•
2-input gate delay = 100 ps; full adder delay = 300 ps
tripple
= NtFA = 32(300 ps) 
= 9.6 ns
tCLA
= tpg + tpg_block + (N/k – 1)tAND_OR + ktFA
= [100 + 600+ (7)200 + 4(300)] ps
= 3.3 ns
tPA
= tpg + log2N(tpg_prefix) + tXOR
= [100 + log232(200) + 100] ps
= 1.2 ns
Unit 2
21

--- [Page 89 of 139] ---
Symbol 
Implementation 
DIGITAL BUILDING BLOCKS
Subtracter
Unit 2
22

--- [Page 90 of 139] ---
As 
B, 
A, 
B, 
Implementation 
i 
D 
— Equal 
DIGITAL BUILDING BLOCKS
Comparator: Equality
Unit 2
23

--- [Page 91 of 139] ---
DIGITAL BUILDING BLOCKS
Comparator: Less Than
Unit 2
24

--- [Page 92 of 139] ---
DIGITAL BUILDING BLOCKS
Arithmetic Logic Unit (ALU)
F2:0
Function
000
A & B
001
A | B
010
A + B
011
not used
100
A & ~B
101
A | ~B
110
A - B
111
SLT
Unit 2
25

--- [Page 93 of 139] ---
A 
B 
AN 
AN 
| N % 
-, 
AN 
C:out 
\ 
+ 
/ 
N-1] |S 
7 
D o 
a 3 
N 
AN 
N 
AN 
[ 
— 
PES 
UNIVERSITY 
DIGITAL BUILDING BLOCKS
ALU Design
F2:0
Function
000
A & B
001
A | B
010
A + B
011
not used
100
A & ~B
101
A | ~B
110
A - B
111
SLT
Unit 2
26

--- [Page 94 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Adder Delay Comparisons
Compare delay of: 32-bit ripple-carry, carry-lookahead, and 
prefix adders
•
CLA has 4-bit blocks
•
2-input gate delay = 100 ps; full adder delay = 300 ps
tripple
= NtFA = 32(300 ps) 
= 9.6 ns
tCLA
= tpg + tpg_block + (N/k – 1)tAND_OR + ktFA
= [100 + 600+ (7)200 + 4(300)] ps
= 3.3 ns
tPA
= tpg + log2N(tpg_prefix) + tXOR
= [100 + log232(200) + 100] ps
= 1.2 ns
Unit 2
27

--- [Page 95 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Set Less Than (SLT) Example
•
Configure 32-bit ALU for SLT 
operation: A = 25 and B = 32
Unit 2
28

--- [Page 96 of 139] ---
A 
B 
N 
AN 
N 
- 
o] 
. 
E 
N 
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Set Less Than (SLT) Example
•
Configure 32-bit ALU for SLT 
operation: A = 25 and B = 32
– A < B, so Y should be 32-bit 
representation of 1 (0x00000001)
– F2:0 = 111
– F2 = 1 (adder acts as 
subtracter), so 25 - 32 = -7
– -7 has 1 in the most significant 
bit (S31 = 1)
– F1:0 = 11 multiplexer selects Y
= S31 (zero extended) = 
0x00000001.
Unit 2
29

--- [Page 97 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Shifters
•
Logical shifter: shifts value to left or right and fills empty spaces with 
0’s
–
Ex: 11001 >> 2 =
–
Ex: 11001 << 2 =
•
Arithmetic shifter: same as logical shifter, but on right shift, fills empty 
spaces with the old most significant bit (msb).
–
Ex: 11001 >>> 2 =
–
Ex: 11001 <<< 2 =
•
Rotator: rotates bits in a circle, such that bits shifted off one end are 
shifted into the other end
–
Ex: 11001 ROR 2 =
–
Ex: 11001 ROL 2 =
Unit 2
30

--- [Page 98 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Shifters
• Logical shifter:
– Ex: 11001 >> 2 = 00110
– Ex: 11001 << 2 = 00100
• Arithmetic shifter:
– Ex: 11001 >>> 2 = 11110
– Ex: 11001 <<< 2 = 00100
• Rotator:
– Ex: 11001 ROR 2 = 01110
– Ex: 11001 ROL 2 = 00111
Unit 2
31

--- [Page 99 of 139] ---
Q f 
@) 
- 
\ 
® 
PES 
UNIVERSITY 
DIGITAL BUILDING BLOCKS
Shifter Design
Unit 2
32

--- [Page 100 of 139] ---
PES 
UNIVERSITY 
piceLarnaTTNED 
1< 4ns 
DIGITAL BUILDING BLOCKS
Shifters as Multipliers,Dividers
• A << N = A × 2N
– Example: 00001 << 2  = 00100  (1 × 22 = 4)
– Example: 11101 << 2  = 10100  (-3 × 22 = -12)
• A >>> N = A ÷ 2N
– Example: 01000 >>> 2 = 00010  (8 ÷ 22 = 2)
– Example: 10000 >>> 2 = 11100  (-16 ÷ 22 = -4)
Unit 2
33

--- [Page 101 of 139] ---
Decimal 
Binary 
230 
multiplicand 
0101 
X 
X 
460 
partia| 
0101 
+ 920 
products 
0101 
9660 
0101 
+ 0000 
result 
0100011 
230 x 42 = 9660 
dX 
7 =35 
® 
PES 
UNIVERSITY 
JiceLEaRATTINED 
1< 4R S 
DIGITAL BUILDING BLOCKS
Multipliers
Department of CSE and AIML
• Partial products formed by multiplying a single digit 
of the multiplier with multiplicand
• Shifted partial products summed to form result
Unit 2
34

--- [Page 102 of 139] ---
PES 
UNIVERSITY 
Jcereanariming 
resrs ) 
A, 
A 
A 
A, 
B 0 
B: 
J] 
VO 
U 
L 
Ar 
Ay 
A 
A 
0 
X 
B, 
B, 
B, 
B, 
B, 
A = A ;// 
A,B, AB, AB, AB, 
. 
A,B, A.B, A,B, 
AB 
3By 
ABy 
ABy AgB, 
B, 
T T T 
A,B, AB, A.B, A,B, 
+ 
A,B, A,B, A.B, A B, 
}0 
I:)7 
p6 
P5 
P4 
P3 
P2 
P1 
PO 
T 
I 
T 
T 
[] 
0y 
| 
! 
Uit 
DA 
DIGITAL BUILDING BLOCKS
4 x 4 Multiplier
Unit 2
35

--- [Page 103 of 139] ---
UNIVERSITY 
Legend 
B 
R 
- 
DA 
DIGITAL BUILDING BLOCKS
4 x 4 Divider
A/B = Q + R/B
Algorithm:
R’ = 0
for i = N-1 to 0
R = {R’ << 1. Ai}
D = R - B
if D < 0, Qi=0, R’=R
else        Qi=1, R’=D
R’=R
Unit 2
36

--- [Page 104 of 139] ---
PES 
UNIVERSITY 
Jcereanariming 
resrs ) 
DA 
MCQs
Q1. What are the different types of Carry 
propagator adders?
a)Ripple carry adders
b)Carry lookahead adders
c)Prefix adders
d)Skip ahead adders
37
Unit 2

--- [Page 105 of 139] ---
PES 
UNIVERSITY 
Jcereanariming 
resrs ) 
DA 
MCQs
Q1. What are the different types of Carry 
propagator adders?
a)Ripple carry adders
b)Carry lookahead adders
c)Prefix adders
d)Skip ahead adders
38
Unit 2

--- [Page 106 of 139] ---
PES 
UNIVERSITY 
Jcereanariming 
resrs ) 
DA 
MCQs
Q2. A comparator is used to:
a. Add two numbers
b. Multiply two numbers
c. Determine relative magnitude of two numbers
d. Shift a number
39
Unit 2

--- [Page 107 of 139] ---
PES 
UNIVERSITY 
Jcereanariming 
resrs ) 
DA 
MCQs
Q2. A comparator is used to:
a. Add two numbers
b. Multiply two numbers
c. Determine relative magnitude of two numbers
d. Shift a number
40
Unit 2

--- [Page 108 of 139] ---
PES 
UNIVERSITY 
Jcereanariming 
resrs ) 
DA 
MCQs
Q3. Which circuit performs arithmetic and logical 
operations?
a. Decoder
b. Multiplexer
c. ALU
d. Counter
41
Unit 2

--- [Page 109 of 139] ---
PES 
UNIVERSITY 
Jcereanariming 
resrs ) 
DA 
MCQs
Q3. Which circuit performs arithmetic and logical 
operations?
a. Decoder
b. Multiplexer
c. ALU
d. Counter
42
Unit 2

--- [Page 110 of 139] ---
UNIVERSITY 
THANK YOU
Team DLCD
Department of CSE and CSE(AI&ML)
Unit 2
43

--- [Page 111 of 139] ---
TM 
In@® 
DIGITALLOGIC AND 
COMPUTER DESIGN
DIGITAL BUILDING BLOCKS 
Number Systems 
Team DLCD
Department of CSE and AIML

--- [Page 112 of 139] ---
PES 
UNIVERSITY 
DIGITAL BUILDING BLOCKS
Number Systems
Team DLCD

--- [Page 113 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Number Systems
Numbers we can represent using binary representations
-Positive numbers
Unsigned binary
-Negative numbers
Two’s complement
Sign/magnitude numbers
What about fractions?

--- [Page 114 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Numbers with Fractions
Two common notations:
– Fixed-point: binary point fixed
– Floating-point: binary point floats to 
the right of the most significant 1

--- [Page 115 of 139] ---
01101100 
0110.1100 
22+ 21+ 21+ 22=6.75 
DIGITAL BUILDING BLOCKS
Fixed-Point Numbers
6.75 using 4 integer bits and 4 fraction bits:
-Binary point is implied
-The number of integer and fraction bits must be agreed upon 
beforehand

--- [Page 116 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Fixed-Point Number Example
Represent 7.510 using 4 integer bits 
and 4 fraction bits.

--- [Page 117 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Fixed-Point Number Example
Represent 7.510 using 4 integer bits 
and 4 fraction bits.
Answer: 01111000

--- [Page 118 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Signed Fixed-Point Numbers
Representations:
–
Sign/magnitude
–
Two’s complement
Example: Represent -7.510 using 4 integer and 4 fraction bits
–
Sign/magnitude:
–
Two’s complement:

--- [Page 119 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Signed Fixed-Point Numbers
Representations:
–
Sign/magnitude
–
Two’s complement
Example: Represent -7.510 using 4 integer and 4 fraction bits
–
Sign/magnitude:
11111000
–
Two’s complement:
1. +7.5:
01111000
2. Invert bits: 
10000111
3. Add 1 to LSB:
+           1
10001000

--- [Page 120 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Numbers
• Binary point floats to the right of the most significant 1
• Similar to decimal scientific notation
Example: write 27310 in scientific notation:
273 = 2.73 × 102
In general, a number is written in scientific notation as:
± M × BE
–
M = mantissa
–
B = base
–
E = exponent
–
In the example, M = 2.73, B = 10, and E = 2

--- [Page 121 of 139] ---
1 bit 
8 bits 
23 bits 
Sign 
Exponent 
Mantissa 
PES 
UNIVERSITY 
N 
TR 
DIGITAL BUILDING BLOCKS
Floating-Point Numbers
We show three versions –final version is called the IEEE 754 floating-point standard
Example: represent the value 22810 using a 32-bit floating point representation

--- [Page 122 of 139] ---
1 bit 
8 bits 
23 bits 
l 0 | 
00000111 
11 1001 0000 0000 0000 0000 
Sign 
Exponent 
Mantissa 
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Representation 1
Example: represent the value 22810 using a 32-bit floating point representation
1. Convert decimal to binary (don’t reverse  steps 1 & 2!): 22810 = 111001002
2. Write the number in “binary scientific notation”: 111001002 = 1.110012 × 27
3. Fill in each field of the 32-bit floating point number:
-The sign bit is positive (0)
-The 8 exponent bits represent the value 7
-The remaining 23 bits are the mantissa

--- [Page 123 of 139] ---
1 bit 
8 bits 
23 bits 
0| 
00000111 
110 0100 0000 0000 0000 0000 
Sign 
Exponent 
Fraction 
PES 
UNIVERSITY 
R YRR 
DIGITAL BUILDING BLOCKS
Floating-Point Representation 2  
•
First bit of the mantissa is always 1:
-22810 = 111001002 = 1.11001 × 27
•
So, no need to store it: implicit leading 1
•
Store just fraction bits in 23-bit field

--- [Page 124 of 139] ---
1 bit 
8 bits 
23 bits 
’ 0| 
10000110 
110 0100 0000 0000 0000 0000 
Sign 
Biased 
Fraction 
Exponent 
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Representation 3
Biased exponent: bias = 127 (011111112)
–
Biased exponent = bias + exponent
–
Exponent of 7 is stored as: 127 + 7 = 134 = 0x100001102
The IEEE 754 32-bit floating-point representation of 22810
In hexadecimal: 0x43640000

--- [Page 125 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Example
Write -58.2510 in floating point (IEEE 754)

--- [Page 126 of 139] ---
1 bit 
8 bits 
23 bits 
1| 
10000100 
110 1001 0000 0000 0000 0000 
Sign 
Exponent 
Fraction 
PES 
UNIVERSITY 
R YRR 
DIGITAL BUILDING BLOCKS
Floating-Point Example
Write -58.2510 in floating point (IEEE 754)
1. Convert decimal to binary: 58.2510 = 111010.012
2. Write in binary scientific notation: 1.1101001 × 25
3. Fill in fields:
Sign bit: 1 (negative)
8 exponent bits: (127 + 5) = 132 = 100001002
23 fraction bits: 110 1001 0000 0000 0000 0000
In hexadecimal: 0xC2690000

--- [Page 127 of 139] ---
Number 
Sign 
Exponent 
Fraction 
0 
X 
00000000 
|{00000000000000000000000 
00 
0 
11111111 | 60000000000000000000000 
- 00 
| 
I11II111T [ 60000000000000000000000 
NaN 
X 
11111111 
|non-zero 
PES 
UNIVERSITY 
R YRR 
DIGITAL BUILDING BLOCKS
Floating-Point: Special Cases

--- [Page 128 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Precision
Single-Precision:
•
32-bit
•
1 sign bit, 8 exponent bits, 23 fraction bits
•
bias = 127
Double-Precision:
•
64-bit
•
1 sign bit, 11 exponent bits, 52 fraction bits
•
bias = 1023

--- [Page 129 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point: Rounding
•
Overflow: number too large to be represented
•
Underflow: number too small to be represented
•
Rounding modes:
- Down
- Up
- Toward zero
- To nearest

--- [Page 130 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point: Rounding
Example: Round 1.100101 (1.578125)  to only 3 fraction bits
Down: 1.100
Up: 1.101
Toward zero: 1.100
To nearest: 1.101 (1.625 is closer to 1.578125 than 1.5 is)

--- [Page 131 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Addition
1. Extract exponent and fraction bits
2. Prepend leading 1 to form mantissa
3. Compare exponents
4. Shift smaller mantissa if necessary
5. Add mantissas
6. Normalize mantissa and adjust exponent if necessary
7. Round result
8. Assemble exponent and fraction back into floating-point format

--- [Page 132 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Addition Example
Add the following floating-point numbers:
0x3FC00000
0x40500000

--- [Page 133 of 139] ---
1 bit 
8 bits 
23 bits 
| 0| 
01111111 
100 0000 0000 0000 0000 0000 
] 
Sign 
Exponent 
Fraction 
1 bit 
8 bits 
23 bits 
0| 
10000000 
101 0000 0000 0000 0000 0000 
| 
Sign 
Exponent 
Fraction 
PES 
UNIVERSITY 
N 
TR 
DIGITAL BUILDING BLOCKS
Floating-Point Addition Example
1. Extract exponent and fraction bits
For first number (N1): 
S = 0, E = 127, F = .1
For second number (N2): 
S = 0, E = 128, F = .101
2. Prepend leading 1 to form mantissa
N1:
1.1
N2:
1.101

--- [Page 134 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Addition Example
3. Compare exponents
127 – 128 = -1, so shift N1 right by 1 bit
4. Shift smaller mantissa if necessary
shift N1’s mantissa: 1.1 >> 1 = 0.11  (× 21)
5. Add mantissas
0.11 × 21
+  1.101 × 21
10.011 × 21

--- [Page 135 of 139] ---
1 bit 
8 bits 
23 bits 
’ 0| 
10000001 
001 1000 0000 0000 0000 0000 
Sign 
Exponent 
Fraction 
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
Floating-Point Addition Example
6. Normalize mantissa and adjust exponent if necessary
10.011 × 21 = 1.0011 × 22
7. Round result
No need (fits in 23 bits)
8. Assemble exponent and fraction back into floating-point format
S = 0, E = 2 + 127 = 129 = 100000012, F = 001100..
In hexadecimal: 0x40980000

--- [Page 136 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
MCQs
1. Which of the following is NOT a representation for signed fixed-
point numbers?
A. Two's Complement
B. Sign/Magnitude
C. Excess-127
D. Both A and B
2. In IEEE 754 single-precision floating-point format, how many bits 
are allocated for the exponent?
A. 1
B. 8
C. 11
D. 23

--- [Page 137 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
MCQs
3. Which IEEE 754 representation corresponds to NaN (Not a Number)?
A. Exponent = 00000000, Fraction = 000...0
B. Exponent = 11111111, Fraction = 000...0
C. Exponent = 11111111, Fraction ≠ 0
D. Exponent = 00000000, Fraction ≠ 0
4. During floating-point addition, what is the first operation performed after 
extracting the exponent and fraction bits?
A. Normalize the mantissa
B. Round the result
C. Prepend the implicit leading 1 to form the mantissa
D. Compare the exponents

--- [Page 138 of 139] ---
PES 
UNIVERSITY 
piceLcsnarimin 
< rs 
DIGITAL BUILDING BLOCKS
MCQs
1.
Answer: C. Excess-127
Explanation: The PPT lists Sign/Magnitude and Two's Complement as signed fixed-
point representations.
2.
Answer: B. 8
Explanation: Single-precision uses 1 sign bit, 8 exponent bits, and 23 fraction 
(mantissa) bits.
3.
Answer: C. Exponent = 11111111, Fraction ≠ 0
Explanation: NaN is represented by an all-ones exponent with a non-zero fraction 
field. 
4.
Answer: C. Prepend the implicit leading 1 to form the mantissa
Explanation: After extracting the fields, the hidden leading 1 is restored before 
comparing exponents and performing the addition.

--- [Page 139 of 139] ---
THANK YOU
Team DLCD
Department of Computer Science & AIML

```

---

<a id="doc-2"></a>
## Document 2: Unit 2 Question Bank Solved (10 Pages)
**Source Document**: `resources/U2QB_soln.docx`
**OCR Extraction File**: `Resources_U2QB_soln.txt`

```
================================================================================
ORIGINAL DOCUMENT : U2QB_soln.docx
OCR PDF FILE      : Resources_U2QB_soln_ocr.pdf
TOTAL PAGES       : 10
WORD COUNT        : 2102
CHARACTER COUNT   : 12689
DATE EXTRACTED    : 2026-11-04 14:04:10
================================================================================

--- [Page 1 of 10] ---
DIGITAL LOGIC AND COMPUTER DESIGN
UNIT 1 — DESCRIPTIVE QUESTIONS WITH ANSWERS
PES University | Descriptive Question Bank | T1: Harris & Harris, 2nd Edition
1. What is meant by a divide-by-3 circuit?
Model Answer / Explanation: A divide-by-3 circuit produces an output signal whose 
frequency is one-third of the input clock frequency. Therefore, f_out = f_in / 3.
2. How many states are required in a basic divide-by-3 FSM?
Model Answer / Explanation: Three states are required: S0, S1, and S2. The FSM repeatedly 
follows S0 → S1 → S2 → S0.
3. What is the next state after S2 in a divide-by-3 FSM?
Model Answer / Explanation: The next state is S0. Returning to S0 completes one cycle of 
the three-state sequence and starts the next cycle.
4. What is the purpose of a reset signal in the divide-by-3 FSM?
Model Answer / Explanation: Reset initializes the FSM to a known state, usually S0. This 
ensures predictable operation when the circuit starts.
5. What is the output frequency when a 30 MHz clock is divided by 3?
Model Answer / Explanation: The output frequency is 10 MHz because f_out = 30 MHz / 3 = 
10 MHz.
6. Draw or describe the state sequence for a Moore FSM that detects 1011.
Model Answer / Explanation: Use five states: S0: no bits matched; S1: matched 1; S2: 
matched 10; S3: matched 101; S4: matched 1011. The main path is S0 --1--> S1 --0--> S2 --1--
> S3 --1--> S4. In S4, output = 1. For overlap, S4 transitions to S1 on input 1 and to S2 on 
input 0.
7. Explain the difference between Moore and Mealy pattern recognizers.
Model Answer / Explanation: In a Moore FSM, output depends only on the present state, 
so a separate detection state is usually required. In a Mealy FSM, output depends on both 
present state and input, so detection can occur on a transition. A Moore design is often 
easier to interpret and has more stable state-based outputs, while a Mealy design may use 
fewer states and respond one transition earlier.
8. Write the state encoding for a Moore recognizer of 1011 and explain it.

--- [Page 2 of 10] ---
Model Answer / Explanation: One possible encoding is S0=3'b000, S1=3'b001, S2=3'b010, 
S3=3'b011, and S4=3'b100. Three bits are required because five states must be represented, 
and 2^2=4 is insufficient while 2^3=8 is sufficient.
9. Explain the role of the state register and next-state logic in Verilog.
Model Answer / Explanation: The state register stores the present state and is updated on 
the active clock edge. The next-state combinational block examines the present state and 
input, then calculates the state to be loaded on the next clock edge. This separation makes 
the FSM easier to design and verify.
10. Explain why a default case is included in the Verilog state-transition block.
Model Answer / Explanation: A default case handles invalid or unused state encodings. 
Assigning next_state = S0 provides a safe recovery path and helps the FSM return to a 
known operating state if an unexpected state occurs.
11. Design a Moore FSM to detect the pattern 1011 with overlapping detection. Explain 
the states and transitions.
Model Answer / Explanation: States: S0=no match, S1=matched 1, S2=matched 10, 
S3=matched 101, S4=matched 1011. Transitions: S0: 0→S0, 1→S1. S1: 0→S2, 1→S1. S2: 
0→S0, 1→S3. S3: 0→S2, 1→S4. S4: 0→S2, 1→S1. Output is 1 only in S4; otherwise it is 0. The 
transitions from S4 preserve overlap because the suffixes of 1011 may be prefixes of a new 
pattern.
12. Write Verilog code for a Moore FSM that recognizes 1011 with overlapping detection. 
Explain the major blocks.
Model Answer / Explanation: module moore_1011(
    input wire clk, reset, x,
    output reg detect
);
localparam S0=3'b000, S1=3'b001,
           S2=3'b010, S3=3'b011,
           S4=3'b100;
reg [2:0] state, next_state;
always @(posedge clk or posedge reset)
    if (reset) state <= S0;
    else       state <= next_state;
always @(*) begin
    case (state)
      S0: if (x) next_state=S1; else next_state=S0;
      S1: if (x) next_state=S1; else next_state=S2;

--- [Page 3 of 10] ---
S2: if (x) next_state=S3; else next_state=S0;
      S3: if (x) next_state=S4; else next_state=S2;
      S4: if (x) next_state=S1; else next_state=S2;
      default: next_state=S0;
    endcase
end
always @(*)
    if (state==S4) detect=1'b1;
    else           detect=1'b0;
endmodule
Explanation: The first block stores the present state. The 
second block implements the transition table. The third block 
is Moore output logic, so detect depends only on state and is 
high only in S4.
13. Develop the state table for a Moore 1011 pattern recognizer and explain the output.
Model Answer / Explanation: State table: S0: x=0→S0, x=1→S1, output=0. S1: x=0→S2, 
x=1→S1, output=0. S2: x=0→S0, x=1→S3, output=0. S3: x=0→S2, x=1→S4, output=0. S4: 
x=0→S2, x=1→S1, output=1. Since this is a Moore machine, the output is associated with 
the present state rather than directly with the input.
14. Explain how overlapping detection is implemented in a Moore FSM for 1011.
Model Answer / Explanation: After reaching S4, the FSM does not always return to S0. If 
the next input is 1, it goes to S1 because the most recent 1 can begin a new pattern. If the 
next input is 0, it goes to S2 because the ending sequence 10 matches the first two bits of 
the target pattern. These transitions retain useful partial matches and allow overlapping 
occurrences to be detected.
15. Compare the hardware and timing characteristics of Moore and Mealy pattern 
recognizers.
Model Answer / Explanation: A Moore recognizer generally uses a separate output state, so 
it may require more states than an equivalent Mealy recognizer. Its output depends only on 
registered state and is therefore state-synchronous and less directly sensitive to input 
changes. A Mealy recognizer can assert output on the transition that receives the final 
pattern bit, often using fewer states and responding earlier. However, because its output 
depends directly on input and state, careful timing design is needed to avoid unwanted 
output changes.
16.  Differentiate Half Adder and Full Adder with truth tables.

--- [Page 4 of 10] ---
Detailed Answer:
Half Adder:
A Half Adder adds two 1-bit binary numbers. It has two inputs (A,B) and two outputs (Sum 
and Carry).
Boolean equations:
Sum = A XOR B
Carry = A AND B
Truth Table:
A B | S C
0 0 | 0 0
0 1 | 1 0
1 0 | 1 0
1 1 | 0 1
Full Adder:
A Full Adder adds three binary inputs (A,B,Cin). It has outputs Sum and Carry.
Sum = A XOR B XOR Cin
Carry = AB + Cin(A XOR B)
A Full Adder can be implemented using two Half Adders and one OR gate. Unlike a Half 
Adder, it can accept an input carry, making it suitable for multi-bit addition.
17. Explain the working of a 4-bit Ripple Carry Adder with its advantages and 
disadvantages.
Detailed Answer:
A 4-bit Ripple Carry Adder is constructed by connecting four Full Adders in cascade.
The carry output from each Full Adder becomes the carry input to the next stage.
Working:
1. The least significant Full Adder receives the external carry input.
2. Each Full Adder computes Sum and Carry.
3. The carry propagates from LSB to MSB until the final carry is produced.
Advantages:
• Simple design.
• Requires less hardware.
Disadvantages:
• Large propagation delay because every stage waits for the previous carry.
• Not suitable for high-speed processors.

--- [Page 5 of 10] ---
18. Explain Carry Lookahead Adder using Generate and Propagate signals.
Detailed Answer:
Carry Lookahead Adders reduce delay by computing carries in parallel.
Generate (G) = A·B
Propagate (P) = A XOR B
Carry equations:
C1 = G0 + P0C0
C2 = G1 + P1G0 + P1P0C0
Because carries are calculated simultaneously rather than waiting for previous stages, the 
CLA is much faster than the Ripple Carry Adder. The trade-off is increased hardware 
complexity.
19. Explain binary subtraction using the Two's Complement method with an example.
Detailed Answer:
To subtract B from A:
1. Find the 2's complement of B.
2. Add it to A.
3. If a carry is generated, discard it.
Example:
A = 1011
B = 0110
1's complement of B = 1001
2's complement = 1010
1011 + 1010 = 10101
Discard carry = 0101
Therefore, 1011 - 0110 = 0101.
20. Explain the functions of an Arithmetic Logic Unit (ALU).
Detailed Answer:
The ALU is the computational unit of a processor.
Arithmetic operations:
• Addition
• Subtraction
• Increment

--- [Page 6 of 10] ---
• Decrement
Logic operations:
• AND
• OR
• XOR
• NOT
Other operations:
• Shift left/right
• Compare
• Set-on-less-than
The Control Unit selects the required ALU operation using control signals.
21. Explain the operation of a binary comparator.
Detailed Answer:
A binary comparator compares two binary numbers.
Outputs:
A>B
A<B
A=B
Comparison starts from the most significant bit.
If MSBs are equal, the next lower bits are compared until a difference is found.
Applications:
• Sorting
• Address comparison
• Processor decision making
• Digital control systems.
22.  Differentiate logical shift and arithmetic shift with examples.
Detailed Answer:
Logical Shift:
• Vacated bits are filled with zero.
• Used for unsigned numbers.
Example:
10110010 → Logical Right Shift

--- [Page 7 of 10] ---
01011001
Arithmetic Shift:
• Sign bit is preserved.
• Used for signed numbers.
Example:
11010010 → Arithmetic Right Shift
11101001
Arithmetic shifts preserve the sign of signed integers.
23. Explain binary multiplication using the shift-and-add method.
Detailed Answer:
Binary multiplication is similar to decimal multiplication.
Example:
1101 × 0011
Partial products:
1101
11010
Adding partial products:
100111
Decimal verification:
13 × 3 = 39
39 = 100111₂
Shift-and-add multiplication is implemented in hardware multipliers.
24.  Explain propagation delay in adders and its effect on performance.
Detailed Answer:
Propagation delay is the time required for a signal to travel from input to output.
In Ripple Carry Adders, every Full Adder must wait for the previous carry.
Hence,
Delay = Number of Full Adders × Delay per Full Adder.

--- [Page 8 of 10] ---
Large delays reduce processor speed.
Carry Lookahead Adders minimize this delay by generating carries simultaneously.
25. Explain why multiplexers are used in ALUs.
Detailed Answer:
An ALU performs many operations simultaneously inside separate hardware blocks.
A multiplexer selects one output according to control signals.
Advantages:
• Reduces hardware duplication.
• Enables multiple operations using one output path.
• Improves processor flexibility.
For example, if control signal = 00, ADD output is selected; 01 selects SUB; 10 selects AND; 
11 selects OR.
26.  Represent the decimal number 9.25 in fixed-point binary notation using 4 integer 
bits and 4 fraction bits.
Solution:

Integer part: 9 = 1001₂

Fraction part: 0.25 = 2⁻² → bit pattern 0100

Combine: 1001.0100
Final Answer: 1001.0100
27.  Convert the fixed-point binary number 0011.1010 (4 integer bits, 4 fraction bits) to 
its decimal value.
Solution:

Integer part: 0011 = 3

Fraction part: 1010 → 2⁻¹ + 2⁻³ = 0.5 + 0.125 = 0.625

Total = 3 + 0.625 = 3.625
Final Answer: 3.625
28.  Encode the decimal number 350 as a 32-bit IEEE 754 single-precision floating-
point number.

--- [Page 9 of 10] ---
Solution:
1. Convert 350 to binary: 350 = 101011110₂
2. Normalize: 101011110 = 1.01011110 × 2⁸
3. Sign bit = 0 (positive)
4. Biased exponent = 8 + 127 = 135 = 10000111
5. Fraction (23 bits, drop implicit leading 1, pad with zeros): 
01011110000000000000000
Final Answer: 0 10000111 01011110000000000000000
29. Encode the decimal number −0.15625 as a 32-bit IEEE 754 single-precision floating-
point number.
Solution:
1. Convert 0.15625 to binary: 0.15625 = 2⁻³ + 2⁻⁵ = 0.00101₂
2. Normalize: 0.00101 = 1.01 × 2⁻³
3. Sign bit = 1 (negative)
4. Biased exponent = −3 + 127 = 124 = 01111100
5. Fraction (23 bits): 01000000000000000000000
Final Answer: 1 01111100 01000000000000000000000
30.  Using the 8-step floating-point addition procedure, compute 12.5 + 0.375 and give 
the final IEEE 754 single-precision encoding of the result.
Solution: Step 1–2 (extract fields, prepend implicit 1):

12.5 = 1100.1₂ = 1.1001 × 2³ (exponent = 3)

0.375 = 0.011₂ = 1.1 × 2⁻² (exponent = −2)
Step 3 (compare exponents):

Difference = 3 − (−2) = 5
Step 4 (shift smaller mantissa):

Express 0.375's mantissa relative to exponent 3: 1.1 × 2⁻⁵ = 0.000011 (shift right 5

--- [Page 10 of 10] ---
bits)
Step 5 (add mantissas):
1.100100
+ 0.000011
1.100111
Step 6 (normalize):

1.100111 is already between 1 and 2 → no renormalization needed. Exponent 
stays 3.
Step 7 (round):

Result is exact → no rounding necessary.
Step 8 (assemble):

Sign = 0

Biased exponent = 3 + 127 = 130 = 10000010

Fraction = 100111 padded to 23 bits: 10011100000000000000000
Verification: 1.100111₂ × 2³ = 1100.111₂ = 12 + 0.5 + 0.25 + 0.125 = 12.875 = 12.5 + 
0.375 
Final Answer: 12.875 → 0 10000010 10011100000000000000000

```

---

<a id="doc-3"></a>
## Document 3: Unit 2 Descriptive Question Bank (2 Pages)
**Source Document**: `resources/U2QB.docx`
**OCR Extraction File**: `Resources_U2QB.txt`

```
================================================================================
ORIGINAL DOCUMENT : U2QB.docx
OCR PDF FILE      : Resources_U2QB_ocr.pdf
TOTAL PAGES       : 2
WORD COUNT        : 585
CHARACTER COUNT   : 3599
DATE EXTRACTED    : 2026-11-04 14:03:57
================================================================================

--- [Page 1 of 2] ---
1. Design and explain a three-state divide-by-3 FSM.
2. Write Verilog code for a divide-by-3 FSM and explain the major blocks.
3. Develop the state table for a divide-by-3 FSM.
4. Explain how the divide-by-3 FSM recovers from an invalid state.
5. Compare a divide-by-3 FSM with a simple modulo-3 counter and discuss duty cycle.
6. Design a Mealy FSM to detect the pattern 1011 with overlapping detection. Explain 
the states and transitions.
7. Write Verilog code for a Mealy FSM that recognizes 1011 with overlapping 
detection. Explain the major blocks.
8. Develop the state table for a Mealy 1011 pattern recognizer and explain the output.
9. Explain how overlapping detection is implemented in a Mealy FSM for 1011.
10. Compare the hardware and timing characteristics of Mealy and Moore pattern 
recognizers.
11. Design a Moore FSM to detect the pattern 1011 with overlapping detection. 
Explain the states and transitions.
12. Write Verilog code for a Moore FSM that recognizes 1011 with overlapping 
detection. Explain the major blocks.
13. Develop the state table for a Moore 1011 pattern recognizer and explain the 
output.
14. Explain how overlapping detection is implemented in a Moore FSM for 1011.
15. Compare the hardware and timing characteristics of Moore and Mealy pattern 
recognizers.
16. Derive the expression for outputs of the half adder and the full adder using SOP 
from their respective truth tables. 
17.  Derive the generator and propagator bits as well as the carry out bit for the 4th bit 
in a 4-bit, in terms of all the lower bits, Ai and Bi where “i" = 3:0 for a carry lookahead 
adder
18. What is the delay for a the following types of 32-bit adders? Assuming each input 
gate delay is 120 ps and that a full adder has 300 ps delay
a. A ripple carry adder
b. A carry-lookahead adder with 4-bit blocks

--- [Page 2 of 2] ---
c.
A prefix adder
19. Write the VHDL implementation for a 8-bit multiplier using the multiply(*) 
operation, also write the synthesized circuit for it.
20. Design two adders: a 64-bit ripple-carry adder and a 64-bit carry lookahead adder 
with 4-bit blocks. Use only two-input gates. Each two-input gate is 15 m2, has a 50 ps 
delay, and has 20 pF of total gate capacitance. You may assume that the static power 
is negligible. (a) Compare the area, delay, and power of the adders (operating at 100 
MHz). (b) Discuss the trade-offs between power, area, and delay.
21. Explain why a designer might choose to use a ripple-carry adder instead of a carry-
look ahead adder.
22. Using the 8-step floating-point addition procedure, compute 6.0 + 2.5, 
showing the renormalization step, and give the final IEEE 754 encoding.
23.  A floating-point addition produces a positive result of magnitude 4.5 × 10³⁸ 
before storage, exceeding the text's stated maximum normal magnitude of 
±3.402824 × 10³⁸. Determine (a) whether overflow occurs, (b) what is stored in 
round-to-nearest mode, and (c) the resulting 32-bit encoding.
24. Using 4 integer bits and 4 fraction bits, compute 2.125 + (−1.8125) in two's 
complement fixed-point notation, showing all conversion and addition steps.
25. (a) Decode the 32-bit pattern 1 10000101 11010000000000000000000 to its 
decimal value, showing all steps. (b) Using Table 5.2's special-value rules, state 
what the patterns 0 00000000 00000000000000000000000 and 0
11111111 00000000000000000000000 each represent.
26. Using 5 integer bits and 4 fraction bits, compute −4.375 + (−2.8125) in two's 
complement fixed-point notation, showing all conversion and addition steps. 
Then express the result in sign-and-magnitude notation as well.

```

---

<a id="doc-4"></a>
## Document 4: Unit 2 Multiple Choice Questions Set 1 (13 Pages)
**Source Document**: `resources/U2MCQ1.docx`
**OCR Extraction File**: `Resources_U2MCQ1.txt`

```
================================================================================
ORIGINAL DOCUMENT : U2MCQ1.docx
OCR PDF FILE      : Resources_U2MCQ1_ocr.pdf
TOTAL PAGES       : 13
WORD COUNT        : 2493
CHARACTER COUNT   : 14878
DATE EXTRACTED    : 2026-11-04 14:04:16
================================================================================

--- [Page 1 of 13] ---
MCQs Finite State Machine (FSM) and Verilog Code
1. What is the main function of a divide-by-3 FSM?

A. To multiply the clock frequency by 3

B. To generate an output frequency equal to one-third of the input clock 
frequency

C. To divide the input voltage by 3

D. To generate three independent clock signals
Answer: B
Explanation: A divide-by-3 circuit produces an output frequency f_out = f_in / 3. 
For example, a 30 MHz input produces a 10 MHz output.
2. How many states are required for a basic divide-by-3 FSM?

A. 1

B. 2

C. 3

D. 4
Answer: C
Explanation: The FSM cycles through three states: S0 
 S1 
 S2 
 S0. Therefore,
→
→
→
 
three states are required.
3. What is the next state after S2 in a divide-by-3 FSM?

A. S0

B. S1

C. S2

D. S3
Answer: A
Explanation: The state sequence is cyclic: S0 
 S1 
 S2 
 S0. After S2, the FSM
→
→
→
 
returns to S0.
4. What is the minimum number of bits required to encode three FSM states?

A. 1 bit

B. 2 bits

--- [Page 2 of 13] ---

C. 3 bits

D. 4 bits
Answer: B
Explanation: One bit represents only two states, while two bits represent four 
states. Thus, two bits are sufficient for three states.
5. Which Verilog statement is commonly used to update the state at the rising 
edge of the clock?

A. always @(*)

B. always @(posedge clk)

C. always @(clk)

D. always @(negedge reset)
Answer: B
Explanation: always @(posedge clk) executes when the clock changes from 0 to 1. 
FSM state registers are commonly updated at this edge.
6. What is the purpose of the reset signal in a divide-by-3 FSM?

A. To increase the clock frequency

B. To initialize the FSM to a known state

C. To generate an output pulse

D. To add a new state
Answer: B
Explanation: Reset initializes the FSM to a known starting state, usually S0, 
preventing an unknown starting condition.
7. Which Verilog code correctly describes the state transitions?

A. S0
S1, S1
S2, S2
S0
→
→
→

B. S0
S0, S1
S1, S2
S2
→
→
→

C. S0
S2, S1
S0, S2
S1
→
→
→

D. S0
S3, S1
S4, S2
S5
→
→
→
Answer: A

--- [Page 3 of 13] ---
Explanation: The correct divide-by-3 sequence is S0 
 S1 
 S2 
 S0, repeating
→
→
→
 
every three clock cycles.
8. What is the purpose of next_state in a two-process FSM?

A. It stores the previous state

B. It represents the state to be loaded at the next clock edge

C. It stores the output frequency

D. It acts as the reset signal
Answer: B
Explanation: next_state is calculated by combinational logic. At the next active 
clock edge, it is copied into the state register.
9. Why is a default case included in FSM transition logic?

A. To increase the number of states

B. To handle invalid or undefined states safely

C. To increase the output frequency

D. To remove the need for reset
Answer: B
Explanation: A default case provides a recovery path. For example, default: 
next_state = S0; returns the FSM to a known state.
10. If the present state is S1 in the following sequence S0
S1
S2
S0, what is
→
→
→
 
the next state?

A. S0

B. S1

C. S2

D. Unknown
Answer: C
Explanation: According to the transition sequence, S1 is followed by S2. The FSM 
enters S2 at the next active clock edge.

--- [Page 4 of 13] ---
Sample Verilog Code: Divide-by-3 FSM
module divide_by_3_fsm (
    input  wire clk,
    input  wire reset,
    output reg  div_out
);
    localparam S0 = 2'b00,
               S1 = 2'b01,
               S2 = 2'b10;
    reg [1:0] state, next_state;
    // State register
    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end
    // Next-state logic
    always @(*) begin
        case (state)
            S0: next_state = S1;
            S1: next_state = S2;
            S2: next_state = S0;
            default: next_state = S0;
        endcase
    end
    // Output logic
    always @(*) begin
        if (state == S0)
            div_out = 1'b1;
        else
            div_out = 1'b0;
    end
endmodule
Note: This simple FSM repeats every three clock cycles. A true 50% duty-cycle 
divide-by-3 clock generally requires additional logic using both clock edges.
MCQs on Moore Pattern Recognizer FSM and Verilog 
Code

--- [Page 5 of 13] ---
Pattern used: 1011 (overlapping pattern detection). In a Moore FSM, the output 
depends only on the present state.
11. What is the main purpose of a pattern recognizer FSM?

A. To increase clock frequency

B. To detect a specified sequence of input bits

C. To divide the input voltage

D. To store unlimited data
Answer: B
Explanation: A pattern recognizer FSM monitors a serial input stream and 
asserts an output when the required bit pattern is detected.
12. In a Moore FSM, the output depends on:

A. Only the present state

B. Only the current input

C. Both present state and current input

D. The clock frequency only
Answer: A
Explanation: In a Moore machine, outputs are determined solely by the current 
state. The input affects the next state, not the output directly.
13. For recognizing the pattern 1011, which state usually produces output 1?

A. Initial state

B. State representing that no bits are matched

C. Final detection state

D. Any state when input is 1
Answer: C
Explanation: A dedicated final state represents successful recognition of 1011. 
The Moore output is asserted in this detection state.
14. How many states are commonly used for a Moore FSM that recognizes 
1011?

A. 2

--- [Page 6 of 13] ---

B. 3

C. 4

D. 5
Answer: D
Explanation: A typical Moore recognizer uses five states: no match, matched 1, 
matched 10, matched 101, and matched 1011.
15. What is the correct progression when the input sequence 1, 0, 1, 1 is 
received?

A. S0 
 S1 
 S2 
 S3 
 S4
→
→
→
→

B. S0 
 S2 
 S1 
 S4 
 S3
→
→
→
→

C. S0 
 S1 
 S1 
 S1 
 S1
→
→
→
→

D. S0 
 S4 
 S3 
 S2 
 S1
→
→
→
→
Answer: A
Explanation: Each state represents the portion of 1011 matched so far. After 
receiving all four bits, the FSM reaches S4, the detection state.
16. Which Verilog construct is commonly used to describe next-state 
transitions?

A. case

B. assign only

C. initial

D. generate only
Answer: A
Explanation: A case statement clearly maps each present state and input 
condition to the appropriate next state.
17. Why is a separate output block used in a Moore FSM?

A. To make output depend directly on input

B. To generate output only from the present state

C. To remove the clock

D. To avoid defining states
Answer: B

--- [Page 7 of 13] ---
Explanation: Moore output logic is based only on the current state. For example, 
detect = 1 when state is S4; otherwise detect = 0.
18. What is the purpose of the reset signal?

A. To force the FSM into a known initial state

B. To detect the pattern immediately

C. To change 0 into 1

D. To increase the number of states
Answer: A
Explanation: Reset initializes the state register, typically to S0, so pattern 
recognition begins from a known condition.
19. What does overlapping detection mean for the pattern 1011?

A. The FSM ignores repeated bits

B. A bit from one detected pattern may also be used as the start of another 
pattern

C. The pattern can be detected only once

D. The input must be reset after every bit
Answer: B
Explanation: Overlapping detection preserves useful suffix bits. For example, 
after detecting 1011, the final 1 can serve as the first 1 of a possible new pattern.
20. Why is a default case included in the next-state logic?

A. To increase the output frequency

B. To handle invalid or undefined states safely

C. To make the output depend on input

D. To eliminate reset
Answer: B
Explanation: A default transition, such as next_state = S0, provides a safe 
recovery path if the FSM enters an unexpected state.

--- [Page 8 of 13] ---
Sample Verilog Code: Moore Pattern Recognizer for 1011
module moore_pattern_1011 (
    input  wire clk,
    input  wire reset,
    input  wire x,
    output reg  detect
);
    localparam S0 = 3'b000, // No match
               S1 = 3'b001, // Matched: 1
               S2 = 3'b010, // Matched: 10
               S3 = 3'b011, // Matched: 101
               S4 = 3'b100; // Matched: 1011
    reg [2:0] state, next_state;
    // State register
    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end
    // Next-state logic
    always @(*) begin
        case (state)
            S0: begin
                if (x) next_state = S1;
                else   next_state = S0;
            end
            S1: begin
                if (x) next_state = S1;
                else   next_state = S2;
            end
            S2: begin
                if (x) next_state = S3;
                else   next_state = S0;
            end
            S3: begin
                if (x) next_state = S4;
                else   next_state = S2;
            end
            S4: begin
                if (x) next_state = S1;
                else   next_state = S2;
            end
            default: next_state = S0;
        endcase
    end
    // Moore output logic
    always @(*) begin
        if (state == S4)
            detect = 1'b1;
        else
            detect = 1'b0;

--- [Page 9 of 13] ---
end
endmodule
Note: The code detects the pattern 1011 with overlapping recognition. Since this is 
a Moore FSM, detect becomes 1 only after the FSM enters the final detection state 
S4.
MCQs on Mealy Pattern Recognizer FSM and Verilog 
Code
Pattern used: 1011 (overlapping pattern detection). In a Mealy FSM, the output 
depends on both the present state and the current input.
21. What is the main purpose of a Mealy pattern recognizer FSM?

A. To multiply the clock frequency

B. To detect a specified sequence in a serial input stream

C. To store all input bits permanently

D. To divide the input voltage
Answer: B
Explanation: A pattern recognizer monitors incoming bits and produces an 
output when the specified sequence is detected.
22. In a Mealy FSM, the output depends on:

A. Only the present state

B. Only the current input

C. Both the present state and the current input

D. Only the reset signal
Answer: C
Explanation: In a Mealy machine, output is a function of the present state and the 
current input. Therefore, the output may change immediately when the input 
changes.
23. For detecting the pattern 1011, how many states are commonly required 
in a Mealy FSM?

--- [Page 10 of 13] ---

A. 2

B. 3

C. 4

D. 5
Answer: C
Explanation: A typical Mealy recognizer uses four states representing: no match, 
matched 1, matched 10, and matched 101. Detection occurs on the transition 
caused by the final input 1.
24. In a Mealy recognizer for 1011, when is detect asserted?

A. Only after entering a separate final state

B. When the FSM is in the matched-101 state and the current input is 1

C. Whenever the input is 1

D. Only during reset
Answer: B
Explanation: When the previous bits have matched 101 and the current input is 
1, the complete pattern 1011 is recognized. The output is asserted on that 
transition.
25. Which statement best describes a key difference between Mealy and 
Moore FSMs?

A. Mealy FSMs have no states

B. Moore outputs depend on input and state, while Mealy outputs depend only 
on state

C. Mealy outputs depend on state and input, while Moore outputs depend only 
on state

D. Both always use the same number of states
Answer: C
Explanation: A Mealy output uses both state and input. A Moore output uses only 
the present state. Mealy machines often require fewer states for the same pattern.
26. Which Verilog construct is commonly used to describe state transitions?

A. case

--- [Page 11 of 13] ---

B. initial only

C. generate only

D. task only
Answer: A
Explanation: A case statement is commonly used to describe the transition rules 
for each present state and input value.
27. What is the purpose of next_state in a two-process FSM design?

A. It stores the output permanently

B. It represents the state to be loaded at the next clock edge

C. It replaces the input signal

D. It acts as the reset signal
Answer: B
Explanation: Combinational logic calculates next_state. The state register loads 
next_state on the active clock edge.
28. What does overlapping pattern detection mean?

A. A detected pattern cannot share bits with another pattern

B. A bit from one detected pattern can also be part of the next pattern

C. The input is ignored after detection

D. The FSM resets after every input bit
Answer: B
Explanation: Overlapping detection allows useful suffix bits to become the 
beginning of another possible pattern. This improves continuous pattern 
recognition.
29. What is the purpose of the reset signal?

A. To initialize the FSM to a known state

B. To force detect permanently high

C. To add a new state

D. To increase input frequency
Answer: A

--- [Page 12 of 13] ---
Explanation: Reset places the FSM in the initial no-match state, ensuring 
predictable operation.
30. Why is a default case included in the FSM logic?

A. To increase the number of states

B. To handle invalid or undefined states safely

C. To make the clock faster

D. To remove the input signal
Answer: B
Explanation: A default assignment provides a safe recovery path, usually 
returning the FSM to the initial state.
Sample Verilog Code: Mealy Pattern Recognizer for 1011
module mealy_pattern_1011 (
    input  wire clk,
    input  wire reset,
    input  wire x,
    output reg  detect
);
    localparam S0 = 2'b00, // No match
               S1 = 2'b01, // Matched: 1
               S2 = 2'b10, // Matched: 10
               S3 = 2'b11; // Matched: 101
    reg [1:0] state, next_state;
    // State register
    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end
    // Next-state and Mealy output logic
    always @(*) begin
        next_state = S0;
        detect = 1'b0;
        case (state)
            S0: begin
                if (x)
                    next_state = S1;
                else
                    next_state = S0;
            end

--- [Page 13 of 13] ---
S1: begin
                if (x)
                    next_state = S1;
                else
                    next_state = S2;
            end
            S2: begin
                if (x)
                    next_state = S3;
                else
                    next_state = S0;
            end
            S3: begin
                if (x) begin
                    detect = 1'b1;
                    next_state = S1;
                end
                else begin
                    next_state = S2;
                end
            end
            default: begin
                next_state = S0;
                detect = 1'b0;
            end
        endcase
    end
endmodule
Note: This Verilog design detects the pattern 1011 with overlapping recognition. In 
the S3 state, receiving x = 1 completes the pattern and immediately asserts detect 
= 1. The next state is S1 because the final 1 can also be the first bit of a new 
pattern.

```

---

<a id="doc-5"></a>
## Document 5: Unit 2 Multiple Choice Questions Set 2 (6 Pages)
**Source Document**: `resources/U2MCQ2.docx`
**OCR Extraction File**: `Resources_U2MCQ2.txt`

```
================================================================================
ORIGINAL DOCUMENT : U2MCQ2.docx
OCR PDF FILE      : Resources_U2MCQ2_ocr.pdf
TOTAL PAGES       : 6
WORD COUNT        : 1411
CHARACTER COUNT   : 6916
DATE EXTRACTED    : 2026-11-04 14:04:05
================================================================================

--- [Page 1 of 6] ---
MCQs for unit -2
1.
What are the different types of Carry propagator adders?
a.
Ripple carry adders
b.
Carry lookahead adders
c.
Prefix adders
d.
Skip ahead adders
2.
What is the delay in the ripple carry adder, given tFA is the delay of 1 full adder?
a.
N x tFA 
b.
tFA
c.
(N-1) x tFA
d.
None of the above
3.
What is the N-bit delay of a prefix adder?
a.
tPA = tpg  + log2N(tpg-prefix) + tXOR
b.
tPA = N X tpg 
c.
tPA = tpg  + log2N 
d.
tPA = tpg  +  tXOR
4.
What is the Sum output of a Half Adder?
a. A + B
b. A ⊕ B
c. AB
d. A̅B + AB̅
5.
What is the Carry output of a Half Adder?
a. A + B
b. AB
c. A ⊕ B
d. A̅B
6.
What is the Sum output of a Full Adder?
a. A + B + Cin
b. A ⊕ B ⊕ Cin
c. AB + Cin
d. A ⊕ B
7.
What is the Carry output of a Full Adder?
a. A ⊕ B ⊕ Cin
b. AB + ACin + BCin
c. AB + Cin
d. A + B + Cin
8.
 A Carry-Lookahead Adder improves speed by:
a. Reducing the number of bits
b. Using fewer gates
c. Computing carries in parallel
d. Removing carries

--- [Page 2 of 6] ---
9.
The generate signal for bit i is:
a. Pi = Ai ⊕ Bi
b. Gi = AiBi
c. Gi = Ai + Bi
d. Gi = Ai − Bi
10. The propagate signal for bit i in the Harris text is:
a. Pi = AiBi
b. Pi = Ai + Bi
c. Pi = Ai ⊕ Bi
d. Pi = Ai − Bi
11. The carry equation for a Carry-Lookahead Adder is:
a. Ci = GiPi
b. Ci = Gi + PiCi-1
c. Ci = Ai + Bi
d. Ci = Pi + Ci-1
12. Which adder generally provides the fastest performance for large word sizes?
a. Ripple Carry Adder
b. Carry Skip Adder
c. Prefix Adder
d. Serial Adder
13. A Carry-Lookahead Adder improves speed by:
a. Reducing the number of bits
b. Using fewer gates
c. Computing carries in parallel
d. Removing carries
14. Which circuit performs arithmetic and logical operations?
a. Decoder
b. Multiplexer
c. ALU
d. Counter
15. Logical left shift by one bit is equivalent to:
a. Division by 2
b. Multiplication by 2
c. Multiplication by 4
d. No change
16. A comparator is used to:
a. Add two numbers
b. Multiply two numbers
c. Determine relative magnitude of two numbers
d. Shift a number

--- [Page 3 of 6] ---
17. In binary multiplication, each partial product is generated using:
a. XOR gates only
b. AND operations between multiplicand and multiplier bits
c. OR gates only
d. NOT gates only
18. Which adder has delay proportional to log₂N?
a. Ripple Carry Adder
b. Serial Adder
c. Prefix Adder
d. Half Adder
19.  You are designing a 32-bit processor for a low-cost embedded device. The propagation delay of a 
full adder is 300 ps, and each two-input gate delay is 100 ps. Which adder implementation would 
you choose if minimizing delay is the primary goal, and what would be the approximate delay?
A. Ripple-Carry Adder, 9.6 ns
B. Carry-Lookahead Adder (4-bit blocks), 3.3 ns
C. Prefix Adder, 1.2 ns
D. Ripple-Carry Adder, 3.3 ns
        Answer: C. Prefix Adder, 1.2 ns 
Reasoning: Ripple-Carry delay = 32×300=9.6ns. CLA delay = 3.3 ns. Prefix Adder delay = 
100+log2 (32)×200+100=1.2ns. Fastest option is Prefix Adder.
20. You are implementing subtraction in an ALU. To compute Y = A - B, which hardware 
configuration is correct?
A. Invert bits of B, add 1, then add to A with Cin = 1
B. Directly subtract B from A using a comparator
C. Use a ripple-carry adder with Cin = 0
D. Use XOR gates to flip A and add B
Answer:  A. Invert bits of B, add 1, then add to A with Cin = 1
Reasoning: Two’s complement subtraction is performed by inverting B, adding 1, and then adding 
to A.
21.  You need to multiply a binary number 0000112by 16 using minimal hardware. Which operation 
achieves this?
A. Arithmetic Right Shift by 4 
B. Logical Left Shift by 4 
C. Rotate Left by 4 
D. Add 16 repeatedly
Answer: B. Logical Left Shift by 4 
Reasoning: 
Left shift by N bits multiplies the number by
 2
N. Here, 
0000112<<4=1100002=4810.
22.  A designer computes A – B and checks sign bit. Q: If sign bit = 1, what does it mean?
A) A > B
B) A < B
C) A = B
D) Overflow

--- [Page 4 of 6] ---
Ans: B
Explanation: Negative result → A < B.
23.  ALU configured with F2 = 1, F1:0 = 10. Q: What operation occurs?
A) A + B
B) A – B
C) A OR B
D) SLT
Ans: B
Explanation: F2 inverts B and adds 1 → subtraction.
 24.  11001 LSR 2. Q: Result?
A) 00110
B) 11110
C) 01110
D) 00100
Ans: A
Explanation: Logical shift right fills with 0s → 00110.
25.  In two’s complement addition, A = 0111 (7), B = 0100 (4). Q: What is the overflow flag?
A) 0
B) 1
C) Depends on carry-in
D) Undefined 
Ans: B 
Explanation: 7 + 4 = 11 → binary 1011 (negative in 4-bit signed). Overflow occurs when adding 
two positives yields a negative.
26.  A 32 × 32 multiplier is implemented. Q: What is product size?
A) 32 bits
B) 64 bits
C) 128 bits
D) 16 bits 
Ans: B 
Explanation: N × N multiplier → 2N-bit result → 64 bits.
27.  A 16-bit logical shifter is built. Q: How many multiplexers are required?
A) 16 × 16
B) 16 × 4
C) 16 × log₂16
D) 16 × 1 
Ans: A 
Explanation: Each bit requires a 16:1 multiplexer → 16 × 16.
28.  A CPU designer chooses between CLA and Prefix adder for a 128-bit ALU. Q: Why might prefix 
adder be chosen despite higher hardware cost?
A) Lower power consumption
B) Logarithmic delay scaling
C) Smaller area footprint
D) Easier HDL coding 
Ans: B 
Explanation: Prefix adder delay ∝ log₂N, critical for wide adders in CPUs.

--- [Page 5 of 6] ---
29.  A 64-bit ripple-carry adder has tFA = 250 ps. A 64-bit CLA with 8-bit blocks has tpg = 100 ps, 
tpg_block = 800 ps, tAND_OR = 200 ps, and tFA = 250 ps. Q: Which design is faster and why?
A) Ripple-carry, because fewer gates
B) CLA, because carry computed in parallel
C) Ripple-carry, because linear delay is smaller
D) Both equal 
Ans: B 
Explanation: Ripple delay = 64 × 250 ps = 16 ns. CLA delay ≈ 100 + 800 + (64/8 – 1) × 200 + (8 × 
250) = 3.9 ns. CLA is much faster.
30.  A = 25, B = 32, F2:0 = 111. Q: What is Y?
A) 0
B) 1
C) 25
D) 32 
Ans: B 
Explanation: SLT → Y = 1 if A < B.
31.  A 4-bit comparator checks if A = B. Q: Which gate is used per bit?
A) XOR
B) XNOR
C) AND
D) OR 
Ans: B 
Explanation: XNOR checks equality per bit.
32.  To compute A – B, the designer inverts B and adds 1. Q: Which input must be set in CPA?
A) Cin = 0
B) Cin = 1
C) Cout = 1
D) None 
Ans: B 
Explanation: Subtraction = A + (¬B + 1) → Cin = 1.
33.  A 32-bit CLA with 4-bit blocks is designed. Q: Why is it faster than ripple-carry?
A) Uses fewer gates
B) Computes carry in parallel using generate/propagate
C) Eliminates carry completely
D) Uses XOR only 
Ans: B 
Explanation: CLA precomputes carry using G and P signals.
34.  A circuit designer wants to add two 1-bit numbers but doesn’t care about carry-in. Q: Which 
outputs does the half adder produce?
A) Sum only
B) Carry only
C) Sum and Carry-out
D) Sum, Carry-in, Carry-out 
Ans: C 
Explanation: Half adder → S = A ⊕ B, Cout = A·B. No Cin input.

--- [Page 6 of 6] ---
35.  In two’s complement addition, A = 0111 (7), B = 0100 (4). Q: What is the overflow flag?
A) 0
B) 1
C) Depends on carry-in
D) Undefined 
Ans: B 
Explanation: 7 + 4 = 11 → binary 1011 (negative in 4-bit signed). Overflow occurs when adding 
two positives yields a negative.

```

---

<a id="doc-6"></a>
## Document 6: Unit 2 Multiple Choice Questions Set 3 - Number Systems (21 Pages)
**Source Document**: `resources/U2MCQ3.pdf`
**OCR Extraction File**: `Resources_U2MCQ3.txt`

```
================================================================================
ORIGINAL DOCUMENT : U2MCQ3.pdf
OCR PDF FILE      : Resources_U2MCQ3_ocr.pdf
TOTAL PAGES       : 21
WORD COUNT        : 2514
CHARACTER COUNT   : 15476
DATE EXTRACTED    : 2026-11-04 14:05:15
================================================================================

--- [Page 1 of 21] ---
MCQs on Number Systems 
1. In a fixed-point number system, the position of the binary point is: 
A. Changed during every arithmetic operation 
B. Fixed at a predetermined position 
C. Always placed after the least significant bit 
D. Stored separately in memory 
Answer: B. Fixed at a predetermined position 
Explanation: In fixed-point representation, the binary point has an implied fixed position agreed 
upon when interpreting the bits. 
2. An 8-bit fixed-point number has 4 integer bits and 4 fractional bits. Where is the implied binary 
point in 01101100? 
A. 0.1101100 
B. 01.101100 
C. 011.01100 
D. 0110.1100 
Answer: D. 0110.1100 
Explanation: Four bits are assigned to the integer part and four to the fractional part: 0110.1100 
3. What is the decimal value of the unsigned fixed-point number 0110.1100? 
A. 6.25 
B. 6.50 
C. 6.75 
D. 6.875 
Answer: C. 6.75 
Explanation: 
0110.1100 
= 22 + 21 + 2−1 + 2−2 
= 4 + 2 + 0.5 + 0.25 = 6.75 
4. In the fixed-point number 0010.0110, the weight of the rightmost bit is: 
A. 2−1 
B. 2−2 
C. 2−3 
D. 2−4 
Answer: D. 2−4 
Explanation: With four fractional bits, their weights are: 
2−1, 2−2, 2−3, 2−4 
5. What is the decimal value of the fractional binary number 0.1000₂? 
A. 0.25 
B. 0.5

--- [Page 2 of 21] ---
C. 0.75 
D. 1.0 
Answer: B. 0.5 
Explanation: 
0.10002 = 1 × 2−1 = 0.5 
6. What is the binary fixed-point representation of 𝟎. 𝟕𝟓𝟏𝟎using four fractional bits? 
A. 0000.0011 
B. 0000.0110 
C. 0000.1100 
D. 0000.1110 
Answer: C. 0000.1100 
Explanation: 
0.75 = 0.5 + 0.25 
= 2−1 + 2−2 
 
Therefore: 
0.7510 = 0000.11002 
7. Which notation can be used to represent signed fixed-point numbers? 
A. Only unsigned binary 
B. Only BCD 
C. Two’s complement or sign-magnitude 
D. Gray code only 
Answer: C. Two’s complement or sign-magnitude 
8. In sign-magnitude representation, the most significant bit generally represents: 
A. Fraction 
B. Sign 
C. Binary point 
D. Least significant value 
Answer: B. Sign 
Explanation: Usually: 
• 
0 → positive  
• 
1 → negative  
 
9. Which binary fraction represents 𝟎. 𝟔𝟐𝟓𝟏𝟎? 
A. 0.1000 
B. 0.1010

--- [Page 3 of 21] ---
C. 0.1100 
D. 0.1110 
Answer: B. 0.1010 
Explanation: 
0.10102 = 2−1 + 2−3 
= 0.5 + 0.125 = 0.625 
10. In an 8-bit fixed-point representation with four fractional bits, the smallest fractional place 
value is: 
A. 2−1 
B. 2−2 
C. 2−4 
D. 2−8 
Answer: C. 2−4 
2−4 = 1
16 = 0.0625 
11. What is the decimal value of the unsigned fixed-point number 0101.1010₂? 
A. 5.25 
B. 5.5 
C. 5.625 
D. 5.75 
Answer: C. 5.625 
Explanation: 
Integer part: 
01012 = 5 
 
Fraction: 
. 10102 = 0.5 + 0.125 = 0.625 
 
Therefore: 
5 + 0.625 = 5.625 
12. What is the decimal value of 0011.0110₂ when interpreted as an unsigned fixed-point number? 
A. 3.25 
B. 3.375 
C. 3.5 
D. 3.75 
Answer: B. 3.375 
Explanation: 
0011.0110

--- [Page 4 of 21] ---
= 2 + 1 + 0.25 + 0.125 
= 3.375 
13. The absolute value +𝟐. 𝟑𝟕𝟓is represented as: 
0010.0110 
What is the sign-magnitude representation of −2.375? 
A. 0010.0110 
B. 1010.0110 
C. 1101.1010 
D. 1110.0110 
Answer: B. 1010.0110 
Explanation: In sign-magnitude representation, only the sign bit changes: 
0010.0110 →1010.0110 
14. The positive fixed-point value +𝟐. 𝟑𝟕𝟓 is: 
0010.0110 
What is its 8-bit two’s complement representation for −2.375? 
A. 1010.0110 
B. 1101.1001 
C. 1101.1010 
D. 1110.0110 
Answer: C. 1101.1010 
Explanation: 
Start with: 
0010 0110 
Invert: 
1101 1001 
Add 1: 
1101 1010 
Therefore: 
−2.375 = 1101.1010 
 
15. Which statement correctly distinguishes sign-magnitude from two’s complement? 
A. Both are always identical for negative numbers 
B. Sign-magnitude changes the sign bit, while two’s complement involves inversion and adding 1 
C. Two’s complement changes only the sign bit 
D. Sign-magnitude requires inversion and adding 1 
Answer: B

--- [Page 5 of 21] ---
16. What is the fixed-point binary representation of 𝟎. 𝟑𝟕𝟓𝟏𝟎using four fractional bits? 
A. 0000.0011 
B. 0000.0110 
C. 0000.1010 
D. 0000.1100 
Answer: B. 0000.0110 
Explanation: 
0.375 = 0.25 + 0.125 
= 2−2 + 2−3 
 
Therefore: 0.375 = 0.01102 
17. Consider the fixed-point number: 
0010.1011 
What is its unsigned decimal value? 
A. 2.625 
B. 2.6875 
C. 2.75 
D. 2.8125 
Answer: B. 2.6875 
Explanation: 
0010.1011 
= 2 + 0.5 + 0.125 + 0.0625 
= 2.6875 
18. Why is two’s complement generally preferred for signed fixed-point arithmetic? 
A. It eliminates fractional bits 
B. It allows signed addition to be performed using ordinary binary addition 
C. It requires no sign bit 
D. It increases the number of bits automatically 
Answer: B 
Explanation: Two’s complement allows positive and negative numbers to be added using the same 
binary addition circuitry. 
19. In an 8-bit fixed-point format with four fractional bits, what bit pattern represents +𝟎. 𝟕𝟓? 
A. 0000 0011 
B. 0000 0110 
C. 0000 1100 
D. 0001 1000 
Answer: C. 0000 1100

--- [Page 6 of 21] ---
Because: 
0.75 = 0.11002 
20. In an 8-bit fixed-point system with 4 integer bits and 4 fractional bits, +𝟎. 𝟔𝟐𝟓is represented 
as: 
0000.1010 
What is −0.625in two’s complement? 
A. 1000.1010 
B. 1111.0101 
C. 1111.0110 
D. 1000.0110 
Answer: C. 1111.0110 
Explanation: 
Positive: 
0000 1010 
Invert: 
1111 0101 
Add 1: 
1111 0110 
Therefore: 
−0.625 = 1111.0110 
 
21. Perform the fixed-point addition: 
0000.1100 + 1111.0110 
 
using 8-bit two’s complement arithmetic. 
A. 0000.0010 
B. 0000.0110 
C. 1111.0010 
D. 10000.0010 
Answer: A. 0000.0010 
Explanation: 
The numbers represent: 
0000.1100 = +0.75 
1111.0110 = −0.625

--- [Page 7 of 21] ---
So: 
0.75 −0.625 = 0.125 
 
and: 
0.125 = 0000.0010 
 
Binary addition produces a carry beyond the 8-bit result, which is discarded. 
22. A bit pattern 01101100 is stored in memory. Can we determine its fixed-point decimal value 
without knowing the binary-point position? 
A. Yes, it is always 108 
B. Yes, it is always 6.75 
C. No, the binary-point position must be known 
D. No, fixed-point values cannot be converted to decimal 
Answer: C 
Explanation: The bits themselves do not store the binary point. 
For example: 
01101100 
could be interpreted as: 
0110.1100 
or 
011.01100 
or 
01.101100 
Each interpretation gives a different numerical value. 
23. Suppose the bit pattern is: 
00110100 
If interpreted with 4 fractional bits, it becomes: 
0011.0100 
What is its decimal value? 
A. 3.125 
B. 3.25 
C. 3.5 
D. 3.75 
Answer: B. 3.25

--- [Page 8 of 21] ---
Explanation: 
0011.0100 
= 3 + 2−2 
= 3 + 0.25 = 3.25 
24. The same bit pattern 00110100 is now interpreted with only 2 fractional bits. What is its value? 
A. 3.25 
B. 6.5 
C. 13 
D. 52 
Answer: C. 13 
Explanation: 
With two fractional bits: 
001101.00 
0011012 = 13 
 
Therefore: 
001101.002 = 13 
 
This demonstrates that the same bits can represent different values depending on the assumed 
binary-point position. 
25. Which of the following correctly represents −𝟐. 𝟑𝟕𝟓in 8-bit fixed-point two’s complement, 
assuming four fractional bits? 
A. 1010.0110 
B. 1101.1010 
C. 0010.0110 
D. 1101.0110 
Answer: B. 1101.1010 
26. An 8-bit fixed-point two’s complement number has four fractional bits. What is the value of the 
least significant bit? 
A. 1 
B. 0.5 
C. 0.125 
D. 0.0625 
Answer: D. 0.0625 
Explanation: 
The rightmost bit has weight: 
2−4 = 1
16 = 0.0625

--- [Page 9 of 21] ---
This is also the resolution/step size of this fixed-point format 
27. Which statement about fixed-point numbers is FALSE? 
A. The binary point is usually implied rather than physically stored 
B. Two’s complement can represent negative fixed-point numbers 
C. The interpretation of the bits depends on the agreed binary-point position 
D. The location of the binary point can always be determined by examining only the stored bits 
Answer: D 
Explanation: A fixed-point number is physically just a collection of bits. The bit pattern itself does 
not tell us where the implied binary point is located. 
28. The main advantage of floating-point representation over fixed-point representation is that 
floating-point can: 
A. Represent only integers 
B. Represent a much wider range of very large and very small numbers 
C. Eliminate the need for binary numbers 
D. Represent only positive numbers 
Answer: B 
Explanation 
In fixed-point representation, the number of integer and fractional bits is fixed. 
Floating-point allows the binary point to effectively “float” by using an exponent. 
Therefore, it can represent both: 
• 
Very large numbers  
• 
Very small numbers  
 
29. A floating-point number is analogous to: 
A. Boolean algebra 
B. Scientific notation 
C. Gray code 
D. Two's complement only 
Answer: B 
Explanation 
Consider decimal scientific notation: 
4500 = 4.5 × 103 
 
Similarly, binary floating-point notation can be written as:

--- [Page 10 of 21] ---
101002 = 1.01002 × 24 
 
Thus, floating-point representation works similarly to scientific notation. 
30. IEEE 754 single-precision floating-point representation uses how many bits? 
A. 16 bits 
B. 32 bits 
C. 48 bits 
D. 64 bits 
Answer: B. 32 bits 
1+8+23=32 bits 
1 – sign bit 
8 – exponent 
23 – Fraction 
31. What does a sign bit of 0 indicate for an ordinary IEEE 754 floating-point number? 
A. Negative 
B. Positive 
C. Infinity 
D. NaN 
Answer: B. Positive 
Explanation 
The sign convention is: 
0 →positive 
1 →negative 
32. What is the bias used in IEEE 754 single-precision floating-point representation? 
A. 63 
B. 127 
C. 128 
D. 1023 
Answer: B. 127 
Explanation 
For normal single-precision numbers: 
𝐸biased = 𝐸actual + 127 
33. If the actual exponent is −𝟑, what is the biased exponent? 
A. 124 
B. 127 
C. 130 
D. 131

--- [Page 11 of 21] ---
Answer: A. 124 
Explanation 
𝐸biased = −3 + 127 
= 124 
 
In binary: 
12410 = 011111002 
 
34. Convert 𝟐𝟎𝟏𝟎into normalized binary scientific notation. 
A. 1.01 × 24 
B. 1.01 × 23 
C. 10.1 × 24 
D. 1.1 × 25 
Answer: A 
Explanation 
First convert 20 to binary: 
2010 = 101002 
 
Normalize: 
101002 = 1.01002 × 24 
 
Therefore: 
1.012 × 24 
 
35. What is the normalized binary representation of 𝟏𝟐𝟏𝟎? 
A. 1.1 × 23 
B. 1.1 × 22 
C. 1.01 × 23 
D. 1.11 × 22 
Answer: A 
Explanation 
1210 = 11002 
 
Move the binary point: 
11002 = 1.1002 × 23

--- [Page 12 of 21] ---
Therefore: 
1.12 × 23 
 
36. The number 𝟏. 𝟏𝟎𝟏𝟐× 𝟐𝟒has an actual exponent of: 
A. 1 
B. 4 
C. 101 
D. 131 
Answer: B. 4 
Explanation 
In: 
𝑀× 2𝐸 
 
the exponent is 𝐸. 
Therefore: 
𝐸= 4 
 
Its biased exponent would be: 
4 + 127 = 131 
 
Do not confuse actual exponent = 4 with biased exponent = 131. 
37. Why is the leading 1 of a normalized binary floating-point number usually not stored? 
A. It is always 0 
B. It is always 1 for normalized nonzero binary numbers 
C. It represents the sign 
D. It represents the exponent 
Answer: B 
Explanation 
A normalized binary number has the form: 
1. 𝑥𝑥𝑥𝑥𝑥× 2𝐸 
 
The digit before the binary point is always: 
1 
 
Therefore, storing it would waste one bit.

--- [Page 13 of 21] ---
It is assumed automatically and is called the: 
implicit leading one 
 
38. What is the biased exponent for an actual exponent of +𝟏𝟎? 
A. 117 
B. 127 
C. 137 
D. 138 
Answer: C. 137 
Explanation 
10 + 127 = 137 
 
In binary: 
13710 = 100010012 
 
39. An IEEE 754 single-precision number has biased exponent 𝟏𝟑𝟎. What is its actual exponent? 
A. 3 
B. −3 
C. 130 
D. 257 
Answer: A. 3 
Explanation 
To recover the actual exponent: 
𝐸= 𝐸biased −127 
 
Therefore: 
130 −127 = 3 
 
40. An IEEE 754 single-precision number has biased exponent 10000010₂. What is the actual 
exponent? 
A. 2 
B. 3 
C. 129 
D. 130 
Answer: B. 3 
Explanation 
First convert:

--- [Page 14 of 21] ---
100000102 = 13010 
 
Then subtract the bias: 
130 −127 = 3 
 
Therefore: 
𝐸= 3 
 
41 What is the normalized binary representation of 𝟒𝟎𝟏𝟎? 
A. 1.01 × 25 
B. 1.01 × 24 
C. 1.1 × 25 
D. 1.001 × 25 
Answer: A 
Explanation 
Convert 40 to binary: 
4010 = 1010002 
 
Normalize: 
1010002 = 1.010002 × 25 
 
Therefore: 
1.012 × 25 
 
42. For 𝟒𝟎𝟏𝟎= 𝟏. 𝟎𝟏𝟐× 𝟐𝟓, what is the biased exponent? 
A. 5 
B. 127 
C. 130 
D. 132 
Answer: D. 132 
Explanation 
Actual exponent: 
𝐸= 5 
 
Bias:

--- [Page 15 of 21] ---
127 
 
Therefore: 
5 + 127 = 132 
 
And: 
13210 = 100001002 
 
43. Which is the correct IEEE 754 representation of +𝟒𝟎𝟏𝟎? 
A. 0 10000100 01000000000000000000000 
B. 0 00000101 01000000000000000000000 
C. 1 10000100 01000000000000000000000 
D. 0 10000100 10100000000000000000000 
Answer: A 
Explanation 
Step 1: 
40 = 1010002 
 
Step 2: Normalize: 
1.01000 × 25 
 
Step 3: Sign: 
0 
 
Step 4: Biased exponent: 
5 + 127 = 132 = 10000100 
 
Step 5: Remove implicit leading 1: 
1. 01000 
 
Fraction: 
01000000000000000000000 
Final: 
0 10000100 01000000000000000000000

--- [Page 16 of 21] ---
44. Convert 𝟏𝟖. 𝟓𝟏𝟎to normalized binary notation. 
A. 1.00101 × 24 
B. 1.01001 × 24 
C. 1.00101 × 25 
D. 1.101 × 23 
Answer: A 
Explanation 
Integer part: 
1810 = 100102 
 
Fraction: 
0.5 = 0.12 
 
Therefore: 
18.5 = 10010.12 
 
Normalize: 
10010.1 = 1.00101 × 24 
 
45 Which is the correct IEEE 754 single-precision representation of −𝟏𝟖. 𝟓? 
A. 1 10000011 00101000000000000000000 
B. 0 10000011 00101000000000000000000 
C. 1 00000100 00101000000000000000000 
D. 1 10000011 10010100000000000000000 
Answer: A 
Explanation 
We found: 
18.5 = 10010.12 
 
Normalize: 
1.00101 × 24 
 
Since negative: 
𝑆= 1 
 
Biased exponent:

--- [Page 17 of 21] ---
4 + 127 = 131 
131 = 100000112 
 
Fraction after removing the implicit 1: 
00101 
 
Pad to 23 bits: 
00101000000000000000000 
Therefore: 
1 10000011 00101000000000000000000 
 
46. Decode: 
1 10000001 01000000000000000000000 
A. −2.5 
B. −5 
C. +5 
D. −10 
Answer: B. −5 
Explanation 
Sign: 
𝑆= 1 ⇒negative 
 
Exponent: 
100000012 = 129 
 
Actual exponent: 
129 −127 = 2 
 
Fraction: 
010000... 
Restore implicit leading 1: 
1.012 
1.012 = 1.25 
 
Therefore:

--- [Page 18 of 21] ---
1.25 × 22 = 5 
 
Apply sign: 
−5 
 
47. A normalized binary number is: 
1.011012 × 2−4 
 
What is its biased exponent in single precision? 
A. 123 
B. 124 
C. 127 
D. 131 
Answer: A. 123 
Explanation 
𝐸= −4 
 
Therefore: 
𝐸biased = −4 + 127 
= 123 
 
In binary: 
123 = 011110112 
 
 
48. Convert 𝟏𝟎. 𝟐𝟓𝟏𝟎to normalized binary notation. 
A. 1.01001 × 23 
B. 1.00101 × 23 
C. 1.0101 × 23 
D. 1.01001 × 24 
Answer: A 
Explanation 
Integer: 
10 = 10102 
 
Fraction:

--- [Page 19 of 21] ---
0.25 = 0.012 
 
Therefore: 
10.25 = 1010.012 
 
Normalize: 
1010.01 = 1.01001 × 23 
 
49 In IEEE 754 single precision, which exponent pattern is reserved for zero and subnormal 
numbers? 
A. All 0s 
B. All 1s 
C. 10000000 
D. 01111111 
Answer: A. All 0s 
Explanation 
An exponent field of: 
00000000 
is reserved for: 
• 
Zero  
• 
Subnormal numbers  
For exact zero, the fraction is also all zeros. 
50. Which exponent pattern is used for infinity and NaN? 
A. All 0s 
B. All 1s 
C. Alternating 1s and 0s 
D. 01111111 
Answer: B. All 1s 
Explanation 
Exponent: 
11111111 
is reserved for special values. 
If fraction = all 0s: 
±∞

--- [Page 20 of 21] ---
If fraction ≠ 0: 
𝑁𝑎𝑁 
 
51. Approximately how many significant decimal digits does double precision provide? 
A. 7 
B. 8 
C. 15 
D. 64 
Answer: C. About 15 digits 
52 A student sees the exponent field 10000101₂ in a normal single-precision number and 
concludes that the actual exponent is 133. What is the correct actual exponent? 
A. 6 
B. 127 
C. 133 
D. 260 
Answer: A. 6 
Explanation 
First: 
100001012 = 133 
 
But 133 is the biased exponent, not the actual exponent. 
Therefore: 
𝐸= 133 −127 
𝐸= 6 
 
This is an important distinction: 
Stored exponent ≠Actual exponent 
 
for normal IEEE 754 numbers. 
53 The IEEE 754 representation of a normal number begins: 
0 10000100 10100000000000000000000 
What is its decimal value? 
A. 26 
B. 52 
C. 13 
D. 104

--- [Page 21 of 21] ---
Answer: B. 52 
Explanation 
Exponent: 
100001002 = 132 
 
Actual exponent: 
132 −127 = 5 
 
Fraction: 
101... 
Restore implicit 1: 
1.1012 
 
Convert: 
1.1012 = 1 + 0.5 + 0.125 = 1.625 
 
Now: 
1.625 × 25 
= 1.625 × 32 
52

```

---

<a id="doc-7"></a>
## Document 7: Lecture Notes: Finite State Machines Comprehensive (24 Pages)
**Source Document**: `notes/FSM.pdf`
**OCR Extraction File**: `Notes_FSM.txt`

```
================================================================================
ORIGINAL DOCUMENT : FSM.pdf
OCR PDF FILE      : Notes_FSM_ocr.pdf
TOTAL PAGES       : 24
WORD COUNT        : 6798
CHARACTER COUNT   : 40151
DATE EXTRACTED    : 2026-11-04 14:06:28
================================================================================

--- [Page 1 of 24] ---
£ 
Fik e Modung 
(FSM) 
¥ 
Mo&e& I Ae,;ifim 
%M\wmm 
%U\peflm Civeuite 
¥ Sl no. 
of d19, ddomiteh Lok m aun e b= 
e, Sy 
¥ b d, Teqidor = T gt 
% TN can or&%ibe'\«om&ficafiia’nm 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN 
FINITE STATE MACHINE 
@ 
An FSM consists of: 
*M Inputs — Signals received from the external 
system. 
* N Outputs — Signals produced by the circuit. 
* k-bit State Register — Stores the current state 
of the FSM. 
*Clock Signal (CLK) — Controls when the state 
changes. 
* Optional Reset Signal — Returns the FSM to its 
inpat=0 
initial state. 
H 
OL&WB 
boused 
OV\JTW@ 
0fi 
FSM 
L 
Moore = F (cpwe. shate) 
CLK 
Working Principle: 
On every clock edge, the FSM: 
1.Reads the current state. 
2.Accepts the current inputs. 
3.Computes the next state. 
4.Updates the state register. 
5.Produces the required outputs. 
DIGITAL LOGIC AND COMPUTER DESIGN 
FSM DESIGN EXAMPLE 
PES 
UNIVERSITY 
Meet Ben, a smart engineering student 
who loves solving real-world problems. 
the busy intersection between Academic Avenue and & _* 
Bravado Boulevard. 
: 
Students are moving between the Dormitories and 
& 
the Labs on Academic Ave. 
# 
Football players are traveling between the Athletic | 
Fields and the Dining Hall on Bravado Blvd. 
Since 
many 
people 
are 
busy 
and 
not 
paying 
attention, several accidents have already occurred at 
the intersection. 
The 
Dean 
of Students 
asks 
Ben 
to design 
an 
attamatic traffic lisht cantroller 
DIGITAL LOGIC AND COMPUTER DESIGN 
FSM DESIGN EXAMPLE 
PES 
UNIVERSITY 
Design an FSM-based traffic light controller 
that uses traffic sensors to control the traffic 
: 
: 
2| 
Dining 
lights and ensure safe, smooth traffic flow at 
2 
Hall 
the campus intersection. 
§ LE 
810 
g4 
Solution: 
Academic @ @ Ave. 
Labs 
LB 
Dorms 
Ben decides to solve the problem using a Finite 
State Machine (FSM) that can monitor traffic 
g Athletic 
and control the signals automatically. 
= 
| Fields 
Vo, T 
Campus map 
oY T F 0 Ly 
itk 
e 
AN 
S 
= 
rfiegej’ 
Mooxe s 
) stde [fL\ 20 Shre francior Digam va Quodor Loste )

--- [Page 2 of 24] ---
\ tegie 
l/lf 
Lyg 
S, QAV%“ Red 
\(e)fiow /QeJe 
\Q\E& 9/{?91’) 
53 
P@& 
%U{/W 
) S 
Tl %fifi@ N fl&él@ 
E} @m@w\ 
S)%J@ {?cm Tfl(on 
Zf) 
Tnwding : 
State Transitions 
Reset—S0 
g 
J 
The FSM always enters State SO whenever the 
Reset signal is activated. 
S0 — $1: If T, = 0, the controller changes from SO 
to S1. 
$1-82: 
After 
5 
seconds, 
the 
automatically changes from S1 to S2. 
82 — 83: If Tz =0, the controller changes from 
S2to S3. 
controller 
83 — S0: After 5 seconds, the controller returns to 
S0, completing one traffic signal cycle. 
Conditions for Remaining in the Same State: 
S0 —»S0whenT, =1 
S§2 - S2whenTp =1 
Why Encoding? 
+ 
Converts 
symbolic states into binary 
values. 
Makes the FSM compat 
atible with digital ci 
Smpu 
s the deri 
of Boolean equations. 
* 
Encoding transforms the FSM from a conceptual model into a form that can 
be implemented using digital hardware. 
Lble 
9 
O 
e e 
ale eflw&m& 
op eww)mgg 
S0 XS | (fon 
S 
S, 
Lo 
b 
Sl x 
Slam 
S 
0 
o] 
o o 
SooX 
X 
S | brngon 
S, 
0 
| 
oo o 
S 
X 
o 
Diaguor) 
<. 
[ 
O 
mly 
0 
SSox 
LS, 
S 
5 
X 
X 
S 
et 
s s by s 
Cubpl ToHe: (fom 
s tokle 
S 
L 
T Te 
& s (o 
S 
% 
nhe 
W 
0 
0 
X 
91| 
th 
0o 
o 
0O 
| 
0 
O 
I 
T 
2 
R 
9 
1 
X 
X 
L 
o 
Eable 
I 
0 
1 
o 
OO0 
o 
x 
0 
| 
V| 
g 
1l 
0 
o] 
| 
O 
X 
|V 
©o 
Gl 
VLo 
x 
X 
0 
O 
ano&lng) 
?) K~MmE5 
1 
/ 
lov 
S 
(from) 
fo S 0D 
7% e ke Wl 
s.|o 
©o 
0 
© 
I 
1 
o 
o 
% 
I 
o 
o 
o 
O 
Ssel 
v 
O 
D 
O 
o 
o 
O 
sl U0 
[ 
o 
O 
| 
=T rsS 
o |C= S5 T t S5 T 
Ly =5 
Ly = 95 
Ly, = 5, 
Lay =S5, 
DIGITAL LOGIC AND COMPUTER DESIGN 
COMPLETE FSM LOGIC CIRCUIT 
state register 
@) 
Ta 
inputs 
(b) 
ofr e 
PES 
UNIVERSITY 
@ 
- 
S'o 
So 
T 
So 
next state logic 
Loy 
+ off fin(pdlmfl)

--- [Page 3 of 24] ---
output 
outputs 
(c) 
logic 
Figure 3.26 State machine circuit for traffic light controller 
DIGITAL LOGIC AND COMPUTER DESIGN 
STATE ENCODING 
@@ PES 
UNIVERSITY 
* 
State Encoding is the process of assigning binary codes to the states of a Finite State 
Machine (FSM). 
* 
The choice of encoding directly affects the hardware implementation, including the 
number of logic gates, propagation delay, and overall circuit complexity. 
Different state encodings can produce different: 
* circuit implementations 
* numbers of logic gates 
* propagation delays 
* hardware complexity 
Therefore, selecting an appropriate encoding helps in designing an efficient FSM. 
DIGITAL LOGIC AND COMPUTER DESIGN 
STATE ENCODING 
@@ PES 
* 
Finding the optimal encoding is difficult because it requires checking all possible 
encoding combinations, which becomes impractical as the number of states increases. 
* 
Instead, designers usually choose a suitable encoding based on the application or use 
Computer-Aided Design (CAD) tools to help select an efficient encoding. 
* 
The choice of state encoding influences the speed, size, and complexity of the final 
digital circuit. 
DIGITAL LOGIC AND COMPUTER DESIGN 
BINARY ENCODING 
@@ PES 
UNIVERSITY 
In Binary Encoding, each state of the FSM is represented using a binary number. 
For an FSM with K states, the number of bits required is: 
Only the minimum number of bits needed to represent all states is used. 
Ex:For 4 states 
State 
Binary Code 
SO 
00 
S1 
01 
S2 
10 
S3 
11 
Advantages 
* 
Uses fewer state bits and requires fewer flip-flops 
» 
Efficient hardware utilization 
DIGITAL LOGIC AND COMPUTER DESIGN 
ONE HOT ENCODING 
% UNIVERSITY 
In One-Hot Encoding, each state is assigned a separate bit. 
Only one bit is HIGH (1) at any given time, while all other bits remain LOW (0). 
For K states, K bits are required. 
Example:For 3 states 
State 
Encoding 
SO 
001 
S1 
010 
S2 
100 
Advantages 
Simpler combinational logic and faster implementation 
Disadvantages 
Requires more flip-flops and higher hardware cost 
DIGITAL LOGIC AND COMPUTER DESIGN 
DESIGNING A DIVIDE-BY-3-COUNTER 
UNIVERSITY 
To understand how different state encoding techniques are applied, consider the 
design of a Divide-by-3 Counter. 
A Divide-by-3 Counter is a sequential circuit that reduces the frequency of the 
input clock by a factor of 3. 
LK 
System Description: 
Y 
« 
The FSM has one output (Y) and three states 
@ 
S0,S1,and S2. 
. 
Rocat

--- [Page 4 of 24] ---
* 
The output Y becomes HIGH (1) for one clock 
cycle out of every three clock cycles. 
Figure 3.28 Divide-by-3 counter 
(a) waveform and (b) state 
transition diagram 
DIGITAL LOGIC AND COMPUTER DESIGN 
DESIGNING A DIVIDE-BY-3-COUNTER 
@ PES 
UNIVERSITY 
Operation: 
The counter continuously cycles through the following sequence: 
SO - S1 - S2 - SO0 - ... 
This repeating sequence divides the clock frequency by 3. 
CLK 
Y 
Reset 
Figure 3.28 Divide-by-3 counter 
(a) waveform and (b) state 
transition diagram 
DIGITAL LOGIC AND COMPUTER DESIGN 
STATE TRANSITION TABLE 
@@ PES 
UNIVERSITY 
1. State Transition Table: 
The State Transition Table defines the next state for every current state. 
Table 3.6 Divide-by-3 counter 
state transition table 
SO 
S1 
S1 
I 
S2 
S2 
I 
SO 
DIGITAL LOGIC AND COMPUTER DESIGN 
OUTPUT TABLE 
@@ PES 
UNIVERSITY 
2. Output Table: 
The Output Table specifies the output value associated with each state. 
Table 3.7 Divide-by-3 counter 
output table 
Current State 
Output 
DIGITAL LOGIC AND COMPUTER DESIGN 
BINARY VS ONE HOT ENCODING 
PES 
UNIVERSITY 
To implement the Divide-by-3 Counter in hardware, each state must be assigned 
a binary code. Two commonly used encoding techniques are Binary Encoding and 
One-Hot Encoding. 
Table 3.8 One-hot and binary encodings for divide-by-3 counter 
One-Hot Encoding 
Binary Encoding 
S, 
0 
50 
0 
0 
| 
0 
0 
51 
0 
| 
0 
0 
1 
§2 
1 
0 
0 
| 
0 
DIGITAL LOGIC AND COMPUTER DESIGN 
STATE TRANSITION TABLE USING BINARY ENCODING 
PES 
UNIVERSITY 
Binary State Transition Table 
* 
The Binary State Transition Table uses the 2-bit binary codes assigned to each state. 
* 
States are represented using 2 bits.

--- [Page 5 of 24] ---
Table 3.9 State transition table with binary encoding 
Next State 
Current State 
S, 
0 
0 
0 
1 
0 
1 
I 
1 
0 
1 
0 
I 
0 
0 
DIGITAL LOGIC AND COMPUTER DESIGN 
STATE TRANSITION TABLE USING ONE-HOT ENCODING 
UNIVERSITY 
One-Hot State Transition Table 
* 
The One-Hot State Transition Table uses one flip-flop for each state 
* 
Each state is represented by a unique active bit. Only one bit is HIGH at any time. 
Table 3.10 State transition table with one-hot encoding 
Current State 
Next State 
Y 
\J 
S« 
0 
0 
1 
0 
1 
0 
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
1 
DIGITAL LOGIC AND COMPUTER DESIGN 
FSM IMPLEMENTATION 
UNIVERSITY 
Binary Encoding Implementation: 
next state logic state register ~ output logic 
output 
One-Hot Encoding Implementation: 
oK 
— 
o 
[ 
Py 
M 
s 
Reset 
DIGITAL LOGIC AND COMPUTER DESIGN 
TYPES OF FSM 
&)PES 
UNIVERSITY 
Moore Machine: 
Output depends only on the current state. Changes in input do not immediately 
affect the output. Output changes only after the state changes. Outputs are written 
inside the state circles. 
Formula 
Output = f(Current State) 
2 Finite state 
(a) Moore machine, 
DIGITAL LOGIC AND COMPUTER DESIGN 
TYPES OF FSM 
UNIVERSITY 
Mealy Machine 
Output depends on both the current state and the current inputs. Output can change 
immediately when the input changes. Generally requires fewer states than a Moore 
machine. Outputs are written on the transition arrows. 
Formula 
Output = f(Current State, Current Input) 
(b) Mealy machine 
DIGITAL LOGIC AND COMPUTER DESIGN 
MOORE VS MEALY MACHINES 
@ UNIVERSITY

--- [Page 6 of 24] ---
Scenario: 
Alyssa P. Hacker owns a pet robotic snail controlled by a Finite State 
Machine (FSM).The snail moves over a paper tape containing 
sequence of 1s and Os. 
At every clock cycle: 
The snail moves one position forward. 
It remembers the last two bits it has read. 
The snail smiles when a specific bit pattern is detected. 
1w 
- 
Irfput:][A]]gurrent bit read by the snail. 
%mfl 
Output:[Y] 
\\\‘\\ 
*Y =1 - Snail smiles. 
*Y = 0 -> Snail does not smile. 
w\\\\\\ 
DIGITAL LOGIC AND COMPUTER DESIGN 
MOORE VS MEALY MACHINES 
@@ PES 
UNIVERSITY 
Objective 
Design both Moore Machine and Mealy Machine .Compare both implementations. 
Moore FSM Design : 
The Moore Machine requires three states. Each state represents the 
previous input history.The output depends only on the current state. 
Reset 
FSM state transition diagrams: (a) Moore machine, 
DIGITAL LOGIC AND COMPUTER DESIGN 
MOORE VS MEALY MACHINES 
@ PES 
UNIVERSITY 
Mealy Machine Design: 
The Mealy Machine requires only two states. Outputs are generated during state 
transitions. 
Each transition is labelled as| Input 
/ Output 
Reset 
1/0 
‘ 
(b) 
DIGITAL LOGIC AND COMPUTER DESIGN 
UNIVERSITY 
MOORE TRANSITION AND OUTPUT TABLE 
PES 
Table 3.11 Moore state transition table 
Current State 
Input 
Next State 
S 
/ 
) 
Table 3.12 Moore output table 
Current State 
~ Output 
NU 
1 
SO 
S 
Y 
S1 
0 
S1 
S1 
1 
52 
S1 
0 
S2 
0 
S1 
S2 
1 
S2 
1 
SO 
DIGITAL LOGIC AND COMPUTER DESIGN 
MOORE TRANSITION AND OUTPUT TABLE WITH BINARY ENCODING 
é@ PES 
UNIVERSITY 
To implement the Moore Machine in digital hardware,each state is assigned a binary 
code.Using these binary encodings,the transition table and output table are rewritten. 
Table 3.13 Moore state transition table with state 
encodings 
Table 3.14 Moore output table 
Current State 
Input 
cht Smtc‘ 
with state encodings 
S 
S 
= 
3 
- 
- 
Current State 
Output 
0 
0 
0 
0 
1 
S 
S 
Y 
0 
0 
1 
0 
0 
0 
1 
0 
0 
1 
0 
1 
0 
0 
1 
1 
1 
0 
1 
0 
1 
1 
0 
0 
0 
1 
1 
0 
1 
0 
0

--- [Page 7 of 24] ---
DIGITAL LOGIC AND COMPUTER DESIGN 
MOORE FSM 
@@ PES 
UNIVERSITY 
Table 3.13 Moore state transition table with state 
encodings 
Table 3.14 Moore output table 
Current State 
Input 
Next State 
S 
A 
S 
S 
with state encodings 
0 
0 
0 
o 
! 
Current State 
Output 
(] 
o 
1 
o 
(8] 
S 
So 
Y 
(8] 
1 
6] 
o 
1 
(o] 
1 
1 
1 
(] 
1 
0 
0 
0 
1 
0 
1 
0 
1 
o 
1 
0 
(] 
1 
0 
1 
Equations: 
S, =A 
Equation 3.3.1 
Y =5 
DIGITAL LOGIC AND COMPUTER DESIGN 
MEALY TRANSITION AND OUTPUT TABLE 
PES 
UNIVERSITY 
The Mealy Machine requires only one state bit. 
Table 3.15 Mealy state transition and output table 
Table 3.16 Mealy state transition and output table with state encodings 
Current State 
Input 
NextState 
Output 
Current State ~ Input ~ NextState 
Output 
§ 
A 
§ 
Y 
5, 
A 
5 
Y 
0 
0 
1 
0 
NI 
1 
50 
0 
0 
1 
0 
0 
St 
0 
51 
0 
| 
0 
1 
0 
St 
1 
N 
1 
1 
1 
0 
1 
DIGITAL LOGIC AND COMPUTER DESIGN 
MOORE VS MEALY MACHINES 
PES 
UNIVERSITY 
Comparison: 
Moore Machine 
Mealy Machine 
More states 
Fewer states 
Stable output 
Faster response 
Output depends only on state 
Output depends on state and input 
One clock delay 
Immediate output 
* 
Choose a Moore Machine when stable outputs are important. 
* 
Choose a Mealy Machine when faster output response is required. 
DIGITAL LOGIC AND COMPUTER DESIGN 
PES 
UNIVERSITY 
FINITE STATE MACHINES 
DIGITAL LOGIC AND COMPUTER DESIGN 
FACTORING STATE MACHINES 
PES 
UNIVERSITY 
As the complexity of a Finite State Machine (FSM) increases, designing and maintaining it 
becomes difficult. 
Instead of designing one large FSM, the system can be divided into multiple smaller FSMs 
that work together. 
This design approach is called Factoring of State Machines. 
How Does It Work? 
* A complex FSM is split into smaller interacting FSMs. 
*The output of one FSM can be used as the input to another FSM.

--- [Page 8 of 24] ---
* I his creates a hierarchical and modular design. 
DIGITAL LOGIC AND COMPUTER DESIGN 
FACTORED AND UNFACTORED STATE MACHINES 
PES 
UNIVERSITY 
To understand the concept of factoring, consider the traffic light controller introduced 
earlier. 
The controller is now modified to include a Parade Mode, which keeps the Bravado 
Boulevard traffic light green while a parade is in progress. 
Additional Inputs: 
Two new control inputs are introduced: 
*P (Parade) — Enables Parade Mode. 
P 
* R (Resume) — Exits Parade Mode. 
R 
Controer: 
> Ly 
Ta— 
FSM 
¥ 
L 
(a) single traffic light controller FSM 
DIGITAL LOGIC AND COMPUTER DESIGN 
FACTORED AND UNFACTORED STATE MACHINES 
é@ PES 
UNIVERSITY 
Controller Behaviour: 
*When P =1, the controller enters Parade Mode. 
* During Parade Mode, the controller follows its normal sequence 
il === 1! 
until LB becomes green. 
P1 
TM 
Mode 
|| 
*Once LB is green, it remains green throughout the parade. 
Al 
FSM 
I 
*When R =1, the controller exits Parade Mode and resumes normal 
| 
: 
traffic operation. 
| 
W 
| 
| 
T 
Lights 
[1*>la 
Objective: 
A 
FSM 
Ly, 
Design the controller using: 
L 
il 
: 
* A single FSM (Unfactored). 
I 
Controller 
| 
: 
FSM 
: 
* Multiple interacting FSMs (Factored). 
M e 
e 
(b) factored designs for modified 
traffic light controller FSM 
DIGITAL LOGIC AND COMPUTER DESIGN 
UNIVERSITY 
UNFACTORED FSM 
@@ PES 
Single FSM Approach: 
In the unfactored design, a single FSM controls both: 
*Normal traffic operation. 
» Parade mode. 
State Organization 
+S0 — S3 — Normal Mode. 
+S4 — S7 — Parade Mode. 
The two halves of the state diagram are almost identical, except that during 
Parade Mode the controller remains in State S6 while LB remains green. 
Characteristics 
*One large FSM. 
*More states. 
« Complex transitions. 
« Difficult to modify and debug. 
DIGITAL LOGIC AND COMPUTER DESIGN 
UNFACTORED FSM 
PES 
UNIVERSITY 
(a) unfactored, 
DIGITAL LOGIC AND COMPUTER DESIGN 
FACTORED FSM 
@@ PES 
UNIVERSITY 
Breaking the FSM into Modules: 
Instead of using one large FSM, the controller is divided into two smaller FSMs. 
Mode FSM: 
Tracks whether the controller is operating in: 
*Normal Mode 
- 
« Parade Mode 
Ressty—~()':

--- [Page 9 of 24] ---
S0 
e 
s1 
Produces output: M 
L, green 
w 
Ly red 
Ly red 
| 
Lights FSM 
, 
‘\ 
| 
Controls the traffic lights using: 
o 
* Traffic Sensors (TA, TB) 
g @ 
* Mode Signal (M) 
N 
Mls W, 
Mode FSM 
Lights FSM 
_ 
. 
(b) factored 
DIGITAL LOGIC AND COMPUTER DESIGN 
FACTORED VS UNFACTORED FSM 
é@ PES 
Unfactored FSM 
Factored FSM 
Single large FSM 
Multiple smaller FSMs 
More states 
Fewer states per FSM 
Complex transitions 
Simpler transitions 
Difficult to debug 
Easier to debug 
Less modular 
Highly modular 
Harder to modify 
Easy to extend 
DIGITAL LOGIC AND COMPUTER DESIGN 
DERIVING AN FSM FROM SCHEMATIC 
PES 
UNIVERSITY 
STEPS FOR DERIVING FSM: 
1.Examine the circuit and identify Inputs,Outputs ,State bits. 
2.Write the next-state and output equations. 
3.Create the next-state and output tables. 
4.Remove unreachable states. 
5.Assign symbolic names to valid states. 
6.Draw the state transition diagram. 
7.Describe the overall function of the FSM. 
DIGITAL LOGIC AND COMPUTER DESIGN 
EXAMPLE 
@@ PES 
UNIVERSITY 
Scenario: 
Alyssa P. Hacker discovers that the keypad lock in her house has been rewired, and the 
original unlock code no longer works.She finds a circuit diagram attached to the keypad 
and suspects it is controlled by a Finite State Machine (FSM).To determine the correct 
unlock sequence, she decides to derive the FSM from the circuit. 
A1 Ao 
CLK 
Figure 3.35 Circuit of found FSM for Example 3.9 
DIGITAL LOGIC AND COMPUTER DESIGN 
STEP1: IDENTIFICATION 
@@ PES 
UNIVERSITY 
Objective 
Determine the FSM states ,State transitions ,Output behaviour 
and Overall 
function of the circuit 
Step 1 - Identify Inputs, Outputs & State Equations: 
From the circuit: 
Inputs: A; A 
Output: Unlock 
State Bits: S¢,So 
Next-State Equations: 
81‘ = SOAlAO 
So' = 51S0A1A0 
Equation (3.12) 
Unlock = S; 
DIGITAL LOGIC AND COMPUTER DESIGN 
STEP2-CREATE TABLES 
PES 
Table 3.17 Next state table derived from circuit 
UNIVERSITY 
Current State 
Input 
Next State 
Step 2 — Create State Tables: 
s 
So 
A 
A, 
s

--- [Page 10 of 24] ---
v 
v 
v 
. 
v 
v 
0 
0 
1 
0 
0 
0 
Table 3.18 Output table derived from circuil 
0 
0 
1 
1 
0 
1 
in Figure 3.35 
0 
1 
0 
) 
0 
0 
Current State 
Output 
0 
! 
0 
! 
! 
0 
Sy 
So 
Unlock 
0 
1 
! 
0 
0 
0 
0 
1 
1 
1 
0 
0 
1 
0 
0 
0 
0 
0 
0 
1 
0 
1 
0 
0 
1 
0 
0 
1 
0 
1 
0 
0 
0 
1 
0 
1 
1 
0 
1 
1 
0 
0 
1 
1 
1 
1 
1 
0 
0 
0 
0 
1 
1 
[ 
1 
1 
0 
1 
1 
1 
0 
0 
0 
1 
1 
1 
1 
0 
o 
DIGITAL LOGIC AND COMPUTER DESIGN 
STEP3-REDUCTION 
% PES 
UNIVERSITY 
Step 3 — Reduce the State Tables: 
Some state combinations are never reached during operation.These are called 
Unreachable States.Removing these states simplifies the FSM. 
Table 3.19 Reduced next state table 
Current State 
Input 
Next State 
. 
' 
" 
" 
= 
’ 
Table 3.20 Reduced output table 
® 
g 
g 
1 
¢ 
® 
Current State 
Output 
0 
0 
1 
0 
0 
0 
Unlock 
0 
0 
1 
1 
0 
1 
0 
1 
0 
0 
0 
0 
0 
0 
0 
[ 
1 
0 
1 
1 
0 
0 
1 
0 
0 
1 
1 
0 
0 
0 
0 
1 
1 
1 
0 
0 
1 
0 
1 
1 
0 
X 
X 
0 
0 
DIGITAL LOGIC AND COMPUTER DESIGN 
STEP4-STATE ASSIGNMENT 
Step 4 — Assign Symbolic State Names: 
After removing unreachable states, each valid state is assigned a symbolic name. 
Binary State 
Symbolic Name 
00 
S0 
01 
S1 
10 
S2 
DIGITAL LOGIC AND COMPUTER DESIGN 
STEP4-STATE ASSIGNMENT 
@@ PES 
UNIVERSITY 
Step 4 — Assign Symbolic State Names: 
Table 3.21 Symbolic next state table 
Current State 
Input 
Next State 
S 
A 
S’ 
Table 3.22 Symbolic output table 
SO 
1 
SO 
S0 
2 
S0 
Currenrl NEE 
Output 
S 
Unlock 
SO 
3 
S1 
S1 
0 
SO 
S1 
1 
S2 
St 
0 
st 
2 
S0 
52 
1 
S1 
3 
SO 
S2 
X 
SO 
DIGITAL LOGIC AND COMPUTER DESIGN 
STEP5-STATE TRANSITION TABLE 
PES 
UNIVERSITY 
Step 5 — Draw the State Transition Diagram: 
Reset 
Using the symbolic tables, the final State Tr: 
Diagram is constructed. 
Overall Behaviour: 
The FSM unlocks the door only after detecting the 
correct input sequence. 
After unlocking, it returns to the initial state, 
ready for the next input sequence 
DIGITAL LOGIC AND COMPUTER DESIGN

--- [Page 11 of 24] ---
FSM REVIEW 
% PES 
UNIVERSITY 
FSM Design Procedure 
General Steps 
1.ldentify the inputs and outputs. 
1.Draw the State Transition Diagram. 
1.Create: 
State Transition Table 
*Output Table 
4.Select a suitable State Encoding. 
4. Write: 
*Next-State Equations 
*Output Equations 
6.Design the circuit schematic. 
PES 
UNIVERSITY 
DIGITAL LOGIC AND COMPUTER DESIGN 
In Example the output Unlock is given by 
Unlock = $; 
This indicates that the output depends on 
A) Current input only 
B) Current state only 
C) Current input and current state 
D) Next state only 
Answer:B 
DIGITAL LOGIC AND COMPUTER DESIGN 
e 
@@ PES 
UNIVERSITY 
2.An FSM is implemented using 5 flip-flops with Binary Encoding. 
What is the maximum number of states that can be represented? 
A)S 
B) 25 
C)31 
D) 32 
Answer 
D 
Explanation: 
In Binary Encoding, each flip-flop stores 1 bit. 
*Number of flip-flops = 5 
*Number of possible states = 2% = 32 
DIGITAL LOGIC AND COMPUTER DESIGN 
Quiz 
@@ PES 
UNIVERSITY 
3.An FSM has 8 states. Using Binary Encoding, how many flip-flops are requirear 
A)2 
B) 3 
C)4 
D) 8 
Answer 
B)3 
Explanation: 
Flip—flops = [log, N1 
llog,8] = [3] = 3 
PES 
THANK YOU 
UNIVERSITY

--- [Page 12 of 24] ---
DIGITAL LOGIC AND COMPUTER DESIGN 
UE25CS152B 
Introduction and Arithmetic Circuits 
Team DLCD 
P Es 
Department of CSE and CSE(AI&ML) 
UNIVE RSITY 
L ceicorvrng 
so v chns§ 
Topics of Discussion 
. 
Operating 
¢ Introduction 
Systems Q 
* Arithmetic Circuits 
R —— 
Micro- 
<« » 
* Number Systems 
i 
| 
* Sequential Building Blocks 
* Memory Arrays 
orcus B 
. 
Analog 
* Logic Arrays 
oo L 
Devices 
—@ 
Physics % 
Unit 2 
- 
2 
DIGITAL BUILDING BLOCKS 
Introduction 
¢ 
Digital building blocks: 
— Gates, multiplexers, decoders, registers, arithmetic circuits, 
counters, memory arrays, logic arrays 
¢ 
Building blocks demonstrate hierarchy, modularity, and regularity: 
— Hierarchy of simpler components 
— Well-defined interfaces and functions 
— Regular structure easily extends to different sizes 
¢ Will use these building blocks in Chapter 7 to build microprocessor 
Unit 2 
‘ 
3 
DIGITAL BUILDING BLOCKS 
1-Bit Adders 
PES 
Half 
Full 
Adder 
Adder 
A 
B 
A 
B 
Cur\ L/ 
Cu\ 
4 
/Cn 
s 
S 
A 
B 
|C, 
S 
c, 
A 
B|C, 
S 
0o 
o 
0o 
0 
o 
o 
1 
o 
o0 
1 
1 
0 
o 
1 
o 
101 
0o 
1 
1 
1 
0 
o0 
s 
= 
1 
0 
1 
Cou = 
1 
1 
o0 
o 
11 
1 
S 
= 
Coul= 
Unit 2 
‘ 
. 
4 
DIGITAL BUILDING BLOCKS 
1-Bit Adders 
PES 
Half 
Full 
Adder 
Adder 
A 
B 
A 
B 
4 
CM«\\‘ vl 
s 
A 
B 
‘ Cox 
S 
c, 
A 
B|C, S 
0 
0 
‘ 
0o 
0 
0 
0 
o 
‘ 
CI) 
0 
1 
0 
1 
0 
0 
1 
0 
1

--- [Page 13 of 24] ---
1 
0 
0 
1 
0 
1 
0 
0 
1 
1 
1 
1 
0 
0 
1 
1 
1 
0 
1 
0 
0 
0 
1 
S 
= 
1 
0 
1 
1 
0 
c 
= 
11 
o0of 
1 
o 
ot 
11 
1] 
1 
1 
S 
= 
Com: 
Unit 2 
i 
5 
DIGITAL BUILDING BLOCKS 
1-Bit Adders 
PES 
Half 
Full 
Adder 
Adder 
A 
B 
A 
B 
L~ 
7 
— 
— 
S 
S 
A 
B 
|C, 
S 
c, 
A 
B 
C, 
S 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
1 
0 
1 
0 
0 
1 
0 
1 
1 
0 
0 
1 
0o 
1 
0 
0 
1 
1 
1 
1 
0 
0o 
1 
1 
1 
0 
1 
0 
0 
0 
1 
S 
=A®B 
1 
0 
1 
1 
0 
C.. 
=AB 
1 
1 
0 
1 
0 
out 
11 
1|1 
1 
S 
=A®B®C, 
C,.=AB+AC,+BC, 
Unit 2 
‘ 
6 
DIGITAL BUILDING BLOCKS 
Multibit Adders (CPAs) 
PES 
* Types of carry propagate adders (CPAs): 
— Ripple-carry 
(slow) 
— Carry-lookahead 
(fast) 
— Prefix 
(faster) 
* 
Carry-lookahead and prefix adders faster for large 
adders but require more hardware 
Symbol 
A 
B 
N 
N 
Cout 
Cln 
N 
S 
Unit 2 
- 
7 
! 
DIGITAL BUILDING BLOCKS 
Ripple-Carry Adder 
Ef 
* Chain 1-bit adders together 
* Carry ripples through entire chain 
* Disadvantage: slow 
Az 
By 
A 
By 
A 
B 
Ay 
B 
C 
- 
C 
Sy 
Sy 
S, 
So 
Unit 2 
8 
DIGITAL BUILDING BLOCKS 
Ripple-Carry Adder Delay 
Ef 
tripple = NtFA 
where t;, is the delay of a 1-bit full adder 
Unit 2 
B 
B 
- 
DIGITAL BUILDING BLOCKS 
Carry-Lookahead Adder 
'_’_Ef 
* 
Compute carry out (C,,) for k-bit blocks using generate and 
propagate signals 
* 
Some definitions:

--- [Page 14 of 24] ---
— Column i produces a carry out by either generating a carry out or 
propagating a carry in to the carry out 
— Generate (G;) and propagate (P;) signals for each column: 
* 
Column i will generate a carry out if A; AND B, are both 1. 
G, =A;B; 
* 
Column j will propagate a carry in to the carry out if A; OR B, is 1. 
P;=A; +B; 
* 
The carry out of column i (C) is: 
C;=A;B; +(A; +B;)C.;=G; +P,C,, 
Unit 2 
DIGITAL BUILDING BLOCKS 
Carry-Lookahead Addition 
* Step 1: Compute G; and P; for all columns 
* Step 2: Compute G and P for k-bit blocks 
* Step 3: C,, propagates through each k-bit 
propagate/generate block 
Unit 2 
DIGITAL BUILDING BLOCKS 
Carry-Lookahead Adder 
* Example: 4-bit blocks (G;.,and P;.) : 
G,.,=G;+P;(G,+P, (G, +P,G,) 
P3.o = P3P, P,P, 
* Generally, 
G;j=G;+P; (G, 
+ P, (G, 
+ P,,G)) 
P;j= PPy Pi,P; 
C =G, +P,;C, 
Unit 2 
DIGITAL BUILDING BLOCKS 
32-bit CLA with 4-bit Blocks 
B 
A 
B 
A 
31:28 " '31:28 
27:24 " 727:24 
‘K_J 
QO—:U_\O N-UNG)(-‘-UDO 
¢l 
I 
O 
I\ 
f 
|| 
O 
o 
nnj»{:u 
Unit 2 
DIGITAL BUILDING BLOCKS 
Carry-Lookahead Adder Delay 
For N-bit CLA with k-bit blocks: 
teia =ty + tog block T (N/k - 1)tAND_OR + ktg, 
= by 
delay to generate all P, G; 
g block 
- 
delay to generate all P, G;; 
— tapor: 
delay from G, to C,, of final AND/OR gate in k-bit CLA 
block 
An N-bit carry-lookahead adder is generally much faster than a 
ripple-carry adder for N > 16 
Unit 2 
DIGITAL BUILDING BLOCKS 
Prefix Adder 
UNIVERSITY 
EEEm 
11 
UNIVERSITY 
T 
UNIVERSITY 
EEE 
UNIVERSITY 
S Em 
14 
PES 
UNIVERSITY

--- [Page 15 of 24] ---
¢ 
Computes carry in (C;,) for each column, then 
computes sum: 
5=(A,®B)DC 
* 
Computes G and P for 1-, 2-, 4-, 8-bit blocks, etc. 
until all G; (carry in) known 
log,N stages 
Unit 2 
15 
DIGITAL BUILDING BLOCKS 
Prefix Adder 
Ef 
* 
Carry in either generated in a column or propagated from a 
previous column. 
* 
Column -1 holds G, so 
G,=¢C,P,=0 
* 
Carryinto column i = carry out of column j-1: 
C1=Giyy 
G,,.1: generate signal spanning columns i-1 to -1 
* 
Sum equation: 
5;=(A,®B)DG.,, 
* 
Goal: Quickly compute G,.,, G;.4, G,.1, G3.1, G4y, Gs.g) - 
(called prefixes) 
Unit 2 
16 
DIGITAL BUILDING BLOCKS 
Prefix Adder 
P_Ef 
* 
Generate and propagate signals for a block spanning bits 
iy 
G =Gy * Py Gyy 
Pij = PisPyy 
* 
Inwords: 
— Generate: block iij will generate a carry if: 
* 
upper part (i:k) generates a carry or 
* 
upper part propagates a carry generated in lower 
part (k-1:j) 
— Propagate: block i:j will propagate a carry if both the 
upper and lower parts propagate the carry 
Unit 2 
17 
DIGITAL BUILDING BLOCKS 
Prefix Adder Schematic 
PES 
[ 15 
\ 1 
= 
f 
Ll 
i1l 
‘J’:TJ ) 
\ 
hr ) 
O 
Unit 2 
18 
DIGITAL BUILDING BLOCKS 
Prefix Adder Delay 
PES 
tPA = tpg + IOgZN(tpg_prefix) + tXOR 
— t,,: delay to produce P; G; (AND or OR gate) 
-t 
: delay of black prefix cell (AND-OR gate) 
pg_prefix* 
Unit 2 
19

--- [Page 16 of 24] ---
DIGITAL BUILDING BLOCKS 
Adder Delay Comparisons 
P_Ef 
Compare delay of: 32-bit ripple-carry, carry-lookahead, and 
prefix adders 
* 
CLA has 4-bit blocks 
e 
2-input gate delay = 100 ps; full adder delay = 300 ps 
Unit 2 
‘ 
) 
20 
DIGITAL BUILDING BLOCKS 
Adder Delay Comparisons 
PES 
Compare delay of: 32-bit ripple-carry, carry-lookahead, and 
prefix adders 
* 
CLA has 4-bit blocks 
* 
2-input gate delay = 100 ps; full adder delay = 300 ps 
t 
= Nt,, = 32(300 ps) 
ripple 
=9.6 ns 
taa 
= thg * tog block t (N/k = L)tanp 
or * ktpa 
=[100 + 600 + (7)200 + 4(300)] ps 
=3.3ns 
tPA 
= tpg + IOgZN(tpg_prefix) + tXOR 
=[100 + log,32(200) + 100] ps 
Unit 2 
=12ns 
. 
21 
DIGITAL BUILDING BLOCKS 
Subtracter 
fff 
Symbol 
Implementation 
A 
B 
N 
N 
N 
Y 
Unit 2 
‘ 
22 
DIGITAL BUILDING BLOCKS 
Comparator: Equality 
e 
Symbol 
Implementation 
Ay 
B, 
A 
B 
Al 
s 
Js 
B, 
fi} 
Equal 
A1 J}T\‘O— 
B1 /i 
Equal 
P A o 
Bo /B 
Unit 2 
‘ 
- 
23 
DIGITAL BUILDING BLOCKS 
PES 
Comparator: LessThan 
e

--- [Page 17 of 24] ---
Unit 
2 
DIGITAL BUILDING BLOCKS 
Arithmetic Logic Unit (ALU) 
24 
UNIVERSITY 
L 
000 
A&B 
001 
A|B 
010 
A+B 
011 
not used 
100 
A& ~B 
101 
A|~B 
110 
A-B 
111 
SLT 
Unit 2 
25 
DIGITAL BUILDING BLOCKS 
ALU Design 
UNIVERSITY 
o 
000 
|A&B 
001 
|AIB 
010 
|A+B 
011 
not used 
Cou 
100 
|A&-~B 
2 
101 
|A[-B 
ok 
110 
|A-B 
\ 
111 
|SLT 
Unit 
2 
DIGITAL BUILDING BLOCKS 
Adder Delay Comparisons 
UNIVERSITY 
T 
Compare delay of: 32-bit ripple-carry, carry-lookahead, and 
prefix adders 
* 
CLA has 4-bit blocks 
* 
2-input gate delay = 100 ps; full adder delay = 300 ps 
t, ripple 
= NtFA = 32(300 pS) 
=9.6ns 
= tpg + tpg_block+ (N/k_ 1)tAND_OR + ktFA 
=[100 + 600 + (7)200 + 4(300)] ps 
=3.3ns 
tPA 
= tpg + IOgZN(tpg_prefix) + tXOR 
= [100 + log,32(200) + 100] ps 
Unit 2 
=12ns 
27 
tCLA 
DIGITAL BUILDING BLOCKS 
Set Less Than (SLT) Example 
UNIVERSITY 
T 
* 
Configure 32-bit ALU for SLT 
operation: A= 25 and B = 32 
Unit 2 
28 
UNIVERSITY 
T 
DIGITAL BUILDING BLOCKS 
Set Less Than (SLT) Example 
N 
N 
* 
Configure 32-bit ALU for SLT 
/ 
operation: 
A =25and B =32 
EN 
— A< B, so Yshould be 32-bit 
\= e/ 
F, 
representation of 1 (0x00000001) 
— Fpo=111

--- [Page 18 of 24] ---
A 
‘ 
— F,=1 (adder acts as 
\ 
\ 
AN ,/ 
‘.; 
, 
Cou —\_+ 
/ 
1 
subtracter), so 25 -32 =-7 
~ns 
— -7 has 1 in the most significant 
o - 
bit (S, = 1) 
T 1T aN 
AN 
/ 
— Fo=11 multiplexer selects Y 
\ 
[% Fro 
=S, (zero extended) = 
YN 
0x00000001. 
Unit 2 
- 
29 
DIGITAL BUILDING BLOCKS 
Shifters 
® 
Logical shifter: shifts value to left or right and fills empty spaces with 
0’s 
— 
Ex:11001>>2= 
— 
Ex:11001<<2= 
® 
Arithmetic shifter: same as logical shifter, but on right shift, fills empty 
spaces with the old most significant bit (msb). 
— 
Ex:11001>>>2= 
— 
Ex:11001<<<2= 
® 
Rotator: rotates bits in a circle, such that bits shifted off one end are 
shifted into the other end 
— 
Ex: 11001 ROR2= 
— 
Ex:11001ROL2= 
Unit 2 
B 
730 
DIGITAL BUILDING BLOCKS 
Shifters 
UNIVERSITY 
T 
Logical shifter: 
— Ex: 11001 >>2=00110 
— Ex: 11001 << 2 =00100 
e Arithmetic shifter: 
— Ex: 11001 >>>2=11110 
— Ex: 11001 <<< 2 =00100 
* 
Rotator: 
— Ex: 11001 ROR 2 =01110 
— Ex: 11001 ROL2 =00111 
Unit 2 
R 
. 
DIGITAL BUILDING BLOCKS 
Shifter Design 
v 
R 
A 
hamt 
+ 
1~ 
shamt,. 
b 
, 1:0 
O:SL 
4 
4 
o ] ! 
Unit 2 
<~ 
32 
DIGITAL BUILDING BLOCKS 
Shifters as Multipliers,Dividers 
UNIVERSITY 
e 
® A<<N=Ax2V 
— Example: 00001 << 2 =00100 (1 x22=4) 
— Example: 11101 << 2 =10100 (-3 x2%2=-12) 
& A>>>N=A<2VN 
— Example: 01000 >>> 2 = 00010 (8 +22=2) 
— Example: 10000 >>>2 =11100 (-16 + 22=-4) 
Unit 2 
o 3 
DIGITAL BUILDING BLOCKS 
Multipliers 
UNIVERSITY 
T 
¢ Partial products formed by multiplying a single digit 
AfthA muldinliav asith manldinlicanA

--- [Page 19 of 24] ---
Ul LHIT TTTUILIPHICE 
WILLL Hdiupneaniu 
e Shifted partial products summed to form result 
Decimal 
Binary 
230 
multiplicand 
0101 
X 4z 
_x U111 
460 
partial 
0101 
+ 920 
products 
0101 
9660 
0101 
+ 0000 
result 
0100011 
230 x 42 = 9660 
5x7=35 
Umt 2 
Dspanmemofcsgalld AIML 
DIGITAL BUILDING BLOCKS 
4 x 4 Multiplier 
PES 
A 
B 
AL A 
A 
A 
x 
B, 
B, 
B 
B 
AB, AB, AB, AB, 
AB, AB, AB, AB, 
AB, AB, AB, AB, 
+ 
ABABABAB, 
P, 
P, 
P, 
P, 
P, 
P 
3 
2 
P\ 
P(l 
Unit 2 
- 
35 
DIGITAL BUILDING BLOCKS 
4 x 4 Divider 
PES 
— 
- 
— 
— 
YT 
LA 
. 
5M|Cfi 
“ 
. 
D 
. 
NR 
A o 
=] 
____/ 
A/B=Q+R/B 
Algorithm: 
R'=0 
fori=N-1to0 
R={R << 1.A} 
D=R-B 
ifD<0,Q=0,R’=R 
else 
Q=1,R=D 
R’=R 
Unit 2 
36 
MCQs 
UNIVERSITY 
oy 
Q1. What are the different types of Carry 
propagator adders? 
a)Ripple carry adders 
b)Carry lookahead adders 
c) Prefix adders 
d)Skip ahead adders 
Unit 2 
37 
MCQs 
UNIVERSITY 
T 
Q1. What are the different types of Carry 
propagator adders? 
a)Ripple carry adders 
b)Carry lookahead adders 
c) Prefix adders 
d)Skip ahead adders 
Unit 2 
38 
oo 
[\

--- [Page 20 of 24] ---
MCQs 
&/ 
Q2. A comparator is used to: 
a. Add two numbers 
b. Multiply two numbers 
c. Determine relative magnitude of two numbers 
d. Shift 
a number 
Unit 2 
39 
MCQs 
PES 
Q2. A comparator is used to: 
a. Add two numbers 
b. Multiply two numbers 
c. Determine relative magnitude of two numbers 
d. Shift a number 
Unit 2 
40 
MCQs 
Q3. Which circuit performs arithmetic and logical 
operations? 
a. Decoder 
b. Multiplexer 
c. ALU 
d. Counter 
Unit 2 
41 
MCQs 
Q3. Which circuit performs arithmetic and logical 
operations? 
a. Decoder 
b. Multiplexer 
c. ALU 
d. Counter 
Unit 2 
42 
— 
THANK YOU 
D 
@ 
Team DLCD 
PES 
Department of CSE and CSE(AI&ML) 
UNIVERSITY 
oL 
<anuriiie 
re vy

--- [Page 21 of 24] ---
DIGITAL LOGIC AND 
COMPUTER DESIGN 
PES 
DIGITAL BUILDING BLOCKS 
UNIVERSITY 
Number Systems 
IR 
Team DLCD 
Department of CSE and AIML 
L 
UNIVERSITY 
per—y 
DIGITAL BUILDING BLOCKS 
Number Systems 
Team DLCD 
DIGITAL BUILDING BLOCKS 
Number Systems 
Numbers we can represent using binary representations 
-Positive numbers 
Unsigned binary 
-Negative numbers 
Two’s complement 
Sign/magnitude numbers 
‘What about fractions? 
DIGITAL BUILDING BLOCKS 
Numbers with Fractions 
Two common notations: 
— Fixed-point: binary point fixed 
— Floating-point: binary point floats to 
the right of the most significant 1 
DIGITAL BUILDING BLOCKS 
Fixed-Point Numbers 
NTVeRSITY 
sty 
6.75 using 4 integer bits and 4 fraction bits: 
01101100 
0110.1100 
22+ 21+ 2V4.22=6.75 
-Binary point is implied 
-The number of integer and fraction bits must be agreed upon 
beforehand 
DIGITAL BUILDING BLOCKS 
Fixed-Point Number Example 
NTveRSITY 
. 
Represent 7.5, using 4 integer bits 
and 4 fraction bits. 
DIGITAL BUILDING BLOCKS 
Fixed-Point Number Example 
Represent 7.5, using 4 integer bits 
and 4 fraction bits. 
Answer: 01111000 
DIGITAL BUILDING BLOCKS 
@ 
Signed Fixed-Point Numbers 
PES 
Representations: 
nveRsTTY 
— 
Sign/magnitude 
— 
Two’s complement 
Example: Represent -7.5, using 4 integer and 4 fraction bits 
— 
Sign/magnitude: 
— 
Two’s complement: 
DIGITAL BUILDING BLOCKS 
Signed Fixed-Point Numbers 
PE 
Representations: 
izl 
— 
Sign/magnitude 
— 
Two’s complement 
Example: Represent -7.5,, using 4 integer and 4 fraction bits 
— 
Sign/magnitude: 
11111000 
— 
Two’s complement: 
1.47.5: 
01111000 
2. Invert bits: 
10000111 
3.Add 1to LSB: 
+ 
1 
10001000 
DIGITAL BUILDING BLOCKS 
Floating-Point Numbers 
® 
Binary point floats to the right of the most significant 1 
UNIVERSITY 
® 
Similar to decimal scientific notation 
43

--- [Page 22 of 24] ---
Example: write 273, 
in scientific notation: 
273=273 % 102 
In general, a number s written in scientific notation as: 
+ M x BE 
— 
M = mantissa 
— 
B =base 
— 
E =exponent 
— 
Inthe example, 
M=2.73,B = 10,and E=2 
DIGITAL BUILDING BLOCKS 
Floating-Point Numbers 
1bit 
8 bits 
23 bits 
Sign Exponent 
Mantissa 
‘We show three versions —final version is called the IEEE 754 floating-point standard 
Example: represent the value 228, using a 32-bit floating point representation 
DIGITAL BUILDING BLOCKS 
Floating-Point Representation 1 
PES 
Example: represent the value 228, using a 32-bit floating point representation 
vy 
1. Convert decimal to binary (don’t reverse steps 1 & 21): 228,, = 11100100, 
2. Write the number in “binary scientific notation”: 11100100, = 1.11001, x 27 
3. Fill in each field of the 32-bit floating point number: 
~The sign bit is positive (0) 
~The 8 exponent bits represent the value 7 
-The remaining 23 bits are the mantissa 
1bit 
s 
it 
00000111 
| 
111001 
0000 0000 0000 0000 
Sign 
Exponent 
Mantissa 
DIGITAL BUILDING BLOCKS 
Floating-Point Representation 2 
* 
First bit of the mantissa is always 1: 
-228,, = 11100100, = 1.11001 x 27 
* 
So, no need to store it: implicit leading 1 
* 
Store just fraction bits in 23-bit field 
1 bit 
8 bits 
0| 
00000111 
110 0100 0000 0000 0000 0000 
Sign 
Exponent 
Fraction 
DIGITAL BUILDING BLOCKS 
Floating-Point Representation 3 
Biased exponent: bias = 127 (01111111,) 
— 
Biased exponent = bias + exponent 
— 
Exponentof 
7 is stored as: 127 + 7 = 134 = 0x 10000110, 
‘The IEEE 754 32-bit floating-point representation of 228, 
1 bit 
8 bits 
0| 
10000110 
110 0100 0000 0000 0000 0000 
Sign 
Biased 
Fraction 
Exponent 
In hexadecimal: 0x43640000 
DIGITAL BUILDING BLOCKS 
Floating-Point Example 
Write -58.25,, in floating point (IEEE 754) 
DIGITAL BUILDING BLOCKS 
Floating-Point Example 
PES 
Write -58.25,, in floating point (IEEE 754) 
umrveRstTy 
1. Convert decimal to binary: 58.25,, = 111010.01, 
2. Write in binary scientific notation: 1.1101001 x 2% 
3. Fill in fields: 
Sign bit: 1 (negative) 
8 exponent bits: (127 + 5) = 132 = 10000100, 
23 fraction bits: 110 1001 0000 0000 0000 0000 
1 bit 
8 bits 
23 bits 
‘ 
1 
‘ 
100 0010 0 
110 1001 0000 0000 0000 0000 
Sign 
Exponent 
Fraction 
In hexadecimal: 0xC2690000 
DIGITAL BUILDING BLOCKS 
Floating-Point: Special Cases 
Number 
Sign 
Exponent Fraction 
0 
X 
00000000 | 00000000000000000000000 
» 
0 
11111111 | 00000000000000000000000 
- 
1 
11111111 
| 00000000000000000000000 
NaN 
X 
11111111 
|non-zero 
DIGITAL BUILDING BLOCKS 
Floating-Point Precision 
Single-Precision: 
= 
* 
32-bit 
+ 
1 sign bit, 8 exponent bits, 23 fraction bits 
* 
bias =127 
Double-Precision: 
* 
64-bit 
+ 
1 sign bit, 11 exponent bits, 52 fraction bits 
+ 
bias=1023 
DIGITAL BUILDING BLOCKS 
Floating-Point: Rounding 
® 
Overflow: number too large to be represented 
* 
Underflow: number too small to be represented 
* 
Rounding modes: 
- Down 
-Up 
- Toward zero 
- To nearest

--- [Page 23 of 24] ---
DIGITAL BUILDING BLOCKS 
Floating-Point: Rounding 
UNIVERSITY 
o 
Example: Round 1.100101 (1.578125) to only 3 fraction bits 
Down: 1.100 
Up: 1.101 
Toward zero: 1.100 
To nearest: 1.101 (1.625 is closer to 1.578125 than 1.5 is) 
DIGITAL BUILDING BLOCKS 
Floating-Point Addition 
UNIVERSITY 
o 
1. Extract exponent and fraction bits 
2. Prepend leading 1 to form mantissa 
3. Compare exponents 
4. Shift smaller mantissa if necessary 
5. Add mantissas 
6. Normalize mantissa and adjust exponent if necessary 
7. Round result 
8. Assemble exponent and fraction back into floating-point format 
DIGITAL BUILDING BLOCKS 
Floating-Point Addition Example 
UNIVERSITY 
e 
Add the following floating-point numbers: 
0x3FC00000 
0x40500000 
DIGITAL BUILDING BLOCKS 
Floating-Point Addition Example 
1. Extract exponent and fraction bits 
gy 
1bit 
8 bits 
23 bits 
0 
01111111 
100 000 
D000 000 0000 0000 
Sign 
Exponent 
Fraction 
1bit_ 
8bits 
23 bits 
0 
1 
101 0000 0000 000D 0000 0000 
Sign 
Exponent 
Fraction 
For first number (N1): 
S=0,E=127,F=.1 
For second number (N2): 
S=0,E=128,F=.101 
2. Prepend leading 1 to form mantissa 
NI: 
1.1 
N2: 
1.101 
DIGITAL BUILDING BLOCKS 
Floating-Point Addition Example 
3. Compare exponents 
unverstTY 
127 — 128 = -1, so shift N1 right by 1 bit 
4. Shift smaller mantissa if necessary 
shift N1’s mantissa: 1.1 >>1=0.11 (x2') 
5. Add mantissas 
0.11 x2! 
+ 1.101 x 2! 
10.011 x 2! 
DIGITAL BUILDING BLOCKS 
Floating-Point Addition Example 
6. Normalize mantissa and adjust exponent if necessary 
fruiiliaiilf 
10.011 x 2'=1.0011 x 22 
7. Round result 
No need (fits in 23 bits) 
8. Assemble exponent and fraction back into floating-point format 
S =0,E=2+127 = 129 = 10000001,, 
F = 001100.. 
1bit 
8bits 
23 bits 
0| 
10000001 
| 
001 1000 0000 0000 0000 0000 
Sign 
Exponent 
Fraction 
In hexadecimal: 0x40980000 
DIGITAL BUILDING BLOCKS 
MCQs 
1. Which of the following is NOT a representation for signed fixed- 
e 
point numbers? 
A. Two's Complement 
B. Sign/Magnitude 
C. Excess-127 
D.BothAandB 
2. In IEEE 754 single-precision floating-point format, how many bits 
are allocated for the exponent? 
B.8 
C.11 
D.23 
DIGITAL BUILDING BLOCKS 
MCQs 
UNIVERSITY 
==y 
3. Which IEEE 754 representation corresponds to NaN (Not a Number)? 
A. Exponent = 00000000, Fraction = 000...0 
B. Exponent = 11111111, Fraction = 000...0 
D. Exponent = 00000000, Fraction # 0 
4. During floating-point addition, what is the first operation performed after 
extracting the exponent and fraction bits? 
A. Normalize the mantissa 
B. Round the result 
C. Prepend the implicit leading 1 to form the mantissa 
D. Compare the exponents 
DIGITAL BUILDING BLOCKS 
MCQs 
@ 
1. 
Answer:C. Excess-127 
BOvERSY 
Explanation: 
The PPT lists 
Sign/| 
i 
d 
igned 
fixed- 
point representations. 
N 
swer: B. 8 
Explanation: Single-precision uses 1 sign bit, 8 exponent bits, and 23 fraction 
(mantissa) bits. 
w 
Answer: C. Exponent 
= 11111111, Fraction # 0 
Explanation: NaN is represented by an all-ones exponent with a non-zero fraction 
field. 
> 
Answer: C. Prepend the implicit leading 1 to form the mantissa 
P 
i 
racting 
the 
fields, the hidden leading 1 is restored before 
comparing exponents and performing the addition. 
— 
THANK YOU 
Team DLCD 
Nanartmant nf Camniitar Srianca 2. AINMI

--- [Page 24 of 24] ---
Ucpal uiiciiu vl LullipuLet OUITIILE X ANVIL

```

---

<a id="doc-8"></a>
## Document 8: Lecture Notes: Unit 2 Topics Part 1 (15 Pages)
**Source Document**: `notes/U2N1.pdf`
**OCR Extraction File**: `Notes_U2N1.txt`

```
================================================================================
ORIGINAL DOCUMENT : U2N1.pdf
OCR PDF FILE      : Notes_U2N1_ocr.pdf
TOTAL PAGES       : 15
WORD COUNT        : 439
CHARACTER COUNT   : 1806
DATE EXTRACTED    : 2026-11-04 14:04:52
================================================================================

--- [Page 1 of 15] ---
URR FJ; U 
*{“"2? 
\ 
\/ 
W@‘W\%\f\& , Y‘i\m% 
%‘3‘3\%%@? O 
A@%{}“{M %éj éfii? v{ opS 
G § / 
«J \\\\ \i‘i &K\S\ 
%\Q\{\ ol 
TF W z& o Ay ‘@é 
R ~AAY 
- 
fi =0 
(? 
Co T/ 
Sa N\ 
\ e oeendes 
\,% T 
\w{/ 
X 
P 
| 
55 
Ty 
\ 
Lo Redl 
& 
\/W&& N 
- 
u@e cmef\ 
~_ 
\S

--- [Page 2 of 15] ---
SOk 
— 
%9 - 
W 17 
= 
. 
; 
&5"?@\&% @m\%wm 
S 
\ Q) 
- 
— 
ks 
v 
\a«k ‘§ 
ek 
Ve, 
A n 
BW@. g on mmw 
_ g@\%\% 
| Sl 
LW Ty 
NS 
\§ 
S/(} 
| 
\%, — (Z} EQ ,%{,‘ 
3% 
r 9% TS 
S Se & Sy v 
OO\ 0

--- [Page 3 of 15] ---
59 = 9%t 4G 
Tois 3% & 
G i& I flR&fi 
M‘; i 
OWR. Wmfi\m 
,\‘X@\@ 2

--- [Page 4 of 15] ---
St I 
RS P 
EVSN 
3

--- [Page 5 of 15] ---
Lo 
% 
1Dy 
59 
.f"z"“/ 
Ry e 
By 3 i 
B 
>q 
oS 
| 
S\ 
\ 
Q0

--- [Page 6 of 15] ---
*Data: 
S 
O 
i 
[N G

--- [Page 7 of 15] ---
1k cebe 
WQ\:% %Xx&@ 
Bm 9 
S«3\ 
;S;% 
Took Sae 
(o~ 
S\ 
S0 
(, 
T} 
(m\ 
O A 
O 
O 
£ 
(\) 
ifi%}’ 
ToSos SOKE LEGRE 
L= 
Clo® v A 8q AR = Py 
%%Q\MEEM (i> Saw%?fi 
%%‘K 
@%jg%fi} &x 
== %% 
23@ So= gm < %@@: N Sm %%g E%%v 2 gfi%g“\; 
%X | %Z %VD

--- [Page 8 of 15] ---
g, 
st 
h 
g, 
0 
D= S SSby 
O8I RY S& &

--- [Page 9 of 15] ---
feEe £ 
% %j‘ 
& 
TR 
Qe Ron- 
ism 157) 
W\onu gm \ag_&wgm ?‘T%M : 
6L e i@fi\ m\x\@& xfi)\f\?sf\ “’%&@ \3%% 
3 e 3% Yo | Cromaledl Rk R, 
\Q@z o »?\GN\% o 
W : 
VX AW 
CQ\NJM% 
03\‘\@‘4\ e 2 @;\‘a 
Ml 
' - 
e Mk A S e BE @ 
Wl heun e angly (331\3%,\{\@\8, e odguk Y i 
Q. 
\d«\% e 4 m SPRER - 
Sl 
o 
W»«»«fifn;% F&M 35”%“”% 
%@?\k %%fi}@’ 
j‘i\fi\fii \ 
“r 
0. 
& . 9 
Oty 
o 
A 
= &< 
%=V 
= SR & %Rt SSoR 
G =D = e 
B

--- [Page 10 of 15] ---
B\ 
LR 
\OWen QWS 
N= &R 
S\fi‘&b\t g\fié;\f“* %\?fi — fi

--- [Page 11 of 15] ---
A Qe 
i_ ; o

--- [Page 12 of 15] ---
Mw& 
e ’E\%gfi v 
== p“ Po o 
\N\\tfix&é Sy 
\ &Qfi dak \ K \f\\t}i@

--- [Page 13 of 15] ---
ACHIEVER 
Dater 
[ 
] 
ot Gnbx 
Ctoh 
ABREGC

--- [Page 14 of 15] ---
| 
— 
\w){j\m\gfi f’“\(\\ ‘E%\ 
N 
e 
| 
%3 ?%%%\ %{} \ 
W 
o 4 
e bW 
J 
N 
3 
PR 
Y 
Doz (g2t hn x © %%@\:\ x4 NG

--- [Page 15 of 15] ---
ALV I 
Data: 
§ 
k&»% P 
T 
\KQM\% = (a0 B 
- 
\WYW\%\Q w\(\\ ;‘%% 
gfi m% 
M»J 
%““W L e SN 
i@vé\wp %\fi;\ 
gw 
T 
e 
R T 
\33@*:; K*?g\g X \3@% R ()%?3 @.\ X 
?’2;

```

---

<a id="doc-9"></a>
## Document 9: Lecture Notes: Unit 2 Topics Part 2 (13 Pages)
**Source Document**: `notes/U2N2.pdf`
**OCR Extraction File**: `Notes_U2N2.txt`

```
================================================================================
ORIGINAL DOCUMENT : U2N2.pdf
OCR PDF FILE      : Notes_U2N2_ocr.pdf
TOTAL PAGES       : 13
WORD COUNT        : 489
CHARACTER COUNT   : 2210
DATE EXTRACTED    : 2026-11-04 14:04:28
================================================================================

--- [Page 1 of 13] ---
& Achiever

--- [Page 2 of 13] ---
(o 
JugsSon 
— 
8¢ =5 E‘“fik R@i i}:}\%%\ 
m\m 
3&\@ 
(ati’ Llodks - %Efi%w\@ @“*&& 
(fik@fl\ AS 
(. 
| )x,u,a = e Gledya (e -T\law) 
‘l@fi\:‘:fi 
G‘N%wm ,C,;\@ ‘, C{’ 
b= 90X 
&\@3\%@‘"& L300} 
150 
\M% %&%fl% R\\m\@ 
3‘21(7(\ \a\m \& w> o 
| % fiv% Q\Qfi:z “‘irifi;l‘;af;\)

--- [Page 3 of 13] ---
AT 
\W%{ T\ NM 
— 
Q&fimw 
mmw,.\«w« B 
@\Me% ( 3 
MW\Q 
‘lfi’@t m&\ 
G-% \m\x\\r gfiw M&m, % \‘flfg 
S (MG RN G - 
&Q%“Q §<\5\5\\&\:\\;\ : TEWX o m\fk 
f?m ) ; 
%{;@?3 
W 
%@% }V‘"XWQ*\)‘ £ 09 
\%Z\QWW 
\-\= C?\\c{, 
L= O 
OB ® G, 
] -\ 
f\:%,, 
%Wm%@ 
CmW» X %i‘\%}\é Gflkm\ o > 
7 
W&%flg@x 
A4 
- 
W‘“fl “flxfi\%\ o 
-~ %W&W W%/ M 
(w»sm%w o T 
P 
W 
WNW@?&Mfi$

--- [Page 4 of 13] ---
e 
RO 
e Y 
s 
e ... 
¥ 
M 
AN B AN 
| 
& B Ro 
bk

--- [Page 5 of 13] ---
WL oyl 
%m% W 9 %g e MR 
Q) Cs\f%\;\\n%z 
TN e 
%‘Q\@ 
\%@}x@ W‘m@%& 
R 
DM 
® 
Q 
\ 
B 
o 9 
Q0 
MY 
D 
ok Wged. 
ka\m% 
R-% 
\ 
0 
\%i\f‘?m 
I\ 
\ 
”%"‘ff\fim 
“7/@{@ @*{5&&@ o 
e@m& 
- 
K\@é*"&!\‘?}\f\ % 
\\\\fx‘f\% 
@{(@&w SN

--- [Page 6 of 13] ---
it 
LSRN 
R S 
.a&i’%% o2 B8 AW 
89 &%‘% 
B=E 
o 
<\\(m j\%\Q 
\Q\%\‘XV‘D\ %\W‘i\@\& &\:\CB\ ((}\f? MT 
Tong = L\ A 
N 
(R 4w 
JM\(\ 
D AOGCL SHIFTE 
i 
s 
<<\ 
3% D8N (el 
= 
00100 
> 
SO 
A 
N 
U 
o T A 
P M 
i, 
L\W& \%fii

--- [Page 7 of 13] ---
&%\g AN 
éfififi%«\% ) aed 
S 
_0.0%, ‘i\& \Yfif j 
?;W*m Kifj‘"% — \ 
e 
e 
Lok on Sale d % 
W\%fi% \m%\ oo & RN 
Ao NI gflf\ W{\ &@f@, ANk 
WVW}&M\‘Q %’ S 
Sone_ox \tAqcal 
\T\:W AN o\ 
Q\\\"’fiw 
B . 
S

--- [Page 8 of 13] ---
Y @“fi 
- 
| 
\ 
\ 
| 
i 
: 
RIS 
, 
~ 
R 
- 
IS 
T 
pe

--- [Page 9 of 13] ---
- . 
" 
- 
; 
ey 
. 
Iy 
; 
’ 
T 
\‘ o 
RS- 
s 
G 
e e 
A 
fifi% 
%@?yf 
i 
%M“VMMWM %J;WMN “\w~_ 
: 
ey

--- [Page 10 of 13] ---


--- [Page 11 of 13] ---
Ofl\@f - Q@W&@mw\%@ 
(\ \ \__fi \ 
R 
\'”'Q Q \'@\ 
05 &W\M@% > A \ m~\ &\ 
\ 
eI 
= 
5L\ Q- 00 
N 
ho 
| 
O 
T\8T7 
k»&e“% %\ «=2 0 QW \qoo 
L 
S 
W 
[0 WO BT MooT o - - 
- 
2 
> 
A\ 
—IOMENES 000y 
\@ ‘\ XQQQQ\\Q\ 115 000 T W xm%g 
09 s> |90 + 100V 
T Wicdesnads © \a B (A QER0 
g

--- [Page 12 of 13] ---
e - ?fi%;iL§§\< 
N 
0 
B35 = WAL 
0L 
- AAONOD 
A 
ol Tk 
R \S%i“ "&; 
A G GV 
Qg et 05 %fii@@\ ot 
Wl 
= 
SR 
“ 
% | g 
Rfi& VIAS=(22)e= 1 000 O \oq 
ifi@fiw\ 
A0\ 00\ 0000 0000 
\fi% 
Oano O00o 
0F (3 630000 
%%%fii,,\&%X»fifi@iép 
0000 
0 
Sy 
4 
N 
| 
~ 
) 
i 
a5ty 
1L V00 o 
R ek Ooan. OO0 
®3M§>®§,§,&k€x% 
Qfififiwgfi%m 00 Q&@u‘;§§mfi 
LML AN 
~ 
Sl 
S0 Lewk Y=o 
T2 T 00 
@Ws \')

--- [Page 13 of 13] ---
BN 2 = (P 
=4 000 001\

```

---

<a id="doc-10"></a>
## Document 10: Lab Week 8: Prefix Adder and 4-bit Comparator Submission (6 Pages)
**Source Document**: `lab/week8/PES2UG25CS615_Yashwanth K_DLCDLab8.docx`
**OCR Extraction File**: `Lab_PES2UG25CS615_Yashwanth K_DLCDLab8.txt`

```
================================================================================
ORIGINAL DOCUMENT : PES2UG25CS615_Yashwanth K_DLCDLab8.docx
OCR PDF FILE      : Lab_PES2UG25CS615_Yashwanth K_DLCDLab8_ocr.pdf
TOTAL PAGES       : 6
WORD COUNT        : 387
CHARACTER COUNT   : 2369
DATE EXTRACTED    : 2026-11-04 14:04:02
================================================================================

--- [Page 1 of 6] ---
Digital Logic and Computer Design Laboratory
3rd Semester, Academic Year 2026
                                                                   Date:28-09-2026
Week#8                                                            Program 
Number:8
WRITE A VERILOG PROGRAM TO CONSTRUCT COMPARTOR AND 
PREFIX ADDER. GENERATE THE VVP OUTPUT AND SIMULATION 
WAVEFORM USING GTKWAVE. VERIFY THE OUTPUT AND WAVEFORM 
WITH THE TRUTH TABLE 
I.
Verilog Code Screenshot
II.
Verilog VVP Output Screen Shot 
III.
GTKWAVE Screenshot
IV.
Output Table (Truth Table) to be completed and 
included
Name: Yatin R
SRN:PES2UG25CS617
Section: J

--- [Page 2 of 6] ---
comparator.vvp 
prefix_adder.vvp 
nodule comparator 
1nput 
a, 
b 
utput greater, 
equal, 
less 
assign greater 
assign equal 
assign less 
endmodule

--- [Page 3 of 6] ---
hodule comparator_tb 
J:B188; 
10 
greater, 
equal, 
less 
comparator vutl(a, 
b, 
greater, 
equal, 
less 
initial begin 
"comparator.vcd" 
O, 
comparator_tb 
" a=%b b=%b 
| 
greater=%b equal=%b less=%b", 
a, 
b, 
greater, 
equal, 
less 
4'b0000O; 
b 
4'b0000 
a 
4'b0101 
4'b0011 
a 
4'b0010 
4'b0110 
a 
4'b1000 
4'b1000 
a 
4'b1111 
4'b0001 
a 
4'b0100 
4'b1100 
a 
4'b1010 
4'b1010 
end 
endmodule 
inodule prefix_adder 
3:0] 
a, 
b 
cin 
3:0] 
sum 
cout 
3 
assign 
assign 
assign 
assign 
assign 
assign 
assign 
assign 
endmodule

--- [Page 4 of 6] ---
jnodule prefix_adder_tb 
reg 
a, 
b 
reg cin 
e 
cout 
prefix_adder vut(a, 
b, 
cin, 
sum, 
cout 
initial begin 
$dumpfile 
prefix_adder_tb 
end 
endmodule 
Signals 
WEVEE 
equal 
greater 
let 
a 
b 
cin 
sum 
cout

--- [Page 5 of 6] ---
Table 1: 4-Bit Magnitude Comparator Verification Table
Test Case
A [3:0] 
(Binary)
A 
(Decimal)
B [3:0] 
(Binary)
B 
(Decimal)
Greater (A 
> B)
Equal (A 
= B)
Less (A < 
B)
1
0000
0
0000
0
0
1
0
2
0101
5
0011
3
1
0
0
3
0010
2
0110
6
0
0
1
4
1000
8
1000
8
0
1
0
5
1111
15
0001
1
1
0
0
6
0100
4
1100
12
0
0
1
7
1010
10
1010
10
0
1
0
Table 2: 4-Bit Prefix / Carry-Lookahead Adder Verification Table
Test 
Case
A [3:0] 
(Binary)
A (Dec)
B [3:0] 
(Binary)
B (Dec)
Cin
Sum [3:0] 
(Binary)
Sum 
(Dec)
Cout
1
0000
0
0000
0
0
0000
0
0
2
0101
5
0011
3
0
1000
8
0
3
1111
15
0001
1
0
0000
0
1
4
1010
10
0101
5
1
0000
0
1
5
1111
15
1111
15
0
1110
14
1
6
1111
15
1111
15
1
1111
15
1

--- [Page 6 of 6] ---
If found plagiarized, I will abide with the disciplinary action of 
the University.
Signature: Yashwanth Karthik
Name: Yashwanth Karthik
SRN: PES2UG25CS615
Section: J
Date: 01/10/2026

```

---

# PART 2: DLCD SYNTHESIZED STUDY PACKAGE

<a id="res-1"></a>
## Synthesized Resource 1: DLCD_Unit_2_Clean_Slides.md
**Source File**: `resources/DLCD_Unit_2_Clean_Slides.md`

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


---

<a id="res-2"></a>
## Synthesized Resource 2: DLCD_Unit_2_Question_Bank.md
**Source File**: `resources/DLCD_Unit_2_Question_Bank.md`

# Unit 2: Question Bank (Comprehensive & Deduplicated)

## Section A: Conceptual & Theory Questions with Detailed Solutions

### Q1. What is meant by a divide-by-3 circuit?

**Solution / Explanation:**
Model Answer / Explanation: A divide-by-3 circuit produces an output signal whose frequency is one-third of the input clock frequency. Therefore, f_out = f_in / 3.

### Q2. How many states are required in a basic divide-by-3 FSM?

**Solution / Explanation:**
Model Answer / Explanation: Three states are required: S0, S1, and S2. The FSM repeatedly follows S0 → S1 → S2 → S0.

### Q3. What is the next state after S2 in a divide-by-3 FSM?

**Solution / Explanation:**
Model Answer / Explanation: The next state is S0. Returning to S0 completes one cycle of the three-state sequence and starts the next cycle.

### Q4. What is the purpose of a reset signal in the divide-by-3 FSM?

**Solution / Explanation:**
Model Answer / Explanation: Reset initializes the FSM to a known state, usually S0. This ensures predictable operation when the circuit starts.

### Q5. What is the output frequency when a 30 MHz clock is divided by 3?

**Solution / Explanation:**
Model Answer / Explanation: The output frequency is 10 MHz because f_out = 30 MHz / 3 = 10 MHz.

### Q6. Draw or describe the state sequence for a Moore FSM that detects 1011.

**Solution / Explanation:**
Model Answer / Explanation: Use five states: S0: no bits matched; S1: matched 1; S2: matched 10; S3: matched 101; S4: matched 1011. The main path is S0 --1--> S1 --0--> S2 --1--> S3 --1--> S4. In S4, output = 1. For overlap, S4 transitions to S1 on input 1 and to S2 on input 0.

### Q7. Explain the difference between Moore and Mealy pattern recognizers.

**Solution / Explanation:**
Model Answer / Explanation: In a Moore FSM, output depends only on the present state, so a separate detection state is usually required. In a Mealy FSM, output depends on both present state and input, so detection can occur on a transition. A Moore design is often easier to interpret and has more stable state-based outputs, while a Mealy design may use fewer states and respond one transition earlier.

### Q8. Write the state encoding for a Moore recognizer of 1011 and explain it.

**Solution / Explanation:**
Model Answer / Explanation: One possible encoding is S0=3'b000, S1=3'b001, S2=3'b010, S3=3'b011, and S4=3'b100. Three bits are required because five states must be represented, and 2^2=4 is insufficient while 2^3=8 is sufficient.

### Q9. Explain the role of the state register and next-state logic in Verilog.

**Solution / Explanation:**
Model Answer / Explanation: The state register stores the present state and is updated on the active clock edge. The next-state combinational block examines the present state and input, then calculates the state to be loaded on the next clock edge. This separation makes the FSM easier to design and verify.

### Q10. Explain why a default case is included in the Verilog state-transition block.

**Solution / Explanation:**
Model Answer / Explanation: A default case handles invalid or unused state encodings. Assigning next_state = S0 provides a safe recovery path and helps the FSM return to a known operating state if an unexpected state occurs.

### Q11. Design a Moore FSM to detect the pattern 1011 with overlapping detection. Explain the states and transitions.

**Solution / Explanation:**
Model Answer / Explanation: States: S0=no match, S1=matched 1, S2=matched 10, S3=matched 101, S4=matched 1011. Transitions: S0: 0→S0, 1→S1. S1: 0→S2, 1→S1. S2: 0→S0, 1→S3. S3: 0→S2, 1→S4. S4: 0→S2, 1→S1. Output is 1 only in S4; otherwise it is 0. The transitions from S4 preserve overlap because the suffixes of 1011 may be prefixes of a new pattern.

### Q12. Write Verilog code for a Moore FSM that recognizes 1011 with overlapping detection. Explain the major blocks.

**Solution / Explanation:**
Model Answer / Explanation: module moore_1011(    input wire clk, reset, x,    output reg detect);localparam S0=3'b000, S1=3'b001,           S2=3'b010, S3=3'b011,           S4=3'b100;reg [2:0] state, next_state;always @(posedge clk or posedge reset)    if (reset) state <= S0;    else       state <= next_state;always @(*) begin    case (state)      S0: if (x) next_state=S1; else next_state=S0;      S1: if (x) next_state=S1; else next_state=S2;      S2: if (x) next_state=S3; else next_state=S0;      S3: if (x) next_state=S4; else next_state=S2;      S4: if (x) next_state=S1; else next_state=S2;      default: next_state=S0;    endcaseendalways @(*)    if (state==S4) detect=1'b1;    else           detect=1'b0;endmoduleExplanation: The first block stores the present state. The second block implements the transition table. The third block is Moore output logic, so detect depends only on state and is high only in S4.

### Q13. Develop the state table for a Moore 1011 pattern recognizer and explain the output.

**Solution / Explanation:**
Model Answer / Explanation: State table: S0: x=0→S0, x=1→S1, output=0. S1: x=0→S2, x=1→S1, output=0. S2: x=0→S0, x=1→S3, output=0. S3: x=0→S2, x=1→S4, output=0. S4: x=0→S2, x=1→S1, output=1. Since this is a Moore machine, the output is associated with the present state rather than directly with the input.

### Q14. Explain how overlapping detection is implemented in a Moore FSM for 1011.

**Solution / Explanation:**
Model Answer / Explanation: After reaching S4, the FSM does not always return to S0. If the next input is 1, it goes to S1 because the most recent 1 can begin a new pattern. If the next input is 0, it goes to S2 because the ending sequence 10 matches the first two bits of the target pattern. These transitions retain useful partial matches and allow overlapping occurrences to be detected.

### Q15. Compare the hardware and timing characteristics of Moore and Mealy pattern recognizers.

**Solution / Explanation:**
Model Answer / Explanation: A Moore recognizer generally uses a separate output state, so it may require more states than an equivalent Mealy recognizer. Its output depends only on registered state and is therefore state-synchronous and less directly sensitive to input changes. A Mealy recognizer can assert output on the transition that receives the final pattern bit, often using fewer states and responding earlier. However, because its output depends directly on input and state, careful timing design is needed to avoid unwanted output changes.

### Q16. Differentiate Half Adder and Full Adder with truth tables.

**Solution / Explanation:**
Detailed Answer:Half Adder:A Half Adder adds two 1-bit binary numbers. It has two inputs (A,B) and two outputs (Sum and Carry).Boolean equations:Sum = A XOR BCarry = A AND BTruth Table:A B | S C0 0 | 0 00 1 | 1 01 0 | 1 01 1 | 0 1Full Adder:A Full Adder adds three binary inputs (A,B,Cin). It has outputs Sum and Carry.Sum = A XOR B XOR CinCarry = AB + Cin(A XOR B)A Full Adder can be implemented using two Half Adders and one OR gate. Unlike a Half Adder, it can accept an input carry, making it suitable for multi-bit addition.

### Q17. Explain the working of a 4-bit Ripple Carry Adder with its advantages and disadvantages.

**Solution / Explanation:**
Detailed Answer:A 4-bit Ripple Carry Adder is constructed by connecting four Full Adders in cascade.The carry output from each Full Adder becomes the carry input to the next stage.Working:1. The least significant Full Adder receives the external carry input.2. Each Full Adder computes Sum and Carry.3. The carry propagates from LSB to MSB until the final carry is produced.Advantages:• Simple design.• Requires less hardware.Disadvantages:• Large propagation delay because every stage waits for the previous carry.• Not suitable for high-speed processors.

### Q18. Explain Carry Lookahead Adder using Generate and Propagate signals.

**Solution / Explanation:**
Detailed Answer:Carry Lookahead Adders reduce delay by computing carries in parallel.Generate (G) = A·BPropagate (P) = A XOR BCarry equations:C1 = G0 + P0C0C2 = G1 + P1G0 + P1P0C0Because carries are calculated simultaneously rather than waiting for previous stages, the CLA is much faster than the Ripple Carry Adder. The trade-off is increased hardware complexity.

### Q19. Explain binary subtraction using the Two's Complement method with an example.

**Solution / Explanation:**
Detailed Answer:To subtract B from A:1. Find the 2's complement of B.2. Add it to A.3. If a carry is generated, discard it.Example:A = 1011B = 01101's complement of B = 10012's complement = 10101011 + 1010 = 10101Discard carry = 0101Therefore, 1011 - 0110 = 0101.

### Q20. Explain the functions of an Arithmetic Logic Unit (ALU).

**Solution / Explanation:**
Detailed Answer:The ALU is the computational unit of a processor.Arithmetic operations:• Addition• Subtraction• Increment• DecrementLogic operations:• AND• OR• XOR• NOTOther operations:• Shift left/right• Compare• Set-on-less-thanThe Control Unit selects the required ALU operation using control signals.

### Q21. Explain the operation of a binary comparator.

**Solution / Explanation:**
Detailed Answer:A binary comparator compares two binary numbers.Outputs:A>BA<BA=BComparison starts from the most significant bit.If MSBs are equal, the next lower bits are compared until a difference is found.Applications:• Sorting• Address comparison• Processor decision making• Digital control systems.

### Q22. Differentiate logical shift and arithmetic shift with examples.

**Solution / Explanation:**
Detailed Answer:Logical Shift:• Vacated bits are filled with zero.• Used for unsigned numbers.Example:10110010 → Logical Right Shift01011001Arithmetic Shift:• Sign bit is preserved.• Used for signed numbers.Example:11010010 → Arithmetic Right Shift11101001Arithmetic shifts preserve the sign of signed integers.

### Q23. Explain binary multiplication using the shift-and-add method.

**Solution / Explanation:**
Detailed Answer:Binary multiplication is similar to decimal multiplication.Example:1101 × 0011Partial products:110111010Adding partial products:100111Decimal verification:13 × 3 = 3939 = 100111₂Shift-and-add multiplication is implemented in hardware multipliers.

### Q24. Explain propagation delay in adders and its effect on performance.

**Solution / Explanation:**
Detailed Answer:Propagation delay is the time required for a signal to travel from input to output.In Ripple Carry Adders, every Full Adder must wait for the previous carry.Hence,Delay = Number of Full Adders × Delay per Full Adder.Large delays reduce processor speed.Carry Lookahead Adders minimize this delay by generating carries simultaneously.

### Q25. Explain why multiplexers are used in ALUs.

**Solution / Explanation:**
Detailed Answer:An ALU performs many operations simultaneously inside separate hardware blocks.A multiplexer selects one output according to control signals.Advantages:• Reduces hardware duplication.• Enables multiple operations using one output path.• Improves processor flexibility.For example, if control signal = 00, ADD output is selected; 01 selects SUB; 10 selects AND; 11 selects OR.

### Q26. Represent the decimal number 9.25 in fixed-point binary notation using 4 integer bits and 4 fraction bits.

**Solution / Explanation:**
Solution:
Integer part: 9 = 1001₂
Fraction part: 0.25 = 2⁻² → bit pattern 0100
Combine: 1001.0100
Final Answer: 1001.0100

### Q27. Convert the fixed-point binary number 0011.1010 (4 integer bits, 4 fraction bits) to its decimal value.

**Solution / Explanation:**
Solution:
Integer part: 0011 = 3
Fraction part: 1010 → 2⁻¹ + 2⁻³ = 0.5 + 0.125 = 0.625
Total = 3 + 0.625 = 3.625
Final Answer: 3.625

### Q28. Encode the decimal number 350 as a 32-bit IEEE 754 single-precision floating-point number.

**Solution / Explanation:**
Solution:
Convert 350 to binary: 350 = 101011110₂
Normalize: 101011110 = 1.01011110 × 2⁸
Sign bit = 0 (positive)
Biased exponent = 8 + 127 = 135 = 10000111
Fraction (23 bits, drop implicit leading 1, pad with zeros): 01011110000000000000000
Final Answer: 0 10000111 01011110000000000000000

### Q29. Encode the decimal number −0.15625 as a 32-bit IEEE 754 single-precision floating-point number.

**Solution / Explanation:**
Solution:
Convert 0.15625 to binary: 0.15625 = 2⁻³ + 2⁻⁵ = 0.00101₂
Normalize: 0.00101 = 1.01 × 2⁻³
Sign bit = 1 (negative)
Biased exponent = −3 + 127 = 124 = 01111100
Fraction (23 bits): 01000000000000000000000
Final Answer: 1 01111100 01000000000000000000000

### Q30. Using the 8-step floating-point addition procedure, compute 12.5 + 0.375 and give the final IEEE 754 single-precision encoding of the result.

**Solution / Explanation:**
Solution: Step 1–2 (extract fields, prepend implicit 1):
12.5 = 1100.1₂ = 1.1001 × 2³ (exponent = 3)
0.375 = 0.011₂ = 1.1 × 2⁻² (exponent = −2)
Step 3 (compare exponents):
Difference = 3 − (−2) = 5
Step 4 (shift smaller mantissa):
Express 0.375's mantissa relative to exponent 3: 1.1 × 2⁻⁵ = 0.000011 (shift right 5 bits)
Step 5 (add mantissas):
1.100100
+ 0.000011
1.100111
Step 6 (normalize):
1.100111 is already between 1 and 2 → no renormalization needed. Exponent stays 3.
Step 7 (round):
Result is exact → no rounding necessary.
Step 8 (assemble):
Sign = 0
Biased exponent = 3 + 127 = 130 = 10000010
Fraction = 100111 padded to 23 bits: 10011100000000000000000
Verification: 1.100111₂ × 2³ = 1100.111₂ = 12 + 0.5 + 0.25 + 0.125 = 12.875 = 12.5 + 0.375
Final Answer: 12.875 → 0 10000010 10011100000000000000000


---
## Section B: Core Numerical & Architectural Design Problems

1. Design and explain a three-state divide-by-3 FSM.

2. Write Verilog code for a divide-by-3 FSM and explain the major blocks.

3. Develop the state table for a divide-by-3 FSM.

4. Explain how the divide-by-3 FSM recovers from an invalid state.

5. Compare a divide-by-3 FSM with a simple modulo-3 counter and discuss duty cycle.

6. Derive the expression for outputs of the half adder and the full adder using SOP from their respective truth tables.

7. Derive the generator and propagator bits as well as the carry out bit for the 4th bit in a 4-bit, in terms of all the lower bits, Ai and Bi where “i" = 3:0 for a carry lookahead adder.

8. What is the delay for the following types of 32-bit adders? Assuming each input gate delay is 120 ps and that a full adder has 300 ps delay:
   - (a) A ripple carry adder
   - (b) A carry-lookahead adder with 4-bit blocks
   - (c) A prefix adder

9. Write the VHDL implementation for an 8-bit multiplier using the multiply(*) operation, and describe the synthesized circuit for it.

10. Design two adders: a 64-bit ripple-carry adder and a 64-bit carry lookahead adder with 4-bit blocks. Use only two-input gates (each gate 15 um², 50 ps delay, 20 pF capacitance). Compare the area, delay, and power operating at 100 MHz, and discuss the trade-offs.

11. Explain why a designer might choose to use a ripple-carry adder instead of a carry-lookahead adder.

12. Using the 8-step floating-point addition procedure, compute 6.0 + 2.5, showing the renormalization step, and give the final IEEE 754 encoding.

13. A floating-point addition produces a positive result of magnitude 4.5 × 10³⁸ before storage, exceeding the stated maximum normal magnitude of ±3.402824 × 10³⁸. Determine (a) whether overflow occurs, (b) what is stored in round-to-nearest mode, and (c) the resulting 32-bit encoding.

14. Using 4 integer bits and 4 fraction bits, compute 2.125 + (−1.8125) in two's complement fixed-point notation, showing all conversion and addition steps.

15. (a) Decode the 32-bit pattern 1 10000101 11010000000000000000000 to its decimal value, showing all steps. (b) Using IEEE 754 special-value rules, state what the patterns 0 00000000 00000000000000000000000 and 0 11111111 00000000000000000000000 each represent.

16. Using 5 integer bits and 4 fraction bits, compute −4.375 + (−2.8125) in two's complement fixed-point notation, showing all conversion and addition steps. Then express the result in sign-and-magnitude notation as well.


---

<a id="res-3"></a>
## Synthesized Resource 3: DLCD_Unit_2_MCQs.md
**Source File**: `resources/DLCD_Unit_2_MCQs.md`

# Unit 2: Multiple Choice Questions (Deduplicated with Explanations)

**Q1. What is the primary architectural difference between a Moore machine and a Mealy machine?**
- A. Moore outputs depend strictly on the current state; Mealy outputs depend on both current state and current inputs
- B. Moore machines have no clock input; Mealy machines are synchronous
- C. Moore machines require fewer states than Mealy machines to detect identical sequences
- D. Mealy machine outputs update only at active clock edges, whereas Moore machine outputs change asynchronously
**Explanation:** In a Moore machine, output logic is $Y = g(S)$ (depends solely on state). In a Mealy machine, output logic is $Y = g(S, X)$ (depends on state and immediate input), which allows faster response but can expose outputs to input glitches.

**Q2. An FSM has 8 distinct states. If One-Hot state encoding is employed, how many flip-flops are required in the state register?**
- A. 3
- B. 4
- C. 8
- D. 16
**Explanation:** In One-Hot encoding, each state is allocated a dedicated flip-flop (where exactly one flip-flop holds a '1' at any time). For 8 states, exactly 8 flip-flops are required. (Binary encoding would require $\lceil \log_2 8 \rceil = 3$ flip-flops).

**Q3. An FSM is implemented using 5 flip-flops with binary state encoding. What is the maximum number of distinct states that can be represented?**
- A. 5
- B. 10
- C. 25
- D. 32
**Explanation:** With $k$ flip-flops using binary encoding, each flip-flop represents one binary digit. Total possible combinations = $2^k = 2^5 = 32$ states.

**Q4. What is the primary operational advantage of using a Moore FSM instead of a Mealy FSM?**
- A. Fewer states are required
- B. Outputs are completely glitch-free and synchronized to the clock
- C. Outputs respond immediately without waiting for a clock edge
- D. Next-state logic requires zero combinational gates
**Explanation:** Because Moore outputs depend only on state flip-flop values (which change only at clock edges), they are isolated from input glitches and combinational race hazards occurring between clock edges.

**Q5. A Moore FSM is designed to detect the 4-bit sequence '1011' with overlapping allowed. How many states are required in its state diagram?**
- A. 3 states
- B. 4 states
- C. 5 states
- D. 8 states
**Explanation:** For an $N$-bit sequence detector implemented as a Moore machine, $N + 1$ states are required: S0 (Reset/No bits matched), S1 (got '1'), S2 (got '10'), S3 (got '101'), and S4 (got '1011', output = 1). Hence, $4 + 1 = 5$ states.

**Q6. In a basic divide-by-3 counter FSM, what is the output clock frequency when the input clock frequency is 30 MHz?**
- A. 90 MHz
- B. 30 MHz
- C. 15 MHz
- D. 10 MHz
**Explanation:** A divide-by-$N$ circuit cycles through $N$ states, completing one full cycle every $N$ clock periods. Therefore, $f_{\text{out}} = f_{\text{in}} / N = 30\text{ MHz} / 3 = 10\text{ MHz}$.

**Q7. When implementing an FSM in Verilog using standard multi-always block methodology, which block must use non-blocking assignments (<=)?**
- A. The combinational next-state logic block
- B. The clocked state-register block
- C. The combinational output logic block
- D. All blocks must strictly use blocking (=) assignments
**Explanation:** In standard Verilog design guidelines, sequential logic (the state register driven by `always @(posedge clk)`) must always use non-blocking assignments (`<=`) to prevent simulation race conditions between flip-flops.

**Q8. Why is a 'default' statement essential in the combinational next-state 'case' block of an FSM in Verilog?**
- A. To force the synthesis tool to insert additional flip-flops
- B. To prevent the synthesis tool from inferring unintended transparent latches for unhandled states
- C. To automatically increase the clock frequency
- D. Because Verilog syntax causes a compilation error without it
**Explanation:** In combinational `always @(*)` blocks, if an output variable is not assigned in every possible branch of a `case` statement, hardware synthesis tools infer memory latches to hold the previous value, which degrades timing and introduces hazards.

**Q9. In the design of complex digital controllers (e.g. traffic light with parade mode), what is the key advantage of Factored FSMs over Unfactored FSMs?**
- A. Factored FSMs always use purely asynchronous logic
- B. Factoring divides a large FSM with $N_1 \times N_2$ states into smaller interacting FSMs with $N_1 + N_2$ states, simplifying debugging and maintenance
- C. Factored FSMs eliminate all flip-flops
- D. Unfactored FSMs consume fewer total gates
**Explanation:** Factoring decomposes a large, monolithic state machine into modular, interacting sub-FSMs (e.g., Mode FSM + Lights FSM). This avoids combinatorial state explosion, significantly reducing total states from multiplicative to additive and enhancing modularity.

**Q10. What are the minimal Boolean equations for the Sum (S) and Carry-out (Cout) of a 1-bit Half Adder with inputs A and B?**
- A. $S = A \cdot B,\quad C_{\text{out}} = A + B$
- B. $S = A \oplus B,\quad C_{\text{out}} = A \cdot B$
- C. $S = A + B,\quad C_{\text{out}} = A \oplus B$
- D. $S = (A \cdot B)',\quad C_{\text{out}} = A \oplus B$
**Explanation:** A half adder adds two 1-bit inputs $A$ and $B$. $S = 1$ when exactly one input is 1 ($S = A \oplus B$). $C_{\text{out}} = 1$ only when both inputs are 1 ($C_{\text{out}} = A \cdot B$).

**Q11. How is a 1-bit Full Adder constructed from Half Adders and basic gates?**
- A. Two Half Adders and one OR gate
- B. Two Half Adders and one AND gate
- C. Three Half Adders in parallel
- D. One Half Adder and two XOR gates
**Explanation:** The first Half Adder adds $A$ and $B$, generating partial sum $S_1 = A \oplus B$ and carry $C_1 = A B$. The second Half Adder adds $S_1$ and $C_{\text{in}}$, producing total sum $S = S_1 \oplus C_{\text{in}}$ and carry $C_2 = S_1 C_{\text{in}}$. The carries are ORed together: $C_{\text{out}} = C_1 + C_2$.

**Q12. In an N-bit Ripple Carry Adder (RCA), what determines the critical path propagation delay?**
- A. The delay of the first Half Adder stage only
- B. The carry propagation chain rippling through all N Full Adders ($t_{\text{ripple}} = N \times t_{\text{FA}}$)
- C. The logarithmic depth of XOR gates ($\log_2 N$)
- D. A constant delay independent of N
**Explanation:** In an RCA, stage $i$ cannot compute its carry-out until carry-in arrives from stage $i-1$. Thus, carry bits ripple sequentially from LSB to MSB, resulting in a worst-case delay that scales linearly: $O(N)$.

**Q13. In a Carry Lookahead Adder (CLA), under what condition is the Generate signal Gi asserted for bit stage i?**
- A. When $A_i + B_i = 1$
- B. When $A_i = 1$ and $B_i = 1$ ($G_i = A_i \cdot B_i$)
- C. When $A_i \oplus B_i = 1$
- D. When $C_{\text{in}} = 1$
**Explanation:** A stage generates a carry independently of incoming carry if both input bits are 1 ($A_i = 1, B_i = 1$). Hence, $G_i = A_i \cdot B_i$. Propagate occurs when at least one input is 1 ($P_i = A_i \oplus B_i$ or $A_i + B_i$).

**Q14. In a 4-bit Carry Lookahead block (bits 3:0), what is the Boolean expression for the block propagate signal P3:0?**
- A. $P_{3:0} = P_3 + P_2 + P_1 + P_0$
- B. $P_{3:0} = P_3 \cdot P_2 \cdot P_1 \cdot P_0$
- C. $P_{3:0} = G_3 + P_3 G_2$
- D. $P_{3:0} = P_3 \oplus P_2 \oplus P_1 \oplus P_0$
**Explanation:** A 4-bit block propagates a carry across all 4 stages if and only if every stage in the block propagates the carry: $P_{3:0} = P_3 \cdot P_2 \cdot P_1 \cdot P_0$.

**Q15. For an N-bit word, how does the critical path propagation delay of a Prefix Adder scale with N?**
- A. Linearly with $N$ ($O(N)$)
- B. Logarithmically with $N$ ($O(\log_2 N)$)
- C. Quadratically with $N$ ($O(N^2)$)
- D. Exponentially with $N$ ($O(2^N)$)
**Explanation:** Prefix adders use tree structures of associative prefix operators (black and gray cells) to compute all carries in parallel across $\log_2 N$ logic stages, giving $O(\log_2 N)$ delay.

**Q16. How is binary subtraction A - B implemented using an N-bit binary adder and 2's complement arithmetic?**
- A. Inverting all bits of A and setting $C_{\text{in}} = 0$
- B. Inverting all bits of B (using XOR gates) and setting initial carry-in $C_{\text{in}} = 1$
- C. Passing A and B directly with $C_{\text{in}} = 1$
- D. Using two cascaded decoders
**Explanation:** By definition of 2's complement, $-B = B' + 1$. Therefore, $A - B = A + B' + 1$. By placing 2-input XOR gates on each bit of $B$ with control signal $Sub$, when $Sub = 1$, $B$ is bitwise complemented and $C_{\text{in}} = 1$.

**Q17. In an N-bit signed 2's complement adder/subtractor, which logic condition flags an arithmetic overflow?**
- A. $V = C_{\text{out}}$ of the most significant bit
- B. $V = C_{N-1} \oplus C_N$ (carry into MSB XOR carry out of MSB)
- C. $V = A_{\text{MSB}} \cdot B_{\text{MSB}}$
- D. $V = S_{\text{MSB}}$
**Explanation:** In 2's complement addition, overflow occurs if and only if the carry into the most significant (sign) bit differs from the carry out of the most significant bit: $V = C_{\text{in,msb}} \oplus C_{\text{out,msb}}$.

**Q18. Which combination of logic gates is used to construct an N-bit binary equality comparator (A == B)?**
- A. $N$ XOR gates followed by an OR gate
- B. $N$ XNOR gates followed by an $N$-input AND gate
- C. $N$ AND gates followed by an inverter
- D. $N$ NAND gates in series
**Explanation:** An XNOR gate outputs 1 when both inputs are equal ($A_i \odot B_i = 1$). To verify that all $N$ bit pairs match simultaneously, the $N$ XNOR outputs are fed into an $N$-input AND gate: $Eq = \prod_{i=0}^{N-1} (A_i \odot B_i)$.

**Q19. What is the key difference between a logical right shift (>>) and an arithmetic right shift (>>>)?**
- A. Logical right shift fills vacant MSB positions with 0; Arithmetic right shift replicates the sign bit (old MSB)
- B. Arithmetic shift rotates bits circularly; Logical shift does not
- C. Logical shift can only shift by 1 bit; Arithmetic shift can shift by any number of bits
- D. Logical shift operates only on negative numbers
**Explanation:** Logical right shift (`>>`) unconditionally fills empty MSB positions with 0s. Arithmetic right shift (`>>>`) replicates the old sign bit (MSB) into vacant positions, preserving the sign for signed 2's complement division by $2^k$.

**Q20. If an 8-bit signed binary number 11110000 (-16 in decimal) is arithmetically right-shifted by 2 positions (>>> 2), what is the resulting 8-bit binary value?**
- A. 00111100 (+60)
- B. 11111100 (-4)
- C. 11000011 (-61)
- D. 00001111 (+15)
**Explanation:** Starting with `11110000`, the MSB is 1. Shifting right arithmetically by 2 replicates the MSB: `11` + `111100` = `11111100`. In 2's complement, `11111100` represents $-4_{10}$, exactly $(-16) / 2^2 = -4$.

**Q21. A barrel shifter capable of shifting a 16-bit word by 0 to 15 positions is designed using 2:1 multiplexers. How many multiplexer stages are required in series?**
- A. 2 stages
- B. 4 stages
- C. 8 stages
- D. 16 stages
**Explanation:** A shift amount from 0 to 15 is specified by a 4-bit control signal ($k = 4$, since $2^4 = 16$). A logarithmic barrel shifter uses $\log_2 N = \log_2 16 = 4$ stages of multiplexers (shifting by 1, 2, 4, and 8 bits).

**Q22. When multiplying an N-bit unsigned integer by an M-bit unsigned integer, how many bits must be allocated for the product to prevent overflow?**
- A. $\max(N, M)$ bits
- B. $N \times M$ bits
- C. $N + M$ bits
- D. $N + M - 1$ bits
**Explanation:** The maximum product of an $N$-bit and $M$-bit unsigned integer is $(2^N - 1)(2^M - 1) = 2^{N+M} - 2^N - 2^M + 1 < 2^{N+M}$. Hence, exactly $N + M$ bits are required to store the full product.

**Q23. In a 32-bit ALU, how is the 'Set Less Than' (SLT) operation (A < B) implemented in hardware?**
- A. By using a separate 32-bit hardware divider
- B. By configuring the adder as a subtractor (A - B) and extracting the sign bit S31 (zero-extended) as the result
- C. By counting the number of 1s in A and B
- D. By performing bitwise AND and checking if all bits are 0
**Explanation:** To check if $A < B$, the ALU computes $A - B$. If $A < B$, the result is negative, making the sign bit $S_{31} = 1$. The ALU multiplexer routes $S_{31}$ to the LSB of output $Y$ (with upper 31 bits zero-extended to give $0x00000001$).

**Q24. What is the numerical range of representable signed integers using N-bit 2's complement notation?**
- A. $-(2^{N-1} - 1)$ to $+(2^{N-1} - 1)$
- B. $-2^{N-1}$ to $+(2^{N-1} - 1)$
- C. $-2^N$ to $+2^N$
- D. $0$ to $2^N - 1$
**Explanation:** Because 2's complement has a unique representation for zero, it can represent one additional negative number. The range is $[-2^{N-1}, 2^{N-1} - 1]$. For $N = 8$, the range is $-128$ to $+127$.

**Q25. Why is 2's complement almost universally preferred over sign-magnitude and 1's complement in modern computer hardware?**
- A. It has two distinct bit patterns for zero (+0 and -0)
- B. Addition and subtraction can use the exact same adder hardware without sign-checking logic, and zero has a unique representation
- C. It requires fewer total bits to represent floating point numbers
- D. It eliminates the need for logic gates
**Explanation:** In 2's complement, addition and subtraction work uniformly on the bit patterns regardless of sign, eliminating special end-around carry and separate sign-handling circuits, and avoiding ambiguous dual zeros (+0 and -0).

**Q26. Convert the fixed-point binary number 0011.1010 (4 integer bits, 4 fraction bits) to decimal.**
- A. 3.5
- B. 3.625
- C. 3.75
- D. 3.125
**Explanation:** Integer part: $0011_2 = 2 + 1 = 3$. Fraction part: $1010_2 = 1 \times 2^{-1} + 0 \times 2^{-2} + 1 \times 2^{-3} + 0 \times 2^{-4} = 0.5 + 0.125 = 0.625$. Total decimal value = $3.625$.

**Q27. Represent the decimal value -7.5 in 8-bit signed fixed-point format (4 integer bits, 4 fraction bits) using 2's complement.**
- A. 1111.1000
- B. 1000.1000
- C. 1000.0111
- D. 0111.1000
**Explanation:** 1. $+7.5_{10} = 0111.1000_2$. 2. Invert bits (1's complement): $1000.0111_2$. 3. Add 1 to LSB ($2^{-4}$): $1000.0111 + 0000.0001 = 1000.1000_2$. Verification: $-8 + 0.5 = -7.5$.

**Q28. In the IEEE 754 single-precision (32-bit) standard, how are the 32 bits partitioned?**
- A. 1 sign bit, 7 exponent bits, 24 fraction bits
- B. 1 sign bit, 8 exponent bits, 23 fraction bits
- C. 2 sign bits, 8 exponent bits, 22 fraction bits
- D. 1 sign bit, 11 exponent bits, 20 fraction bits
**Explanation:** IEEE 754 single precision allocates: Bit 31 = Sign ($S$, 1 bit), Bits 30-23 = Biased Exponent ($E$, 8 bits), Bits 22-0 = Fraction / Mantissa ($F$, 23 bits).

**Q29. What is the exponent bias used in the IEEE 754 32-bit single-precision floating-point standard?**
- A. 63
- B. 127
- C. 128
- D. 1023
**Explanation:** Single-precision floating-point uses a bias of $2^{8-1} - 1 = 127$. Stored exponent $E = \text{actual exponent } e + 127$. (Double precision uses bias 1023).

**Q30. In normalized IEEE 754 floating-point numbers, what is the value of the implicit (hidden) leading bit of the significand?**
- A. Always 0
- B. Always 1
- C. Determined by the sign bit
- D. Determined by the least significant bit of the exponent
**Explanation:** In normalized numbers, the binary point floats such that the significand is in the range $[1.0, 2.0)$, meaning the leading bit before the binary point is always 1. To save memory, this 1 is not explicitly stored.

**Q31. In IEEE 754 single-precision format, what bit combination represents +Infinity (+inf)?**
- A. Sign = 0, Exponent = 11111111, Fraction = 000...0
- B. Sign = 1, Exponent = 11111111, Fraction = 000...0
- C. Sign = 0, Exponent = 11111111, Fraction != 0
- D. Sign = 0, Exponent = 00000000, Fraction = 000...0
**Explanation:** $+\infty$ is represented by Sign $= 0$, all-ones exponent ($E = 255 = 11111111_2$), and an all-zeros fraction field ($F = 0$).

**Q32. Which field combination defines NaN (Not a Number) in IEEE 754 single-precision format?**
- A. Exponent = 00000000, Fraction = 000...0
- B. Exponent = 11111111, Fraction = 000...0
- C. Exponent = 11111111, Fraction ≠ 0
- D. Exponent = 00000000, Fraction ≠ 0
**Explanation:** NaN (Not a Number, e.g. $0/0$ or $\sqrt{-1}$) is designated by an all-ones exponent field ($E = 255 = 11111111_2$) combined with a non-zero fraction field ($F \ne 0$).

**Q33. What category of numbers is represented when the exponent field is all zeros (E = 00000000) and the fraction is non-zero (F ≠ 0)?**
- A. Normalized numbers
- B. Denormalized (Subnormal) numbers
- C. Infinity
- D. Quiet NaNs
**Explanation:** When $E = 0$ and $F \ne 0$, the implicit leading bit becomes 0 instead of 1 ($0.F$). These are subnormal (denormalized) numbers, enabling gradual underflow near zero with value $(-1)^S \times (0.F) \times 2^{-126}$.

**Q34. What is the 32-bit IEEE 754 single-precision floating-point representation of the decimal integer 228 in hexadecimal?**
- A. 0x43640000
- B. 0xC3640000
- C. 0x42E40000
- D. 0x43E40000
**Explanation:** 1. $228_{10} = 11100100_2 = 1.11001_2 \times 2^7$. 2. Sign $S = 0$. 3. Exponent $E = 7 + 127 = 134 = 10000110_2$. 4. Fraction $F = 1100100...$ (23 bits). Binary: `0 10000110 11001000000000000000000` = `0100 0011 0110 0100 ...` = `0x43640000`.

**Q35. Encode the decimal number -58.25 into IEEE 754 single-precision 32-bit hexadecimal format.**
- A. 0x42690000
- B. 0xC2690000
- C. 0xC1690000
- D. 0x41690000
**Explanation:** 1. Sign is negative $\implies S = 1$. 2. $58.25_{10} = 111010.01_2 = 1.1101001_2 \times 2^5$. 3. Exponent $E = 5 + 127 = 132 = 10000100_2$. 4. Fraction $F = 11010010...$ Bits: `1 10000100 11010010000000000000000` = `1100 0010 0110 1001 ...` = `0xC2690000`.

**Q36. During the standard 8-step floating-point addition procedure, what step immediately follows extracting the exponent and fraction bits?**
- A. Compare the exponents
- B. Prepend the implicit leading 1 to form the complete significand/mantissa
- C. Normalize the sum
- D. Round the result
**Explanation:** Step 1 extracts sign, exponent, and fraction bits. Step 2 restores the hidden/implicit leading 1 before the binary point to reconstruct the true significand ($1.F$) prior to exponent comparison and shifting.

**Q37. When adding two floating-point numbers with different exponents, why must the significand of the number with the smaller exponent be shifted right?**
- A. To prevent arithmetic underflow
- B. To align their binary points so that bit weights correspond during significand addition
- C. To convert the number to 2's complement
- D. To eliminate the sign bit
**Explanation:** Addition of binary numbers requires matching place values (exponents). Shifting the smaller number's significand right by $|E_1 - E_2|$ positions increases its effective exponent to match the larger number without altering its numerical value.

**Q38. Which of the following is NOT a recognized representation for signed fixed-point binary numbers?**
- A. Two's Complement
- B. Sign/Magnitude
- C. Excess-127
- D. One's Complement
**Explanation:** Excess-127 (biased exponent) is used in floating-point exponent encoding (IEEE 754). Signed fixed-point numbers are represented using Two's Complement, Sign/Magnitude, or One's Complement.

**Q39. What is the main function of a divide-by-3 FSM?**
- A. To multiply the clock frequency by 3
- B. To generate an output frequency equal to one-third of the input clock frequency
- C. To divide the input voltage by 3
- D. To generate three independent clock signals
**Answer:** B
**Explanation:** A divide-by-3 circuit produces an output frequency f_out = f_in / 3. For example, a 30 MHz input produces a 10 MHz output.

**Q40. How many states are required for a basic divide-by-3 FSM?**
- A. 1
- B. 2
- C. 3
- D. 4
**Answer:** C
**Explanation:** The FSM cycles through three states: S0 → S1 → S2 → S0. Therefore, three states are required.

**Q41. What is the next state after S2 in a divide-by-3 FSM?**
- A. S0
- B. S1
- C. S2
- D. S3
**Answer:** A
**Explanation:** The state sequence is cyclic: S0 → S1 → S2 → S0. After S2, the FSM returns to S0.

**Q42. What is the minimum number of bits required to encode three FSM states?**
- A. 1 bit
- B. 2 bits
- C. 3 bits
- D. 4 bits
**Answer:** B
**Explanation:** One bit represents only two states, while two bits represent four states. Thus, two bits are sufficient for three states.

**Q43. Which Verilog statement is commonly used to update the state at the rising edge of the clock?**
- A. always @(*)
- B. always @(posedge clk)
- C. always @(clk)
- D. always @(negedge reset)
**Answer:** B
**Explanation:** always @(posedge clk) executes when the clock changes from 0 to 1. FSM state registers are commonly updated at this edge.

**Q44. What is the purpose of the reset signal in a divide-by-3 FSM?**
- A. To increase the clock frequency
- B. To initialize the FSM to a known state
- C. To generate an output pulse
- D. To add a new state
**Answer:** B
**Explanation:** Reset initializes the FSM to a known starting state, usually S0, preventing an unknown starting condition.

**Q45. Which Verilog code correctly describes the state transitions?**
- A. S0→S1, S1→S2, S2→S0
- B. S0→S0, S1→S1, S2→S2
- C. S0→S2, S1→S0, S2→S1
- D. S0→S3, S1→S4, S2→S5
**Answer:** A
**Explanation:** The correct divide-by-3 sequence is S0 → S1 → S2 → S0, repeating every three clock cycles.

**Q46. What is the purpose of next_state in a two-process FSM?**
- A. It stores the previous state
- B. It represents the state to be loaded at the next clock edge
- C. It stores the output frequency
- D. It acts as the reset signal
**Answer:** B
**Explanation:** next_state is calculated by combinational logic. At the next active clock edge, it is copied into the state register.

**Q47. Why is a default case included in FSM transition logic?**
- A. To increase the number of states
- B. To handle invalid or undefined states safely
- C. To increase the output frequency
- D. To remove the need for reset
**Answer:** B
**Explanation:** A default case provides a recovery path. For example, default: next_state = S0; returns the FSM to a known state.

**Q48. If the present state is S1 in the following sequence S0→S1→S2→S0, what is the next state?**
- A. S0
- B. S1
- C. S2
- D. Unknown
**Answer:** C
**Explanation:** According to the transition sequence, S1 is followed by S2. The FSM enters S2 at the next active clock edge. Sample Verilog Code: Divide-by-3 FSM module divide_by_3_fsm (    input  wire clk,    input  wire reset,    output reg  div_out);    localparam S0 = 2'b00,               S1 = 2'b01,               S2 = 2'b10;    reg [1:0] state, next_state;    // State register    always @(posedge clk or posedge reset) begin        if (reset)            state <= S0;        else            state <= next_state;    end    // Next-state logic    always @(*) begin        case (state)            S0: next_state = S1;            S1: next_state = S2;            S2: next_state = S0;            default: next_state = S0;        endcase    end    // Output logic    always @(*) begin        if (state == S0)            div_out = 1'b1;        else            div_out = 1'b0;    endendmodule Note: This simple FSM repeats every three clock cycles. A true 50% duty-cycle divide-by-3 clock generally requires additional logic using both clock edges. MCQs on Moore Pattern Recognizer FSM and Verilog Code Pattern used: 1011 (overlapping pattern detection). In a Moore FSM, the output depends only on the present state.

**Q49. What is the main purpose of a pattern recognizer FSM?**
- A. To increase clock frequency
- B. To detect a specified sequence of input bits
- C. To divide the input voltage
- D. To store unlimited data
**Answer:** B
**Explanation:** A pattern recognizer FSM monitors a serial input stream and asserts an output when the required bit pattern is detected.

**Q50. In a Moore FSM, the output depends on:**
- A. Only the present state
- B. Only the current input
- C. Both present state and current input
- D. The clock frequency only
**Answer:** A
**Explanation:** In a Moore machine, outputs are determined solely by the current state. The input affects the next state, not the output directly.

**Q51. For recognizing the pattern 1011, which state usually produces output 1?**
- A. Initial state
- B. State representing that no bits are matched
- C. Final detection state
- D. Any state when input is 1
**Answer:** C
**Explanation:** A dedicated final state represents successful recognition of 1011. The Moore output is asserted in this detection state.

**Q52. How many states are commonly used for a Moore FSM that recognizes 1011?**
- A. 2
- B. 3
- C. 4
- D. 5
**Answer:** D
**Explanation:** A typical Moore recognizer uses five states: no match, matched 1, matched 10, matched 101, and matched 1011.

**Q53. What is the correct progression when the input sequence 1, 0, 1, 1 is received?**
- A. S0 → S1 → S2 → S3 → S4
- B. S0 → S2 → S1 → S4 → S3
- C. S0 → S1 → S1 → S1 → S1
- D. S0 → S4 → S3 → S2 → S1
**Answer:** A
**Explanation:** Each state represents the portion of 1011 matched so far. After receiving all four bits, the FSM reaches S4, the detection state.

**Q54. Which Verilog construct is commonly used to describe next-state transitions?**
- A. case
- B. assign only
- C. initial
- D. generate only
**Answer:** A
**Explanation:** A case statement clearly maps each present state and input condition to the appropriate next state.

**Q55. Why is a separate output block used in a Moore FSM?**
- A. To make output depend directly on input
- B. To generate output only from the present state
- C. To remove the clock
- D. To avoid defining states
**Answer:** B
**Explanation:** Moore output logic is based only on the current state. For example, detect = 1 when state is S4; otherwise detect = 0.

**Q56. What is the purpose of the reset signal?**
- A. To force the FSM into a known initial state
- B. To detect the pattern immediately
- C. To change 0 into 1
- D. To increase the number of states
**Answer:** A
**Explanation:** Reset initializes the state register, typically to S0, so pattern recognition begins from a known condition.

**Q57. What does overlapping detection mean for the pattern 1011?**
- A. The FSM ignores repeated bits
- B. A bit from one detected pattern may also be used as the start of another pattern
- C. The pattern can be detected only once
- D. The input must be reset after every bit
**Answer:** B
**Explanation:** Overlapping detection preserves useful suffix bits. For example, after detecting 1011, the final 1 can serve as the first 1 of a possible new pattern.

**Q58. Why is a default case included in the next-state logic?**
- A. To increase the output frequency
- B. To handle invalid or undefined states safely
- C. To make the output depend on input
- D. To eliminate reset
**Answer:** B
**Explanation:** A default transition, such as next_state = S0, provides a safe recovery path if the FSM enters an unexpected state. Sample Verilog Code: Moore Pattern Recognizer for 1011 module moore_pattern_1011 (    input  wire clk,    input  wire reset,    input  wire x,    output reg  detect);    localparam S0 = 3'b000, // No match               S1 = 3'b001, // Matched: 1               S2 = 3'b010, // Matched: 10               S3 = 3'b011, // Matched: 101               S4 = 3'b100; // Matched: 1011    reg [2:0] state, next_state;    // State register    always @(posedge clk or posedge reset) begin        if (reset)            state <= S0;        else            state <= next_state;    end    // Next-state logic    always @(*) begin        case (state)            S0: begin                if (x) next_state = S1;                else   next_state = S0;            end            S1: begin                if (x) next_state = S1;                else   next_state = S2;            end            S2: begin                if (x) next_state = S3;                else   next_state = S0;            end            S3: begin                if (x) next_state = S4;                else   next_state = S2;            end            S4: begin                if (x) next_state = S1;                else   next_state = S2;            end            default: next_state = S0;        endcase    end    // Moore output logic    always @(*) begin        if (state == S4)            detect = 1'b1;        else            detect = 1'b0;    endendmodule Note: The code detects the pattern 1011 with overlapping recognition. Since this is a Moore FSM, detect becomes 1 only after the FSM enters the final detection state S4. MCQs on Mealy Pattern Recognizer FSM and Verilog Code Pattern used: 1011 (overlapping pattern detection). In a Mealy FSM, the output depends on both the present state and the current input.

**Q59. For detecting the pattern 1011, how many states are commonly required in a Mealy FSM?**
- A. 2
- B. 3
- C. 4
- D. 5
**Answer:** C
**Explanation:** A typical Mealy recognizer uses four states representing: no match, matched 1, matched 10, and matched 101. Detection occurs on the transition caused by the final input 1.

**Q60. In a Mealy recognizer for 1011, when is detect asserted?**
- A. Only after entering a separate final state
- B. When the FSM is in the matched-101 state and the current input is 1
- C. Whenever the input is 1
- D. Only during reset
**Answer:** B
**Explanation:** When the previous bits have matched 101 and the current input is 1, the complete pattern 1011 is recognized. The output is asserted on that transition.

**Q61. Which statement best describes a key difference between Mealy and Moore FSMs?**
- A. Mealy FSMs have no states
- B. Moore outputs depend on input and state, while Mealy outputs depend only on state
- C. Mealy outputs depend on state and input, while Moore outputs depend only on state
- D. Both always use the same number of states
**Answer:** C
**Explanation:** A Mealy output uses both state and input. A Moore output uses only the present state. Mealy machines often require fewer states for the same pattern.

**Q62. What does overlapping pattern detection mean?**
- A. A detected pattern cannot share bits with another pattern
- B. A bit from one detected pattern can also be part of the next pattern
- C. The input is ignored after detection
- D. The FSM resets after every input bit
**Answer:** B
**Explanation:** Overlapping detection allows useful suffix bits to become the beginning of another possible pattern. This improves continuous pattern recognition.

**Q63. What are the different types of Carry propagator adders?**
- Ripple carry adders
- Carry lookahead adders
- Prefix adders
- Skip ahead adders

**Q64. What is the delay in the ripple carry adder, given tFA is the delay of 1 full adder?**
- N x tFA
- tFA
- (N-1) x tFA
- None of the above

**Q65. What is the N-bit delay of a prefix adder?**
- tPA = tpg  + log2N(tpg-prefix) + tXOR
- tPA = N X tpg
- tPA = tpg  + log2N
- tPA = tpg  +  tXOR

**Q66. What is the Sum output of a Half Adder?**
- a. A + Bb. A ⊕ Bc. ABd. A̅B + AB̅

**Q67. What is the Carry output of a Full Adder?**
- a. A ⊕ B ⊕ Cinb. AB + ACin + BCinc. AB + Cind. A + B + Cin
- A Carry-Lookahead Adder improves speed by:
- a. Reducing the number of bitsb. Using fewer gatesc. Computing carries in paralleld. Removing carries
- The generate signal for bit i is:
- a. Pi = Ai ⊕ Bib. Gi = AiBic. Gi = Ai + Bid. Gi = Ai − Bi
- The propagate signal for bit i in the Harris text is:
- a. Pi = AiBib. Pi = Ai + Bic. Pi = Ai ⊕ Bid. Pi = Ai − Bi
- The carry equation for a Carry-Lookahead Adder is:
- a. Ci = GiPib. Ci = Gi + PiCi-1c. Ci = Ai + Bid. Ci = Pi + Ci-1

**Q68. Which adder generally provides the fastest performance for large word sizes?**
- a. Ripple Carry Adderb. Carry Skip Adderc. Prefix Adderd. Serial Adder

**Q69. A Carry-Lookahead Adder improves speed by:**
- a. Reducing the number of bitsb. Using fewer gatesc. Computing carries in paralleld. Removing carries

**Q70. Which circuit performs arithmetic and logical operations?**
- a. Decoderb. Multiplexerc. ALUd. Counter

**Q71. Logical left shift by one bit is equivalent to:**
- a. Division by 2b. Multiplication by 2c. Multiplication by 4d. No change

**Q72. A comparator is used to:**
- a. Add two numbersb. Multiply two numbersc. Determine relative magnitude of two numbersd. Shift a number

**Q73. In binary multiplication, each partial product is generated using:**
- a. XOR gates onlyb. AND operations between multiplicand and multiplier bitsc. OR gates onlyd. NOT gates only

**Q74. Which adder has delay proportional to log₂N?**
- a. Ripple Carry Adderb. Serial Adderc. Prefix Adderd. Half Adder

**Q75. You are designing a 32-bit processor for a low-cost embedded device. The propagation delay of a   full adder is 300 ps, and each two-input gate delay is 100 ps. Which adder implementation would you choose if minimizing delay is the primary goal, and what would be the approximate delay?**
- A. Ripple-Carry Adder, 9.6 ns
- B. Carry-Lookahead Adder (4-bit blocks), 3.3 ns
- C. Prefix Adder, 1.2 ns
- D. Ripple-Carry Adder, 3.3 ns
- Answer: C. Prefix Adder, 1.2 ns
- Reasoning: Ripple-Carry delay = ns. CLA delay = 3.3 ns. Prefix Adder delay = ns. Fastest option is Prefix Adder.

**Q76. You are implementing subtraction in an ALU. To compute , which hardware             configuration is correct?**
- A. Invert bits of B, add 1, then add to A with Cin = 1
- B. Directly subtract B from A using a comparator
- C. Use a ripple-carry adder with Cin = 0
- D. Use XOR gates to flip A and add B
- Answer:  A. Invert bits of B, add 1, then add to A with Cin = 1
- Reasoning: Two’s complement subtraction is performed by inverting B, adding 1, and then adding to A.

**Q77. You need to multiply a binary number by 16 using minimal hardware. Which operation achieves this?**
- A. Arithmetic Right Shift by 4
- B. Logical Left Shift by 4
- C. Rotate Left by 4
- D. Add 16 repeatedly
- Answer: B. Logical Left Shift by 4
- Reasoning: Left shift by N bits multiplies the number by . Here, .

**Q78. A designer computes A – B and checks sign bit. Q: If sign bit = 1, what does it mean?**
- A) A > B
- B) A < B
- C) A = B
- D) Overflow
- Ans: B
- Explanation: Negative result → A < B.

**Q79. ALU configured with F2 = 1, F1:0 = 10. Q: What operation occurs?**
- A) A + B
- B) A – B
- C) A OR B
- D) SLT
- Ans: B
- Explanation: F2 inverts B and adds 1 → subtraction.

**Q80. 11001 LSR 2. Q: Result?**
- A) 00110
- B) 11110
- C) 01110
- D) 00100
- Ans: A
- Explanation: Logical shift right fills with 0s → 00110.

**Q81. In two’s complement addition, A = 0111 (7), B = 0100 (4). Q: What is the overflow flag?**
- A) 0
- B) 1
- C) Depends on carry-in
- D) Undefined
- Ans: B
- Explanation: 7 + 4 = 11 → binary 1011 (negative in 4-bit signed). Overflow occurs when adding two positives yields a negative.

**Q82. A 32 × 32 multiplier is implemented. Q: What is product size?**
- A) 32 bits
- B) 64 bits
- C) 128 bits
- D) 16 bits
- Ans: B
- Explanation: N × N multiplier → 2N-bit result → 64 bits.

**Q83. A 16-bit logical shifter is built. Q: How many multiplexers are required?**
- A) 16 × 16
- B) 16 × 4
- C) 16 × log₂16
- D) 16 × 1
- Ans: A
- Explanation: Each bit requires a 16:1 multiplexer → 16 × 16.

**Q84. A CPU designer chooses between CLA and Prefix adder for a 128-bit ALU. Q: Why might prefix adder be chosen despite higher hardware cost?**
- A) Lower power consumption
- B) Logarithmic delay scaling
- C) Smaller area footprint
- D) Easier HDL coding
- Ans: B
- Explanation: Prefix adder delay ∝ log₂N, critical for wide adders in CPUs.

**Q85. A 64-bit ripple-carry adder has tFA = 250 ps. A 64-bit CLA with 8-bit blocks has tpg = 100 ps, tpg_block = 800 ps, tAND_OR = 200 ps, and tFA = 250 ps. Q: Which design is faster and why?**
- A) Ripple-carry, because fewer gates
- B) CLA, because carry computed in parallel
- C) Ripple-carry, because linear delay is smaller
- D) Both equal
- Ans: B
- Explanation: Ripple delay = 64 × 250 ps = 16 ns. CLA delay ≈ 100 + 800 + (64/8 – 1) × 200 + (8 × 250) = 3.9 ns. CLA is much faster.

**Q86. A = 25, B = 32, F2:0 = 111. Q: What is Y?**
- A) 0
- B) 1
- C) 25
- D) 32
- Ans: B
- Explanation: SLT → Y = 1 if A < B.

**Q87. A 4-bit comparator checks if A = B. Q: Which gate is used per bit?**
- A) XOR
- B) XNOR
- C) AND
- D) OR
- Ans: B
- Explanation: XNOR checks equality per bit.

**Q88. To compute A – B, the designer inverts B and adds 1. Q: Which input must be set in CPA?**
- A) Cin = 0
- B) Cin = 1
- C) Cout = 1
- D) None
- Ans: B
- Explanation: Subtraction = A + (¬B + 1) → Cin = 1.

**Q89. A 32-bit CLA with 4-bit blocks is designed. Q: Why is it faster than ripple-carry?**
- A) Uses fewer gates
- B) Computes carry in parallel using generate/propagate
- C) Eliminates carry completely
- D) Uses XOR only
- Ans: B
- Explanation: CLA precomputes carry using G and P signals.

**Q90. A circuit designer wants to add two 1-bit numbers but doesn’t care about carry-in. Q: Which outputs does the half adder produce?**
- A) Sum only
- B) Carry only
- C) Sum and Carry-out
- D) Sum, Carry-in, Carry-out
- Ans: C
- Explanation: Half adder → S = A ⊕ B, Cout = A·B. No Cin input.

**Q91. In a fixed-point number system, the position of the binary point is:**
- A. Changed during every arithmetic operation
- B. Fixed at a predetermined position
- C. Always placed after the least significant bit
- D. Stored separately in memory
**Answer:** B. Fixed at a predetermined position
**Explanation:** In fixed-point representation, the binary point has an implied fixed position agreed upon when interpreting the bits.

**Q92. An 8-bit fixed-point number has 4 integer bits and 4 fractional bits. Where is the implied binary**
- A. 0.1101100
- B. 01.101100
- C. 011.01100
- D. 0110.1100
**Answer:** D. 0110.1100
**Explanation:** Four bits are assigned to the integer part and four to the fractional part: 0110.1100

**Q93. What is the decimal value of the unsigned fixed-point number 0110.1100?**
- A. 6.25
- B. 6.50
- C. 6.75
- D. 6.875
**Answer:** C. 6.75

**Q94. In the fixed-point number 0010.0110, the weight of the rightmost bit is:**
- A. 2−1
- B. 2−2
- C. 2−3
- D. 2−4
**Answer:** D. 2−4
**Explanation:** With four fractional bits, their weights are: 2−1 , 2−2 , 2−3 , 2−4

**Q95. What is the decimal value of the fractional binary number 0.1000₂?**
- A. 0.25
- B. 0.5
- C. 0.75
- D. 1.0
**Answer:** B. 0.5

**Q96. What is the binary fixed-point representation of 𝟎. 𝟕𝟓𝟏𝟎 using four fractional bits?**
- A. 0000.0011
- B. 0000.0110
- C. 0000.1100
- D. 0000.1110
**Answer:** C. 0000.1100

**Q97. Which notation can be used to represent signed fixed-point numbers?**
- A. Only unsigned binary
- B. Only BCD
- C. Two’s complement or sign-magnitude
- D. Gray code only
**Answer:** C. Two’s complement or sign-magnitude

**Q98. In sign-magnitude representation, the most significant bit generally represents:**
- A. Fraction
- B. Sign
- C. Binary point
- D. Least significant value
**Answer:** B. Sign
**Explanation:** Usually: • 0 → positive • 1 → negative

**Q99. Which binary fraction represents 𝟎. 𝟔𝟐𝟓𝟏𝟎 ?**
- A. 0.1000
- B. 0.1010
- C. 0.1100
- D. 0.1110
**Answer:** B. 0.1010

**Q100. In an 8-bit fixed-point representation with four fractional bits, the smallest fractional place**
- A. 2−1
- B. 2−2
- C. 2−4
- D. 2−8
**Answer:** C. 2−4

**Q101. What is the decimal value of 0011.0110₂ when interpreted as an unsigned fixed-point number?**
- A. 3.25
- B. 3.375
- C. 3.5
- D. 3.75
**Answer:** B. 3.375

**Q102. The absolute value +𝟐. 𝟑𝟕𝟓is represented as:**
- A. 0010.0110
- B. 1010.0110
- C. 1101.1010
- D. 1110.0110
**Answer:** B. 1010.0110
**Explanation:** In sign-magnitude representation, only the sign bit changes: 0010.0110 → 1010.0110

**Q103. The positive fixed-point value +𝟐. 𝟑𝟕𝟓 is:**
- A. 1010.0110
- B. 1101.1001
- C. 1101.1010
- D. 1110.0110
**Answer:** C. 1101.1010

**Q104. Which statement correctly distinguishes sign-magnitude from two’s complement?**
- A. Both are always identical for negative numbers
- B. Sign-magnitude changes the sign bit, while two’s complement involves inversion and adding 1
- C. Two’s complement changes only the sign bit
- D. Sign-magnitude requires inversion and adding 1
**Answer:** B

**Q105. Consider the fixed-point number:**
- A. 2.625
- B. 2.6875
- C. 2.75
- D. 2.8125
**Answer:** B. 2.6875

**Q106. Why is two’s complement generally preferred for signed fixed-point arithmetic?**
- A. It eliminates fractional bits
- B. It allows signed addition to be performed using ordinary binary addition
- C. It requires no sign bit
- D. It increases the number of bits automatically
**Answer:** B
**Explanation:** Two’s complement allows positive and negative numbers to be added using the same binary addition circuitry.

**Q107. In an 8-bit fixed-point format with four fractional bits, what bit pattern represents +𝟎. 𝟕𝟓?**
- A. 0000 0011
- B. 0000 0110
- C. 0000 1100
- D. 0001 1000
**Answer:** C. 0000 1100

**Q108. In an 8-bit fixed-point system with 4 integer bits and 4 fractional bits, +𝟎. 𝟔𝟐𝟓is represented**
- A. 1000.1010
- B. 1111.0101
- C. 1111.0110
- D. 1000.0110
**Answer:** C. 1111.0110

**Q109. Perform the fixed-point addition:**
- A. 0000.0010
- B. 0000.0110
- C. 1111.0010
- D. 10000.0010
**Answer:** A. 0000.0010

**Q110. A bit pattern 01101100 is stored in memory. Can we determine its fixed-point decimal value**
- A. Yes, it is always 108
- B. Yes, it is always 6.75
- C. No, the binary-point position must be known
- D. No, fixed-point values cannot be converted to decimal
**Answer:** C
**Explanation:** The bits themselves do not store the binary point. For example: 01101100 could be interpreted as: 0110.1100 or 011.01100 or 01.101100 Each interpretation gives a different numerical value.

**Q111. Suppose the bit pattern is:**
- A. 3.125
- B. 3.25
- C. 3.5
- D. 3.75
**Answer:** B. 3.25

**Q112. The same bit pattern 00110100 is now interpreted with only 2 fractional bits. What is its value?**
- A. 3.25
- B. 6.5
- C. 13
- D. 52
**Answer:** C. 13

**Q113. Which of the following correctly represents −𝟐. 𝟑𝟕𝟓in 8-bit fixed-point two’s complement,**
- A. 1010.0110
- B. 1101.1010
- C. 0010.0110
- D. 1101.0110
**Answer:** B. 1101.1010

**Q114. An 8-bit fixed-point two’s complement number has four fractional bits. What is the value of the**
- A. 1
- B. 0.5
- C. 0.125
- D. 0.0625
**Answer:** D. 0.0625

**Q115. Which statement about fixed-point numbers is FALSE?**
- A. The binary point is usually implied rather than physically stored
- B. Two’s complement can represent negative fixed-point numbers
- C. The interpretation of the bits depends on the agreed binary-point position
- D. The location of the binary point can always be determined by examining only the stored bits
**Answer:** D
**Explanation:** A fixed-point number is physically just a collection of bits. The bit pattern itself does not tell us where the implied binary point is located.

**Q116. The main advantage of floating-point representation over fixed-point representation is that**
- A. Represent only integers
- B. Represent a much wider range of very large and very small numbers
- C. Eliminate the need for binary numbers
- D. Represent only positive numbers
**Answer:** B

**Q117. A floating-point number is analogous to:**
- A. Boolean algebra
- B. Scientific notation
- C. Gray code
- D. Two's complement only
**Answer:** B

**Q118. IEEE 754 single-precision floating-point representation uses how many bits?**
- A. 16 bits
- B. 32 bits
- C. 48 bits
- D. 64 bits
**Answer:** B. 32 bits

**Q119. What does a sign bit of 0 indicate for an ordinary IEEE 754 floating-point number?**
- A. Negative
- B. Positive
- C. Infinity
- D. NaN
**Answer:** B. Positive

**Q120. What is the bias used in IEEE 754 single-precision floating-point representation?**
- A. 63
- B. 127
- C. 128
- D. 1023
**Answer:** B. 127

**Q121. If the actual exponent is −𝟑, what is the biased exponent?**
- A. 124
- B. 127
- C. 130
- D. 131
**Answer:** A. 124

**Q122. Convert 𝟐𝟎𝟏𝟎 into normalized binary scientific notation.**
- A. 1.01 × 24
- B. 1.01 × 23
- C. 10.1 × 24
- D. 1.1 × 25
**Answer:** A

**Q123. What is the normalized binary representation of 𝟏𝟐𝟏𝟎 ?**
- A. 1.1 × 23
- B. 1.1 × 22
- C. 1.01 × 23
- D. 1.11 × 22
**Answer:** A

**Q124. The number 𝟏. 𝟏𝟎𝟏𝟐 × 𝟐𝟒 has an actual exponent of:**
- A. 1
- B. 4
- C. 101
- D. 131
**Answer:** B. 4

**Q125. Why is the leading 1 of a normalized binary floating-point number usually not stored?**
- A. It is always 0
- B. It is always 1 for normalized nonzero binary numbers
- C. It represents the sign
- D. It represents the exponent
**Answer:** B

**Q126. What is the biased exponent for an actual exponent of +𝟏𝟎?**
- A. 117
- B. 127
- C. 137
- D. 138
**Answer:** C. 137

**Q127. An IEEE 754 single-precision number has biased exponent 𝟏𝟑𝟎. What is its actual exponent?**
- A. 3
- B. −3
- C. 130
- D. 257
**Answer:** A. 3

**Q128. An IEEE 754 single-precision number has biased exponent 10000010₂. What is the actual**
- A. 2
- B. 3
- C. 129
- D. 130
- A. 1.01 × 25
- B. 1.01 × 24
- C. 1.1 × 25
- D. 1.001 × 25
**Answer:** A

**Q129. For 𝟒𝟎𝟏𝟎 = 𝟏. 𝟎𝟏𝟐 × 𝟐𝟓 , what is the biased exponent?**
- A. 5
- B. 127
- C. 130
- D. 132
**Answer:** D. 132

**Q130. Which is the correct IEEE 754 representation of +𝟒𝟎𝟏𝟎 ?**
- A. 0 10000100 01000000000000000000000
- B. 0 00000101 01000000000000000000000
- C. 1 10000100 01000000000000000000000
- D. 0 10000100 10100000000000000000000
**Answer:** A

**Q131. Convert 𝟏𝟖. 𝟓𝟏𝟎 to normalized binary notation.**
- A. 1.00101 × 24
- B. 1.01001 × 24
- C. 1.00101 × 25
- D. 1.101 × 23
- A. 1 10000011 00101000000000000000000
- B. 0 10000011 00101000000000000000000
- C. 1 00000100 00101000000000000000000
- D. 1 10000011 10010100000000000000000
**Answer:** A

**Q132. Decode:**
- A. −2.5
- B. −5
- C. +5
- D. −10
**Answer:** B. −5

**Q133. A normalized binary number is:**
- A. 123
- B. 124
- C. 127
- D. 131
**Answer:** A. 123

**Q134. Which exponent pattern is used for infinity and NaN?**
- A. All 0s
- B. All 1s
- C. Alternating 1s and 0s
- D. 01111111
**Answer:** B. All 1s

**Q135. Approximately how many significant decimal digits does double precision provide?**
- A. 7
- B. 8
- C. 15
- D. 64
- A. 6
- B. 127
- C. 133
- D. 260
- A. 26
- B. 52
- C. 13
- D. 104
**Answer:** B. 52


---

# PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS

<a id="topic-1"></a>
## Topic Module 1: 08_fsm-moore-mealy-design.md
**Source File**: `docs/08_fsm-moore-mealy-design.md`

# 08. Finite State Machines — Moore vs Mealy, Design Process

> **Source:** Harris & Harris Ch. 3, Unit 2 Slides 2–64

---

## FSM Components

| Component | Function |
|-----------|----------|
| **M Inputs** | External signals |
| **N Outputs** | External signals |
| **k-bit State Register** | Stores current state (2ᵏ states) |
| **Clock** | Controls state updates |
| **Reset (optional)** | Initializes to known state |

---

## Three-Block Structure

```
         ┌──────────────┐
Inputs ──►│ Next-State   │──► Next State
          │   Logic      │
State ───►│ (Combinational)│
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │  State Reg   │──► Current State (k FFs)
          │  (k FFs)     │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │  Output      │──► Outputs
          │  Logic       │
          └──────────────┘
```

---

## Moore vs Mealy

| Property | Moore | Mealy |
|----------|-------|-------|
| **Output depends on** | Current state only | Current state + inputs |
| **Output formula** | Y = g(S) | Y = g(S, X) |
| **States needed** | More (usually) | Fewer |
| **Output timing** | State-synchronous | Can be asynchronous |
| **Glitch immunity** | High | Lower |
| **Diagram** | Outputs **in** circles | Outputs **on** arcs |

---

## FSM Design Procedure

1. **Identify inputs/outputs**
2. **Draw State Transition Diagram**
3. **Create State Transition Table**
4. **Create Output Table**
5. **Select State Encoding** (Binary, One-Hot, etc.)
6. **Derive Next-State Equations** (K-maps/inspection)
7. **Derive Output Equations**
8. **Draw Circuit Schematic**

---

## Traffic Light Controller Example

**Inputs:** Tₐ (Academic Ave sensor), Tᵦ (Bravado Blvd sensor)
**Outputs:** Lₐ, Lᵦ (traffic lights)
**Clock:** 5-second period

**States (Moore):**
| State | Meaning | Lₐ | Lᵦ |
|-------|---------|----|----|
| S0 | Academic Green | G | R |
| S1 | Academic Yellow | Y | R |
| S2 | Bravado Green | R | G |
| S3 | Bravado Yellow | R | Y |

**State Encoding (Binary):** S0=00, S1=01, S2=10, S3=11

---

## Divide-by-3 Counter (Moore)

| State | Binary | One-Hot | Output Y |
|-------|--------|---------|----------|
| S0 | 00 | 001 | 1 |
| S1 | 01 | 010 | 0 |
| S2 | 10 | 100 | 0 |

**Sequence:** S0 → S1 → S2 → S0 → ...
**Output:** Y=1 only in S0 (1 cycle out of 3)

---

## Pattern Recognizer (1011, Overlapping)

### Moore (5 states)
| State | Matched | Output |
|-------|---------|--------|
| S0 | — | 0 |
| S1 | 1 | 0 |
| S2 | 10 | 0 |
| S3 | 101 | 0 |
| S4 | 1011 | **1** |

**Overlap transitions from S4:**
- Input 1 → S1 (new '1' starts next pattern)
- Input 0 → S2 ('10' suffix matches prefix)

### Mealy (4 states)
| State | Matched |
|-------|---------|
| S0 | — |
| S1 | 1 |
| S2 | 10 |
| S3 | 101 |

**Output:** Detect=1 when in S3 **and** input=1 (on transition)

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Moore output depends on? | Current state only |
| Mealy output depends on? | Current state + inputs |
| Which has fewer states? | Mealy |
| Which has glitch-free output? | Moore |
| Divide-by-3 states? | 3 (S0, S1, S2) |
| Moore 1011 states? | 5 (S0-S4) |
| Mealy 1011 states? | 4 (S0-S3) |

---

## Exam-Relevant MCQ Patterns

1. **Moore vs Mealy definition** — output dependency (Q1, Q49, Q50)
2. **State count comparison** — Moore = N+1, Mealy = N for N-bit pattern (Q5, Q52, Q59)
3. **Binary encoding** — k FFs → 2ᵏ states (Q2, Q3, Q42)
4. **One-Hot encoding** — K states → K FFs (Q2)
5. **Divide-by-3 frequency** — f_out = f_in / 3 (Q6, Q39)
6. **Overlap detection** — suffix becomes prefix (Q57, Q62)
7. **Verilog default case** — prevents latches, safe recovery (Q8, Q47)
8. **Non-blocking (≤)** — state register block (Q7)

---

## Key Formulas (Memorize)

```
Binary encoding: k FFs → 2ᵏ states
One-Hot: K states → K FFs
Divide-by-N: f_out = f_in / N
Moore 1011: 5 states, Mealy 1011: 4 states
```

---

<a id="topic-2"></a>
## Topic Module 2: 09_state-encoding-factoring.md
**Source File**: `docs/09_state-encoding-factoring.md`

# 09. State Encoding & Factoring State Machines

> **Source:** Harris & Harris Ch. 3, Unit 2 Slides 24–54

---

## State Encoding Techniques

| Encoding | FFs for K States | Advantages | Disadvantages |
|----------|------------------|------------|---------------|
| **Binary** | ⌈log₂K⌉ | Fewest FFs, compact | Complex next-state logic |
| **One-Hot** | K | Simple logic, fast | More FFs, higher cost |
| **Gray** | ⌈log₂K⌉ | Single-bit transitions | Complex logic |
| **Custom** | — | Application-specific | Manual effort |

---

## Divide-by-3 Counter: Binary vs One-Hot

### Binary Encoding (2 FFs)

| State | Code |
|-------|------|
| S0 | 00 |
| S1 | 01 |
| S2 | 10 |
| (11) | Unused |

**Next-state logic:** More complex, multi-bit changes

### One-Hot Encoding (3 FFs)

| State | Code |
|-------|------|
| S0 | 001 |
| S1 | 010 |
| S2 | 100 |

**Next-state logic:** Simple shifts (S0→S1→S2→S0 = rotate left)

---

## Choosing Encoding

- **Small FSMs / speed critical:** One-Hot
- **Large FSMs / area critical:** Binary
- **CAD tools** can optimize automatically
- **Trade-off:** FFs vs logic complexity vs speed

---

## Factoring State Machines

### Problem: State Explosion
Complex FSM → many states → hard to design/debug

### Solution: Decompose into Smaller Interacting FSMs

```
Unfactored:        Factored:
  1 Large FSM    →   FSM_A + FSM_B
  N₁×N₂ states       N₁ + N₂ states
```

---

## Traffic Light with Parade Mode

**Unfactored:** 8 states (S0-S3 normal, S4-S7 parade)
- Two nearly identical halves
- Complex, hard to modify

**Factored:**
| Sub-FSM | Function | States |
|---------|----------|--------|
| **Mode FSM** | Tracks Normal/Parade | 2 |
| **Lights FSM** | Controls lights (uses Mode) | 4 |

**Interaction:** Mode FSM output `M` → Lights FSM input
**Result:** 2+4=6 states vs 8, modular, easier to extend

---

## Factored vs Unfactored Comparison

| Aspect | Unfactored | Factored |
|--------|------------|----------|
| Structure | Single large FSM | Multiple small FSMs |
| States | N₁ × N₂ | N₁ + N₂ |
| Transitions | Complex | Simple per FSM |
| Debugging | Difficult | Easier |
| Modularity | Low | High |
| Extensibility | Hard | Easy |

---

## Deriving FSM from Schematic

### Steps
1. Identify Inputs, Outputs, State bits
2. Write next-state & output equations
3. Create next-state & output tables
4. Remove unreachable states
5. Assign symbolic names
6. Draw state diagram
7. Describe function

### Example: Keypad Lock Circuit
**Given:** 2 state bits (S₁,S₀), inputs (A₁,A₀), output (Unlock)
**Equations:**
- S₁' = S₀·A₁·A₀
- S₀' = S₁'·S₀·A₁·A₀
- Unlock = S₁

**Result:** 3 reachable states → pattern detector

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Binary FFs for 8 states? | 3 (2³=8) |
| One-Hot FFs for 8 states? | 8 |
| Binary FFs for 5 states? | 3 (2²=4<5, 2³=8≥5) |
| Factoring benefit? | N₁×N₂ → N₁+N₂ states |
| Parade mode factoring? | Mode FSM + Lights FSM |

---

## Exam-Relevant MCQ Patterns

1. **Binary encoding states** — 2ᵏ for k FFs (Q2, Q3, Q42)
2. **One-Hot FFs** — equals number of states (Q2)
3. **Factoring advantage** — multiplicative → additive states (Q9)
4. **Binary vs One-Hot trade-off** — FFs vs logic complexity (Q26, Q27)
5. **Deriving FSM** — steps from circuit to diagram (Q55)

---

## Key Formulas (Memorize)

```
Binary:    K states → ⌈log₂K⌉ FFs
One-Hot:   K states → K FFs
Factored:  N₁×N₂ states → N₁+N₂ states
```

---

<a id="topic-3"></a>
## Topic Module 3: 10_arithmetic-adders.md
**Source File**: `docs/10_arithmetic-adders.md`

# 10. Arithmetic Circuits — Adders (RCA, CLA, Prefix)

> **Source:** Harris & Harris Ch. 5, Unit 2 Slides 68–100

---

## Half Adder

| A | B | Sum | Cout |
|---|---|-----|------|
| 0 | 0 | 0   | 0    |
| 0 | 1 | 1   | 0    |
| 1 | 0 | 1   | 0    |
| 1 | 1 | 0   | 1    |

**Equations:**
- `Sum = A ⊕ B`
- `Cout = A·B`

**Gates:** 1 XOR, 1 AND

---

## Full Adder

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 | 0   | 0   | 0    |
| 0 | 0 | 1   | 1   | 0    |
| 0 | 1 | 0   | 1   | 0    |
| 0 | 1 | 1   | 0   | 1    |
| 1 | 0 | 0   | 1   | 0    |
| 1 | 0 | 1   | 0   | 1    |
| 1 | 1 | 0   | 0   | 1    |
| 1 | 1 | 1   | 1   | 1    |

**Equations:**
- `Sum = A ⊕ B ⊕ Cin`
- `Cout = A·B + A·Cin + B·Cin = AB + Cin(A⊕B)`

**Implementation:** 2 Half Adders + 1 OR gate

---

## Ripple-Carry Adder (RCA)

- Chain N full adders
- Carry ripples LSB → MSB
- **Delay:** `t_ripple = N × t_FA`
- **32-bit, t_FA=300ps:** 9.6 ns

**Disadvantage:** Slow for large N (O(N) delay)

---

## Carry-Lookahead Adder (CLA)

### Generate & Propagate
- **Generate (Gᵢ):** Stage creates carry → `Gᵢ = Aᵢ·Bᵢ`
- **Propagate (Pᵢ):** Stage passes carry → `Pᵢ = Aᵢ ⊕ Bᵢ` (or `Aᵢ + Bᵢ`)

### Carry Equations
```
C₁ = G₀ + P₀·C₀
C₂ = G₁ + P₁·G₀ + P₁·P₀·C₀
C₃ = G₂ + P₂·G₁ + P₂·P₁·G₀ + P₂·P₁·P₀·C₀
C₄ = G₃ + P₃·G₂ + P₃·P₂·G₁ + P₃·P₂·P₁·G₀ + P₃·P₂·P₁·P₀·C₀
```

### Block CLA (k-bit blocks)
- Compute block G and P
- Carry jumps block-to-block
- **Delay:** `t_CLA = t_pg + t_pg_block + (N/k - 1)t_AND_OR + k·t_FA`

**32-bit, 4-bit blocks, t_AND_OR=200ps:** ~3.3 ns

---

## Prefix Adder (Fastest)

### Principle
- Compute all carries in parallel using prefix tree
- **log₂N stages** of prefix cells (black/gray)
- **Delay:** `t_PA = t_pg + log₂N(t_pg_prefix) + t_XOR`

**32-bit:** ~1.2 ns

### Prefix Cell (Black Cell)
```
G_out = G_upper + P_upper·G_lower
P_out = P_upper·P_lower
```

### Gray Cell
```
G_out = G_upper + P_upper·G_lower
P_out = P_lower (pass through)
```

---

## Delay Comparison (32-bit)

| Adder Type | Delay | Formula |
|------------|-------|---------|
| Ripple-Carry | 9.6 ns | N·t_FA |
| CLA (4-bit blocks) | 3.3 ns | t_pg + t_pg_block + 7·t_AND_OR + 4·t_FA |
| Prefix | 1.2 ns | t_pg + log₂N·t_pg_prefix + t_XOR |

**Parameters:** t_FA=300ps, t_AND_OR=200ps, t_pg=100ps, t_pg_prefix=200ps, t_XOR=100ps

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Half Adder Sum? | A ⊕ B |
| Full Adder Cout? | AB + ACin + BCin |
| RCA delay scaling? | O(N) |
| CLA block size benefit? | Parallel carry within block |
| Prefix delay scaling? | O(log N) |
| Fastest for 32-bit? | Prefix Adder |

---

## Exam-Relevant MCQ Patterns

1. **Half/Full Adder equations** — Sum XOR, Cout majority (Q10, Q66, Q67)
2. **RCA delay** — N × t_FA (Q12, Q74)
3. **CLA Generate** — Gᵢ = Aᵢ·Bᵢ (Q13)
4. **CLA Propagate** — Pᵢ = Aᵢ ⊕ Bᵢ (or Aᵢ + Bᵢ) (Q13)
5. **Block P** — P₃:₀ = P₃·P₂·P₁·P₀ (Q14)
6. **Prefix delay** — O(log N) (Q15, Q74)
7. **Subtraction via 2's complement** — invert B, Cin=1 (Q16)
8. **Overflow detection** — C_in,MSB ⊕ C_out,MSB (Q17)
9. **Adder selection for CPU** — Prefix for speed despite area (Q75, Q84)

---

## Key Formulas (Memorize)

```
Half Adder:  S = A⊕B,    Cout = AB
Full Adder:  S = A⊕B⊕Cin, Cout = AB + ACin + BCin
RCA:         t = N × t_FA
CLA (k-block): t = t_pg + t_pg_block + (N/k-1)t_AND_OR + k·t_FA
Prefix:      t = t_pg + log₂N·t_pg_prefix + t_XOR
Subtract:    A - B = A + B' + 1 (Cin=1)
Overflow:    V = C_in,MSB ⊕ C_out,MSB
```

---

<a id="topic-4"></a>
## Topic Module 4: 11_alu-comparator-shifter-multiplier.md
**Source File**: `docs/11_alu-comparator-shifter-multiplier.md`

# 11. ALU, Comparators, Shifters & Multipliers

> **Source:** Harris & Harris Ch. 5, Unit 2 Slides 88–103

---

## ALU (Arithmetic Logic Unit)

### 32-bit ALU Operations (F₂:₀)
| F₂ | F₁ | F₀ | Operation |
|----|----|----|-----------|
| 0  | 0  | 0  | A AND B   |
| 0  | 0  | 1  | A OR B    |
| 0  | 1  | 0  | A + B     |
| 0  | 1  | 1  | (unused)  |
| 1  | 0  | 0  | A AND ~B  |
| 1  | 0  | 1  | A OR ~B   |
| 1  | 1  | 0  | A - B     |
| 1  | 1  | 1  | SLT       |

### ALU Structure
- Multiple operation units in parallel
- **MUX selects output** based on F₂:₀
- **F₂=1** → inverters on B + Cin=1 (for SUB/SLT)

### SLT (Set Less Than)
- Computes `A - B` using subtractor
- If result negative (sign bit = 1) → A < B
- Output = sign bit zero-extended (0x00000001 or 0x00000000)
- **Example:** A=25, B=32 → 25-32=-7 → S₃₁=1 → Y=1

---

## Comparators

### Equality (A == B)
- **Per bit:** XNOR (Aᵢ ⊙ Bᵢ = 1 if equal)
- **Overall:** N-input AND of all XNORs
- `Eq = Π(Aᵢ ⊙ Bᵢ)`

### Less Than (A < B) — Unsigned
- Compare MSB to LSB
- First differing bit decides
- Can use subtractor: A < B iff (A-B) sign = 1

### Less Than (A < B) — Signed (2's comp)
- Same as unsigned if no overflow
- With overflow: sign bit inverted
- `V = C_in,MSB ⊕ C_out,MSB`

---

## Shifters

### Types
| Shift | Left (<<) | Right (>>) | Notes |
|-------|-----------|------------|-------|
| **Logical** | Fill 0 | Fill 0 | Unsigned |
| **Arithmetic** | Fill 0 | Replicate MSB | Signed (preserves sign) |
| **Rotate** | Circular | Circular | Bits wrap around |

### Examples (11001)
| Operation | Result |
|-----------|--------|
| Logical >> 2 | 00110 |
| Arithmetic >> 2 | 11110 (sign=1) |
| Rotate ROR 2 | 01110 |
| Logical << 2 | 00100 |
| Arithmetic << 2 | 00100 |
| Rotate ROL 2 | 00111 |

### Barrel Shifter
- **Log₂N stages** of 2:1 MUXes
- Stage i shifts by 2ⁱ positions
- **16-bit:** 4 stages (1, 2, 4, 8)
- **Delay:** O(log N)

### Shifts as Multiply/Divide
- `A << N = A × 2ᴺ`
- `A >>> N = A ÷ 2ᴺ` (arithmetic, signed)

---

## Multipliers

### 4×4 Array Multiplier
- Partial products: each multiplier bit × multiplicand
- Shifted and summed
- **Result:** N+M bits for N×M multiply

### 32×32 Multiplier
- **Product size:** 64 bits

---

## Dividers

### 4×4 Divider Algorithm
```
R' = 0
for i = N-1 downto 0:
    R = {R' << 1, Aᵢ}
    D = R - B
    if D < 0:  Qᵢ = 0, R' = R
    else:      Qᵢ = 1, R' = D
```

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| ALU F₂=1 means? | Invert B, Cin=1 (subtract) |
| SLT implementation? | A-B, take sign bit |
| Equality comparator? | N XNORs + N-input AND |
| Logical vs Arithmetic right shift? | Logical=0-fill, Arithmetic=sign-fill |
| 11001 >>> 2? | 11110 |
| 16-bit barrel shifter stages? | 4 (log₂16) |
| 32×32 multiplier product bits? | 64 |

---

## Exam-Relevant MCQ Patterns

1. **ALU control decode** — F₂:₀ mapping (Q70, Q79)
2. **SLT uses sign bit** — of A-B result (Q23, Q86)
3. **Equality = XNOR + AND** (Q18, Q87)
4. **Logical vs Arithmetic shift** — MSB fill (Q19, Q20, Q80)
5. **Barrel shifter stages** — log₂N (Q21)
6. **Multiply bits** — N+M for N×M (Q22, Q82)
7. **Shift = multiply/divide by 2ᴺ** (Q77)
8. **Subtraction Cin=1** (Q26, Q88)
9. **CLA vs Prefix for wide adders** — log delay (Q84, Q94)
10. **Overflow in signed add** — two positives → negative (Q81)

---

## Key Formulas (Memorize)

```
Equality:  Eq = Π(Aᵢ ⊙ Bᵢ)
SLT:       Y = sign(A - B) zero-extended
Logical >>:  fill 0
Arithmetic >>: replicate MSB
<< N:       × 2ᴺ
>>> N:      ÷ 2ᴺ (signed)
Barrel stages: log₂N
Multiply N×M: N+M bits
```

---

<a id="topic-5"></a>
## Topic Module 5: 12_number-systems-fixedpoint.md
**Source File**: `docs/12_number-systems-fixedpoint.md`

# 12. Number Systems — Fixed-Point & Signed Representations

> **Source:** Harris & Harris Ch. 1, Unit 2 Slides 111–130

---

## Binary Number Representations

| Type | Range | Notes |
|------|-------|-------|
| **Unsigned** | 0 to 2ᴺ-1 | Positive only |
| **Sign/Magnitude** | -(2ᴺ⁻¹-1) to +(2ᴺ⁻¹-1) | MSB=sign, two zeros |
| **One's Complement** | -(2ᴺ⁻¹-1) to +(2ᴺ⁻¹-1) | Invert bits, two zeros |
| **Two's Complement** | -2ᴺ⁻¹ to +(2ᴺ⁻¹-1) | **Preferred** — unique zero, simple add/sub |

---

## Two's Complement (Memorize!)

### Negation Algorithm
```
1. Invert all bits (1's complement)
2. Add 1 to LSB
```

**Example: -5 in 8-bit**
- +5 = 0000 0101
- Invert = 1111 1010
- Add 1 = 1111 1011 = 0xFB

### Range (N bits)
- **Min:** -2ᴺ⁻¹ (e.g., -128 for 8-bit)
- **Max:** +2ᴺ⁻¹ - 1 (e.g., +127 for 8-bit)
- **One extra negative** because zero is unique

### Why 2's Complement Wins
- Single zero representation
- Addition/subtraction identical hardware
- No end-around carry needed

---

## Fixed-Point Numbers

### Format: Q-format (e.g., Q4.4 = 4 integer, 4 fraction bits)
**Binary point is IMPLIED** — not stored

### Example: 4 integer + 4 fraction bits
```
Binary:    0110.1100
           └┬┘ └┬┘
         int frac
Value:  6 + 0.5 + 0.25 = 6.75
```

### Fractional Weights
| Position | Weight |
|----------|--------|
| 2⁻¹ | 0.5 |
| 2⁻² | 0.25 |
| 2⁻³ | 0.125 |
| 2⁻⁴ | 0.0625 |

### Conversions

**Decimal → Fixed-Point (4.4):**
- 7.5 → 7 = 0111, 0.5 = 1000 → **0111.1000**
- 3.625 → 3 = 0011, 0.625 = 1010 → **0011.1010**
- -7.5 (2's comp): +7.5=0111.1000 → invert=1000.0111 → +1=**1000.1000**

**Fixed-Point → Decimal:**
- 0011.1010 = 3 + 0.5 + 0.125 = **3.625**
- 1000.1000 (2's comp, negative) → invert=0111.0111 → +1=0111.1000 = **-7.5**

---

## Fixed-Point Arithmetic
- **Addition:** Same as integer (align binary points)
- **Multiplication:** Qm.n × Qp.q = Q(m+p).(n+q) — double fraction bits
- **Overflow:** Same as integer

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| 8-bit 2's comp range? | -128 to +127 |
| Sign/Magnitude zero? | +0=00000000, -0=10000000 |
| 2's comp zero? | Only 00000000 |
| Negate 2's comp? | Invert + add 1 |
| 3.625 in Q4.4? | 0011.1010 |
| -7.5 in Q4.4 (2's comp)? | 1000.1000 |
| Q4.4 smallest fraction? | 2⁻⁴ = 0.0625 |

---

## Exam-Relevant MCQ Patterns

1. **2's complement range** — -2ᴺ⁻¹ to 2ᴺ⁻¹-1 (Q24)
2. **Negation procedure** — invert + 1 (Q27, Q113)
3. **Fixed-point conversion** — integer + fraction parts (Q26, Q27, Q93-Q112)
4. **Binary point implied** — not stored, must be agreed (Q91, Q110, Q115)
5. **Smallest fractional weight** — 2⁻ⁿ for n fraction bits (Q114)
6. **Sign/Magnitude vs 2's comp** — sign bit flip vs invert+1 (Q104)
7. **Fixed-point addition** — align points, add as integers (Q109)
8. **Why 2's comp preferred** — same adder for +/- (Q106)

---

## Key Formulas (Memorize)

```
2's Complement N-bit:  [-2ᴺ⁻¹, 2ᴺ⁻¹-1]
Negation:  invert + 1
Qm.n format:  m integer bits, n fraction bits
Fraction weight:  2⁻¹, 2⁻², ..., 2⁻ⁿ
Fixed-point add:  align binary points, integer add
Multiply Qm.n × Qp.q:  Q(m+p).(n+q)
```

---

<a id="topic-6"></a>
## Topic Module 6: 13_floating-point-ieee754.md
**Source File**: `docs/13_floating-point-ieee754.md`

# 13. Floating-Point — IEEE 754 Single/Double Precision

> **Source:** Harris & Harris Ch. 1, Unit 2 Slides 120–138

---

## IEEE 754 Single Precision (32-bit)

```
| S |    E (8 bits)    |      F (23 bits)       |
| 31| 30 ────────── 23 | 22 ──────────────── 0 |
```

| Field | Bits | Description |
|-------|------|-------------|
| **Sign (S)** | 1 | 0=positive, 1=negative |
| **Exponent (E)** | 8 | Biased: E = e + 127 |
| **Fraction (F)** | 23 | Significand = 1.F (implicit leading 1) |

**Value:** `(-1)ˢ × 1.F × 2ᴱ⁻¹²⁷`

---

## Encoding Steps (Decimal → IEEE 754)

### Example: 228₁₀
1. **Binary:** 228 = 11100100₂
2. **Normalize:** 1.11001₂ × 2⁷
3. **Sign:** 0 (positive)
4. **Exponent:** 7 + 127 = 134 = 10000110₂
5. **Fraction:** 11001 + zeros = 11001000000000000000000
6. **Result:** `0 10000110 11001000000000000000000` = **0x43640000**

### Example: -58.25₁₀
1. **Binary:** 58.25 = 111010.01₂
2. **Normalize:** 1.1101001₂ × 2⁵
3. **Sign:** 1 (negative)
4. **Exponent:** 5 + 127 = 132 = 10000100₂
5. **Fraction:** 1101001 + zeros
6. **Result:** `1 10000100 11010010000000000000000` = **0xC2690000**

---

## Special Values

| Value | Exponent | Fraction | Notes |
|-------|----------|----------|-------|
| **±0** | 00000000 | 000...0 | S=0/1 |
| **Denormalized** | 00000000 | ≠0 | 0.F × 2⁻¹²⁶ |
| **±∞** | 11111111 | 000...0 | S=0/1 |
| **NaN** | 11111111 | ≠0 | Not a Number |
| **Normalized** | 00000001–11111110 | any | 1.F × 2ᴱ⁻¹²⁷ |

---

## Double Precision (64-bit)
| Field | Bits |
|-------|------|
| Sign | 1 |
| Exponent | 11 (bias = 1023) |
| Fraction | 52 |
**Value:** `(-1)ˢ × 1.F × 2ᴱ⁻¹⁰²³`

---

## Floating-Point Addition (8 Steps)

1. **Extract** sign, exponent, fraction
2. **Prepend** implicit leading 1 → mantissa (1.F)
3. **Compare** exponents
4. **Shift** smaller mantissa right by |E₁-E₂|
5. **Add** mantissas
6. **Normalize** result (shift if ≥2 or <1)
7. **Round** (to 23 fraction bits)
8. **Assemble** back to IEEE format

### Example: 0x3FC00000 + 0x40500000
| Step | N1 (1.5) | N2 (3.25) |
|------|----------|-----------|
| 1. Extract | S=0, E=127, F=.1 | S=0, E=128, F=.101 |
| 2. Mantissa | 1.1 | 1.101 |
| 3. Compare | 127 vs 128 | diff = 1 |
| 4. Shift N1 | 1.1 >> 1 = 0.11 | (×2¹) |
| 5. Add | 0.11 + 1.101 = 10.011 | (×2¹) |
| 6. Normalize | 1.0011 × 2² | |
| 7. Round | fits 23 bits | |
| 8. Result | S=0, E=129, F=0011... | **0x40980000** |

---

## Rounding Modes
| Mode | Behavior |
|------|----------|
| **To nearest** | Round to closest (ties to even) |
| **Toward zero** | Truncate |
| **Down** | Toward -∞ |
| **Up** | Toward +∞ |

---

## Precision
| Format | Significant Digits (decimal) |
|--------|------------------------------|
| Single (32-bit) | ~7 |
| Double (64-bit) | ~15 |

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Single precision bias? | 127 |
| Double precision bias? | 1023 |
| Implicit leading bit? | Always 1 for normalized |
| +∞ encoding? | S=0, E=255, F=0 |
| NaN encoding? | E=255, F≠0 |
| Denormalized? | E=0, F≠0 (value = 0.F × 2⁻¹²⁶) |
| FP add step 2? | Prepend implicit 1 |

---

## Exam-Relevant MCQ Patterns

1. **Single precision layout** — 1/8/23 bits (Q28)
2. **Exponent bias** — 127 (Q29, Q120)
3. **Implicit leading 1** — always 1 for normalized (Q30)
4. **+∞ encoding** — E=all 1s, F=0 (Q31)
5. **NaN encoding** — E=all 1s, F≠0 (Q32)
6. **Denormalized** — E=0, F≠0 (Q33)
7. **Decimal → IEEE encoding** — normalize, bias, drop leading 1 (Q34, Q35, Q122-Q131)
8. **FP add step order** — extract→prepend 1→compare→shift→add→normalize→round→assemble (Q36, Q37)
9. **Shift smaller mantissa** — align exponents (Q37)
10. **Excess-127 NOT fixed-point** — it's floating-point exponent bias (Q38, Q116)

---

## Key Formulas (Memorize)

```
Single:    S(1) | E(8, bias=127) | F(23)
Double:    S(1) | E(11, bias=1023) | F(52)
Value:     (-1)ˢ × 1.F × 2ᴱ⁻ᵇⁱᵃˢ
Normalize: 1.xxxx × 2ᵉ
Denorm:    0.F × 2⁻¹²⁶ (single)
+∞:        E=255, F=0
NaN:       E=255, F≠0
FP Add:    1)Extract 2)Prepend 1 3)Compare 4)Shift 5)Add 6)Normalize 7)Round 8)Assemble
```

---

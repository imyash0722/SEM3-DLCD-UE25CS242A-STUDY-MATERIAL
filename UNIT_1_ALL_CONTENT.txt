# UNIT 1: COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
**Generated**: 2026-11-04 14:14:16
**Course**: Digital Logic and Computer Design (DLCD) — UE25CS242A / UE25CS251A

---

## TABLE OF CONTENTS

### PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS
1. [DLCD - Unit 1 Combined Lecture Slides (255 Pages)](#doc-1) — *Source: `resources/DLCD - Unit 1 Combined Slides.pdf`*
2. [Unit 1 Descriptive Question Bank with Model Solutions (30 Pages)](#doc-2) — *Source: `resources/U1QB_soln.docx`*
3. [Unit 1 Complete 120 Question Bank (19 Pages)](#doc-3) — *Source: `resources/QB.doc`*
4. [Lecture Notes: Problem Solving 1](#doc-4) — *Source: `notes/question1.jpeg`*
5. [Lecture Notes: Sequential Logic & Latches (Part 1)](#doc-5) — *Source: `notes/sequential-1.jpg`*
6. [Lecture Notes: Sequential Logic & Latches (Part 2)](#doc-6) — *Source: `notes/sequential-2.jpg`*

### PART 2: DLCD SYNTHESIZED STUDY PACKAGE (Clean Slides, Question Banks, MCQs)
1. [DLCD_Unit_1_Clean_Slides.md](#res-1)
2. [DLCD_Unit_1_Question_Bank.md](#res-2)
3. [DLCD_Unit_1_MCQs.md](#res-3)

### PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS
1. [01_digital-circuits-introduction.md](#topic-1)
2. [02_boolean-equations.md](#topic-2)
3. [03_logic-minimization-kmaps-3var.md](#topic-3)
4. [04_kmaps-4var-seven-segment.md](#topic-4)
5. [05_combinational-building-blocks.md](#topic-5)
6. [06_sequential-basics-latches.md](#topic-6)
7. [07_flipflops-timing-metastability.md](#topic-7)

---

# PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS

<a id="doc-1"></a>
## Document 1: DLCD - Unit 1 Combined Lecture Slides (255 Pages)
**Source Document**: `resources/DLCD - Unit 1 Combined Slides.pdf`
**OCR Extraction File**: `Resources_DLCD - Unit 1 Combined Slides.txt`

```
================================================================================
ORIGINAL DOCUMENT : DLCD - Unit 1 Combined Slides.pdf
OCR PDF FILE      : Resources_DLCD - Unit 1 Combined Slides_ocr.pdf
TOTAL PAGES       : 255
WORD COUNT        : 20117
CHARACTER COUNT   : 102606
DATE EXTRACTED    : 2026-11-04 14:11:19
================================================================================

--- [Page 1 of 255] ---
PES 
UNIVERSITY 
CeLERATINGLED 
/= 4Rz 
Digital Logic and Computer Design
 Unit1
Combinational and Sequential Logic Design
Topic:Introduction
Team DLCD
         Department of CSE and CSE(AI &ML)

--- [Page 2 of 255] ---
Application 
|>"hello 
Software 
|world!” 
Operating 
Systems 
Architecture 
Micro- 
architecture 
Digital 
Circuits 
L] 
A A 
A 
4 
L] 
Analog 
Circuits 
Devices 
Physics 
PES 
UNIVERSITY 
b ceLcaraTTNGBD V=7 
• Introduction
• Boolean Equations
• Karnaugh maps
• Combinational building Blocks.
• Introduction
• Latches and Flip-Flops
• Synchronous Logic Design
• Finite state Machines
UNIT 1
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN ::

--- [Page 3 of 255] ---
A 
:0 
= T 
5 UN 
A/ 
What is a circuit?
• In digital electronics, a circuit is a network that processes discrete-valued variables. 
• A circuit can be viewed as a black box, shown as in Figure with 
 one or more discrete-valued input terminals 
▶
 one or more discrete-valued output terminals 
▶
 a functional specification describing the relationship between inputs and outputs 
▶
 a timing specification describing the delay between inputs changing and outputs 
▶
responding.
inputs
outputs
functional spec
timing spec
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Introduction

--- [Page 4 of 255] ---
\AA 
~ 
_/ 
v v 
E 
A/ 
• Nodes
• Inputs: A, B, C
• Outputs: Y, Z
• Internal: n1
• Circuit elements
• E1, E2, E3
• Each a circuit
A
E1
E2
E3
B
C
n1
Y
Z
Circuits
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Introduction 
inputs
outputs
functional spec
timing spec

--- [Page 5 of 255] ---
\AA 
:"0 
= T 
5 UN 
A/ 
Types of Digital circuits/logic
• Combinational Logic 
• Memory less
• Outputs determined only by current values of inputs
• Examples:
• Adders,  Multiplexers, Decoders, Encoders,  Comparators
• Sequential Logic
• Has memory
• Outputs determined by previous and current values of inputs
• Examples:
• Registers, Counters, Flip-flops,  Memory devices 
inputs
outputs
functional spec
timing spec
Types of Logic Circuits
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Introduction

--- [Page 6 of 255] ---
:"0 
= M 
3 UN 
Combinational Logic
• A circuit is combinational if it consists of interconnected circuit 
elements such that 
 Every circuit element is itself combinational. 
▶
 Every node of the circuit is either designated as an input to 
▶
the circuit or connects to exactly one output terminal of a 
circuit element. 
 The circuit contains no cyclic paths: every path through the 
▶
circuit visits each circuit node at most once.
Rules of Combinational Composition
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Introduction

--- [Page 7 of 255] ---
@ 
(o 
(9 
mn@w 
Ha. 
-z M 
3 UN 
Rules of Combinational Composition
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Introduction 
Which of the circuits are combinational circuits according to the rules of combinational 
composition?
Circuit (a) is combinational. 
(b) is not combinational, because there is a cyclic path 
starting at n4 passes through the XOR to n5,which returns 
to n4. 
(c) is combinational. 
(d) is not combinational, because node n6 connects to 
the output terminals of both I3 and I4. 
(e)Is combinational, illustrating two combinational circuits 
connected to form a larger combinational circuit. 
(f) does not obey the rules of combinational composition 
because it has a cyclic path through the two elements. 
Depending on the functions of the elements, it may or 
may not be a combinational circuit

--- [Page 8 of 255] ---
E2 
\ 
E3 
> 
Y 
> 
Z 
PES 
UNIVERSITY 
b ceLcanaTINGBD V=75 
Circuits
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Think About it? 
MCQ 1
Correct Answer B 
A designer replaces E2 with a faster implementation that preserves the 
same Boolean function.
Which statement is most accurate?
A. Functional specification changes.
B. Timing specification may improve while functionality remains unchanged.
C. Both functional and timing specifications change.
D. Overall logic becomes sequential.

--- [Page 9 of 255] ---
o 
Ed 
E2 
PE 
UNIVERSITY 
> 
Y 
» Z 
Circuits
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Think About it? 
MCQ 2
Assume:
Delay(E1) = 5 ns
Delay(E2) = 8 ns
Delay(E3) = 4 ns
E3 begins computation only after both E1 and E2 outputs 
become valid.
What is the worst-case propagation delay?
A. 9 ns
B. 12 ns
 Correct Answer: B
Explanation:
Longest input path = 
max(5,8)+4 = 12 ns

--- [Page 10 of 255] ---
PE 
UNIVERSITY 
b ceLcaraTTNGBD V=7 
Circuits
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Think About it? 
MCQ 3
Consider two digital circuits:
Circuit X: Output depends only on current inputs.
Circuit Y: Output depends on previous and current inputs.
Which classification is correct?
A. X is Sequential, Y is Combinational
B. X is Combinational, Y is Sequential
C. Both are Sequential
D. Both are Combinational
Correct Answer B 
X is Combinational, Y is 
Sequential

--- [Page 11 of 255] ---
@ 
PES 
UNIVERSITY 
fCELEaRATING 
ED vE4R=] 
THANK YOU
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 12 of 255] ---
Digital Logic and Computer Design
 Unit1
Combinational and Sequential Logic Design
Topic:Boolean Equations
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 13 of 255] ---
Course Outline
Digital Design
 Combinational logic design
Logic Minimization, K-Maps
 Sequential logic design
Concepts covered
Boolean Formula Terminology
Sum of Products and Product of 
Sums  standard forms
Truth Table to Boolean Formula  
Logic  Circuit
Logic Minimization using Boolean  
Identities
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 14 of 255] ---
• Functional specification of outputs in terms of inputs
• Example:    S     = F(A, B, Cin)
                  
     Cout = F(A, B, Cin) 
A
S
S      = A  B  Cin
Cout  = AB + ACin + BCin
B
Cin
CL
Cout
Boolean Equations
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 15 of 255] ---
PE 
UNIVERSITY 
b ceLcaraTTNGBD V=7 
Terminology
• Complement: variable with a bar over it
    A’, B’,   C’
• Literal: variable or its complement
    A, A’, B, B’, C, C’
• Implicant: product of literals
    ABC, A’C, BC’
• Minterm: product that includes all input variables
A’B’C’, AB’C,ABC
• Maxterm: sum that includes all input variables
    (A+B+C’), (A+B’+C), (A’+B’+C’)
Some Definitions
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 16 of 255] ---
5@ 
Literal Boolean variable or its complement (ex:c’) 
Product (or implicant) AND of two or  more literals (ex: abc’) 
Minterm Product involving all inputs to  Boolean function
a
b
c
minterm
name
0
0
0
a’b’c’
m0
0
0
1
a’b’c
m1
0
1
0
a’bc’
m2
0
1
1
a’bc
m3
1
0
0
ab’c’
m4
1
0
1
ab’c
m5
1
1
0
abc’
m6
Minterms for three inputs a, b and c
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Formula Terminology

--- [Page 17 of 255] ---
c "0 
iU 
Sum OR of two or more literals
Maxterm Sum involving all inputs to  Boolean function
a
b
c
maxterm
Name
0
0
0
a+b+c
M0
0
0
1
a+b+c’
M1
0
1
0
a+b’+c
M2
0
1
1
a+b’+c’
M3
1
0
0
a’+b+c
M4
1
0
1
a’+b+c’
M5
1
1
0
a’+b’+c
M6
1
1
1
a’+b’+c’
Maxterms for three inputs a, 
b and c
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Formula Terminology

--- [Page 18 of 255] ---
PE 
UNIVERSITY 
fc.conurmin v1is 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
From Truth Table to Boolean Formula and its Minimization
Given a combinational logic circuit or Boolean formula, we have learnt to 
construct  its truth table
But, given a truth table, how to construct a Boolean formula (or combinational 
logic  circuit) for it?
Also, as there are multiple Boolean formulas / logic circuits for each truth table, 
how  to pick the minimal one?
Above problem is called logic minimization
many metrics: smallest, fastest, least power consumption
our metric: smallest two level Sum of Products formula
may be more than one solution

--- [Page 19 of 255] ---
PES 
UNIVERSITY 
TR 
Y = F(A, B) =
• All equations can be written in SOP form
• Each row has a minterm
• A minterm is a product (AND) of literals
• Each minterm is TRUE for that row (and only that row)
• Form function by ORing minterms where the output is TRUE 
• Thus, a sum (OR) of products (AND terms)
Sum-of-Products (SOP) Form
A
B
Y
0
0
0
1
1
0
1
1
0
1
0
1
minterm
A B
A B
A B
A B
minterm
name
m0
m1
m2
m3
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations 
Sum of Products Form

--- [Page 20 of 255] ---
~ 
| 
| 
| 
| 
: "0 
3 UN 
Sum-of-Products Form
Y = F(A, B) =
Sum-of-Products (SOP) Form
• All equations can be written in SOP form
• Each row has a minterm
• A minterm is a product (AND) of literals
• Each minterm is TRUE for that row (and only that row)
• Form function by ORing minterms where the output is TRUE 
• Thus, a sum (OR) of products (AND terms)
A
B
Y
0
0
0
1
1
0
1
1
0
1
0
1
minterm
A B
A B
A B
A B
minterm
name
m0
m1
m2
m3
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations 
Sum of Products Form

--- [Page 21 of 255] ---
Y ) 
2 
Sum-of-Products Form
Y = F(A, B) = A’B + AB = Σ(1, 3)
Sum-of-Products (SOP) Form
• All equations can be written in SOP form
• Each row has a minterm
• A minterm is a product (AND) of literals
• Each minterm is TRUE for that row (and only that row)
• Form function by ORing minterms where the output is TRUE 
• Thus, a sum (OR) of products (AND terms)
A
B
Y
0
0
0
1
1
0
1
1
0
1
0
1
minterm
A B
A B
A B
A B
minterm
name
m0
m1
m2
m3
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations 
Sum of Products Form

--- [Page 22 of 255] ---
& 
PES 
UNIVERSITY 
e 
s 
oo o 
= o~ oly 
oooPlm 
Figure 210 Ben’s truth table 
Sum of Products Form
Ben Bitdiddle is having a picnic. He won’t enjoy it if it rains or if 
there are ants.Design a circuit that will output TRUE only if Ben 
enjoys the picnic
Solution:First define the inputs and outputs. The inputs are A and R, 
which indicate if there are ants and if it rains. A is TRUE when there 
are ants and FALSEwhen there are no ants. 
Likewise, R is TRUE when it rains and FALSE when the sun smiles on 
Ben. The output is E, Ben’s enjoyment of the picnic. E is TRUE
if Ben enjoys the picnic and FALSE if he suffers. 
Using sum-of-products form, we write the equation as: E = A’R’  or
 E = Σ0
Boolean Equations Example
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 23 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Formula using Sum of Products (SOP)
SOP Form
Sum of all minterms corresponding to a 1 output
SOP Example
Truth table:
a
b
c
y
minterm
name
0
0
0
0
a’b’c’
m0
0
0
1
0
a’b’c
m1
0
1
0
0
a’bc’
m2
0
1
1
1
a’bc
m3
1
0
0
1
ab’c’
m4
1
0
1
0
ab’c
m5
1
1
0
1
abc’
m6
1
1
1
1
abc
m7
SOP form Boolean formula:
y  = a’bc + ab’c’ + abc’ + abc  
y  = m3 + m4 + m6 + m7
Sigma (Σ) notation:
y  = Σ(m3, m4, m6, m7)
y  = Σ(3, 4, 6, 7)
If the Boolean function is called f :
y  = f (a, b, c)

--- [Page 24 of 255] ---
SN 
HHHHHHHHH 
) 
Y = F(A, B) = (A + B)(A’ + B) = Π(0, 2)
• All Boolean equations can be written in POS form
• Each row has a maxterm
• A maxterm is a sum (OR) of literals
• Each maxterm is FALSE for that row (and only that row)
• Form function by ANDing the maxterms for which the output is 
FALSE
• Thus, a product (AND) of sums (OR terms)
Product-of-Sums (POS) Form
A + B
A
B
Y
0
0
0
1
1
0
1
1
0
1
0
1
maxterm
A + B
A + B
A + B
maxterm
name
M0
M1
M2
M3
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations 
 Product of Sums Form

--- [Page 25 of 255] ---
5@ 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Formula using Products of Sum (POS)
a
b
c
y
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
0
1
0
1
1
0
1
1
1
1
1
POS Form
Product of all maxterms corresponding to a 0 output
POS Example

--- [Page 26 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Formula using Products of Sum (POS)
POS Form
Product of all maxterms corresponding to a 0 output
POS Example
Truth 
table:
a
b
c
y
maxterm
name
0
0
0
0
a+b+c
M0
0
0
1
0
a+b+c’
M1
0
1
0
0
a+b’+c
M2
0
1
1
1
a+b’+c’
M3
1
0
0
1
a’+b+c
M4
1
0
1
0
a’+b+c’
M5
1
1
0
1
a’+b’+c
SOP form Boolean formula:
y  = (a +b +c)(a +b +c’)
(a +b’+c)(a’+b +c’)
y = M0M1M2M5

--- [Page 27 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Formula using Products of Sum (POS)
POS Form
Product of all maxterms corresponding to a 0 output
POS Example
Truth 
table:
a
b
c
y
maxterm
name
0
0
0
0
a+b+c
M0
0
0
1
0
a+b+c’
M1
0
1
0
0
a+b’+c
M2
0
1
1
1
a+b’+c’
M3
1
0
0
1
a’+b+c
M4
1
0
1
0
a’+b+c’
M5
1
1
0
1
a’+b’+c
SOP form Boolean formula:
y  = (a +b +c)(a +b+c’)(a +b’ 
+c)(a’ +b +c’)
y = M0M1M2M5
Pi (Π) notation:
y  = Π(M0M1M2M5)
y  = (
Π 0, 1, 2, 5)

--- [Page 28 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Formula using Products of Sum (POS)
POS Form
Product of all maxterms corresponding to a 0 output
POS Example
Truth 
table:
a
b
c
y
maxterm
name
0
0
0
0
a+b+c
M0
0
0
1
0
a+b+c’
M1
0
1
0
0
a+b’+c
M2
0
1
1
1
a+b’+c’
M3
1
0
0
1
a’+b+c
M4
1
0
1
0
a’+b+c’
M5
1
1
0
1
a’+b’+c
If the Boolean function is called f :
y  = f (a, b, c)
SOP form Boolean formula:
y  = (a +b +c)(a +b+c’)(a +b’ 
+c)(a’ +b +c’)
y = M0M1M2M5
Pi (Π) notation:
y  = Π(M0M1M2M5)
y  = (
Π 0, 1, 2, 5)

--- [Page 29 of 255] ---
HHHHHHHHH 
• You are going to the cafeteria for lunch
• You won’t eat lunch (E) 
• If it’s not open (O) or
• If they only serve corndogs (C)
• Write a truth table for determining if you will eat lunch (E).
O
C
E
0
0
0
1
1
0
1
1
Boolean Equations Example
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 30 of 255] ---
HHHHHHHHH 
• You are going to the cafeteria for lunch
• You won’t eat lunch (E) 
• If it’s not open (O) or
• If they only serve corndogs (C)
• Write a truth table for determining if you will eat lunch (E).
O
C
E
0
0
0
1
1
0
1
1
0
0
1
0
Boolean Equations Example
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 31 of 255] ---
‘»n 
• SOP – sum-of-products
• POS – product-of-sums
O + C
O
C
E
0
0
0
1
1
0
1
1
0
0
1
0
maxterm
O + C
O + C
O + C
O
C
E
0
0
0
1
1
0
1
1
0
0
1
0
minterm
O C
O C
O C
O C
E = (O + C)(O + C)(O + C)
   = Π(0, 1, 3)
E = OC
   = Σ(2)
SOP & POS Form
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations 
SOP & POS Form

--- [Page 32 of 255] ---
PE 
UNIVERSITY 
b ceLcaraTTNGBD V=7 
SOP & POS Form
• SOP – sum-of-products
• POS – product-of-sums
O
C
E
0
0
0
1
1
0
1
1
minterm
O C
O C
O C
O C
O + C
O
C
E
0
0
0
1
1
0
1
1
maxterm
O + C
O + C
O + C
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 33 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Logic Minimization
Logic Minimization 
Example
Minimize:
y  = a’bc + ab’c’ + 
abc’ + abc

--- [Page 34 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Logic Minimization
Logic Minimization Example
Minimize:
y  = a’bc + ab’c’ + abc’ + abc
Using distributive law:
y  = bc(a’ + a) + ac’(b’ + b)
Using complement law:
y  = bc(1) + ac’(1)
Using identity law:
y  = bc + ac’
The three representations below are different ways of  
specifying the same Boolean function:
ac’+ b c
c
b
a
a
b
c
y
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
0
1
0
1
1
0
1
1
1
1
1

--- [Page 35 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Logic Minimization
Logic Minimization Example
1
Minimize:
2
y  = a’bc + abc’ + abc’ + abc
Using distributive law:
y  = bc(a’+ a) + ac’(b’ + b)
Using complement law:
y  = bc(1) + ac’(1)
Using identity law:
y  = bc + ac’
The three representations below are different ways of 
 specifying the same Boolean function:
a · c + b · c
c
b
a
a
b
c
y
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
0
1
0
1
1
0
1
1
1
1
1

--- [Page 36 of 255] ---
PE 
UNIVERSITY 
fceLesrATINGED =1 
1.What is a " minterm" in Boolean algebra?
 A) A sum of two or more literals
 B) A product (AND) involving all inputs to the Boolean function
 C) Any single literal
D) A product involving only some inputs
 
Correct Answer B 
MCQ 1
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 37 of 255] ---
2. In Product-of-Sums (POS) form, how is a Boolean formula constructed?
 A) Sum of all minterms corresponding to a 1 output
 B) Product of all maxterms corresponding to a 0 output
 C) Product of all minterms corresponding to a 1 output
 D) Sum of all maxterms corresponding to a 0 output
MCQ 2
Correct Answer B
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 38 of 255] ---
PE 
UNIVERSITY 
b ceLcaraTTNGBD V=7 
Circuits
A Boolean function has four inputs and is TRUE only for 
m(3,7,11,15)
Which characteristic do these minterms share?
A. A=1
B. D=1
C. C=0
D. B=1
Correct Answer B
(Each binary 
representation ends with 
D = 1.) 
MCQ 3
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 39 of 255] ---
Logic Circuit Example 
Draw the logic circuit diagram for: 
y =abc+abc +abc+ abc 
Equivalence Example 
Prove that: bc+ ac+ ab = bc+ ac 
Hint: bc 
+ ac 
+ ab(c 
+ T) 
Minimization Example 
Minimize: 
y =(a+b+c)la+b+C)a+b+c)(a+b+cC) 
Hint: 
y=(ala+b+c)+bla+b+C)+cla+b+T¢C)) 
(ala+b+cC)+bla+b+C)+cla+b+7C)) 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Boolean Equations

--- [Page 40 of 255] ---
THANK YOU
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 41 of 255] ---
DIGITAL LOGIC AND  
COMPUTER DESIGN
Karnaugh Maps 
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 42 of 255] ---
& 
PES 
UNIVERSITY 
oA 
DIGITAL LOGIC AND  COMPUTER DESIGN
Karnaugh Maps
Department of CSE and CSE(AI &ML)

--- [Page 43 of 255] ---
Karnaugh Maps- Three Input
Why use K-Maps? 
a
b
c
y
minterm
name
0
0
0
0
a’b’c’
m0
0
0
1
0
a’b’c
m1
0
1
0
0
a’bc’
m2
0
1
1
1
a’bc
m3
1
0
0
1
ab’c’
m4
1
0
1
0
ab’c
m5
1
1
0
1
abc’
m6
1
1
1
1
abc
m7
Example 1
SOP form:
y  = a’bc+ ab’c’ + abc’+ abc
Minimized form:
y  = bc + ac’
Minimization requires:
 Combining implicants on row 3 and 7
 Combining implicants on row 4 and 6
 Takes some effort to determine implicants  
to combine

--- [Page 44 of 255] ---
k_ 
a
b
c
y
minterm
name
0
0
0
0
a’b’c’
m0
0
0
1
0
a’b’c
m1
0
1
0
0
a’bc’
m2
0
1
1
1
a’bc
m3
1
0
0
1
ab’c’
m4
1
0
1
0
ab’c
m5
1
1
0
1
abc’
m6
1
1
1
1
abc
m7
Example 1
SOP form:
y  = a’bc + ab’c’ + abc’+ abc
Minimized form:
y  = bc + ac’
Minimization requires:
Combining implicants on row 3 and 7
Combining implicants on row 4 and 6
Takes some effort to determine implicants  to 
combine
Minimizing:
y  = bc + ac’ + ab
Requires converting to:
bc + ac’ + ab(c + c’)
Minimization may require: 
Unintuitve steps
Trial and error
So minimization with Boolean identities is important to know since useful in some cases, but difficult to use in general
Karnaugh Maps- Three input
Why use K-Maps?

--- [Page 45 of 255] ---
PES 
UNIVERSITY 
NS TR 
Karnaugh Maps- Three input
K-Map Structure
Kanaugh Map (K-Map)
Maurice Karnaugh’s refinement in  
1953 of original idea from 1881
Key idea: Minterms that differ in  
one literal must be adjacent
Utilize brain’s visual processing for  
efficient logic minimization
a
b
c
y
minterm
0
0
0
0
a’b’c’
0
0
1
0
a’b’c
0
1
0
0
a’bc’
0
1
1
1
a’bc
1
0
0
1
ab’c’
1
0
1
0
ab’c
1
1
0
1
abc’
1
1
1
1
abc
K-Map Structure (three input Boolean functon)
bc
a
00
    01        
11                 10   
10
0
1
a’b’c’  0
a’b’c  1 a’bc  3
a’bc’2
ab’c’4
ab’c5
           
abc
7
abc’
6
Each square corresponds to a row of the truth table  
Any two adjacent squares differ only in one literal  
Achieved using two rows and binary order 00,01,11,10
Notion of “wrap-around”: far left and right squares are  
adjacent

--- [Page 46 of 255] ---
Karnaugh Maps- Three input
K-Map Structure
Kanaugh Map (K-Map)
Maurice Karnaugh’s refinement in  
1953 of original idea from 1881
Key idea: Minterms that differ in  
one literal must be adjacent
Utilize brain’s visual processing for  
efficient logic minimization
a
b
c
y
minterm
0
0
0
0
a’b’c’
0
0
1
0
a’b’c
0
1
0
0
a’bc’
0
1
1
1
a’bc
1
0
0
1
ab’c’
1
0
1
0
ab’c
1
1
0
1
abc’
1
1
1
1
abc
K-Map Structure (three input Boolean functon)
bc
a
00
01
11
10
0
1
0
0
1
0
0
1
3
2
1
0
1
1
4
5
7
6
Each square corresponds to a row of the truth table  
Any two adjacent squares differ only in one literal  
Achieved using two rows and binary order 00,01,11,10
Notion of “wrap-around”: far left and right squares are  
adjacent

--- [Page 47 of 255] ---
Karnaugh Maps- Three input
K-Map Method
K-Map Implicants
Implicant
 K-Map area composed of squares containing 1’s
 Area is square or rectangular (wraparound allowed)
 No. of squares in area is a power of two (1, 2, 4, . . .)
       Each implicant corresponds to a product of literals
 Double the area, one less literal
Prime implicant
 Implicant having largest number of squares obeying  
above rules
Essential prime implicant
 Prime implicant containing a square not in any other  
prime implicant
K-Map Method
Include all required prime  
implicants
 Include all essential prime  
implicants
 Include other prime implicants  
such that:
 Each square containing 1 is  
covered
 Boolean formula is minimal
(may not be unique)
Convert required implicants to  
Boolean formula
 Each implicant is a product of  
literals
 Include literals which do not
change over its area

--- [Page 48 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps- Three input
MCQs
1. Why are K-Map rows/columns arranged in the order 00, 01, 11, 10 
rather than 00, 01, 10, 11?
 A) To make the K-Map easier to draw
 B) So that any two adjacent squares differ in exactly one literal, 
matching the key K-Map principle
 C) Because it matches decimal counting order
 D) It's arbitrary, with no particular reason
Correct Answer 
Option B

--- [Page 49 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps- Three input
MCQs
2. What does "wrap-around" mean in a K-Map?
 A) The far left and right (and, for larger maps, top and bottom) squares 
are considered adjacent
 B) The K-Map can be rotated 90 degrees
 C) Squares in different rows are never adjacent
 D) Wrap-around only applies when using POS form
Correct Answer 
Option A

--- [Page 50 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps- Three input
MCQs
3. What defines a "prime implicant" in K-Map minimization?
 A) Any implicant containing exactly one square
 B) An implicant that is the largest possible grouping of adjacent 1s 
(can't be enlarged further while following the rules)
 C) An implicant found only using Boolean algebra
 D) An implicant covering all squares in the K-Map
Correct Answer 
Option B

--- [Page 51 of 255] ---
D—‘!—‘OI—‘I—‘OOO. 
= 
=R O&) O (& 
== 0 0 =M= 
O 
_HOMEORMROMO 
abc 
abc 
abc 
abc 
abc 
abc 
abc 
abc 
PES 
UNIVERSITY 
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
0
0 0
1 1
3 0
2
1
4 0
5 1
7 1
6
bc00    01    11   10

--- [Page 52 of 255] ---
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
0
0 0
1 1
3 0
2
1
4 0
5 1
7 1
6
bc00    01    11   10

--- [Page 53 of 255] ---
IIIIIIIIII 
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
0 0
1 1
3 0
2
1
4 0
5 1
7 1
6
0
1
bc00    01    11   10

--- [Page 54 of 255] ---
IIIIIIIIII 
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
2
3
0
0
Three prime implicants
bc00    01    11   10
0     0     1     0
1     0     1     1

--- [Page 55 of 255] ---
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
2
3
4
5
6
7
0
Three prime implicants
bc00    01    11   10
1
0     0     1     0
1     0     1     1

--- [Page 56 of 255] ---
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
2
3
4
5
6
7
0
Three prime implicants
Two essential prime implicants
bc00    01    11   10
1
0     0     1     0
1     0     1     1

--- [Page 57 of 255] ---
I;I—fll% 
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
2
3
4
5
6
7
Three prime implicants
Two essential prime implicants
bc00    01    11   10
0    0     0     1     0
1    1     0     1     1

--- [Page 58 of 255] ---
I;]—%l]—q 
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
2
3
4
5
6
7
Three prime implicants
Two essential prime implicants  
Required prime implicants: bc,ac’
bc00    01    11   10
0    0     0     1     0
1    1     0     1     1

--- [Page 59 of 255] ---
I:]—Pl]—q 
Karnaugh Maps- Three input
K-Map Example 1
Prime implicants: green colour
Essential prime implicants: blue 
 colour
Required prime implicants: dark 
 red colour
a
0
1
2
3
4
5
6
7
Three prime implicants
Two essential prime implicants  
Required prime implicants: bc, ac’
 Boolean formula:
f (a, b, c) = ac’ + bc
bc00    01    11   10
0    0     0     1     0
1    1     0     1     1

--- [Page 60 of 255] ---
Karnaugh Maps- Three input
K-Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
Truth table

--- [Page 61 of 255] ---
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
0 1
1 1
3 0
2
1
4 1
5 1
7 1
6
Truth table
bc00    01    11   10

--- [Page 62 of 255] ---
IIIIIIIIII 
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
a
0
1
6
0
0 1
1 1
3 0
2
1 4 1 5 1 7 1
Truth table
bc00    01    11   10

--- [Page 63 of 255] ---
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
Two prime implicants
Truth table
a
0
1
0
0 1
1 1
3 0
2
1
4 1
5 1
7 1
6
bc00    01    11   10

--- [Page 64 of 255] ---
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
Two prime implicants
Truth table
a
0
1
0
0 1
1 1
3 0
2
1
4 1
5 1
7 1
6
bc00    01    11   10

--- [Page 65 of 255] ---
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
Truth table
Two prime implicants
a
0
1
0
0 1
1 1
3 0
2
1
4 1
5 1
7 1
6
bc00    01    11   10

--- [Page 66 of 255] ---
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
Truth table
Two prime implicants
a
0
1
0
0 1
1 1
3 0
2
1
4 1
5 1
7 1
6
bc00    01    11   10
Two essential prime implicants

--- [Page 67 of 255] ---
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
Truth table
Two prime implicants
Two essential prime implicants
Two required prime implicants: c, a
a
0
1
0
0 1
1 1
3 0
2
1
4 1
5 1
7 1
6
bc00    01    11   10

--- [Page 68 of 255] ---
Karnaugh Maps- Three input
K Map Example 2
K-Map Minimization 
Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
0
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
0
1
1
1
1
0
1
1
1
1
1
Truth table
Minimal Boolean formula:
f (a, b, c) = c + a
Two prime implicants
Two essential prime implicants
Two required prime implicants: c, a
a
0
1
0
0 1
1 1
3 0
2
1
4 1
5 1
7 1
6
bc00    01    11   10

--- [Page 69 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
Truth table

--- [Page 70 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
Truth table
0
1
0
1
0
1
0
1
1
1
bc00    01    11   10

--- [Page 71 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization 
Example a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
1
0
1
0
1
1
1
Truth table
bc00    01    11   10

--- [Page 72 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization 
Example a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
bc00    01    11   10
0
1
0
1
0
1
0
1
1
1
Truth table

--- [Page 73 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
1
0
1
0
1
1
1
Truth table
bc00    01    11   10

--- [Page 74 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
1
0
1
0
1
1
1
Truth table
bc00    01    11   10

--- [Page 75 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
1
1
0
0
1
1
1
Four prime implicants
Truth table
bc00    01    11   10

--- [Page 76 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
1
1
0
0
1
1
1
Four prime implicants
Truth table
bc00    01    11   10

--- [Page 77 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization Example
a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
1
1
0
0
1
1
1
Four prime implicants
Truth table
bc00    01    11   10

--- [Page 78 of 255] ---
Karnaugh Three input
K Map Example 3
K-Map Minimization 
Example a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
a
0
1
0
1
1
0
0
1
1
1
Four prime implicants
Two essential prime 
implicants
Truth table
bc00    01    11   10

--- [Page 79 of 255] ---
Karnaugh Maps- Three input
K Map Example 3
K-Map Minimization 
Example a
b
c
y
0
0
0
0
0
0
1
1
0
1
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
1
0
1
1
1
1
0
1
1
1
1
1
Truth table
a
0
1
0
1
1
0
0
1
1
1
Four prime implicants
Two essential prime implicants
Three required prime implicants: b’c, bc’ along with either
ca or ab
Minimal Boolean formulas: 
 f (a, b, c) = b’c+ bc’+ ab
f (a, b, c) = b’c+ bc’+ac
bc00    01    11   10

--- [Page 80 of 255] ---
0 
11 
10 
0 
1 
1 
0 
0 
1 
01]0 
PES 
UNIVERSITY 
N TR 
Karnaugh Maps- Three input
K Map Example 4
K-Map Minimization 
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
0
Truth table

--- [Page 81 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
0
1
2
3

--- [Page 82 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
1
0 0
1
1
2 1
3

--- [Page 83 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
1
0 0
1
1
2 1
3

--- [Page 84 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
2
3
0
1
01
1
1
Two prime implicants

--- [Page 85 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
2
3
0
1
01
1
1
Two prime implicants

--- [Page 86 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
2
3
0
1
01
1
1
Two prime implicants 
 Two essential prime
implicants

--- [Page 87 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
2
3
0
1
01
1
1
Two prime implicants 
 Two essential prime
implicants

--- [Page 88 of 255] ---
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
2
3
0
1
01
1
1
Two prime implicants 
 Two essential prime
implicants
Two required prime 
 implicants

--- [Page 89 of 255] ---
o= 
IVERSITY 
o 
= 
= 
= 
E 
9HaA® 
Karnaugh Maps-Two input
K-Map Example 1
K-Map Example (two inputs)
a
b
y
0
0
1
0
1
0
1
0
1
1
1
1
Two Input Truth Table
b
a
0
1
0
1
2
3
0
1
01
1
1
Two prime implicants 
 Two essential prime
implicants
Two required prime 
 implicants
Minimized Boolean 
 formula:
f (a, b, c, d ) = b + 
a

--- [Page 90 of 255] ---
Karnaugh Maps- Three input
Think About It
Minimize using K-Maps
1. f (a, b, c) = Σ(0, 3, 5)
2. f (a, b, c) = Σ(0, 1, 2, 4, 5, 6)
3. f (a, b, c) = Σ(0, 2, 3, 4, 6, 7)
All prime implicants and essential prime implicants shown for clarity, okay to 
directly  mark required prime implicants on K-Map

--- [Page 91 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps- Three input
MCQs
1. In a worked example with three prime implicants where two are 
essential, what determines which prime implicants are included in the 
final formula?
 A) All prime implicants must always be included regardless of overlap
 B) The essential prime implicants must be included (to cover their 
unique squares), plus any additional prime implicants needed to cover 
remaining 1s
 C) Only the prime implicant with the fewest literals is used
 D) Required prime implicants are chosen randomly
Correct Answer 
Option B

--- [Page 92 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps- Three input
MCQs
2. One example shows the minimal formula can be written as either f = 
bc' + b'c + ca or f = bc' + b'c + ab. What does this illustrate?
 A) K-Maps always produce a unique minimal solution
 B) The minimal SOP solution isn't always unique - different valid 
choices of non-essential prime implicants can give equally minimal 
formulas
 C) POS form is always required in such cases
 D) The K-Map method fails when there are multiple prime implicants
Correct Answer 
Option B

--- [Page 93 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps- Three input
MCQs
3. Regarding marking prime implicants, essential prime implicants, and 
required prime implicants on a K-Map, what does the slide note?
 A) All three must always be marked with different colors in every 
solution
 B) It's acceptable to skip marking all prime implicants and essential 
prime implicants separately, and directly mark just the required prime 
implicants
 C) Only maxterms need to be marked
 D) None of them need to be marked; only the final formula matters
Correct Answer 
Option B

--- [Page 94 of 255] ---
PES 
UNIVERSITY 
frceconariies 
sy 
Karnaugh Maps-Four Inputs
K-Map Structure (four inputs)
K-Map Structure (four input Boolean function)
a
b
c
d
y
Minterm
0
0
0
0
1
a’b’c’d’
0
0
0
1
0
a’b’c’d
0
0
1
0
1
a’b’cd’
0
0
1
1
0
a’b’cd
0
1
0
0
0
a’bc’d’
0
1
0
1
1
a’bc’d
0
1
1
0
0
a’bcd’
0
1
1
1
1
a’bcd
1
0
0
0
1
ab’c’d’
1
0
0
1
0
ab’c’d
1
0
1
0
1
ab’cd’
1
0
1
1
0
ab’cd
1
1
0
0
0
abc’d’
1
1
0
1
1
abc’d
1
1
1
0
0
abcd’
1
1
1
1
1
abcd
ab
cd
00
     01       11           10
00
01
11
10
a’b’c’d’
0
a’b’c’d
1
a’b’cd
3
a’b’cd’
2
a’bc’d’    
4
a’bc’d
5
a’bcd
7 a’bcd’
6
abc’d’
12
abc’d
           13
abcd
15
abcd’
        14
ab’c’d’
8
ab’c’d
9
ab’cd
11
ab’cd’
10
Each square corresponds 
 to a row of the truth  
table
Any two adjacent  
squares differ only in 
 one literal
Columns as well as rows
 arranged in binary order
 00,01,11,10
Notion of “wrap-around”
Far left and right squares 
are adjacent
Top and bottom squares 
are also adjacent
Four Input Truth Table

--- [Page 95 of 255] ---
Karnaugh Maps-Four Inputs
K-Map Structure (four inputs)
K-Map Structure (four input Boolean function)
ab
cd
00
01
11
10
00
01
11
10
1
0
0
1
0
3
1
2
0
4
1
5
1
7
0
6
0
12
1
13
1
15
0
14
1
8
0
9
0
11
1
10
Each square corresponds 
 to a row of the truth  
table
Any two adjacent  
squares differ only in 
 one literal
Columns as well as rows arranged in binary order 00,01,11,10
Notion of “wrap-around”
Four Input Truth Table
Far left and right squares are adjacent
Top and bottom squares are also adjacent
a
b
c
d
y
Minterm
0
0
0
0
1
a’b’c’d’
0
0
0
1
0
a’b’c’d
0
0
1
0
1
a’b’cd’
0
0
1
1
0
a’b’cd
0
1
0
0
0
a’bc’d’
0
1
0
1
1
a’bc’d
0
1
1
0
0
a’bcd’
0
1
1
1
1
a’bcd
1
0
0
0
1
ab’c’d’
1
0
0
1
0
ab’c’d
1
0
1
0
1
ab’cd’
1
0
1
1
0
ab’cd
1
1
0
0
0
abc’d’
1
1
0
1
1
abc’d
1
1
1
0
0
abcd’
1
1
1
1
1
abcd

--- [Page 96 of 255] ---
Karnaugh Maps-Four Inputs
K-Map Example 1 (four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
cd
Four Input Truth Table
00
01
11
10
ab
00
01
11
10
1
0
0
1
0
3
1
2
0
4
1
5
1
7
0
6
0
12
1
13
1
15
0
14
1
8
0
9
0
11
1
10

--- [Page 97 of 255] ---
Karnaugh Maps-Four Inputs 
K-Map Example 1(four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
cd 00
01
11
10
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
ab
00
1
0
1
0
01
0
1
0
1
10
1
0
1
0
11
0
1
0
1
Four Input Truth Table

--- [Page 98 of 255] ---
Karnaugh Maps-Four Inputs
K-Map Example 1 (four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
cd 00
01
11
10
0
1
2
3
4
5
6
7
12
13
14
15
ab
00
1
0
1
0
01
0
1
0
1
10
1
0
1
0
11
0
1
0
1
Two prime 
 implicants
8
9
11
10
Four Input Truth Table

--- [Page 99 of 255] ---
Karnaugh Maps-Four Inputs
K-Map Example 1 (four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
cd 00
01
11
10
0
1
2
3
4
5
6
7
12
13
14
15
ab
00
1
0
1
0
01
0
1
0
1
10
1
0
1
0
11
0
1
0
1
Two prime 
 implicants
8
9
11
10
Four Input Truth Table

--- [Page 100 of 255] ---
Karnaugh Maps-Four Inputs 
K-Map Example 1(four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
cd 00
01
11
10
0
1
2
3
4
5
6
7
12
13
14
15
ab
00
1
0
1
0
01
0
1
0
1
10
1
0
1
0
11
0
1
0
1
Two prime 
 implicants
Two essential prime 
 implicants
8
9
11
10
Four Input Truth Table

--- [Page 101 of 255] ---
Karnaugh Maps-Four Inputs 
K-Map Example 1(four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
cd 00
01
11
10
0
1
2
3
4
5
6
7
12
13
14
15
ab
00
1
0
1
0
01
0
1
0
1
10
1
0
1
0
11
0
1
0
1
Two prime 
 implicants
Two essential prime 
 implicants
8
9
11
10
Four Input Truth Table

--- [Page 102 of 255] ---
Karnaugh Maps-Four Inputs
K-Map Example 1 (four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
cd 00
01
11
10
0
1
2
3
12
13
14
15
ab
00
1
0
1
0
01
0
4
1
5
0
6
1
7
10
1
0
1
0
11
0
1
0
1
Two prime 
 implicants
Two essential prime 
 implicants
Two required prime 
 implicants: bd , 
b’d’
8
9
11
10
Four Input Truth Table

--- [Page 103 of 255] ---
Karnaugh Maps-Four Inputs 
K-Map Example 1 (four inputs)
K-Map Example (four inputs)
a
b
c
d
y
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
1
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
1
1
1
0
0
1
0
1
0
1
0
1
1
0
1
0
0
1
1
0
1
0
1
1
0
1
1
1
1
1
1
0
1
1
1
1
1
Four Input Truth Table
cd 00
01
11
10
0
1
2
3
8
9
10
11
12
13
14
15
ab
00
1
0
1
0
01
0
4
1
5
0
6
1
7
10
1
0
1
0
11
0
1
0
1
Two prime 
 implicants
Two essential prime 
 implicants
Two required prime 
 implicants: bd , 
b’d’
Minimized Boolean 
 formula:
f (a, b, c, d ) =
bd + b’d’

--- [Page 104 of 255] ---
PES 
UNIVERSITY 
- 
0010 
0o11 
0100 
0101 
0110 
o111 
1000 
1001 
others 
DA 
Karnaugh Maps-Four Inputs 
K-Map Example 2
A seven-segment display decoder 
takes a 4-bit data input D3:0 and 
produces seven outputs to control 
light-emitting diodes to display a 
digit from 0 to 9. The seven outputs 
are often called segments a through 
g, or Sa–Sg, as defined in Figure. The 
digits are shown.
Write a truth table for the outputs, 
and use K-maps to find Boolean 
equations for outputs Sa and Sb. 
Assume that illegal input values (10–
15) produce a blank readout.

--- [Page 105 of 255] ---
& 
PES 
UNIVERSITY 
DD TED 
0,00, 
:}We 
L) 
N 
0 
1 
theof 
o 
D;D,D, 
[ 
[ 
0 
10/ 
1 
0 
0 
0 
== i/ 
[ 
[ 
§,0D101+ D00+ 00,04+ D201y 
Syn DyDy 030+ D00y DD 
Sy=DaDy 
+ DaD,Dg + DaD,D; 
+ DaD,0 
O 
) 
I 
ul 
it 
Karnaugh Maps-Four Inputs 
K-Map Example 2
Sa = D3’ D1+ D3' D2D0 +  D2’D1’ D0’ + D3 D2' D1'
Sb = D3' D2' + D2' D1' + D3' D1 D0 + D3' D1' D0’
 Sc = D3' D0 + D3' D2 + D2' D1'
Sd = D3' D2' D1 + D3' D2 D1’ D0+D2’D1’D0’+D3’D1D0
Se = D3' D1 D0' + D2' D1' D0’
Sf = D3' D2 D0' + D3' D2 D1' + D3 D2' D1' + D3' D1' D0’
Sg = D3' D1 D0' + D3' D2' D1 + D3' D2 D1' + D3 D2' D1'

--- [Page 106 of 255] ---
—_ 
—_ 
—_— 
Karnaugh Maps-(Don’t Cares)
Example  1(Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
0
bc
a
00
01
11
10
1
1
0
0
1
1
0
1
0
1
Truth table

--- [Page 107 of 255] ---
PES 
—_ 
—_ 
—_— 
UNIVERSITY 
e coraniino v<.ns 
CaseD:y 
=b + d 
oyl 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
0
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
0
Truth table

--- [Page 108 of 255] ---
PES 
—_ 
— 
—_— 
UNIVERSITY 
e coraniino v<.ns 
Case:y 
= b+¢ta 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
1
bc
a
00
01
11
10
1
1
0
0
1
1
1
1
0
1
Truth table

--- [Page 109 of 255] ---
PES 
UNIVERSITY 
e coraniino v<.ns 
—_ 
— 
— 
—_— 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
1
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
1
Truth table

--- [Page 110 of 255] ---
—_ 
—_ 
—_— 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
1
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
1
Case 1: y = b’ +a
Truth table

--- [Page 111 of 255] ---
PES 
—_ 
—_ 
—_— 
UNIVERSITY 
e coraniino v<.ns 
Case0:y=b+ca 
Casel:y=hb +a 
Either O or 1 canresultin smaller formula 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
1
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
1
Truth table

--- [Page 112 of 255] ---
PES 
—_ 
—_ 
—_— 
UNIVERSITY 
e coraniino v<.ns 
Case0:y 
= b +ca 
Casel:y=b+a 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
1
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
1
Truth table

--- [Page 113 of 255] ---
—_ 
— 
— 
R — 
Case 0:y = b +¢a 
Casel:y=b+a 
Either 0 or 1 can result in smaller formula 
So initially write X in truth table and K-Map 
PES 
UNIVERSITY 
DD TED 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
X
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
X
Truth table

--- [Page 114 of 255] ---
PES 
UNIVERSITY 
—_ 
— 
— 
—_— 
Case0:y 
= b +¢a 
Casel:y=b+a 
Either 0 or 1 can result in smaller formula 
So initially write X in truth table and K-Map 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
X
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
X
Don’t Care
Output(s) we don’t care about are denoted by X , can be treated 
 as either 0 or 1
Truth table

--- [Page 115 of 255] ---
PES 
UNIVERSITY 
—_ 
— 
— 
R — 
Case0:y 
= b +ca 
IBEEBE 
Casel:y=b+a 
Either 0 or 1 can result in smaller formula 
So initially write X in truth table and K-Map 
Karnaugh Maps-(Don’t Cares)
Example  1 (Three inputs)
Suppose we are asked to design a  
three input logic circuit all whose  
inputs can never be 1  
simultaneously
logic circuit
1
1
1
guaranteed can’t happen
a
b
c
y
0
0
0
1
0
0
1
1
0
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
1
1
0
1
1
1
1
0
1
1
1
1
X
bc
a
00
01
11
10
0
1
1
1
0
0
1
1
1
X
Don’t Care
Output(s) we don’t care about are denoted by X , can be treated 
 as either 0 or 1
Truth table

--- [Page 116 of 255] ---
1 
X 
| X 
Sa=Dy+ 0,00+ Bo0y + D, 
PES 
UNIVERSITY 
RN ERRAR AN 
RRRRRARERIER N 
2 
3 
4 
5 
6 
1 
8§ 
9§ 
N 
Dy 
o011 
10 
00 
1 
1 
X 
1 
01 
1 
0 
X 
1 
1 F 
1 
X 
x) 
10 
1 
0 
X 
X 
— 
| — 
Sp=D,+D1Dy+ 
D15, 
O 
[l 
= 
= 
= 
Karnaugh Maps-(Don’t Cares)
Example  2(Four inputs)
K-Map Structure (four input Boolean function)
A seven-segment display decoder 
takes a 4-bit data input D3:0 and 
produces seven outputs to control 
light-emitting diodes to display a 
digit from 0 to 9. The seven outputs 
are often called segments a through 
g, or Sa–Sg, as defined in Figure. The 
digits are shown.
Write a truth table for the outputs, 
and use K-maps to find Boolean 
equations for outputs Sa and Sb. Use 
don’t care about the output values 
for illegal input 
values of 10 to 15

--- [Page 117 of 255] ---
1 
X 
| X 
Sa=Dy+ 0,00+ Bo0y + D, 
6 
7 
9 
N 
D 
o0 
11 
10 
00 
1 
1 
X 
1 
01 
1 
0 
X 
1 
1 (1 
1 
X 
x) 
10 
1 
0 
X 
X 
I 
— 
Sp=D,+ DDy 
+ D; 5o 
PES 
UNIVERSITY 
DD TED 
Karnaugh Maps-Four Inputs 
K-Map Example 2
Sa = D3+D2D0+D2’D0’+D1
Sb = D2' + D1'D0' + D1D0
Sc = D0 + D2 + D1’
Sd = D1D0' + D2’D1+ D0'D2' + D2D1’D0
Se = D1D0' + D2'D0’
Sf = D3 + D2D0' + D2D1' + D1’ D0'
Sg = D3 + D1D0' + D2'D1 + D2D1'

--- [Page 118 of 255] ---
Karnaugh Maps-(Don’t Cares)
 Think About It
Minimize using K-Maps
Minimize using 
K-Maps
1.f (a, b) = Σ(0, 1, 2, 3)
2.f (a, b, c, d ) =Σ(0, 1, 5, 7, 15, 14, 10)
a
b
c
d
y
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
1
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
1
1
0
1
0
X
1
1
0
1
0
1
1
0
1
0
1
1
1
1
0
1
1
1
1
X

--- [Page 119 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps-(Don’t Cares)
MCQs
1. In a four-input K-Map, which pairs of squares are adjacent due to 
wrap-around?
 A) Only left and right squares
 B) Only top and bottom squares
 C) Both left-right AND top-bottom squares are adjacent (wrap-around 
applies to both rows and columns)
 D) No squares wrap around in a four-input K-Map
Correct Answer 
Option C

--- [Page 120 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps-(Don’t Cares)
MCQs
2. What does an "X" (don't care) in a K-Map or truth table represent?
 A) An output that is always 0
 B) An output that is always 1
 C) An output whose value is unspecified/irrelevant, which can be 
treated as either 0 or 1, whichever gives the smaller formula
 D) An invalid input combination that always causes an error
Correct Answer 
Option C

--- [Page 121 of 255] ---
PES 
UNIVERSITY 
ceuccaaring 
s 
Karnaugh Maps-(Don’t Cares)
MCQs
3. In the example of a three-input circuit whose inputs can never all be 
1 simultaneously, why do don't-care values help simplify the formula?
 A) Because don't cares always force the output to 0
 B) Because input combinations guaranteed never to occur can be 
assigned whichever output value (0 or 1) yields a smaller/simpler 
formula
 C) Because don't cares eliminate the need for a K-Map entirely
 D) Because don't cares only apply to four-input functions
Correct Answer 
Option B

--- [Page 122 of 255] ---
THANK YOU
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 123 of 255] ---
® 
PES 
UNIVERSITY 
I TR 
   Digital Logic and Computer Design
 Unit1
Combinational and Sequential Logic Design
Topic:Combinational Buiding Blocks
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 124 of 255] ---
UNIVERSITY 
50 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
OUTLINE
• Combinational logic is often grouped into larger building blocks 
to build more complex systems. 
• This is an application of the principle of abstraction, hiding the 
unnecessary gate-level details to emphasize the function of the 
building block.
• Commonly used building blocks: Multiplexers , Decoders

--- [Page 125 of 255] ---
& 
PES 
UNIVERSITY 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Multiplexer (Mux)
Multiplexers are among the most commonly used combinational circuits.
A Multiplexer is a digital switch that selects one of several inputs and 
forwards it to a single output.
They choose an output from among several possible inputs based on the 
value of a select signal. A multiplexer is sometimes affectionately called a 
mux.
Multiplexers reduce hardware and simplify circuit design.

--- [Page 126 of 255] ---
® 
PES 
UNIVERSITY 
o v 
>QQ 
0lo 
- 
XlodoHoO 
HAH 
DOOllOOll 
Ncoooo 
- - 
Y =SDy 
+ SD; 
The Boolean expression is: 
•Selects between one of N inputs to   
  connect to output
•log2N-bit select input – control input
•Example:                    
2:1 Multiplexer 
Symbol and Truth Table
S is called Control Signal/Select input
Multiplexer (Mux)
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 127 of 255] ---
Number of Select Lines 
The slide mentions 
log,N 
where 
. 
N = number of inputs 
This tells us how many select lines are required. 
PES 
UNIVERSITY 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Inputs
Select Lines
2
1
4
2
8
3
16
4

--- [Page 128 of 255] ---
- © 
UNIVERSITY 
S TR 
3 
00 
01 
1 
B 
o (&) 
” D°§+ DS 
1. Logic gates
•
Sum-of-products form
2. Tristates
Multiplexer using tristate buffers
•
For an N-input mux, use N 
tristates
•
Turn on exactly one to select 
the appropriate input
Two different ways to implement a 2:1 Multiplexer:
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 129 of 255] ---
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
A tri-state buffer has three output 
states: 0, 1, and High Impedance (Z). 
In a tri-state MUX, only one buffer is 
enabled at a time, ensuring that only 
the selected input reaches the output 
while all others remain disconnected 
(Z).
How does the Tri-state MUX work?
For a 2:1 MUX:
The select signal controls which buffer is 
enabled.
If S = 0: 
D₀ buffer is enabled. 
D₁ buffer outputs Z. 
So, Y = D₀. 
If S = 1: 
D₁ buffer is enabled. 
D₀ buffer outputs Z. 
So, Y = D₁. 
Only one buffer drives the output at a time.

--- [Page 130 of 255] ---
» 
P 
@) 
S5 
5,5, 
Do —[}— 
S:S 
D, 4} 
s,5, 
D, 
8.5 
Ds 
®) 
S 
UNIVERSITY 
J ceiconarimino 
v=ans g 
=% 
s, 
P 5o 
o 
% 
< 
-~ 
~ 
c 
O 
) 
I 
ul 
it 
N) 
Je) 
Q9 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
4:1 Mux
4:1 multiplexer implementations:
 (a) two-level logic, (b) tristates, (c) hierarchical
S1 S0   Output
------  --------
00  →   D0
01  →   D1
10  →   D2
11  →   D3

--- [Page 131 of 255] ---
R~ ool 
R or ol 
A B 
00 
01 
10 
= O O OIK 
@ 
PES 
UNIVERSITY 
e 
DA 
Using the mux as a lookup table to implement AND gate.
Logic using Multiplexers
Multiplexers can be used as lookup tables to perform logic functions.
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
4:1 multiplexer
implementation of two-input AND
Function
The inputs, A and B, serve as select lines. The 
multiplexer data inputs are connected to 0 or 1 
according to the corresponding row of the truth 
table.

--- [Page 132 of 255] ---
Y 
010 
%7*0 
B B—1 
y 
0 
0 
?J—»C 
A 
0 
\0 
1 
\ 
Y=AB 
•Reducing the size of the mux (2:1 Mux)
Logic using Multiplexers- (AND implementation)
we can cut the multiplexer size in half, using only a 2N–1 -input multiplexer to 
perform any N-input logic function. The strategy is to provide one of the literals, 
as well as 0’s and 1’s, to the multiplexer data inputs.
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
For example, in the case 
of AND, 
when A = 0, Y = 0, 
regardless of B. 
When A = 1, Y = 0 if B = 0 
and Y = 1 if B = 1, so Y = 
B. We then use the 
multiplexer as a lookup 
table according to the 
new, smaller truth table.

--- [Page 133 of 255] ---
•Reducing the size of the mux
Logic using Multiplexers  - XOR
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 134 of 255] ---
& 
PES 
UNIVERSITY 
Logic using Multiplexers  - OR  ?
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 135 of 255] ---
Logic using Multiplexers  - OR  ?
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
A
B
Y(A+B)
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
1
Assume:
Select line (S) = A 
Data inputs = I₀ and I₁
Look only at the rows where A = 0.
A
B
Output
0
0
0
0
1
1
The output follows B.
So,
I₀ = B
Look only at the rows where A = 1.
A
B
Output
1
0
1
1
1
1
The output is always 1.
So,
I₁ = 1
Draw the figure
A
Y(A+B)
0
B-I0
0
B-I0
1
1-I1
1
1-I1

--- [Page 136 of 255] ---
i 
S S 
= e N 
n—-n—-oon—-n—-oom 
o e o 
o o0 
ooo—-»—-»—aoo»—al-< 
Y=AB+BC+ABC 
(a) 
PES 
UNIVERSITY 
G TINEE 
Logic using Multiplexers
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Alyssa P. Hacker needs to implement the 
function Y = AB’+B’C’ + A’BC to finish her 
senior project, but when she looks in her 
lab kit, the only part she has left is an 8:1 
multiplexer. How does she implement the 
function?

--- [Page 137 of 255] ---
® 
PES 
UNIVERSITY 
Y 
B 
A 
A 
B ClY 
Logic using Multiplexers
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Alyssa turns on her circuit one more time 
before the final presentation and blows up 
the 
8:1 
multiplexer. 
(She 
accidently 
powered it with 20 V instead of 5 V after
not sleeping all night.) She begs her friends 
for spare parts and they give her a 4:1
multiplexer and an inverter. 
Can she build her circuit with only these 
parts?
Y = AB’+B’C’ + A’BC

--- [Page 138 of 255] ---
& 
PES 
UNIVERSITY 
Implement the function
1. Y=A′B+A′C+AB′ 
using a 4:1 MUX.
2. Implement a 3-variable function using a 4:1 
MUX
Consider:
F(A,B,C)=Σm(1,2,5,7) 
Also implement using 2:1 Mux
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 139 of 255] ---
& 
PES 
UNIVERSITY 
How many 2:1 Mux’s are required to implement 
1. 4:1 
2. 8:1
3. 16:1 and so on
How many 4:1 Mux’s are required to implement 
4. 8:1
5. 16:1 
6. 64:1 and so on
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 140 of 255] ---
So you can remember the general rule: 
Number of k : 
1 MUXes to build an N : 
1 MUX = N—ll 
o~ 
Build an 8:1 MUX
Now we have 8 inputs.
First level
We need:
8→4 
So we need 4 × 2:1 MUXes.
Second level
Those 4 outputs need to become 2 outputs.
So we need 2 × 2:1 MUXes.
Third level
Finally, 2 outputs need to become 1.
So we need 1 × 2:1 MUX.
Therefore:
4+2+1=7 8:1=7 two-to-one MUXes​
So the general formula is:
2n:1 MUX requires (2n−1) 2:1 MUXes​
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Step 1: First level
A 64:1 MUX has 64 inputs.
Each 4:1 MUX can reduce 4 inputs to 1 output.
So:
64/4=16​ 
We need 16 - 4:1 MUXes.
Step 2: Second level
Now we have 16 outputs.
Each 4:1 MUX can take 4 of these:
16​/4=4 
So we need 4 - 4:1 MUXes.
Step 3: Third level
Now we have 4 outputs.
One 4:1 MUX can combine them:
4/4​=1 
So we need 1 -4:1 MUX.
Total
16+4+1=21 
General formula

--- [Page 141 of 255] ---
® 
PES 
UNIVERSITY 
Y, 
Vi 
Y 
Ys 
O 
(&) 
O 
SIS 
L] 
© 
8 
[0 
a) 
|| 
< 
Ao 
A 
O 
— 
DA 
Decoders
•N inputs, 2N outputs
•It asserts exactly one of its outputs 
depending on the input 
combination.
•One-hot outputs: only one output 
HIGH at once
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 142 of 255] ---
Aq 
Ao 
Ys 
£ 
Y7 
Yo 
UL 
2:4 Decoder Implementation
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 143 of 255] ---
Minterm 
AB 
AB 
AB 
AB 
2:4 
Decoder 
11 
A 
10 
B — 
01 
00 
Y = AB + AB 
[ 
> 
D 
o 
E 
9HaA 
Logic Using Decoders
•Decoders can be 
combined with OR 
gates to build logic 
functions.
•Ex: Fig shows the 
two-input XNOR 
function using a 2:4 
decoder and a single 
OR gate.
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 144 of 255] ---
& 
PES 
UNIVERSITY 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Implementing Logic Functions Using Decoders
•
A Boolean function can be represented using a Truth Table or Canonical 
Sum-of-Products (SOP) form.
•
An N-input Boolean function requires an N : 2ᴺ Decoder.
•
The decoder generates all possible minterms.
•
Each decoder output represents one minterm.
•
If the function has M output 1's in its truth table:
•
Connect the corresponding M minterm outputs of the decoder to 
an M-input OR gate.
General Structure:
N Inputs → N : 2ᴺ Decoder → Selected Minterms → M-input OR Gate → 
Function Output

--- [Page 145 of 255] ---
Ex: To implement the logic of a full adder, we need a 3:8 decoder and OR gates. unersry 
If sum and Carry is 
— 
5=5(1,2,4,7) 
C=>(3567) 
(o] 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 146 of 255] ---
DES 
[VERSITY 
it 
S 
Je) 
Q9 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Encoder
An encoder is a digital combinational circuit that converts multiple input signals 
into a binary code. It typically has one active input at a time and generates a 
binary output representing the position of that active input.
The number of inputs is usually 2n, with n output lines.
Inputs are usually active high, meaning high voltage represents an active signal.
Binary-weighted encoders assign codes based on input position using binary values.
Encoders help convert parallel inputs into compact binary formats for processing.
Encoders are useful in digital systems for data compression and efficient 
transmission.
For example, a 4-to-2 encoder has four inputs and produces a 2-bit output code.

--- [Page 147 of 255] ---
2" Input Lines 
¥ 
v 
¥ 
¥ 
¥ 
Encoder 
@ 
= 
N Output Lines 
> 
> 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
The number of inputs is usually 2n, with n output lines.

--- [Page 148 of 255] ---
& 
PES 
UNIVERSITY 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
Types of Encoders
1. 4 to 2 Encoder
2. Octal to Binary Encoder (8 to 3 Encoder)
3. Decimal to BCD Encoder
4. Priority Encoder

--- [Page 149 of 255] ---
PES 
UNIVERSITY 
DHAQ 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
1. 4 to 2 Encoder
The 4 to 2 Encoder consists of four inputs Y3, Y2, Y1 & 
Y0, and two outputs A1 & A0. At any time, only one of 
these 4 inputs can be ‘1’ in order to get the respective 
binary code at the output. 
INPUTS(Y3Y2Y1Y0)
OUTPUTS(A1A0)
0001
00
0010
01
0100
10
1000
11
Truth Table
Logical expression 
for A1 and A0:
A1 = Y3 + Y2
A0 = Y3 + Y1
Circuit Diagram
Logic symbol of the 4 to 2 encoder.

--- [Page 150 of 255] ---
PES 
UNIVERSITY 
50 
Y6 
Y5 
DIV 
YO 
Y1 Y2 Y3Y4Y5Y6Y7 S 
— 
o 
DA 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
2. Octal to Binary Encoder (8 to 3 Encoder)
The 8 to 3 Encoder or octal to Binary encoder consists of 8 inputs: Y 7 to 
Y0 and 3 outputs: A2, A1 & A0. Each input line corresponds to each octal 
digit value and three outputs generate corresponding binary code. 
Truth Table
Logical expression 
for A2, A1, and A0:
A2 = Y7 + Y6 + Y5 + Y4
A1 = Y7 + Y6 + Y3 + Y2
A0 = Y7 + Y5 + Y3 + Y1
Circuit Diagram
Logic symbol of the Octal or 8 to 3 encoder.
INPUTS(Y7Y6Y5Y4Y3Y2Y1Y0) OUTPUTS(A2A1
A0)
00000001
000
00000010
001
00000100
010
00001000
011
00010000
100
00100000
101
01000000
110
10000000
111

--- [Page 151 of 255] ---
& 
PES 
UNIVERSITY 
GRS 
———— 
A3 
vs— 
5 
Decimalto 
[———42 
va— BCD Encoder — 
. a1 
YO Y1 Y2 
Y3 YAY5Y6 
Y7 Y8 
Y9 fi ———~A3 
) 
a2 
] 
) 
A 1 
] 
A| 
/ 
Vv 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
3. Decimal to BCD Encoder
The decimal-to-binary encoder usually consists of 10 input lines and 4 
output lines. Each input line corresponds to each decimal digit and 4 
outputs correspond to the BCD code.
Truth Table
Logical expression for
A3, A2, A1, and A0:
A3 = Y9 + Y8
A2 = Y7 + Y6 + Y5 +Y4
A1 = Y7 + Y6 + Y3 +Y2
A0 = Y9 + Y7 +Y5 +Y3 + Y1
Circuit Diagram
Logic symbol of the BCD encoder.
NPUTS(Y9Y8Y7Y6Y5Y4Y3Y2Y1Y0)
OUTPUTS(A3A2A1
A0)
0000000001
0000
0000000010
0001
0000000100
0010
0000001000
0011
0000010000
0100
0000100000
0101
0001000000
0110
0010000000
0111
0100000000
1000
1000000000
1001

--- [Page 152 of 255] ---
PES 
UNIVERSITY 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
What is an ordinary encoder?
An encoder converts one active input into a binary code.
For example, a 4-to-2 encoder has 4 inputs and 2 outputs:
INPUTS(Y3Y2Y1Y0)
OUTPUTS(A1A0)
0001
00
0010
01
0100
10
1000
11
Here we assume only one input is 1 at a time.
For example:
Y3 Y2 Y1 Y0
0    1    0    0  →  10
So, input Y₂ is active, and the encoder produces binary 10.
2. What is the problem? (NEED OF PRIORITY ENCODER)
Suppose two inputs become 1:
Y3 Y2 Y1 Y0
0    1    1    0  
Which one should the encoder represent?
An ordinary encoder cannot decide because D₂ and D₁ are 
both active.
This is where the priority encoder comes in.

--- [Page 153 of 255] ---
& 
PES 
UNIVERSITY 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
4. Priority Encoder
A 4 to 2 priority encoder has 4 inputs: Y3, Y2, Y1 & Y0, and 2 outputs: A1 & A0. Here, the input, 
Y3 has the highest priority
Y0 has the lowest priority. 
In this case, even if more than one input is ‘1’ at the same time, the output will be the (binary) 
code corresponding to the input, which is having higher priority.
INPUTS(Y3Y2Y1Y0)
OUTPUTS(A1A0V)
0000
XX0
0001
001
001X
011
01XX
101
1XXX
111
Truth Table   (Here X means “don't care”)
Case 1:
Y3 Y2 Y1 Y0
0    0    0    1
Only Y₀ is active.
Output:
A1 A0 = 00
Case 2:
Y3 Y2 Y1 Y0
0    0    1    X
Only Y1 is active.
Output:
A1 A0 = 01
Case 3:
Y3 Y2  Y1  Y0
0    1    X    X
Only Y2 is active.
Output:
A1 A0 = 10
Case 4:
Y3 Y2 Y1 Y0
1    X    X    X
Only Y3 is active.
Output:
A1 A0 = 11

--- [Page 154 of 255] ---
@ 
PES 
UNIVERSITY 
Y1Y0 
Y3Y2 
00 
01 
11 
10 
00 
X 
0 
0 
0 
01 
J 
il 
i 
1 
11 
b 
1 
1 
il 
10 
1 
i 
1 
1 
Al=Y3+Y2 
O 
Oy 
I 
ul 
it 
N) 
Je) 
P 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
4. Priority Encoder
INPUTS(Y3Y2Y1Y0)
OUTPUTS(A1A0V)
0000
XX0
0001
001
001X
011
01XX
101
1XXX
111
Truth Table   (Here X means “don't care”)
Logical Expressions using K-Map
The logical expression for A1 is shown below:

--- [Page 155 of 255] ---
Y3Y2 
Y1YO0 
00 
01 
11 
10 
00 
X 
0 
1 
1 
01 | 0 
0 
0 
0 
11 
X 
X 
X 
X 
10 || 1 
1 
1 
1 
A0=Y3+Y3’Y1 
@ 
PES 
UNIVERSITY 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
4. Priority Encoder
INPUTS(Y3Y2Y1Y0)
OUTPUTS(A1A0V)
0000
XX0
0001
001
001X
011
01XX
101
1XXX
111
Truth Table   (Here X means “don't care”)
Logical Expressions using K-Map
The logical expression for A0 is shown below:

--- [Page 156 of 255] ---
A0 
Y3 
Y2 
Y1 
YO 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks
4. Priority Encoder
INPUTS(Y3Y2Y1Y0)
OUTPUTS(A1A0V)
0000
XX0
0001
001
001X
011
01XX
101
1XXX
111
Truth Table   (Here X means “don't care”)
Circuit Diagram
Why do we need the Valid output(V)?
Just to mention no input is high V=0
All other cases V=1

--- [Page 157 of 255] ---
nm sy avs 
~ 
1] 
Full name 
Basic function 
Inputs 
Outputs 
Main purpose 
Select lines 
Example 
Typical output 
Multiple active inputs? 
Special version 
Multiplexer 
Many — One 
Many data inputs + select 
lines 
Select one input 
Yes 
4:1 MUX 
Selected data 
Not applicable to data 
selection 
Decoder 
n— 2" 
n input/select lines 
211. 
Activate one output 
Yes/input lines act as 
selection code 
2:4 Decoder 
One-hot output 
Output depends on input 
combination 
Priority decoder, etc. 
Encoder 
Encoder 
271 —n 
2TM input lines 
Identify which input is active 
No separate select lines 
4:2 Encoder 
Binary code 
Usually assumes one active 
input 
Priority encoder 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 158 of 255] ---
@ 
PES 
UNIVERSITY 
lines. 
A muiupiexer wid v npus requires logzN select 
Fora 4:1 MUX: 
log,4 = 2 
DA 
MCQ 1
Q1. A 4:1 Multiplexer requires how many select lines?
A) 1
B) 2
C) 3
D) 4
 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 159 of 255] ---
@ 
MCQ 2 
UNIVERSITY 
Q2. A decoder with N inputs has how many outputs? 
A) N 
B) N2 
Answer: C) 2N 
c) 2N 
Explanation: 
D)N + 2 
A decoder activates exactly one of ZNDLItpLItS 
depending on the input combination. 
Example: 
*2 inputs - 4 outputs 
*3 inputs - 8 outputs 
*4 inputs - 16 outputs 
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 160 of 255] ---
PES 
UNIVERSITY 
MCQ 3
Q3. In a decoder, the outputs are called one-hot because
A) All outputs are HIGH simultaneously.
B) Exactly one output is HIGH for any input combination.
C) All outputs are LOW.
D) Outputs keep changing randomly.
Answer: B) Exactly one output is HIGH for any input 
combination.
Explanation:
For every valid input, only one decoder output becomes 
HIGH while all others remain LOW.
COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN
Combinational Building Blocks

--- [Page 161 of 255] ---
THANK YOU
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 162 of 255] ---
Digital Logic and Computer Design
Latches, Flip-flops 
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 163 of 255] ---
o 
PES 
UNIVERSITY 
Digital Logic and 
Computer Design
Latches, Flip-flops 
Team DLCD
Department of CSE and AIML

--- [Page 164 of 255] ---
o 
PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
 
Course Outline
Digital Design
Combinational logic design
Sequential logic design
          
                      - Latches, Flip-flops

--- [Page 165 of 255] ---
) PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
How does Sequential Logic differ from Combinational Logic?
•
Previously we analysed and designed combinational logic. 
The output of combinational logic depends only on current 
input values. Given a specification in the form of a truth 
table or Boolean equation, we can create an optimized 
circuit to meet the specification. 
•
Now we will analyse and design sequential logic. The 
outputs of sequential logic depend on both current and 
prior input values.

--- [Page 166 of 255] ---
PES 
UNIVERSITY 
Sequential Circuits
• It consists of a combinational circuit to which storage elements are connected 
to form a feedback path. 
• The storage elements are devices capable of storing binary information. 
• The binary information stored in these elements at any given time defines the 
state of the sequential circuit at that time. 
• The sequential circuit receives binary information from external inputs that, 
together with the present state of the storage elements, determine the binary 
value of the outputs.
• These external inputs also determine the condition for changing the state in the 
storage elements. 
• The next state of the storage elements is also a function of external inputs and 
the present state.

--- [Page 167 of 255] ---
PES 
UNIVERSITY 
Types of Sequential Circuits
There are two main types of sequential circuits, and their classification 
is a function of the timing of their signals. 

A synchronous sequential circuit is a system whose behavior can 
be defined from the knowledge of its signals at discrete instants of 
time. 

The behavior of an asynchronous sequential circuit depends upon 
the input signals at any instant of time and the order in which the 
inputs change.

--- [Page 168 of 255] ---
PES 
UNIVERSITY 
Two Memory Elements
LATCH
FLIPFLOP

--- [Page 169 of 255] ---
{3 
E } UNIVERSITY 
How to Implement Memory?
●
The inverter is essentially the 
simplest  logic gate
●
What happens when we connect 
its  output to input, forming a 
loop?
●
Inverter loop is thus not in a stable 
state
●
Hence, a single inverter loop 
cannot store a stable bit.
●
How about a loop of two inverters?
●
A two-inverter loop can be in one of 
two stable states.
●
A bit can have one of two different 
values.
Thus, a two-inverter loop can store (or 
“remember”) a single bit.
●
But how can we change the bit stored 
or the stable state?

--- [Page 170 of 255] ---
PES 
UNIVERSITY 
How to Implement Memory?
How do we CHANGE the stored bit?
This is the crucial problem.
Suppose the circuit currently stores:
A=0, B=1​ 
The feedback keeps reinforcing this state.
How can we force it to become:
A=1, B=0​ 
We need some external control mechanism to temporarily 
override the feedback.
So we need cross coupled inverters

--- [Page 171 of 255] ---
Figure 3.1 Cross-coupled 
inverter pair 
@ UNIVERSITY 
= 
9ac 
LATCHES, FLIP-FLOPS 
Latches and Flip Flops
• The fundamental building block of memory is a bistable element, an element 
with two stable states.
• The inverters are cross-coupled, meaning that the input of I1 is the output of I2 
and vice versa.

--- [Page 172 of 255] ---
(a) 
(b) 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
Latches and Flip Flops
•
Bistable operation of cross-coupled inverters
Case I: Q = 0
As shown in Figure (a), I2 receives a FALSE input, Q, so 
it produces a TRUE output on Q' I1 receives a TRUE 
input, Q’ so it produces a FALSE output on Q. This is 
consistent with the original assumption that Q = 0, so 
the case is said to be stable.
Case II: Q = 1
As shown in Figure (b), I2 receives a TRUE input and 
produces a FALSE output on Q’. I1 receives a FALSE 
input and produces a TRUE output on Q. This is again 
stable.
The cross-coupled inverters 
have two stable states, Q = 0 
and Q = 1, so the circuit is 
said to be bistable.

--- [Page 173 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
Latches and Flip Flops
Problem with cross coupled inverters
Although the cross-coupled inverters can store a bit of 
information, they are not practical because the user has no 
inputs to control the state. 
However, other bistable elements, such as latches and flip-
flops, provide inputs to control the value of the state 
variable. The remainder of this section considers these 
circuits.

--- [Page 174 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
Latches and Flip Flops
• Although the cross-coupled inverters can store a bit of information, they are not 
practical because the user has no inputs to control the state. 
• However, other bistable elements, such as latches and flip-flops, provide  inputs to 
control the value of the state variable.
Latch
A latch is a 1-bit memory element that stores a value and can change 
its output as long as its enable/control signal is active.
In simple terms:
Latch = level-sensitive memory
For example, an Enable signal controls the latch:
•
Enable = 1 → latch can change/update 
•
Enable = 0 → latch holds the previous value

--- [Page 175 of 255] ---
@ UNIVERS§ 
Inputs ——— 
> Outputs 
Combinational 
circuit 
Flip-flops 
Clock pulses 4I—> 
(a) Block diagram 
(b) Timing diagram of clock pulses 
LATCHES, FLIP-FLOPS 
Latches and Flip Flops

--- [Page 176 of 255] ---
Figure 3.3 SR latch schematic 
Case 
IV 
I 
Il 
I 
Figure 3.5 SR latch truth table 
1 ==1[" 
R 
0 
1 
0 
1 
=000 
3 
== 
slias] 
3 
@ UNIVERSITY 
—R 
Q- 
S 
Q- 
Figure 3.6 SR latch symbol 
DA 
Oy 
I 
ul 
it 
LATCHES, FLIP-FLOPS 
 
SR Latch
One of the simplest sequential circuits is the SR latch, which is composed of two cross-
coupled NOR gates. The SR latch is similar to the cross-coupled inverters, but its state can 
be controlled through the S and R inputs, which set and reset the output Q.
Cross-coupled inverters + control inputs = SR latch

--- [Page 177 of 255] ---
UNIVERSITY 
(b) 
(a) 
LATCHES, FLIP-FLOPS 
 
SR Latch
SR Latch Operation   when S=R=0
a)
Q=0 and Q’=1                                        
b) Q=1 and Q’=0 
q
 
s

--- [Page 178 of 255] ---
o 
PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
 
SR Latch
• Like the cross-coupled inverters, the SR latch is a bistable element with one bit of 
state stored in Q. 
• However, the state can be controlled through the S and R inputs. When R is 
asserted, the state is reset to 0. 
• When S is asserted, the state is set to 1. When neither is asserted, the state retains 
its old value.
• No matter what pattern of setting and resetting occurred in the past, all that is 
needed to predict the future behavior of the SR latch is whether it was most 
recently set or reset.
•
S=1 → Q becomes 1
•
S=0,R=0 → Q stays 1
•
R=1 → Q becomes 0
•
S=0,R=0 → Q stays 0
•
S=1 → Q becomes 1

--- [Page 179 of 255] ---
LATCHES, FLIP-FLOPS 
 
Problems with SR Latch
1. Problem with the SR latch
In an SR latch:
•
S tells us what to store → Q=1 
•
R tells us what to store → Q=0 
But they also directly cause the 
change.
For example:
S=1  
  Q becomes 1 
⇒
There is no separate signal saying:
"Change now."
So what to store and when to change 
are mixed together.
2. The problem with both S and R
For the SR latch:
S
R
Action
0
0
Hold
0
1
Reset → (Q=0)
1
0
Set → (Q=1)
1
1
 Invalid
❌
The S=R=1 case is awkward.
So we want a simpler memory element where 
we don't have to separately worry about Set 
and Reset.

--- [Page 180 of 255] ---
o 
PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
 
D Latch
• Designing circuits becomes easier when these questions of 
what and when are separated.
• D latch solves these problems.
• It has two inputs. The data input, D, controls what the next 
state should be. The clock input, CLK, controls when the 
state should change.
So:
D=WHAT to store​
So:
CLK=WHEN to change​

--- [Page 181 of 255] ---
CLK 
(a) 
UNIVERSITY 
D 
‘ER 
Q-Q 
CLK 
_DOQ 
) 
H o M|D 
= dli~] 
= o o|h 
El'.)l 
n] 
[ 
)i 
1 
(b) 
(c) 
Figure 3.7 D latch: (a) schematic, (b) truth table, (c) symbol 
DA 
O 
) 
I 
Il 
it 
LATCHES, FLIP-FLOPS 
 
D Latch
•
When CLK = 1, the latch is transparent(open). The data at D flows through to Q as if the 
latch were just a buffer. When CLK = 0, the latch is opaque(closed).
•
It blocks the new data from flowing  through to Q, and Q retains the old value. Hence, 
the D latch is some- times called a transparent latch or a level-sensitive latch.
•
The circuit guarantees that S and R can never both be 1.

--- [Page 182 of 255] ---
&%) PES 
[ 
O 
UNIVERSITY 
(a) Response to positive level 
P 
L 
L 1] 
(b) Positive-edge response 
[ 
S 
O A O 
(c) Negative-edge response 
Clock response in latch and flip-flop 
DA 
LATCHES, FLIP-FLOPS 
 
Problem with latch (Need of Flipflop)
•
The problem with the latch is that it responds to a change in the level of a clock pulse.
 As shown in Fig. 5.8 (a), a positive level 
response in the enable input allows 
changes in the output when the D input 
changes while the clock pulse stays at logic 
1. The result is an unpredictable situation, 
since the state of the latches may keep 
changing for as long as the clock pulse 
stays at the active level. The key to the 
proper operation of a flip-flop is to trigger it 
only during a signal transition .

--- [Page 183 of 255] ---
LATCHES, FLIP-FLOPS 
 
Problem with latch (Need of Flipflop) 
1.Problem with the latch (fig 5.8a)
While CLK is HIGH, every change in 
D can potentially change Q.
So if D changes many times while:
CLK=1 
then Q can also change many times.
This is unpredictable because the 
final state can depend on exactly 
when the input changes during the 
active level.
2. What do we really want?
We want the memory element to say:
"I will look at D only at one particular 
instant."
Not:
"I will keep looking at D for the entire HIGH 
period."
That particular instant is called an edge.
CLK = 1    D changes:
D:    0 ─── 1 ─── 0 ─── 1
            ↓     ↓     ↓
Q:    0 ─── 1 ─── 0 ─── 1
3. What is an edge?
A clock signal has two transitions:
Rising edge (fig 5.8b)
0→1​
This is also called the positive edge or 
positive-going edge.
Falling edge (fig 5.8c)
1→0​ This is the negative edge or negative-
going edge.
Flip-flop changes only at the edge
This is the fundamental difference:
Latch
Level sensitive​ 
For positive-level latch:
CLK=1
Q may change 
⇒
Flip-flop
Edge sensitive​ 
For positive-edge flip-flop:
CLK:0→1
Q changes 
⇒
only at that instant.

--- [Page 184 of 255] ---
PES 
UNIVERSITY 
Difference b/w Latches & Flip-Flops
Latches
Flip-Flops
Latches are building blocks of sequential 
circuits, these can be built from logic gates
Flip flops are also building blocks of sequential circuits. But, these 
can be built from the latches.
Latch continuously checks its inputs and 
changes its output correspondingly.
Flip flop continuously checks its inputs and changes its output 
correspondingly only at times determined by clocking signal
The latch is sensitive to the duration of the 
pulse and can send or receive the data when 
the switch is on.
Flipflop is sensitive to a signal change. They can transfer data only 
at the single instant and data cannot be changed until next signal 
change.Flip flops are used as a register.
It is based on the enable function input.
It works on the basis of clock pulses.
It is a level triggered, it means that the output 
of the present state and input of the next state 
depends on the level that is binary input 1 or 
0. (asynchronous circuits)
It is an edge triggered, it means that the output and the next state 
input changes when there is a change in clock pulse whether it may 
a+ve or-ve clock pulse.(synchronous circuits)

--- [Page 185 of 255] ---
PES 
UNIVERSITY 
Difference b/w Latches & Flip-Flops
Example: Traffic Light Controller
Scenario:
A city traffic light controller uses digital storage elements to decide when to change from Green 
→ Yellow → Red.
Using a Latch (Level-triggered)
Suppose the system uses a latch to store the current state of the traffic light.
Since a latch is level-sensitive, whenever the clock/enable signal is high, the latch is 
“transparent” — it immediately passes input changes to the output.
Problem: If there is noise or a small glitch during the enable-high period, the latch will capture 
it. This could cause the traffic light to change state unexpectedly (e.g., Green jumps to Red 
without Yellow).
 Application-level interpretation: Not safe for traffic control, because continuous input changes 
during the active level may corrupt the output.

--- [Page 186 of 255] ---
UNIVERSITY 
oHa 
ES 
ERSITY 
Difference b/w Latches & Flip-Flops
Example: Traffic Light Controller
Scenario:
A city traffic light controller uses digital storage elements to decide when to change from Green 
→ Yellow → Red.
 Using a Flip-Flop (Edge-triggered)
If the system uses a  Flip-Flop, the light state is updated only at the clock’s rising (or falling) 
edge.
Input changes happening in between edges are ignored until the next edge.
Advantage: The traffic light changes state in a controlled manner (e.g., every 30 seconds on the 
rising clock edge). Even if input glitches occur while the clock is low, they won’t affect the state.
Application-level interpretation: Much safer and reliable for real-world sequential control 
(traffic lights, elevators, etc.).

--- [Page 187 of 255] ---
UNIVERSITY 
oHa 
ES 
ERSITY 
Difference b/w Latches & Flip-Flops
https://www.youtube.com/watch?v=LTtuY
eSmJ2g

--- [Page 188 of 255] ---
o 
PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
 
What is Flipflop and how to build it?
 There are two ways that a latch can be modified to form a flip-flop. 
•
One way is to employ two latches in a special configuration that isolates the output 
of the flip-flop and prevents it from being affected while the input to the flip-flop is 
changing – Example-D flipflop
•
Another way is to produce a flip-flop that triggers only during a signal transition (from 
0 to 1 or from 1 to 0) of the synchronizing signal (clock) and is disabled during the rest 
of the clock pulse.

--- [Page 189 of 255] ---
CLK 
CLK 
CLK 
N1 
D 
Q 
2 
11 
Q 
o 
master 
o 
(a) 
| 
~ 
D 
(b) 
= 
4 i e 
(a) schematic, (b) symbol, 
QI 
O 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
D FIip-Flop
•
A D flip-flop can be built from two back-to-back D latches controlled by complementary 
clocks
The first latch, L1, is called the master. The second latch, L2, is 
called the slave. The node between them is named N1.
When CLK = 0, the master latch is transparent and the slave is 
opaque. Therefore, whatever value was at D propagates through 
to N1.
When CLK = 1, the master goes opaque and the slave becomes 
transparent.

--- [Page 190 of 255] ---
CLK 
CLK 
CLK 
N1 
D 
Q 
2 
11 
Q 
o 
master 
o 
(a) 
| 
~ 
D 
n,(: ) 
(c) 
N By 
(a) schematic, (b) symbol, 
e 
QI 
O 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
D FIip-Flop
•
A D flip-flop can be built from two back-to-back D latches controlled by complementary 
clocks
Hence, whatever value was at D immediately before the clock 
rises from 0 to 1 gets copied to Q immediately after the clock 
rises. 
At all other times, Q retains its old value, because there is always 
an opaque latch blocking the path between D and Q.
In other words, a D flip-flop copies D to Q on the rising edge of 
the clock, and remembers its state at all other times.
The rising edge of the clock is often just called the clock edge for 
brevity. The D input specifies what the new state will be.

--- [Page 191 of 255] ---
PES 
UNIVERSITY 
«O>r 
< Fr <= 
«=)» 
Q> 
LATCHES, FLIP-FLOPS 
D FIip-Flop
•
A D flip-flop is also known as a master-slave flip-flop, an edge-triggered flip-flop, or a 
positive edge-triggered flip-flop. The triangle in the symbols denotes an edge-triggered 
clock input. The Q output is often omitted when it is not needed.
The main idea is:
When the clock triggers the flip-flop, whatever is present at D gets stored in Q.
So we can remember it as:
Q(next) = D
Here ↑ means the rising edge of the clock.
D
Clock event
Q(next)
0
↑
0
1
↑
1

--- [Page 192 of 255] ---
PES 
UNIVERSITY 
Flip-Flops(2ND METHOD)
Flip-Flops have following representation:
●Function table- output Q and Q`
●Characteristic table- They define next state
●Characteristic equation-solve using K map- The logical properties of a flip-
flop, as described in the characteristic table, can be  expressed algebraically 
with a characteristic equation.
●Excitation table- predict the i/p based on current state and next state to build 
state diagram

--- [Page 193 of 255] ---
PES 
UNIVERSITY 
Characteristic table & Excitation Table
The easiest way to remember it is:
Characteristic table = What the flip-flop DOES
Excitation table = What we MUST GIVE to the flip-flop to make it DO 
what we want

--- [Page 194 of 255] ---
= 
CLK 
R— 
INPUTS 
OUTPU | STATE 
T 
CLK 
S 
R 
Q 
X 
0 
0 
No 
|Previous 
Change 
A 
0 
1 
0 
Reset 
A 
1 
0 
1 
Set 
? 
1 
1 
- 
Forbidde 
n 
Ol 
S 
R 
Qx 
Qx 
0 
0 
0 
0 
0 
0 
[ 
[ 
0 
1 
0 
0 
0 
T 
] 
0 
1 
0 
0 
[ 
I 
0 
[ 
[ 
[ 
I 
0 
- 
@ PES 
UNIVERSITY 
SR Flip-Flops  Characteristic table and Characteristic equation
Characteristic table 
Characteristic equation by simplifying using K maps
Qn+1= S +R`Qn

--- [Page 195 of 255] ---
a4 
1 
x 
o 
Excitation table of SR flip flop 
Inwvalid states 
$,R=0,0 
$,R=0,0 
Truth table of SR fhp flop 
O 
= 
- 
Hae 
Excitation Table and State Diagram
Source: Electrically4u
State Diagram
Characteristic Table of SR

--- [Page 196 of 255] ---
@ UNIVERSITY 
o 
= 
= 
= 
= 
©ac 
D Flip-Flop-Data FF

--- [Page 197 of 255] ---
@ UNIVERSITY 
En D | Nextstate of Q 
0 X | Nochange 
I 
0 
Q=0;resetstate 
_ 
I 
1| 
Q= Il;setstate 
(b) Function table 
D Flip-Flop 
D 
Qt+1) 
0 
|0 
Reset 
1 
|1 
Set 
O(t+1)=D 
D Flip-Flop
D
Qn
Qn+1
0
0
0
0
1
0
1
0
1
1
1
1
Simplifying using K maps- 
characteristic equation is
Characterstic Table
Qn
Q(n+1)
D
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
1
1
Excitation table

--- [Page 198 of 255] ---
@ UNIVERSITY 
XU 
©l 
Y 
—P>Clk 
—_—J 
— 
—K 
o—— 
(b) Graphic symbol 
JK Flip-Flop
A JK flip-flop is required mainly to overcome the limitations of the SR flip-flop and to 
provide a more versatile storage element in sequential circuits. 
In an SR flip-flop, when S=1 and R=1 simultaneously, the output becomes indeterminate 
(invalid).

--- [Page 199 of 255] ---
PES 
UNIVERSITY 
JK Flip-Flop-function table/Truth table
Clk
J
K
Q
0
x
x
Qn
1
0
0
Qn
1
0
1
0
1
1
0
1
1
1
1
Qn
Memory
Toggle
race around condition

--- [Page 200 of 255] ---
@ UNIVERSITY 
Excitation table 
Characteristics table 
an) 
J 
K | Q) 
o amil) 
2 
K 
0 
0 
0 
X 
o 
0o 
o] 
o 
s 
3 
T 
= 
1 
0 
o 
1 
1 
0 
1 
0 
1 
1 
ol 
1 
1 
1 
1| 
o 
JK Flip-Flop
Solve using K map:
J= Qn+1            K = Q’n+1 
Clk
J
K
Q
0
x
x
Qn
1
0
0
Qn
1
0
1
0
1
1
0
1
1
1
1
Qn
Truth Table
Solve using K map to get 
characterstic equation:
Qn+1= QnK` + Qn`J

--- [Page 201 of 255] ---
T 
—1> Clk 
K 
o———— 
> Clk 
o 
Clk 
(a) From JK flip-flop 
(b) From D flip-flop 
(c) Graphic symbol 
DA 
@ PES 
UNIVERSITY 
T Flip-Flop (Toggle Flip-Flop)

--- [Page 202 of 255] ---
CLK 
Qn+1 
! 
Qn 
} 
Qn’ 
@ UNIVERSITY 
Qt+1)=TeQ=T0'+ T'Q 
T Flip-Flop (Toggle Flip-Flop)
Truth table- if clk=0 
then previous state
T
Qn
Qn+1
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
Characterstic Table
Excitation table

--- [Page 203 of 255] ---
PES 
UNIVERSITY 
Flip-Flops
•JK flip-flop can function as:
•SR flip-flop (J = S, K = R)
•T flip-flop (J=K=1 → toggles)
•D flip-flop (J=D, K=¬D)
•Hence, it’s a universal flip-flop that can emulate other 
types.

--- [Page 204 of 255] ---
Flip-Flop Characteristic Tables 
JK Flip-Flop 
J 
K | Qi + 1) 
0 
0 
Q(t) 
No change 
] 
1 
0 
Reset 
1 
0 
1 
Set 
1 
1 
Q'(r) 
Complement 
D Flip-Flop 
T Flip-Flop 
D | Q(t 
+ 1) 
T 
|Qt+ 1) 
0 
0 
Reset 
0 
Q) 
No change 
1 
1 
Set 
1 
Q') 
Complement 
@ PES 
UNIVERSITY 
DA 
Characteristics Table  -summary

--- [Page 205 of 255] ---
@ 
The logical properties of a flip-flop, as described in the characteristic table, can be 
expressed algebraically with a characteristic equation. For the D flip-flop, we have the 
characteristic equation 
Ot+1)=D 
which states that the next state of the output will be equal to the value of input D in the 
present state. The characteristic equation for the JK flip-flop can be derived from the 
characteristic table or from the circuit of Fig. 5.12. We obtain 
Oot+1)=JO"+ K'O 
where Q is the value of the flip-flop output prior to the application of a clock edge. The 
characteristic equation for the T flip-flop is obtained from the circuit of Fig. 5.13: 
Qt+1)=T®Q=TQ' + T'Q 
PES 
UNIVERSITY 
Characteristics Equations-summary

--- [Page 206 of 255] ---
STEPS: - 
1. Identify available and required flip flop. 
2. Make characteristic table for required flip flop. 
3. Make excitation table for available flip flop. 
4. Write boolean expression for available ff. 
5. Draw the circuit. 
Steps for Flipflop Conversion

--- [Page 207 of 255] ---
@ UNIVERSITY 
JK to D FF (b)
•STEP1-Identify available and required FF
  Available is JK and required is D
•Step-3- Make Excitation table of 
available FF 
•Step-2  Make characteristic table of 
required FF

--- [Page 208 of 255] ---
% UNIVERSITY 
JK to D FF
•STEP-4-write Boolean Expression for Available FF(JK) using required FF (D)
•STEP-5 Write the circuit diagram

--- [Page 209 of 255] ---
Excitation Table of the D Flip-Flop 
% UNIVERSITY 
2. D to JK FF (a)

--- [Page 210 of 255] ---
D to JK  FF

--- [Page 211 of 255] ---
% UNIVERSITY 
D=JQn’+K 
Qn 
D to JK  FF

--- [Page 212 of 255] ---
@ 
v 
m 
w0 
= 
z 
= 
< 
3 
m 
o 
7 
= 
) 
2 
Exercise 3.10 A JK flip-flop receives a clock and two inputs, ] and K. On the rising 
edge of the clock, it updates the output, Q. If 
] and K are both 0, Q retains its old 
value. If only 
[ is 1, O becomes 
1. If only K is 1, Q becomes 0. If both [ and K are 1, 
Q becomes the opposite of its present state. 
(a) Construct a JK flip-flop using a D flip-flop and some combinational logic. 
(b) Constructa D flip-flop using a JK flip-flop and some combinational logic. 
(c) Constructa T flip-flop (see Exercise 3.9) using a JK flip-flop. 
0 
Q 
I 
w 
it 
A 
Exercise 3.10

--- [Page 213 of 255] ---
PES 
UNIVERSITY 
Solve it.
(c) Construct a T flip-flop using a JK flip-flop

--- [Page 214 of 255] ---
CLK 
O 
Pl P (e 
N 
Ny 
N | 
D, —D 
d o 
CLK 
el ol 
4 
‘ 
Dso 
— 
(a) 
o 
PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
     Registers           
An N-bit register is a bank of N flip-flops that share a common CLK  input, 
so that all bits of the register are updated at the same time.
 Registers are the key building block of most sequential circuits.
Figure A 4-bit register:
(a) schematic and (b) symbol
Four-bit register with inputs D3:0
and outputs Q3:0. D3:0 and Q3:0 
are both 4-bit buses.

--- [Page 215 of 255] ---
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
     Registers           
How much information can a N-bit register store?
Each flip-flop stores either 0 or 1.
Four flip-flops can therefore store:
24=16  different combinations.
From:
0000 
to:
1111 
So a 4-bit register can store 16 different values.
Hence N bit register = N Flip flops and can store 2N different combinations.
"N-bit register stores N bits, but it can represent 2N different values."

--- [Page 216 of 255] ---
CLK EN 
(c) 
EN 
Figure 3.10 Enabled flip-flop: 
(a, b) schematics, (c) symbol 
PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
 
Enabled Flip-Flop 
• An enabled flip-flop adds another input called EN or ENABLE to determine whether 
data is loaded on the clock edge. 
• When EN is TRUE, the  enabled flip-flop behaves like an ordinary D flip-flop. 
• When EN is FALSE, the enabled flip-flop ignores the clock and retains its state 
• Enabled flip-flops are useful when we wish to load a new value into a  flip-flop only 
some of the time, rather than on every clock edge.

--- [Page 217 of 255] ---
PN - g
[Ty 
CLK EN 
EN 
o 
| 
D—D 
(a) 
Q- 
(b) 
(a, b) schematics, (c) ’¥m|,,,|' 
© 
o 
LATCHES, FLIP-FLOPS 
Enabled Flip-Flop 
• In Figure 3.10(a), an input multiplexer chooses whether to pass the value at D, if EN is 
TRUE, or to recycle the old state from Q, if EN is FALSE.
• In Figure 3.10(b), the clock is gated.
• If EN is TRUE, the CLK input to the flip-flop toggles normally.
• If EN is FALSE, the CLK input is also FALSE and the flip-flop retains its old value.
• EN must not change while CLK = 1, let the flip-flop  see a clock glitch(switch at an 
incorrect time).

--- [Page 218 of 255] ---
LATCHES, FLIP-FLOPS 
 
Enabled Flip-Flop 
EN = 1 → LOAD
When:
EN=1 
the flip-flop behaves like a normal D flip-flop.
At the clock edge:
                                          Qnext​=D​ 
Example
Suppose:
Q = 0
D = 1
EN = 1
When the clock edge arrives:
The new data 1 is loaded
So output Q=1
EN = 0 → HOLD
Now suppose:
Q = 1
D = 0
but:
EN = 0
When the clock edge arrives, the flip-flop says:
"EN is 0. I am not allowed to load D."
Therefore:
                                            Qnext​=Q​ 
So Q remains:
Q=1 Even though D is 0. 
i.e. (the new data D is not loaded to Q) 
An enabled flip-flop loads new data only when EN = 1; when EN = 0, it ignores the clock 
edge and keeps its previous value.

--- [Page 219 of 255] ---
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
 
Resettable Flip-Flop 
• A resettable flip-flop adds another input called RESET. When RESET is FALSE, the 
resettable flip-flop behaves like an ordinary D flip-flop.
• When RESET is TRUE, the resettable flip-flop ignores D and resets the output to 0.
• Resettable flip-flops are useful when we want to force a known state (i.e., 0) into all 
the flip-flops in a system when we first turn it on.
• Such flip-flops may be synchronously or asynchronously resettable.
• Synchronously resettable flip-flops reset themselves only on the rising edge of CLK. 
Asynchronously resettable flip-flops reset themselves as soon as RESET becomes 
TRUE, independent of CLK.

--- [Page 220 of 255] ---
CLK 
| 
D 
RESETD— D a—a 
(a) 
1 
D 
Q "' 
V% 
RESET 
[ 
(b) 
(c) 
Figure 3.11 Synchronously 
resettable flip-flop: 
(a) schematic, (b, c) symbols 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
Resettable Flip-Flop 
• Figure 3.11(a) shows how to construct a synchronously 
resettable flip-flop from an ordinary D flip-flop and an 
AND gate. 
• When RESET`  is FALSE, the AND gate forces a 0 into the 
input of the flip-flop. When RESET` is TRUE, the AND 
gate passes D to the flip-flop.
• RESET`  is an active low signal
• Asynchronously resettable flip-flops require modifying 
the internal structure of the flip-flop settable flip-flops 
are also occasionally used. 
• They load a 1 into the flip-flop when SET is asserted
• Resettable and settable flip-flops may also have an 
enable input and may be grouped into N-bit  registers.

--- [Page 221 of 255] ---
LATCHES, FLIP-FLOPS 
Resettable Flip-Flop 
Normal D Flip-Flop
A normal D flip-flop does:
Qnext​=D​ 
at the active clock edge.
For example:
D = 1 → clock edge → Q = 1
Add RESET
Now we add another input:
D + CLK + RESET
RESET has higher priority than D.
Think of it like this:
IF RESET = 0 → behave normally
IF RESET = 1 → forget D and make Q = 0
So the basic behavior is:
Here X means "don't care."
When RESET = 1, we don't care whether D is 0 or 1.
RESET
Clock edge
D
Q(next)
0
↑
0
0
0
↑
1
1
1
↑
X
0

--- [Page 222 of 255] ---
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
Flip Flop and Latch Comparison
• Latches and flip-flops are the fundamental building blocks of sequential circuits.
• Remember that a D latch is level-sensitive, whereas a D flip-flop is edge-
triggered.
• The D latch is transparent when CLK = 1, allowing the input D to flow through 
to the output Q. 
• The D flip-flop copies D to Q on the rising edge of CLK. At all other times, 
latches and flip-flops retain their old state. 
• A register is a bank of several D flip-flops that share a common CLK signal.

--- [Page 223 of 255] ---
@ UNIVERSITY 
CLK 
\ 
/ 
\ 
/ 
0 
i 
_/ 
\/ 
Q (latch) 
Q (flop) 
Figure 3.14 Example waveforms 
LATCHES, FLIP-FLOPS 
 
Flip-Flop and Latch Comparison
• Ben Bitdiddle applies the D and CLK inputs shown in Figure 3.14 to a D latch and
a D flip-flop. Help him determine the output, Q, of each device.

--- [Page 224 of 255] ---
UNIVERSITY 
A 
/T 
CLK 
D 
[ 
Q (latch) (\;\ 
% 
atop) 
A e 
Figure 3.15 Solution waveforms 
LATCHES, FLIP-FLOPS 
    Flip-Flop and Latch Comparison
• Ben Bitdiddle applies the D and CLK inputs shown in Figure 3.14 to a D latch and
a D flip-flop. Help him determine the output, Q, of each device.

--- [Page 225 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
MCQs
Q1: Why can a loop of two cross-coupled inverters store one bit of 
information?
 A) Because it has two outputs
 B) Because it consumes low power
 C) Because it can settle into one of two stable states, matching the 
two values a bit can take
 D) Because it uses NAND gates only

--- [Page 226 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
MCQs
Q1: Why can a loop of two cross-coupled inverters store one bit of 
information?
 A) Because it has two outputs
 B) Because it consumes low power
 C) Because it can settle into one of two stable states, matching the 
two values a bit can take
 D) Because it uses NAND gates only

--- [Page 227 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
MCQs
Q2: In a NOR-gate SR latch, what happens when both inputs S = 1 and 
R = 1?
 A) The latch remembers the previous state
 B) The output q is set to 1
 C) Both outputs q and q' become 0 — an invalid state since they're no 
longer complementary
 D) The output is reset to q = 0

--- [Page 228 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
MCQs
Q2: In a NOR-gate SR latch, what happens when both inputs S = 1 and 
R = 1?
 A) The latch remembers the previous state
 B) The output q is set to 1
 C) Both outputs q and q' become 0 — an invalid state since they're no 
longer complementary
 D) The output is reset to q = 0

--- [Page 229 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
MCQs
Q3: Why is the NAND-gate based SR latch sometimes called an S'R' 
latch?
 A) Because it uses only NOR gates internally
 B) Because its input signals are complemented (active-low) compared 
to the NOR latch
 C) Because it stores complemented data only
 D) Because S' and R' represent set and reset simultaneously

--- [Page 230 of 255] ---
oHa 
@ PES 
UNIVERSITY 
LATCHES, FLIP-FLOPS 
MCQs
Q3: Why is the NAND-gate based SR latch sometimes called an S'R' 
latch?
 A) Because it uses only NOR gates internally
 B) Because its input signals are complemented (active-low) compared 
to the NOR latch
 C) Because it stores complemented data only
 D) Because S' and R' represent set and reset simultaneously

--- [Page 231 of 255] ---
THANK YOU
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 232 of 255] ---
IIIIIIIIII 
PES 
UNIVERSITY 
= 
& 
= 
= 
= 
wae 
DIGITAL LOGIC  AND  
COMPUTER DESIGN
Synchronous Sequential Logic Circuits
Team DLCD
Department of CSE and CSE(AI &ML)

--- [Page 233 of 255] ---
PES 
UNIVERSITY 
DIGITAL LOGIC  AND  
COMPUTER DESIGN
Synchronous Sequential Logic Circuits

--- [Page 234 of 255] ---
@ 
PES 
UNIVERSITY 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
 
Course Outline
Digital Design
• Combinational logic design
• Sequential logic design
        - Synchronous Sequential Logic Circuits

--- [Page 235 of 255] ---
o 
& 
= 
E 
= 
©ac 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
Potential Problems with Sequential Logic Circuits
Combinational logic circuits do not  
contain loops or cyclic paths but  
sequential logic circuits do
Loops can cause problems
•
Output is unstable
Memory elements can suffer from
race conditions
clk1
clk2
d
d   q
q
•
Output depends upon input sequence

--- [Page 236 of 255] ---
= 
©ac 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
Cyclic paths are broken by inserting flip-flops in them
Flip-flops are synchronized by connecting them to a common clock
 Race conditions are eliminated if the clock time period is long enough
clk1
clk2
d  q
d q
Cyclic paths can be broken by converting combinational ckts and 
register(synchronize with clock) 
Sequential Logic Circuits

--- [Page 237 of 255] ---
E 
9HaA® 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
q
Cyclic paths are broken by inserting flip-flops in them
clk
d
Flip-flops are synchronized by connecting them to a common clock
Race conditions are eliminated if the clock time period is long enough
clk1
clk2
d  q
d q
Sequential Logic Circuits

--- [Page 238 of 255] ---
E 
9HaA® 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
q
Cyclic paths are broken by inserting flip-flops in them
clk
d
Flip-flops are synchronized by connecting them to a common clock
Race conditions are eliminated if the clock time period is long enough
clk
d  q
d q
Sequential Logic Circuits

--- [Page 239 of 255] ---
\_ 
Figure 3.16 Three-inverter loop 
_/ 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
   Potential Problems with Sequential Logic Circuits
ASTABLE CIRCUITS
Alyssa P. Hacker encounters three misbegotten inverters who have tied themselves
in a loop, as shown in Figure 3.16. The output of the third inverter is fed back to
the first inverter. Each inverter has a propagation delay of 1 ns. Determine what
the circuit does.

--- [Page 240 of 255] ---
PES 
UNIVERSITY 
0123456 
7 8 Time(ns) 
Hao 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
 
Potential Problems with Sequential Logic Circuits
•
Suppose node X is initially 0. Then Y = 1, Z = 0, and hence X = 1, 
which is inconsistent with our original assumption. The circuit has 
no stable states and is said to be unstable or astable. 
•
Figure 3.17 shows the behavior of the circuit. If X rises at time 0, Y 
will fall at 1 ns, Z will rise at 2 ns, and X will fall again at 3 ns.
•
In turn, Y will rise at 4 ns, Z will fall at 5 ns, and X will rise again at 
6 ns, and then the pattern will repeat. 
•
Each node oscillates between 0 and 1 with a period (repetition 
time) of 6 ns. This circuit is called a ring oscillator.
Figure 3.16 Three-inverter loop

--- [Page 241 of 255] ---
PES 
UNIVERSITY 
SR TN 
CLK D Qye 
0= CLKD+ OLK Qyey 
N1=CLKD 
I’ 
N2= CL_K'Oprav 
S 
S 
D e 
S 
i 
— e = — 
[l — I 
i 
— 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
 
Potential Problems with Sequential Logic Circuits
RACE CONDITIONS
Ben Bitdiddle designed a new D latch that 
he claims is better than the one  because
 it uses fewer gates. He has written the 
truth table to find the output, Q, given 
the two inputs, D and CLK, and the old 
state of the latch, Qprev.
Based on this truth table, he has derived
Boolean equations. 
He obtains Qprev by feeding back the 
output, Q in his design. 
Does his latch work correctly,independent 
of the delays of each gate?

--- [Page 242 of 255] ---
OLK D Qe 
O 
— 
= 
= 
O O O O 
—_——_O 
O 
= -OoO O 
—_O 
O 
O 
=t 
O O 
O 
O 
Q= CLKD + CLK Qyey 
D 
\N1=CLKD 
CLK— 
_V 
0 
CLK 
prev 
DA 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
 
Potential Problems with Sequential Logic Circuits
• This is an example of asynchronous 
circuit design in which outputs are 
directly fed back to inputs. 
• Asynchronous circuits are infamous for 
having race conditions where the 
behaviour of the circuit depends on 
which of two paths through logic gates is 
fastest.

--- [Page 243 of 255] ---
@ 
PES 
UNIVERSITY 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
 
Problem with Cyclic Paths
•
Sequential circuits contain feedback (cyclic) paths. 
•
These paths can cause race conditions and unstable behavior. 
•
Analyzing such circuits is difficult and may lead to design errors. 
Solution
•
Insert registers in the feedback path. 
•
Registers store the system state and update only on the clock edge. 
•
This converts the design into combinational logic + registers, eliminating races. 
Synchronous Sequential Circuit
State changes only at the rising edge of the clock. 
Uses: 
•
Current State – Present state of the system. 
•
Next State – State after the next clock edge. 
•
If the clock is slow enough for signals to settle, the circuit operates reliably.
Registers synchronize state changes with the clock, preventing race conditions and 
ensuring reliable sequential circuit operation.

--- [Page 244 of 255] ---
IIIIIIII 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
Rules of Synchronous Sequential Circuit Composition
A circuit is synchronous if:
•
Every circuit element is either a Register or Combinational Logic. 
•
The circuit contains at least one register. 
•
All registers share the same clock signal. 
•
Every feedback (cyclic) path contains at least one register. 
Asynchronous Sequential Circuit
•
Sequential circuits that do not follow these rules are called Asynchronous Circuits. 
•
They are more prone to race conditions and unpredictable behavior. 
Flip-Flop: Basic Synchronous Sequential Circuit
A Flip-Flop is the simplest synchronous sequential circuit. 
Inputs: D (Data), CLK (Clock) 
Output: Q 
States: {0, 1} 
Function: On every clock edge, the next state = D, and Q represents the current state. 
 Synchronous circuits use registers and a common clock to ensure predictable, stable, and reliable operation.
✅

--- [Page 245 of 255] ---
CLK 
'fl 
CLK 
CLK 
(e) 
'um 
= 
F 
= 
= 
E 
9HaA® 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
1From “Digital Design and Computer Architecture 2nd Ed.”, Harris and Harris, ©Elsevier, 2013.
Rules of Synchronous Sequential Circuit Composition

--- [Page 246 of 255] ---
@ 
PES 
UNIVERSITY 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
Circuit (a) is combinational, not sequential, because it has no registers.
(b) is a simple sequential circuit with no feedback. 
(c) is neither a combinational
circuit nor a synchronous sequential circuit, because it has a latch that is neither
a register nor a combinational circuit.
 (d) and (e) are synchronous sequential logic;
(f) is neither combinational nor synchronous sequential, because it has a cyclic
path from the output of the combinational logic back to the input of the same
logic but no register in the path. 
(g) is synchronous sequential logic in the form of a pipeline 
(h) is not, strictly speaking, a synchronous sequential circuit, because the second register receives a different clock 
signal than the first, delayed by two inverter delays.
1From “Digital Design and Computer Architecture 2nd Ed.”, Harris and Harris, ©Elsevier, 2013.
Rules of Synchronous Sequential Circuit Composition

--- [Page 247 of 255] ---
IIIIIIII 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
Asynchronous vs. Synchronous Circuit Design
Asynchronous vs. Synchronous Circuit Design
•
Asynchronous circuits are more general and flexible since they are not restricted by a global 
clock. 
•
Similar to analog circuits, they can use arbitrary feedback and timing. 
•
Synchronous circuits are easier to design, verify, and implement, making them the preferred 
choice in digital systems. 
•
Asynchronous circuits are mainly used for: 
•
Communication between different clock domains. 
•
Handling inputs arriving at unpredictable times. 
•
Research in asynchronous design continues to provide innovative techniques that also benefit 
synchronous systems. 
•
Despite decades of research, nearly all modern digital systems are predominantly synchronous 
due to their simplicity and reliability.

--- [Page 248 of 255] ---
@ 
PES 
UNIVERSITY 
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
 
Think  About It
Classify the following logic circuits as combinational or synchrnous 
sequential or  neither
•
AND gate (output not connected to any input)
•
AND gate (output connected to an input)
•
D flip-flop
•
SR latch
•
Series of D flip-flops (with common clock) with output of one connected to the input 
of the next via  an inverter

--- [Page 249 of 255] ---
UNIVERSITY 
Reccontii 
sy 
MCQs
1. In a sequential logic circuit with an unresolved race condition, why is the 
output described as "unstable"?
A) Because the circuit consumes too much power
B) Because the flip-flops are not connected to any clock at all
C) Because the output depends on the order/timing of inputs rather than 
settling to one well-defined value
D) Because combinational gates need more chip area
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

--- [Page 250 of 255] ---
UNIVERSITY 
Reccontii 
sy 
MCQs
1. In a sequential logic circuit with an unresolved race condition, why is the 
output described as "unstable"?
A) Because the circuit consumes too much power
B) Because the flip-flops are not connected to any clock at all
C) Because the output depends on the order/timing of inputs rather than 
settling to one well-defined value
D) Because combinational gates need more chip area
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

--- [Page 251 of 255] ---
UNIVERSITY 
Reccontii 
sy 
MCQs
2. Race conditions are eliminated when flip-flops are synchronized to a 
common clock, provided that:
A) The clock is asynchronous
B) There is no clock signal
C) Multiple independent clocks are used
D) The clock time period is long enough
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

--- [Page 252 of 255] ---
UNIVERSITY 
Reccontii 
sy 
MCQs
2. Race conditions are eliminated when flip-flops are synchronized to a 
common clock, provided that:
A) The clock is asynchronous
B) There is no clock signal
C) Multiple independent clocks are used
D) The clock time period is long enough
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

--- [Page 253 of 255] ---
UNIVERSITY 
Reccontii 
sy 
MCQs
3. An AND gate whose output is fed back into one of its own inputs, with no 
flip-flop breaking the loop, would be classified as:
A) Synchronous sequential logic
B) Combinational logic
C) Neither combinational nor synchronous sequential (unbroken feedback 
loop, no clock)
D) A flip-flop
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

--- [Page 254 of 255] ---
UNIVERSITY 
Reccontii 
sy 
MCQs
3. An AND gate whose output is fed back into one of its own inputs, with no 
flip-flop breaking the loop, would be classified as:
A) Synchronous sequential logic
B) Combinational logic
C) Neither combinational nor synchronous sequential (unbroken feedback 
loop, no clock)
D) A flip-flop
SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

--- [Page 255 of 255] ---
PES 
UNIVERSITY 
heLconaTTiRD V=i 
THANK YOU
Team DLCD
Department of CSE and CSE(AI &ML)

```

---

<a id="doc-2"></a>
## Document 2: Unit 1 Descriptive Question Bank with Model Solutions (30 Pages)
**Source Document**: `resources/U1QB_soln.docx`
**OCR Extraction File**: `Resources_U1QB_soln.txt`

```
================================================================================
ORIGINAL DOCUMENT : U1QB_soln.docx
OCR PDF FILE      : Resources_U1QB_soln_ocr.pdf
TOTAL PAGES       : 30
WORD COUNT        : 3297
CHARACTER COUNT   : 18418
DATE EXTRACTED    : 2026-11-04 14:07:21
================================================================================

--- [Page 1 of 30] ---
DIGITAL LOGIC AND COMPUTER DESIGN
UNIT 1 — DESCRIPTIVE QUESTIONS WITH ANSWERS
PES University | Descriptive Question Bank | T1: Harris & Harris, 2nd Edition
Q1. Define a digital circuit. Explain the functional specification and timing 
specification of a digital circuit. Distinguish between input, output and internal 
nodes.
Answer:
A digital circuit is a network of elements that processes discrete-valued variables, 
generally represented using binary values 0 and 1.
A digital circuit can be viewed as a black box having:
1. One or more input terminals
2. One or more output terminals
3. A functional specification
4. A timing specification
Functional specification describes the relationship between inputs and outputs. For 
example, for an AND function, Y = AB. The output is 1 only when both inputs are 1.
Timing specification describes how long the output takes to respond after an input 
changes. Thus, two circuits may implement the same Boolean function but have different 
delays.
A node is a wire that carries a digital signal. An input node receives information from 
outside the circuit, an output node sends information to another circuit/system, and an 
internal node connects elements inside the circuit.
Therefore, a digital circuit must be analyzed from both functional and timing 
perspectives.

--- [Page 2 of 30] ---
Q2. A digital control system has three inputs A, B, C. The output Y must be HIGH 
whenever at least two of the inputs are HIGH. Obtain the truth table and derive the 
Boolean equation in sum-of-products form.
Answer:
Since the output is HIGH whenever at least two inputs are HIGH, the required input 
combinations are 011, 101, 110, and 111.
Truth table:
A B C | Y
0 0 0 | 0
0 0 1 | 0
0 1 0 | 0
0 1 1 | 1
1 0 0 | 0
1 0 1 | 1
1 1 0 | 1
1 1 1 | 1
The corresponding minterms are:
m3 = A'BC
m5 = AB'C
m6 = ABC'
m7 = ABC
Therefore:
Y = A'BC + AB'C + ABC' + ABC
or
Y = Σ(3,5,6,7).
This demonstrates obtaining a Boolean equation directly from a truth table in canonical 
sum-of-products form.

--- [Page 3 of 30] ---
Q3. For the Boolean function F(A,B,C) = Σ(1,3,5,7), obtain the canonical sum-of-
products expression and simplify it using a K-map.
Answer:
The minterms are:
1 = 001
3 = 011
5 = 101
7 = 111
Hence the canonical SOP expression is:
F = A'B'C + A'BC + AB'C + ABC
Factor C:
F = C(A'B' + A'B + AB' + AB)
The expression in brackets contains all possible combinations of A and B:
A'B' + A'B + AB' + AB = 1
Therefore:
F = C
Hence:
F = C.
A K-map gives the same result by grouping the four 1s corresponding to C = 1.

--- [Page 4 of 30] ---
Q4. Explain the difference between sum-of-products and product-of-sums canonical 
forms. Give a suitable example for each.
Answer:
In Sum-of-Products (SOP) form, the function is represented as an OR of product terms. 
Each product term corresponds to a row where the output is 1.
Example:
F(A,B) = Σ(1,3)
F = A'B + AB
In Product-of-Sums (POS) form, the function is represented as an AND of sum terms. 
Each maxterm corresponds to a row where the output is 0.
Example:
F = Π(0,2)
F = (A+B)(A'+B)
Difference:
SOP is an OR of AND terms and is based on output-1 rows (minterms). POS is an AND 
of OR terms and is based on output-0 rows (maxterms). SOP uses Σ notation, while POS 
uses Π notation.

--- [Page 5 of 30] ---
Q5. A safety system produces output 1 for minterms 2, 3, 6, 7. Write the canonical 
SOP expression and explain how the resulting equation can be used to implement 
the circuit.
Answer:
For three variables A, B, C:
2 = 010
3 = 011
6 = 110
7 = 111
Therefore:
F = A'BC' + A'BC + ABC' + ABC
Factor B:
F = A'B(C'+C) + AB(C'+C)
Since C'+C = 1:
F = A'B + AB
F = B(A'+A)
F = B
Therefore:
F = B.
Implementation: instead of implementing four minterms using multiple gates, the 
minimized circuit can simply connect B to F. This reduces gate count, hardware 
complexity, and propagation delay.

--- [Page 6 of 30] ---
Q6. A digital system has the following functional requirement: the output should be 
HIGH when the input combination is 0, 2, 4, or 6. Derive the Boolean function and 
explain how a K-map can be used to minimize it.
Answer:
Assume three inputs A, B, C.
The required minterms are:
F = Σ(0,2,4,6)
Canonical SOP:
F = A'B'C' + A'BC' + AB'C' + ABC'
Every selected minterm has C = 0. Therefore, on the K-map the four 1s form a group of 
four. Within this group A and B change, while C remains 0.
Thus:
F = C'
Therefore:
F = C'.

--- [Page 7 of 30] ---
Q7. Explain the procedure for minimizing a Boolean function using a four-variable 
Karnaugh map. State the rules that must be followed while forming groups.
Answer:
A Karnaugh map is a graphical method for simplifying Boolean functions. A four-
variable K-map contains 2^4 = 16 cells.
Procedure:
1. Draw the four-variable K-map.
2. Enter 1s corresponding to the specified minterms.
3. Enter X for don't-care conditions if given.
4. Identify adjacent 1s.
5. Form groups containing 1, 2, 4, 8, ... cells.
6. Make groups as large as possible.
7. Groups may wrap around the edges.
8. A cell may belong to more than one group when useful.
9. Obtain the implicant corresponding to each group.
10. OR all required implicants.
The objective is to obtain a minimal expression using the fewest/largest valid groups.

--- [Page 8 of 30] ---
Q8. Minimize the following function using a four-variable K-map: F(A,B,C,D) = 
Σ(0,1,2,3,8,9,10,11).
Answer:
The minterms are 0, 1, 2, 3, 8, 9, 10, and 11. These eight cells form one group of eight.
Throughout this group:
B = 0
while A, C, and D vary.
Therefore the only remaining variable is B'.
Hence:
F = B'.

--- [Page 9 of 30] ---
Q9. Minimize F(A,B,C,D) = Σ(1,3,5,7,9,11,13,15) using a K-map. Explain your 
grouping.
Answer:
All the specified minterms are odd. In binary, every odd number has D = 1.
Therefore, all eight cells corresponding to D = 1 can be grouped together. A, B, and C 
vary within the group, while D remains constant.
Hence:
F = D.
Thus the minimized function is:
F = D.

--- [Page 10 of 30] ---
Q10. Minimize F(A,B,C,D) = Σ(0,2,8,10,11,14,15) using a four-variable K-map.
Answer:
Form the largest possible groups.
Group 1: minterms 0, 2, 8, 10 form a group of four. For this group B = 0 and D = 0, 
giving:
B'D'
Group 2: minterms 10, 11, 14, 15 form a group of four. For this group A = 1 and C = 1, 
giving:
AC
Therefore:
F = B'D' + AC.
The key point is to prefer maximum-sized valid groups so that the resulting expression 
contains fewer literals.

--- [Page 11 of 30] ---
Q11. What are don't-care conditions? Explain how they help in K-map 
minimization.
Answer:
A don't-care condition occurs when the output of a circuit does not matter for a particular 
input combination. It is represented by X.
In a K-map, an X can be treated as either 0 or 1 depending on which choice produces a 
simpler expression.
For example, if a circuit uses only decimal inputs 0–9, inputs 10–15 are invalid. Their 
outputs can therefore be treated as don't-cares.
A don't-care should be included in a group when it helps form a larger group. If it does 
not help, it can be ignored.
Advantages include fewer product terms, fewer literals, fewer gates, and simpler 
hardware.

--- [Page 12 of 30] ---
Q12. A seven-segment display receives a 4-bit input representing decimal digits 0–9. 
Inputs 10–15 are never used. Explain how these unused inputs can be exploited 
during K-map minimization.
Answer:
Since inputs 10–15 never occur during normal operation, their corresponding output 
values are irrelevant. They can be marked X in the K-map.
While grouping required 1s, these Xs may be included whenever they help produce a 
larger group. For example, a group of 2 may become a group of 4, or a group of 4 may 
become a group of 8.
Larger groups eliminate more variables, producing fewer gates and a simpler circuit.
Thus, unused input combinations can be exploited as don't-care conditions during K-map 
minimization.

--- [Page 13 of 30] ---
Q13. Why is the minimal K-map expression not necessarily unique? Explain with 
reference to prime implicants.
Answer:
A Boolean function can sometimes be minimized in more than one valid way. This 
happens when a particular 1-cell can be included in more than one equally large prime 
implicant.
A prime implicant is an implicant that cannot be combined further to remove another 
literal.
If two different valid groupings cover all required 1s and each produces an expression 
with the same minimum cost, both expressions are minimal.
Therefore, the minimal expression of a Boolean function is not necessarily unique. What 
matters is that the expression is logically equivalent to the original function and meets the 
desired minimization criterion.

--- [Page 14 of 30] ---
Q14. Explain the operation of a 2:1 multiplexer. Derive its Boolean equation and 
explain its truth table.
Answer:
A 2:1 multiplexer has two data inputs D0 and D1, one select input S, and one output Y.
Operation:
S = 0 -> Y = D0
S = 1 -> Y = D1
Therefore:
Y = S'D0 + SD1
When S = 0:
Y = 1·D0 + 0·D1 = D0
When S = 1:
Y = 0·D0 + 1·D1 = D1
Hence:
Y = S'D0 + SD1.
The multiplexer therefore selects one of several inputs and forwards the selected input to 
the output.

--- [Page 15 of 30] ---
Q15. Explain how a 4:1 multiplexer can be constructed using 2:1 multiplexers. 
Determine the number of 2:1 multiplexers required.
Answer:
A 4:1 MUX has D0, D1, D2, D3 and two select lines S1 and S0.
First stage:
- MUX 1 selects between D0 and D1 using S0.
- MUX 2 selects between D2 and D3 using S0.
Second stage:
- MUX 3 selects between the outputs of MUX 1 and MUX 2 using S1.
Therefore:
3 two-to-one multiplexers are required.
The first stage performs two selections in parallel, while the second stage selects between 
the resulting two signals.

--- [Page 16 of 30] ---
Q16. A processor needs to select one of eight possible data sources. Determine the 
type of multiplexer required and the number of select lines needed. Explain your 
answer.
Answer:
There are eight possible data inputs, so an 8:1 multiplexer is required.
For an N:1 multiplexer, the number of select lines is:
log2(N)
For N = 8:
log2(8) = 3
Therefore:
- Multiplexer required = 8:1
- Select lines required = 3
The three select bits provide 2^3 = 8 possible combinations, allowing each of the eight 
data sources to be selected.

--- [Page 17 of 30] ---
S2=/1=B0=C 
Q17. Implement F(A,B,C) = Σ(1,2,5,7) using an 8:1 multiplexer.
Answer:
An 8:1 MUX has three select inputs. Choose:
S2 = A, S1 = B, S0 = C.
The data inputs correspond to minterms 0 through 7. Since the function is 1 for minterms 
1, 2, 5, and 7:
D0 = 0
D1 = 1
D2 = 1
D3 = 0
D4 = 0
D5 = 1
D6 = 0
D7 = 1
Thus:
D0=0, D1=1, D2=1, D3=0, D4=0, D5=1, D6=0, D7=1.
With A, B, C connected to the select inputs, the MUX directly realizes the Boolean 
function.

--- [Page 18 of 30] ---
Q18. Explain the operation of a decoder. How is a decoder different from a 
multiplexer?
Answer:
A decoder converts an N-bit binary input into one of up to 2^N outputs. For example, a 2-
to-4 decoder has two inputs and four outputs. For each input combination, exactly one 
output is asserted.
Difference:
Multiplexer: many data inputs -> one output. It selects one input according to select lines.
Decoder: binary input -> one selected output. It identifies or activates an output according 
to the input code.
Thus, a MUX is primarily a data-selection circuit, whereas a decoder is primarily a code-
to-one-of-many-output circuit.

--- [Page 19 of 30] ---
Q19. A memory system contains eight memory modules. A 3-bit address is used to 
select exactly one module at a time. Explain how a decoder can be used for module 
selection.
Answer:
A 3-bit address has 2^3 = 8 possible combinations. Therefore, a 3:8 decoder can be used.
The three address bits are connected to the decoder inputs. Each decoder output 
corresponds to one memory module:
000 -> M0
001 -> M1
010 -> M2
011 -> M3
100 -> M4
101 -> M5
110 -> M6
111 -> M7
Only the selected decoder output is asserted, enabling the corresponding memory 
module. Thus, the decoder performs address decoding and ensures that one module is 
selected for each address.

--- [Page 20 of 30] ---
Q20. Differentiate between combinational and sequential logic. Explain the role of 
memory/state in sequential circuits.
Answer:
In a combinational circuit, the output depends only on the current inputs:
Y = f(X)
There is no memory of previous inputs. Examples include multiplexers and decoders.
In sequential logic, the output depends on current inputs and previous state:
Y = f(X,Q)
where Q represents stored state.
The state stores information about past events. Therefore, sequential circuits can perform 
functions such as counting, storing data, and controlling a sequence of operations.
The key distinction is that combinational logic has no memory, whereas sequential logic 
has state/memory.

--- [Page 21 of 30] ---
Q21. Given the input waveforms of an SR latch, explain how the output Q is 
determined. Discuss the SET, RESET and HOLD conditions.
Answer:
An SR latch has two inputs: S (Set) and R (Reset).
For an active-high SR latch:
S=0, R=0 -> HOLD
S=0, R=1 -> RESET
S=1, R=0 -> SET
S=1, R=1 -> invalid/forbidden
Set: when S=1 and R=0, Q becomes 1.
Reset: when S=0 and R=1, Q becomes 0.
Hold: when S=0 and R=0, the latch retains its previous state.
The important feature is memory: during HOLD, the current output depends on the 
previous state.

--- [Page 22 of 30] ---
Q22. A D latch is transparent when CLK=1. If D during a HIGH clock period is 0 -> 
1 -> 0 -> 1, explain the output sequence. What happens when the clock becomes 
LOW?
Answer:
A D latch is level-sensitive. When CLK=1, it is transparent, so Q follows D.
Therefore, during the HIGH clock period:
D: 0 -> 1 -> 0 -> 1
Q: 0 -> 1 -> 0 -> 1
When CLK becomes 0, the latch becomes opaque and holds its last value.
Therefore, after the clock goes LOW:
Q = 1
Even if D subsequently changes while CLK remains LOW, Q does not change until the 
latch becomes transparent again.

--- [Page 23 of 30] ---
Q23. Compare a D latch and a positive-edge-triggered D flip-flop for the same 
changing input signal. Explain why the two devices can produce different outputs.
Answer:
A D latch is level-sensitive. When its active clock level is present, changes in D can 
propagate to Q.
A positive-edge-triggered D flip-flop is edge-sensitive. It copies D to Q only at the rising 
clock edge.
If D changes several times while CLK is HIGH:
- A D latch can respond to all those changes.
- A positive-edge-triggered D flip-flop captures only the value present at the rising edge.
Therefore, the two devices can produce different output waveforms for the same input 
sequence.
This difference is fundamental: a latch is transparent during an active level, while a flip-
flop samples at a clock edge.

--- [Page 24 of 30] ---
Q24. Construct a T flip-flop using a D flip-flop and logic. Derive the required D 
input equation.
Answer:
A T flip-flop toggles when T=1 and holds its state when T=0.
Truth table:
T Q | Q+
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0
Therefore:
Q+ = T XOR Q
For a D flip-flop:
Q+ = D
Hence:
D = T XOR Q
So the implementation is:
1. Feed T and the current Q into an XOR gate.
2. Connect the XOR output to D.
3. Use the same clock for the D flip-flop.
Thus:
D = T 
 Q.
⊕

--- [Page 25 of 30] ---
Q25. A JK flip-flop is to be implemented using a D flip-flop. Derive the expression 
for D in terms of J, K and Q.
Answer:
The JK flip-flop has:
J=0, K=0 -> Hold
J=0, K=1 -> Reset
J=1, K=0 -> Set
J=1, K=1 -> Toggle
Its characteristic equation is:
Q+ = JQ' + K'Q
For a D flip-flop:
Q+ = D
Therefore:
D = JQ' + K'Q
Hence, a D flip-flop can implement a JK flip-flop by connecting the output of 
combinational logic implementing JQ' + K'Q to D.

--- [Page 26 of 30] ---
Q26. Explain the operation of an N-bit register. Why are multiple flip-flops 
required?
Answer:
An N-bit register stores an N-bit binary value. It is constructed using N flip-flops, 
normally D flip-flops, with a common clock.
For a 4-bit register:
Inputs: D3, D2, D1, D0
Outputs: Q3, Q2, Q1, Q0
At the active clock edge, all flip-flops capture their corresponding inputs simultaneously.
Therefore:
Q3:0+ = D3:0
Multiple flip-flops are required because each flip-flop stores one bit. Thus N bits require 
N storage elements.
A register is therefore a bank of flip-flops sharing a common clock.

--- [Page 27 of 30] ---
Q27. A processor register should load new data only when ENABLE is HIGH. 
When ENABLE is LOW, it must retain its previous value even when clock edges 
occur. Explain how an enabled flip-flop achieves this requirement.
Answer:
An enabled flip-flop has D, CLK, EN, and Q.
Its operation is:
EN=1 -> at the active clock edge, Q loads D.
EN=0 -> at the active clock edge, Q retains its old value.
Therefore:
Q+ = D, when EN=1
Q+ = Q, when EN=0
A MUX can be placed before the D input:
DFF = EN·D + EN'·Q
When EN=1:
DFF = D
When EN=0:
DFF = Q
Thus the old output is fed back and retained when the register is disabled.

--- [Page 28 of 30] ---
Q28. A digital system requires a flip-flop to return to a known state whenever 
RESET is asserted. Explain the purpose of a resettable flip-flop and distinguish 
between resetting the state and loading normal data.
Answer:
A resettable flip-flop contains an additional RESET input. When RESET is asserted, the 
flip-flop is forced to a known state, generally Q=0.
This is important because sequential circuits need a known starting state.
During normal operation, when RESET is inactive, the flip-flop captures D at the active 
clock edge:
Q+ = D
When RESET is asserted:
Q -> 0
Thus, RESET is used for initialization or recovery to a known state, while D is used for 
normal data storage.

--- [Page 29 of 30] ---
Q29. A ring oscillator consists of three identical inverters connected in a loop. Each 
inverter has a propagation delay of 2 ns. Determine the oscillation period and 
frequency. Explain why the circuit is not a stable combinational circuit.
Answer:
There are N=3 inverters and each has propagation delay tp=2 ns.
For a ring oscillator:
T = 2Ntp
Therefore:
T = 2(3)(2 ns)
T = 12 ns
Frequency:
f = 1/T
  = 1/(12 × 10^-9)
  ≈ 83.33 MHz
The circuit is not a stable combinational circuit because the output of each inverter is fed 
back into the input of another. The feedback prevents a stable Boolean assignment and 
causes the signal to continually propagate around the loop, producing oscillation.

--- [Page 30 of 30] ---
Q30. An elevator controller is designed for a building containing 25 floors, but floor 
13 does not exist. The controller must remember the current floor. Determine the 
minimum number of state bits required and explain your reasoning.
Answer:
The controller must represent 25 valid floor positions.
The number of state bits N must satisfy:
2^N >= 25
For 4 bits:
2^4 = 16 < 25
Therefore 4 bits are insufficient.
For 5 bits:
2^5 = 32 >= 25
Hence:
N = 5 state bits
Therefore, at least 5 bits of state are required to uniquely represent all 25 valid floor 
positions. The unused state encodings can be treated as invalid/unreachable states and 
handled appropriately in the controller design.

```

---

<a id="doc-3"></a>
## Document 3: Unit 1 Complete 120 Question Bank (19 Pages)
**Source Document**: `resources/QB.doc`
**OCR Extraction File**: `Resources_QB.txt`

```
================================================================================
ORIGINAL DOCUMENT : QB.doc
OCR PDF FILE      : Resources_QB_ocr.pdf
TOTAL PAGES       : 19
WORD COUNT        : 4455
CHARACTER COUNT   : 26529
DATE EXTRACTED    : 2026-11-04 14:05:07
================================================================================

--- [Page 1 of 19] ---
Digital Logic and Computer Design
UNIT 1 - Question bank(120 questions)
1. Differentiate between combinational and sequential logic circuits. 
Support your answer with two real-life analogies other than the 
automatic-door and ATM examples. 
2. Explain the rules that must be satisfied for a circuit to be considered a 
combinational circuit. In particular, discuss why cyclic paths are not 
permitted. 
3. State and explain the three rules that must simultaneously hold for a c
ircuit to be classified as combinational.
4. Explain why a circuit containing a cyclic feedback path cannot be 
classified as combinational, even if every individual element within it is 
itself combinational. 
5. A circuit is built from three combinational elements E1, E2, and E3, 
where E3 begins computing only after the outputs of both E1 and E2 
become valid. Given Delay(E1), Delay(E2), and Delay(E3), derive a 
general formula for the worst-case propagation delay of the overall circuit
 and explain your reasoning. 
6. Define the terms Literal, Implicant, Minterm, and Maxterm, giving 
one worked example of each for a 3-variable function with inputs a, b, c. 
7. Implement the Boolean function F = xy + x’y’ + y’z (a) With AND, 
OR, and inverter gates (b)  With OR and inverter gates (c) With AND and 
inverter gates (d) (e) With NAND and inverter gates With NOR and 
inverter gates.
8. Express the following function as a sum of minterms and as a product 
of maxterms: F(A, B, C, D) = B’D + A’D + BD.
9. Express the complement of the following functions in sum‐of
‐minterms form: ( a ) F(A,B ,C, D) = g(2, 4, 7, 10, 12, 14) (b) F ( x, y, z ) 
= w(3, 5, 7).
10. Starting from y = a′bc + ab′c′ + abc′ + abc, minimize the expression u
sing only Boolean algebra laws (distributive, complement, and identity 
laws). Show every intermediate step and name the law used at each stage. 
11. Convert the POS expression y = (a + b + c)(a + b′ + c)(a′ + b + c′) into 
its equivalent canonical SOP form, and then convert that SOP form back i
nto POS, showing every step so that the two final expressions match. 
12. What is meant by "logic minimization"? Describe at least three 
different metrics that can be used to judge the quality of a Boolean 
expression or its circuit realization, and state which specific metric is 
adopted as the standard in this course.

--- [Page 2 of 19] ---
13. For a three-variable Boolean function, explain how a truth table is 
converted into canonical SOP form. Include the construction of minterms 
and Σ-notation. 
14. For a three-variable Boolean function, explain how canonical POS 
form is obtained from the rows where the output is 0. Include maxterms a
nd Π-notation. 
15. Given a Boolean equation containing several product terms, simplify i
t using Boolean identities. Explain at every stage which identity is being a
pplied and compare the gate count before and after minimization.
16. State the Complement law, Identity law, and Distributive law used in 
Boolean minimization, and prove each using a truth table. Then apply all 
three, in sequence, to minimize y = xy′z + xyz + xyz′. 
17. Convert each of the following expressions into sum of products and p
roduct of sums: ( a ) ( u + xw )( x + u’v ) (b) x’ + x(x + y’)(y + z’)
18. Show that the dual of the exclusive‐OR is equal to its complement. 
19. Show that a positive logic NAND gate is a negative logic NOR gate a
nd vice versa. 
20. Write the Boolean equations and draw the logic diagram of the circuit 
whose outputs are defined by the following truth table:  
21. Determine whether the following Boolean equation is true or false. 
x’y’ + x’z + x’z’ = x’z’ + y’z’ + x’z .
22. Write the following Boolean expressions in sum of products form: 
(b+d)(a’ +b’ +c).
23. Write the following Boolean expression in product of sums form: a’b 
+a’c’ +abc.
24. Simplify the Boolean function F (x, y, z) = Σ(3, 4, 6, 7).
25. Explain why Boolean-algebra-based minimization becomes 
increasingly difficult and error-prone as the number of variables in a 
function increases, and describe how the K-map method overcomes this 
limitation. 
26. Explain why Karnaugh-map rows and columns are arranged in Gray-c
ode order rather than ordinary binary order. Demonstrate how this 
ordering guarantees that adjacent cells differ in only one variable.

--- [Page 3 of 19] ---
27. A student groups three cells together in a K-Map because all three 
cells contain 1. Explain why this grouping is invalid. State the rules 
governing the number and shape of cells in a valid K-Map group. 
28. Construct a 3-variable K-Map for   F(A,B,C)=Σ(0,1,2,4,5,6)  and 
obtain the minimum SOP expression. Clearly identify the groups and 
explain which variables are eliminated.
29. Explain the difference between an implicant, prime implicant, and 
essential prime implicant. Illustrate the difference using a suitable K-Map.
 
30. T Clock A sequential circuit has two JK flip-flops A and B and one 
input x . The circuit is described by the following flip-flop input 
equations: JA = x KA= B JB = x KB= A’ (a) Derive the state equations A 
( t + 1) and B ( t + 1) by substituting the input equations for the J and K v
ariables. (b) Draw the state diagram of the circuit. 
31. Starting from state a, and the input sequence 01110010011, determine 
the output sequence for (a) The state table of the previous problem. (b) 
The reduced state table from the previous problem. Show that the same o
utput sequence is obtained for both.
32. Minimize F(A,B,C)=Σ(0,2,3,4,6,7)  using a K-Map. Identify all useful 
prime implicants and determine which are essential.
33. What is the main difference between an initial statement and an 
always statement in Verilog HDL? 
34. Explain K-Map wrap-around adjacency. Demonstrate how cells at 
opposite edges of a K-Map can form a valid group. 
35. Explain the concept of don't-care conditions. Why can a don't-care 
cell be treated as either 0 or 1 during minimization? Give an example 
where assigning a don't-care as 1 produces a substantially simpler 
expression. 
36. A seven-segment display accepts a 4-bit input representing decimal 
digits 0–9. Inputs 10–15 are invalid. Construct the truth table and use K-
Maps to derive the simplified equation for segment Sa. 
37. Minimize f(a, b, c, d) = Σ(0, 1, 2, 3, 8, 9, 10, 11) using a 4-variable K-
map. Derive the simplest SOP expression and explain the reasoning 
behind every grouping used. 
38. A PN flip-flop has four operations: clear to 0, no change, complement,
 and set to 1, when inputs P and N are 00, 01, 10, and 11, respectively. (a) 
Tabulate the characteristic table. (b)  Derive the characteristic equation. 
(c) Tabulate the excitation table. (d) Show how the PN flip-flop can be 
converted to a D flip-flop.

--- [Page 4 of 19] ---
Next State 
Output 
Present State 
x=20 
x=1 
x=0 
x=1 
a 
J 
b 
0 
0 
b 
d 
C 
0 
0 
C 
Jr 
€ 
0 
0 
d 
g 
a 
| 
0 
e 
d 
C 
0 
0 
¥ 
E 
b 
1 
1 
g 
g 
h 
0 
1 
h 
g 
a 
| 
0 
X 
- 
y 
g 
Clk <] 
Clock 
39. For the following state table 
(a) Draw the corresponding state diagram.
(b)  Tabulate the reduced state table. 
(c) Draw the state diagram corresponding to the reduced state table. 
40. Explain the differences among a truth table, a state table, a 
characteristic table, and an excitation table. Also, explain the difference a
mong a Boolean equation, a state equation, a characteristic equation, and 
a flip-flop input equation. 
41. A sequential circuit has one flip-flop Q, two inputs x and y, and one o
utput S . It consists of a full-adder circuit connected to a D flip-flop, as 
shown in Fig . Derive the state table and state diagram of the sequential 
circuit.

--- [Page 5 of 19] ---
42. Explain why a group of 8 cells eliminates three variables, a group of 4 
eliminates two variables, and a group of 2 eliminates one variable. Derive 
this rule logically rather than merely stating it. 
43. Given a 4-variable K-Map with several 1s and don't-care cells, 
describe a systematic algorithm for obtaining the minimum SOP 
expression, starting from identifying the largest possible groups and 
ending with the selection of required groups.
44. A sequential circuit has three flip-flops A, B, C ; one input x_in ; and 
one output y_out . The state diagram is shown in Fig below . The circuit i
s to be designed by treating the unused states as don’t-care conditions. 
Analyze the circuit obtained from the design to determine the effect of the 
unused states. (a)Use D flip-flops in the design. (b) Use JK flip-flops in 
the design. 
45. Design the sequential circuit specified by the state diagram of Figure, 
using T flip-flops. 
46. Explain the operation of a 2:1 multiplexer using its block diagram, 
truth table, Boolean equation, and gate-level implementation. 
47. Derive the relationship between the number of inputs and select lines 
for a multiplexer. Determine the number of select lines required for 2:1, 4:
1, 8:1, 16:1, and 32:1 MUXes. Explain three different ways of 
implementing a 4:1 multiplexer:
i.
two-level logic,
ii.
tri-state buffers,
iii.
hierarchical composition of smaller MUXes.Compare their 
structures.

--- [Page 6 of 19] ---
48. Implement Y=A+B using a 2:1 multiplexer. Use one variable as the s
elect input and derive the required data inputs systematically from the 
truth table.
49. Explain the concept of a multiplexer (mux). Derive the general 
relationship between the number of data inputs N and the number of 
select lines required (log₂N), and tabulate this relationship for N = 2, 4, 8, 
and 16. 
50. Implement Y=A
B using a 2:1 multiplexer. Explain why your
⊕
 
selected data-input connections produce XOR.
51. Explain how a multiplexer can be used as a lookup table to implement 
an arbitrary Boolean function. Demonstrate the process using a three-
variable function and an 8:1 MUX. 
52. Implement a three-variable Boolean function using an 8:1 MUX. 
Determine the eight data-input values directly from the function's truth 
table and explain the mapping. 
53. Implement F(A,B,C)=Σ(1,3,5,7) using a 3:8 decoder and an OR gate. 
Clearly identify which decoder outputs must be connected to the OR gate 
and explain why the implementation works.
54. Compare implementing a Boolean function using a multiplexer versus 
implementing it using a decoder + OR gate. Discuss the selection 
mechanism, number of components, flexibility, and how the Boolean 
function maps onto the hardware. 
55. Explain the operation of an N-input decoder and why it produces 2N 
outputs. Explain the meaning of one-hot output and show how decoder 
outputs correspond to minterms. 
56. Implement F(A,B,C,D)=Σ(1,3,4,7,9,11,12,15) using a 4:16 decoder 
and external OR gates. Determine which decoder outputs must be 
connected.
57. Implement F(A,B,C)=A′B+AC using a 2:1 MUX. You are allowed to 
use one inverter. Determine:select input,I0,I1,inverter connection. Then v
erify your circuit using the truth table.
58. A decoder is constructed using two levels of logic gates. The first 
level has a propagation delay of 20ns, and the second level has a 
propagation delay of 30ns. Determine:
i.
the propagation delay,
ii.
the critical path,
iii.
the contamination delay if the corresponding gate 
contamination delays are given.
59. Explain why the longest path determines propagation delay.The 
textbook includes decoder design problems specifically involving critical 
path, propagation delay, and contamination delay

--- [Page 7 of 19] ---
60. Implement the following three Boolean functions using a single 3-
to-8 decoder: F1(A,B,C)=Σ(1,3,5) F2(A,B,C)=Σ(0,2,6,7) F3(A,B,C)=Σ(2,
3,6) Determine the decoder-output connections required for each function.
 Design an 8:1 multiplexer with the shortest possible delay from the data i
nputs to the output. You are given the available gate types and their 
propagation/contamination delays. Your answer must include:
i.
circuit structure,
ii.
critical path,
iii.
propagation delay,
iv.
contamination delay,
Justify 
why your architecture is faster than alternative
 
implementations.
61. A Boolean function is given by F(A,B,C,D)=Σ(0,2,3,6,7,8,10,14,15). 
Implement it using a 4:1 MUX with the minimum number of additional g
ates. You must:
i.
select appropriate select variables,
ii.
derive each data input,
iii.
simplify each data input,
iv.
identify the additional gates required,
v.
draw the final implementation.
62. The D latch of Figure is constructed with four NAND gates and an 
inverter. 
Consider the following three other ways for obtaining a D latch. In each c
ase, draw the logic diagram and verify the circuit operation.

--- [Page 8 of 19] ---
(a) Use NOR gates for the SR latch part and AND gates for the other two. 
An inverter may be needed.
(b) Use NOR gates for all four gates. Inverters may be needed.
(c) Use four NAND gates only (without an inverter). This can be done by 
connecting the output of the upper gate in Figure (the gate that goes to the 
SR latch) to the input of the lower gate (instead of the inverter output).
63. Given the input wave-forms shown in the Figure, sketch the output, Q,
 of an SR latch.
64. Given the input wave-forms shown in the Figure, sketch the output, Q,
 of an SR latch.
65. Given the input wave-forms shown in Figure, sketch the output, Q, of 
a D latch.
66. Given the input wave-forms shown in the Figure, sketch the output, Q,
 of a D latch.

--- [Page 9 of 19] ---
67. Design an asynchronously resettable D latch using logic gates.
68. Design an asynchronously resettable D flip-flop using logic gates.
69. Explain the differences among a truth table, a state table, a 
characteristic table, and an excitation table. Also, explain the difference a
mong a Boolean equation, a state equation,a characteristic equation, and a 
flip-flop input equation. 
70. A sequential circuit with two D flip-flops A and B, two inputs, x and 
y ; and one output z is specified by the following next-state and output 
equations:
A(t + 1) = xy’+ xB
B(t + 1) = xA + xB’
z = A
(a) Draw the logic diagram of the circuit.
(b) List the state table for the sequential circuit.
(c) Draw the corresponding state diagram.
71. A sequential circuit has one flip-flop Q, two inputs x and y, and one o
utput S.It consists of a full-adder circuit connected to a D flip-flop, as 
shown in the Figure . Derive the state table and state diagram of the 
sequential circuit.

--- [Page 10 of 19] ---
" 
YYY 
Full 
adder 
Clk <}— Clock 
lAr 
lB ; 
B 
ik 
Clk 
2N 
T 
A 
" 
Clock 
72.
73. Derive the state table and the state diagram of the sequential circuit s
hown in the Figure.Explain the function that the circuit performs.
74. For the circuit described by the state diagram of the Figure ,

--- [Page 11 of 19] ---
1,/0 
01 
Next State 
Output 
Present State 
x=0 
x=1 
=0 
x=1 
a 
i 
b 
0 
0 
b 
d 
c 
0 
0 
c 
¥ 
e 
0 
0 
d 
g 
a 
1 
0 
e 
d 
& 
0 
0 
f 
f 
b 
1 
1 
g 
g 
h 
0 
I 
h 
g 
a 
1 
0 
(a) Determine the state transitions and output sequence that will be 
generated when an input sequence of 010110111011110 is applied to the 
circuit and it is initially in the state 00.
(b) Find all of the equivalent states in the Figure and draw a simpler, but e
quivalent, state diagram.
(c) Using D flip-flops, design the equivalent machine (including its logic 
diagram) described by the state diagram in (b).
75. For the following state table
(a) Draw the corresponding state diagram.
(b) Tabulate the reduced state table.

--- [Page 12 of 19] ---
(c) Draw the state diagram corresponding to the reduced state table.
76. Starting from state a, and the input sequence 01110010011, determine 
the output sequence for
(a) The state table of the previous problem.
(b) The reduced state table from the previous problem. Show that the 
same output sequence is obtained for both.
77. Design a sequential circuit with two D flip-flops A and B, and one 
input x_in .
(a) When x_in = 0, the state of the circuit remains the same. When x_in = 
1, the circuit goes through the state transitions from 00 to 01, to 11, to 10, 
back to 00, and repeats.
(b) When x_in = 0, the state of the circuit remains the same. When x_in =
1, the circuit goes through the state transitions from 00 to 11, to 01, to 10, 
back to 00, and repeats.
78. Which of the circuits in the Figure  are synchronous sequential 
circuits? Explain.

--- [Page 13 of 19] ---
0 
79. Implement a full adder with two 4x1 multiplexers. 
80. Design a combinational circuit with three inputs, x, y, and z, and three 
outputs, A, B, and C. When the binary input is 0, 1, 2, or 3, the binary 
output is one greater than the input. When the binary input is 4, 5, 6, or 7, 
the binary output is two less than the input. 
81. A majority circuit is a combinational circuit whose output is equal to 
1 if the input variables have more 1's than 0's. The output is 0 otherwise. 
(a)* Design a 3-input majority circuit by finding the circuit's truth table, 
Boolean equation, and a logic diagram. (b) Write and verify a Verilog 
gate-level model of the circuit. 
82. Design a four-bit combinational circuit 2's complementer. (The output 
generates the 2's complement of the input binary number.) Show that the 
circuit can be constructed with exclusive-OR gates. Can you predict what 
the output functions are for a five-bit 2's complementer? 
83. In an SR latch, both S and R are accidentally asserted high at the 
same time due to a wiring fault. Predict the resulting outputs Q and Q', 
and explain why this condition is considered invalid or problematic for 
circuit design.
84. You are designing a circuit and need the stored value to change 
immediately whenever the data input changes, as long as the clock is high
 Would you choose a D latch or a D flip-flop for this requirement? Justify 
your choice.

--- [Page 14 of 19] ---
85. Two flip-flops in a circuit are accidentally connected to two different 
clock signals, clk1 and clk2, instead of a shared clock. Explain what 
problems this could cause in a supposedly synchronous system, and how 
you would fix it.
86. A system needs all its flip-flops to start from a known state (0) the 
moment power is turned on, without waiting for a clock edge. Which type 
of flip-flop input would you use, and how would its internal circuit differ 
from a standard resettable flip-flop?
87. A ring oscillator is built using five inverters instead of three, each 
with a propagation delay of 1 ns. Derive the oscillation period of this 
circuit and generalize a formula for an odd-numbered inverter loop, 
explaining why an even number of inverters would not oscillate in the 
same way.
88. Ben Bitdiddle has designed the circuit in the Figure  to compute a 
registered four-input XOR function. Each two-input XOR gate has a 
propagation delay of 100 ps and a contamination delay of 55 ps. Each 
flip-flop has a setup time of 60 ps, a hold time of 20 ps, a clock-to-Q 
maximum delay of 70 ps, and a clock-to-Q minimum delay of 50 ps.
(a) If there is no clock skew, what is the maximum operating 
frequency of the circuit?
(b) How much clock skew can the circuit tolerate if it must operate 
at 
2 GHz?
(c) How much clock skew can the circuit tolerate before it might 
experience a hold time violation?
89. Alyssa P. Hacker points out that she can redesign the combinational l
ogic between the registers to be faster and tolerate more clock skew. Her i
mproved circuit also uses three two-input XORs, but they are arranged 
differently. What is her circuit? What is its maximum frequency if there i
s no clock skew? How much clock skew can the circuit tolerate before it 
might experience a hold time violation?

--- [Page 15 of 19] ---
90. Two D flip-flops are connected back-to-back (output of the first 
feeding the input of the second) and share the same clock signal, but a 
buffer introduces a small delay between the clock reaching the first and 
second flip-flop. Analyze whether this circuit will function correctly as a 
synchronous shift register, and identify the potential failure mode this 
delay could introduce (hint: consider hold-time violations).
91. You are asked to design a resettable, enabled D flip-flop that must 
also synchronously load new data only when EN is high, and reset to 0 
regardless of D when RESET is high, without introducing clock glitches. 
Draw a gate-level design combining the enable and reset logic, and justify 
the order in which the reset and enable conditions should be prioritized.
92. What is the difference between a latch and a flip-flop? Under what 
circumstances is each one preferable?
93. A combinational circuit's output is mistakenly fed back into one of its 
own inputs without any register in the path, but the designer argues the 
circuit is "fast and works fine in simulation." Explain, using the concept o
f race conditions and propagation delay, why this design is unsafe for real 
hardware even if simulation shows no errors.
94. Given a synchronous circuit with a feedback path containing exactly 
one register, and a clock period that is deliberately shortened until errors 
appear, explain — in terms of combinational propagation delay and setup 
time — what determines the minimum safe clock period, and derive a 
general inequality relating clock period, propagation delay, and setup 
time for correct operation.

--- [Page 16 of 19] ---
[ 
CLK 
| 
95. Ben Bitdiddle has hundreds of friends coming to his party and needs t
o bake cookies faster. He is considering using spatial and/or temporal 
parallelism.
a)
Spatial Parallelism: Ben asks Alyssa P. Hacker to help out. She has 
her own cookie tray and oven.
b)
Temporal Parallelism: Ben gets a second cookie tray. Once he puts 
one cookie tray in the oven, he starts rolling cookies on the other tray 
rather than waiting for the first tray to bake.
c)
What is the throughput and latency using spatial parallelism? Using 
temporal parallelism? Using both?
96. Given the input waveforms shown in the Figure, sketch the output Q, 
of a D flip-flop.
97. Given the input waveforms shown in the Figure, sketch the output, Q, 
of a D flip-flop.
98. Explain why combinational logic circuits cannot "remember" data, 
and describe how breaking the no-feedback restriction enables storage 
elements.
99. Describe the bistable operation of a cross-coupled inverter loop and e
xplain why it is not practical as a usable memory element.

--- [Page 17 of 19] ---
100.
With the help of a circuit diagram, explain the working of an SR 
latch built from two cross-coupled NOR gates, and describe the 
significance of its invalid state.
101.
 Why is the SR latch considered "awkward," and how does the D 
latch resolve this problem by separating the concepts of "what" 
and "when"?
102.
Explain the transparent (level-sensitive) behavior of a D latch when 
CLK = 1 and CLK = 0.
103.
 Describe how a D flip-flop is constructed from two back-to-back 
D latches (master-slave configuration), and explain its operation on the 
rising clock edge.
104.
 Differentiate between a latch and a flip-flop in terms of triggering 
mechanism, with relevant examples.
105.
 Explain the working of an enabled flip-flop and describe two 
different circuit techniques used to implement it.
106.
Describe the difference between a synchronously resettable and an 
asynchronously resettable flip-flop, with the help of a circuit diagram.
107.
What is an N-bit register? Explain its structure and significance as 
a building block of sequential circuits.
108.
Explain how race conditions arise in sequential circuits containing 
cyclic feedback paths, and describe how inserting registers eliminates 
them.
109.
With reference to the three-inverter loop example, explain what an 
astable circuit (ring oscillator) is and describe its output behavior over 
time.
110.
 State and explain the four rules that a circuit must satisfy to be 
classified as a synchronous sequential circuit.
111.
Differentiate between synchronous and asynchronous circuit 
design, and explain why most modern digital systems favor synchronous 
design.
112.
Analyze the classification of different example circuits 
(combinational, synchronous sequential, or neither) based on the presence 
of registers and feedback paths.

--- [Page 18 of 19] ---
113.
A cross-coupled NAND-based SR latch (S'R' latch) is used in a 
circuit where both inputs are inadvertently pulled low (S'=0, R'=0) briefly 
during a glitch. Predict the resulting state of Q and Q', and explain why 
this differs from the invalid condition of the NOR-based SR latch.
114.
You are given a black-box sequential element and told only that its 
output changes multiple times while the clock is held high. Determine, 
with reasoning, whether this element is a latch or a flip-flop, and describe 
an experiment (input pattern) you could apply to confirm your answer.
115.
A 4-bit register is built from four D flip-flops sharing a common 
clock, but one flip-flop's clock line has a broken trace causing it to 
receive a stuck-low signal. Predict the observable behavior of the 
register's output bus D3:0 → Q3:0, and explain how this fault could be 
diagnosed using only input/output waveforms.
116.
In a synchronously resettable flip-flop built using an AND gate 
ahead of the D input, the RESET signal glitches briefly HIGH for a 
duration shorter than the clock period, occurring while CLK = 0. Explain 
whether this glitch will affect the stored state, and contrast this with what 
would happen in an asynchronously resettable design under the same 
glitch.
117.
A designer cascades two enabled flip-flops (Flip-Flop A's output 
feeds Flip-Flop B's D input) and toggles EN on Flip-Flop A while CLK is 
HIGH, violating the stated design rule. Explain, using the concept of 
clock gating, what specific hazard this could introduce into the circuit's b
ehavior.
118.
A digital system needs to load a new value into a flip-flop only 
once every 4 clock cycles, otherwise retain its current value. Design the r
equired circuit modification and explain how it behaves using a timing 
diagram.
119.
You are given a D flip-flop and a D latch, both fed the same D and 
CLK waveforms containing glitches while CLK = 1. Sketch and justify 
the resulting Q output for each device, explaining why their behavior 
differs.
120.
A synchronous sequential circuit is composed of combinational 
logic blocks and registers, but a designer accidentally omits a register on 
one of the feedback paths while keeping registers on all others. Explain w
hy this circuit fails the formal definition of a synchronous sequential 
circuit, and predict what kind of behavioral problems could result during 
operation.

--- [Page 19 of 19] ---
121.
Consider a system with two independent clock domains, each 
synchronous internally, that need to exchange a single data bit. Using the 
asynchronous-vs-synchronous design concepts discussed, explain why 
directly connecting a flip-flop output from one clock domain to a flip-flop 
input in the other domain is risky, and propose a safer approach at a 
conceptual level.

```

---

<a id="doc-4"></a>
## Document 4: Lecture Notes: Problem Solving 1
**Source Document**: `notes/question1.jpeg`
**OCR Extraction File**: `Notes_question1.txt`

```
================================================================================
ORIGINAL DOCUMENT : question1.jpeg
OCR PDF FILE      : Notes_question1_ocr.pdf
TOTAL PAGES       : 1
WORD COUNT        : 131
CHARACTER COUNT   : 817
DATE EXTRACTED    : 2026-11-04 14:03:53
================================================================================

--- [Page 1 of 1] ---
VRS wasts TR 0020 
- 
Exercise 3.26 You have been enlisted to design a soda machine dispenser for yo 
department lounge. Sodas are partially subsidized by the student chapter of the 
IEEE. so they cost only 25 cents. The machine accepts nickels, dimes, and quarter;, 
When enough coins have been inserted, it dispenses the soda and returns any 
necessary change. Design an FSM controller for the soda machine. The FSM inpus 
are Nickel, Dime, and Quarter, indicating which coin was inserted. Assume that 
exactly one coin is inserted on each cycle. The outputs are Dispense, ReturnNicke, 
ReturnDime, and ReturnTwoDimes. When the FSM reaches 25 cents, it asserts 
Dispense and the necessary Return outputs required to deliver the appropriate 
change. Then it should be ready to start accepting coins for another soda.

```

---

<a id="doc-5"></a>
## Document 5: Lecture Notes: Sequential Logic & Latches (Part 1)
**Source Document**: `notes/sequential-1.jpg`
**OCR Extraction File**: `Notes_sequential-1.txt`

```
================================================================================
ORIGINAL DOCUMENT : sequential-1.jpg
OCR PDF FILE      : Notes_sequential-1_ocr.pdf
TOTAL PAGES       : 1
WORD COUNT        : 20
CHARACTER COUNT   : 97
DATE EXTRACTED    : 2026-11-04 14:03:54
================================================================================

--- [Page 1 of 1] ---
o oI 
Yorg 
(ordiRgn Wheae Qo 
Lo loulsuon 
S§ o 
S B AL 
SR Jatry 
Shaengh 
QAL 
%a‘ha 
3 
J{\om

```

---

<a id="doc-6"></a>
## Document 6: Lecture Notes: Sequential Logic & Latches (Part 2)
**Source Document**: `notes/sequential-2.jpg`
**OCR Extraction File**: `Notes_sequential-2.txt`

```
================================================================================
ORIGINAL DOCUMENT : sequential-2.jpg
OCR PDF FILE      : Notes_sequential-2_ocr.pdf
TOTAL PAGES       : 1
WORD COUNT        : 0
CHARACTER COUNT   : 0
DATE EXTRACTED    : 2026-11-04 14:03:55
================================================================================

--- [Page 1 of 1] ---


```

---

# PART 2: DLCD SYNTHESIZED STUDY PACKAGE

<a id="res-1"></a>
## Synthesized Resource 1: DLCD_Unit_1_Clean_Slides.md
**Source File**: `resources/DLCD_Unit_1_Clean_Slides.md`

# Unit 1: Combinational and Sequential Logic Design - Clean Lecture Notes

> Cleaned and condensed from original slides. Diagram artifacts, watermark overlaps, and animation duplicates removed.

### Slide 2: ::
- Introduction
- Boolean Equations
- Karnaugh maps
- Combinational building Blocks.
- Introduction
- Latches and Flip-Flops
- Synchronous Logic Design
- Finite state Machines

### Slide 3: Introduction
- What is a circuit?
- In digital electronics, a circuit is a network that processes discrete-valued variables.
- A circuit can be viewed as a black box, shown as in Figure with
- one or more discrete-valued input terminals
- one or more discrete-valued output terminals
- a functional specification describing the relationship between inputs and outputs
- a timing specification describing the delay between inputs changing and outputs
- responding.

### Slide 4: Circuits
- Introduction
- Nodes
- **Inputs:** A, B, C
- **Outputs:** Y, Z
- **Internal:** n1
- Circuit elements
- E1, E2, E3
- Each a circuit

### Slide 5: Types
- LOGIC
- DESIGN
- of Logic
- Circuits
- Introduction
- Types of Digital circuits/logic
- Combinational Logic
- Memory less
- Outputs determined only by current values of inputs

**Examples:**
- Adders, Multiplexers, Decoders, Encoders, Comparators
- Sequential Logic
- Has memory
- Outputs determined by previous and current values of inputs

**Examples:**
- Registers, Counters, Flip-flops, Memory devices

### Slide 6: Rules
- LOGIC DESIGN Composition
- of Combinational
- Introduction
- Combinational Logic
- A circuit is combinational if it consists of interconnected circuit
- elements such that
- Every circuit element is itself combinational.
- Every node of the circuit is either designated as an input to
- the circuit or connects to exactly one output terminal of a
- circuit element.
- The circuit contains no cyclic paths: every path through the
- circuit visits each circuit node at most once.

### Slide 7: Rules
- LOGIC DESIGN Composition
- of Combinational
- Introduction
- Which of the circuits are combinational circuits according to the rules of combinational
- composition?
- Circuit (a) is combinational.
- (b) is not combinational, because there is a cyclic path
- starting at n4 passes through the XOR to n5,which returns
- to n4.
- (c) is combinational.
- (d) is not combinational, because node n6 connects to
- the output terminals of both I3 and I4.
- (e)Is combinational, illustrating two combinational circuits
- connected to form a larger combinational circuit.
- (f) does not obey the rules of combinational composition
- because it has a cyclic path through the two elements.
- Depending on the functions of the elements, it may or
- may not be a combinational circuit

### Slide 8: Circuits
- Think About it?

**MCQ 1**
- A designer replaces E2 with a faster implementation that preserves the
- same Boolean function.
- Which statement is most accurate?

**A. Functional specification changes.**

**B. Timing specification may improve while functionality remains unchanged.**

**C. Both functional and timing specifications change.**

**D. Overall logic becomes sequential.**
- Correct Answer B

### Slide 9: Circuits
- Think About it?

**MCQ 2**
- **Assume:** 
- Delay(E1) = 5 ns
- Delay(E2) = 8 ns
- Delay(E3) = 4 ns
- E3 begins computation only after both E1 and E2 outputs
- become valid.
- What is the worst-case propagation delay?
- **Correct Answer:** B

**A. 9 ns**
- **Explanation:** 

**B. 12 ns**
- Longest input path =
- max(5,8)+4 = 12 ns

### Slide 10: Circuits
- Think About it?

**MCQ 3**
- Consider two digital circuits:
- **Circuit X:** Output depends only on current inputs.
- **Circuit Y:** Output depends on previous and current inputs.
- Which classification is correct?

**A. X is Sequential, Y is Combinational**

**B. X is Combinational, Y is Sequential**

**C. Both are Sequential**

**D. Both are Combinational**
- Correct Answer B
- X is Combinational, Y is
- Sequential

### Slide 13: Boolean Equations
- Combinational logic design
- Logic Minimization, K-Maps
- Sequential logic design
- Concepts covered
- Boolean Formula Terminology
- Sum of Products and Product of
- Sums standard forms
- Truth Table to Boolean Formula
- Logic Circuit
- Logic Minimization using Boolean
- Identities

### Slide 14: Boolean
- LOGIC
- DESIGN
- Equations
- Boolean Equations
- Functional specification of outputs in terms of inputs

**Example: S**
- = F(A, B, Cin)
- Cout = F(A, B, Cin)
- Cin
- Cout
- = A  B  Cin
- Cout = AB + ACin + BCin

### Slide 15: Some
- Definitions
- Boolean Equations
- Terminology
- **Complement:** variable with a bar over it
- A’, B’, C’
- **Literal:** variable or its complement
- A, A’, B, B’, C, C’
- **Implicant:** product of literals
- ABC, A’C, BC’
- **Minterm:** product that includes all input variables
- A’B’C’, AB’C,ABC
- **Maxterm:** sum that includes all input variables
- (A+B+C’), (A+B’+C), (A’+B’+C’)

### Slide 16: Boolean Formula Terminology
- Literal Boolean variable or its complement (ex:c’)
- Product (or implicant) AND of two or more literals (ex: abc’)
- Minterm Product involving all inputs to Boolean function
- minterm
- a’b’c’
- name
- a’b’c
- a’bc’
- a’bc
- ab’c’
- ab’c
- Minterms for three inputs
- a, b and c
- abc’

### Slide 17: Boolean Formula Terminology
- Sum OR of two or more literals
- Maxterm Sum involving all inputs to Boolean function
- maxterm
- a+b+c
- Name
- a+b+c’
- a+b’+c
- a+b’+c’
- a’+b+c
- a’+b+c’
- a’+b’+c
- a’+b’+c’
- Maxterms for three inputs a,
- b and c

### Slide 18: From Truth Table to Boolean Formula and its Minimization
- Given a combinational logic circuit or Boolean formula, we have learnt to
- construct its truth table
- But, given a truth table, how to construct a Boolean formula (or combinational
- logic circuit) for it?
- Also, as there are multiple Boolean formulas / logic circuits for each truth table,
- how to pick the minimal one?
- Above problem is called logic minimization
- **many metrics:** smallest, fastest, least power consumption
- **our metric:** smallest two level Sum of Products formula
- may be more than one solution

### Slide 20: AND
- SEQUENTIAL
- LOGIC
- DESIGN
- Sum-of-Products
- (SOP)
- Form
- Boolean Equations
- Sum-of-Products
- Form
- Sum of Products Form
- All equations can be written in SOP form
- Each row has a minterm
- A minterm is a product (AND) of literals
- Each minterm is TRUE for that row (and only that row)
- Form function by ORing minterms where the output is TRUE
- Thus, a sum (OR) of products (AND terms)
- Y = F(A, B) =
- minterm
- minterm name
- A B
- A B
- A B
- A B

### Slide 21: Sum-of-Products
- (SOP)
- Form
- Boolean Equations
- Sum-of-Products
- Form
- Sum of Products Form
- All equations can be written in SOP form
- Each row has a minterm
- A minterm is a product (AND) of literals
- Each minterm is TRUE for that row (and only that row)
- Form function by ORing minterms where the output is TRUE
- Thus, a sum (OR) of products (AND terms)
- Y = F(A, B) = A’B + AB = Σ(1, 3)
- minterm
- minterm name
- A B
- A B
- A B
- A B

### Slide 22: Boolean
- Equations

**Example**
- Boolean Equations
- Sum of Products Form
- Ben Bitdiddle is having a picnic. He won’t enjoy it if it rains or if
- there are ants.Design a circuit that will output TRUE only if Ben
- enjoys the picnic
- **Solution:** First define the inputs and outputs. The inputs are A and R,
- which indicate if there are ants and if it rains. A is TRUE when there
- are ants and FALSEwhen there are no ants.
- Likewise, R is TRUE when it rains and FALSE when the sun smiles on
- Ben. The output is E, Ben’s enjoyment of the picnic. E is TRUE
- if Ben enjoys the picnic and FALSE if he suffers.
- Using sum-of-products form, we write the equation as: E = A’R’ or
- E = Σ0

### Slide 23: Boolean Formula using Sum of Products (SOP)
- SOP Form
- Sum of all minterms corresponding to a 1 output
- SOP Example
- **Trutha table:** 
- b c y
- minterm
- name
- a’b’c’
- a’b’c
- a’bc’
- a’bc
- ab’c’
- ab’c
- abc’
- abc
- **SOP form Boolean formula:** 
- y = a’bc + ab’c’ + abc’ + abc
- y = m3 + m4 + m6 + m7
- **Sigma (Σ) notation:** 
- y = Σ(m3, m4, m6, m7)
- y = Σ(3, 4, 6, 7)
- If the Boolean function is called f :
- y = f (a, b, c)

### Slide 24: Product-of-Sums
- (POS)
- Form
- Boolean Equations
- Product of Sums Form
- All Boolean equations can be written in POS form
- Each row has a maxterm
- A maxterm is a sum (OR) of literals
- Each maxterm is FALSE for that row (and only that row)
- Form function by ANDing the maxterms for which the output is
- FALSE
- Thus, a product (AND) of sums (OR terms)
- Y = F(A, B) = (A + B)(A’ + B) = Π(0, 2)
- maxterm
- Y maxterm name
- 0 A + B
- 1 A + B
- 0 A + B
- 1 A + B

### Slide 28: Boolean Formula using Products of Sum (POS)
- POS Form
- Product of all maxterms corresponding to a 0 output
- POS Example
- Truth
- **table:** 
- maxterm
- a+b+c
- name
- a+b+c’
- a+b’+c
- **SOP form Boolean formula:** 
- y = (a +b +c)(a +b+c’)(a +b’
- +c)(a’ +b +c’)
- y = M 0 M1 M 2 M5
- a+b’+c’
- a’+b+c
- **Pi (Π) notation:** 
- y = Π(M0M1M2M5)
- a’+b+c’
- If the Boolean function is called
- **f:** 
- (a, b,a’+b’+c
- c)
- 1 y
- 1 =
- 0f 1
- y = Π(0, 1, 2, 5)

### Slide 30: Boolean
- Equations

**Example**
- Boolean Equations
- You are going to the cafeteria for lunch
- You won’t eat lunch (E)
- If it’s not open (O) or
- If they only serve corndogs (C)
- Write a truth table for determining if you will eat lunch (E).

### Slide 31: SOP & POS Form
- Boolean Equations
- SOP – sum-of-products
- SOP & POS Form
- minterm
- O C
- O C
- O C
- O C
- maxterm
- E = OC
- = Σ(2)
- POS – product-of-sums
- O + C
- O + C
- O + C
- O + C
- E = (O + C)(O + C)(O + C)
- = Π(0, 1, 3)

### Slide 32: Boolean Equations
- SOP & POS Form
- SOP – sum-of-products
- minterm
- O C
- O C
- O C
- O C
- maxterm
- O + C
- O + C
- O + C
- O + C
- POS – product-of-sums

### Slide 33: Logic Minimization
- Logic Minimization

**Example**
- **Minimize:** 
- y = a’bc + ab’c’ +
- abc’ + abc

### Slide 34: Logic Minimization
- Logic Minimization Example
- **Minimize:** 
- The three representations below are different ways of
- specifying the same Boolean function:
- y = a’bc + ab’c’ + abc’ + abc
- y = bc(a’ + a) + ac’(b’ + b)
- **Using distributive law:** 
- **Using complement law:** 
- y = bc(1) + ac’(1)
- **Using identity law:** 
- y = bc + ac’
- ac’+ b c

### Slide 35: Logic Minimization
- Logic Minimization Example
- **Minimize:** 
- y = a’bc + abc’ + abc’ + abc
- **Using distributive law:** 
- y = bc(1) + ac’(1)
- **Using complement law:** 
- y = bc(a’+ a) + ac’(b’ + b)
- **Using identity law:** 
- y = bc + ac’
- The three representations below are different ways of
- specifying the same Boolean function:
- a·c+ b·c

### Slide 36: Boolean Equations

**MCQ 1**

**1.What is a " minterm" in Boolean algebra?**
- A) A sum of two or more literals
- B) A product (AND) involving all inputs to the Boolean function
- C) Any single literal
- D) A product involving only some inputs
- Correct Answer B

### Slide 37: Boolean Equations

**MCQ 2**

**2. In Product-of-Sums (POS) form, how is a Boolean formula constructed?**
- A) Sum of all minterms corresponding to a 1 output
- B) Product of all maxterms corresponding to a 0 output
- C) Product of all minterms corresponding to a 1 output
- D) Sum of all maxterms corresponding to a 0 output
- Correct Answer B

### Slide 38: Boolean EquationsCircuits

**MCQ 3**
- A Boolean function has four inputs and is TRUE only for
- m(3,7,11,15)
- Which characteristic do these minterms share?

**A. A=1**

**B. D=1**

**C. C=0**

**D. B=1**
- Correct Answer B
- (Each binary
- representation ends with
- D = 1.)

### Slide 39: Boolean Equations

### Slide 41: DIGITAL LOGIC AND
- COMPUTER DESIGN
- Karnaugh Maps

### Slide 42: Karnaugh Maps

### Slide 43: Karnaugh Maps- Three Input
- Why use K-Maps?
- minterm
- a’b’c’
- a’b’c
- a’bc’
- a’bc
- ab’c’
- ab’c
- abc’
- abc
- name

**Example 1**
- **SOP form:** 
- y = a’bc+ ab’c’ + abc’+ abc
- **Minimized form:** 
- y = bc + ac’
- **Minimization requires:** 
- Combining implicants on row 3 and 7
- Combining implicants on row 4 and 6
- Takes some effort to determine implicants
- to combine

### Slide 44: Karnaugh Maps- Three input
- Why use K-Maps?
- minterm
- a’b’c’
- a’b’c
- a’bc’
- a’bc
- ab’c’
- ab’c
- abc’
- abc
- **Minimizing:** 
- y = bc + ac’ + ab
- **Requires converting to:** 
- bc + ac’ + ab(c + c’)
- name

**Example 1**
- **SOP form:** 
- y = a’bc + ab’c’ + abc’+ abc
- **Minimized form:** 
- y = bc + ac’
- **Minimization requires:** 
- Combining implicants on row 3 and 7
- Combining implicants on row 4 and 6
- Takes some effort to determine implicants to
- combine
- **Minimization may require:** 
- Unintuitve steps
- Trial and error
- So minimization with Boolean identities is important to know since useful in some cases, but difficult to use in general

### Slide 45: Karnaugh Maps- Three input
- K-Map Structure
- Kanaugh Map (K-Map)
- Maurice Karnaugh’s refinement in
- 1953 of original idea from 1881
- **Key idea:** Minterms that differ in
- one literal must be adjacent
- Utilize brain’s visual processing for
- efficient logic minimization
- minterm
- a’b’c’
- a’b’c
- a’bc’
- a’bc
- ab’c’
- ab’c
- abc’
- abc
- K-Map Structure (three input Boolean functon)
- a’b’c’ 0
- a’b’c 1 a’bc 3
- a’bc’2
- ab’c’4
- ab’c5 abc
- abc’
- Each square corresponds to a row of the truth table
- Any two adjacent squares differ only in one literal
- Achieved using two rows and binary order 00,01,11,10
- **Notion of “wrap-around”:** far left and right squares are
- adjacent

### Slide 46: Karnaugh Maps- Three input
- K-Map Structure
- Kanaugh Map (K-Map)
- Maurice Karnaugh’s refinement in
- 1953 of original idea from 1881
- **Key idea:** Minterms that differ in
- one literal must be adjacent
- Utilize brain’s visual processing for
- efficient logic minimization
- minterm
- a’b’c’
- a’b’c
- a’bc’
- a’bc
- ab’c’
- ab’c
- abc’
- abc
- K-Map Structure (three input Boolean functon)
- Each square corresponds to a row of the truth table
- Any two adjacent squares differ only in one literal
- Achieved using two rows and binary order 00,01,11,10
- **Notion of “wrap-around”:** far left and right squares are
- adjacent

### Slide 47: Karnaugh Maps- Three input
- K-Map Method
- K-Map Implicants
- Implicant
- K-Map area composed of squares containing 1’s
- Area is square or rectangular (wraparound allowed)
- No. of squares in area is a power of two (1, 2, 4, . . .)
- Each implicant corresponds to a product of literals
- Double the area, one less literal
- Prime implicant
- Implicant having largest number of squares obeying
- above rules
- Essential prime implicant
- Prime implicant containing a square not in any other
- prime implicant
- K-Map Method
- Include all required prime
- implicants
- Include all essential prime
- implicants
- Include other prime implicants
- **such that:** 
- Each square containing 1 is
- covered
- Boolean formula is minimal
- (may not be unique)
- Convert required implicants to
- Boolean formula
- Each implicant is a product of
- literals
- Include literals which do not
- change over its area

### Slide 48: Karnaugh Maps- Three input

**MCQs**

**1. Why are K-Map rows/columns arranged in the order 00, 01, 11, 10**
- rather than 00, 01, 10, 11?
- A) To make the K-Map easier to draw
- B) So that any two adjacent squares differ in exactly one literal,
- matching the key K-Map principle
- C) Because it matches decimal counting order
- D) It's arbitrary, with no particular reason
- Correct Answer
- Option B

### Slide 49: Karnaugh Maps- Three input

**MCQs**

**2. What does "wrap-around" mean in a K-Map?**
- A) The far left and right (and, for larger maps, top and bottom) squares
- are considered adjacent
- B) The K-Map can be rotated 90 degrees
- C) Squares in different rows are never adjacent
- D) Wrap-around only applies when using POS form
- Correct Answer
- Option A

### Slide 50: Karnaugh Maps- Three input

**MCQs**

**3. What defines a "prime implicant" in K-Map minimization?**
- A) Any implicant containing exactly one square
- B) An implicant that is the largest possible grouping of adjacent 1s
- (can't be enlarged further while following the rules)
- C) An implicant found only using Boolean algebra
- D) An implicant covering all squares in the K-Map
- Correct Answer
- Option B

### Slide 59: Karnaugh Maps- Three input
- K-Map Example 1
- **Prime implicants:** green colour
- **Essential prime implicants:** blue
- colour
- **Required prime implicants:** dark
- red colour
- Three prime implicants
- Two essential prime implicants
- **Required prime implicants:** bc, ac’
- **Boolean formula:** 
- f (a, b, c) = ac’ + bc

### Slide 60: Karnaugh Maps- Three input
- K-Map Example 2
- K-Map Minimization Example
- Truth table

### Slide 68: Karnaugh Maps- Three input
- K Map Example 2
- K-Map Minimization

**Example**
- a b c y
- Truth table
- Two prime implicants
- Two essential prime implicants
- Two required prime implicants: c, a
- **Minimal Boolean formula:** 
- f (a, b, c) = c + a

### Slide 76: Karnaugh Maps- Three input
- K Map Example 3
- K-Map Minimization Example
- a b c y
- Truth table
- Four prime implicants

### Slide 78: Karnaugh Three input
- K Map Example 3
- K-Map Minimization

**Example**
- Truth table
- Four prime implicants
- Two essential prime
- implicants

### Slide 79: Karnaugh Maps- Three input
- K Map Example 3
- K-Map Minimization

**Example**
- Truth table
- Four prime implicants
- Two essential prime implicants
- Three required prime implicants: b’c, bc’ along with either
- ca or ab
- **Minimal Boolean formulas:** 
- f (a, b, c) = b’c+ bc’+ ab
- f (a, b, c) = b’c+ bc’+ac

### Slide 80: Karnaugh Maps- Three input
- K Map Example 4
- K-Map Minimization
- Truth table

### Slide 89: Karnaugh Maps-Two input
- K-Map Example 1
- K-Map Example (two inputs)
- a b y
- Two Input Truth Table
- Two prime implicants
- Two essential prime
- implicants
- Two required prime
- implicants
- Minimized Boolean
- **formula:** 
- f (a, b, c, d ) = b +

### Slide 90: Karnaugh Maps- Three input
- Think About It
- Minimize using K-Maps

**1. f (a, b, c) = Σ(0, 3, 5)**

**2. f (a, b, c) = Σ(0, 1, 2, 4, 5, 6)**

**3. f (a, b, c) = Σ(0, 2, 3, 4, 6, 7)**
- All prime implicants and essential prime implicants shown for clarity, okay to
- directly mark required prime implicants on K-Map

### Slide 91: Karnaugh Maps- Three input

**MCQs**

**1. In a worked example with three prime implicants where two are**
- essential, what determines which prime implicants are included in the
- final formula?
- A) All prime implicants must always be included regardless of overlap
- B) The essential prime implicants must be included (to cover their
- unique squares), plus any additional prime implicants needed to cover
- remaining 1s
- C) Only the prime implicant with the fewest literals is used
- D) Required prime implicants are chosen randomly
- Correct Answer
- Option B

### Slide 92: Karnaugh Maps- Three input

**MCQs**

**2. One example shows the minimal formula can be written as either f =**
- bc' + b'c + ca or f = bc' + b'c + ab. What does this illustrate?
- A) K-Maps always produce a unique minimal solution
- B) The minimal SOP solution isn't always unique - different valid
- choices of non-essential prime implicants can give equally minimal
- formulas
- C) POS form is always required in such cases
- D) The K-Map method fails when there are multiple prime implicants
- Correct Answer
- Option B

### Slide 93: Karnaugh Maps- Three input

**MCQs**

**3. Regarding marking prime implicants, essential prime implicants, and**
- required prime implicants on a K-Map, what does the slide note?
- A) All three must always be marked with different colors in every
- solution
- B) It's acceptable to skip marking all prime implicants and essential
- prime implicants separately, and directly mark just the required prime
- implicants
- C) Only maxterms need to be marked
- D) None of them need to be marked; only the final formula matters
- Correct Answer
- Option B

### Slide 94: Karnaugh Maps-Four Inputs
- K-Map Structure (four inputs)
- K-Map Structure (four input Boolean function) Four Input Truth Table
- Minterm
- a’b’c’d’
- a’b’c’d
- a’b’cd’
- a’b’cd
- a’bc’d’
- a’bc’d
- a’bcd’
- a’bcd
- ab’c’d’
- ab’c’d
- ab’cd’
- ab’cd
- abc’d’
- abc’d
- abcd’
- abcd
- a’b’c’d’ a’b’c’d
- a’bc’d
- a’bc’d’
- a’bcd’
- abcd
- abcd’
- ab’c’d
- ab’c’d’
- a’b’cd’
- abc’d
- abc’d’
- a’b’cd
- a’bcd
- ab’cd
- ab’cd’
- Each square corresponds
- to a row of the truth
- table
- Any two adjacent
- squares differ only in
- one literal
- Columns as well as rows
- arranged in binary order
- 00,01,11,10
- Notion of “wrap-around”
- Far left and right squares
- are adjacent
- Top and bottom squares
- are also adjacent

### Slide 95: Karnaugh Maps-Four Inputs
- K-Map Structure (four inputs)
- K-Map Structure (four input Boolean function)
- Minterm
- a’b’c’d’
- a’b’c’d
- a’b’cd’
- a’b’cd
- a’bc’d’
- a’bc’d
- a’bcd’
- a’bcd
- ab’c’d’
- ab’c’d
- ab’cd’
- ab’cd
- abc’d’
- abc’d
- abcd’
- abcd
- Four Input Truth Table
- Each square corresponds
- to a row of the truth
- table
- Any two adjacent
- squares differ only in
- one literal
- Columns as well as rows arranged in binary order 00,01,11,10
- Notion of “wrap-around”
- Far left and right squares are adjacent
- Top and bottom squares are also adjacent

### Slide 103: Karnaugh Maps-Four Inputs
- K-Map Example 1 (four inputs)
- K-Map Example (four inputs)
- Four Input Truth Table
- Two prime
- implicants
- Two essential prime
- implicants
- Two required prime
- **implicants:** bd ,
- b’d’
- Minimized Boolean
- **formula:** 
- f (a, b, c, d ) =
- bd + b’d’

### Slide 104: Karnaugh Maps-Four Inputs
- K-Map Example 2
- A seven-segment display decoder
- **takes a 4-bit data input D3:** 0 and
- produces seven outputs to control
- light-emitting diodes to display a
- digit from 0 to 9. The seven outputs
- are often called segments a through
- g, or Sa–Sg, as defined in Figure. The
- digits are shown.
- Write a truth table for the outputs,
- and use K-maps to find Boolean
- equations for outputs Sa and Sb.
- Assume that illegal input values (10–
- 15) produce a blank readout.

### Slide 105: Karnaugh Maps-Four Inputs
- K-Map Example 2
- Sa = D3’ D1+ D3' D2D0 + D2’D1’ D0’ + D3 D2' D1'
- Sb = D3' D2' + D2' D1' + D3' D1 D0 + D3' D1' D0’
- Sc = D3' D0 + D3' D2 + D2' D1'
- Sd = D3' D2' D1 + D3' D2 D1’ D0+D2’D1’D0’+D3’D1D0
- Se = D3' D1 D0' + D2' D1' D0’
- Sf = D3' D2 D0' + D3' D2 D1' + D3 D2' D1' + D3' D1' D0’
- Sg = D3' D1 D0' + D3' D2' D1 + D3' D2 D1' + D3 D2' D1'

### Slide 115: Karnaugh Maps-(Don’t Cares)

**Example 1 (Three inputs)**
- Suppose we are asked to design a
- three input logic circuit all whose
- inputs can never be 1
- simultaneously
- logic circuit
- guaranteed can’t happen
- b c y
- 1 1 X
- Truth table
- Don’t Care
- Output(s) we don’t care about are denoted by X , can be treated
- as either 0 or 1

### Slide 116: Karnaugh Maps-(Don’t Cares)

**Example 2(Four inputs)**
- K-Map Structure (four input Boolean function)
- A seven-segment display decoder
- **takes a 4-bit data input D3:** 0 and
- produces seven outputs to control
- light-emitting diodes to display a
- digit from 0 to 9. The seven outputs
- are often called segments a through
- g, or Sa–Sg, as defined in Figure. The
- digits are shown.
- Write a truth table for the outputs,
- and use K-maps to find Boolean
- equations for outputs Sa and Sb. Use
- don’t care about the output values
- for illegal input
- values of 10 to 15

### Slide 117: Karnaugh Maps-Four Inputs
- K-Map Example 2
- Sa = D3+D2D0+D2’D0’+D1
- Sb = D2' + D1'D0' + D1D0
- Sc = D0 + D2 + D1’
- Sd = D1D0' + D2’D1+ D0'D2' + D2D1’D0
- Se = D1D0' + D2'D0’
- Sf = D3 + D2D0' + D2D1' + D1’ D0'
- Sg = D3 + D1D0' + D2'D1 + D2D1'

### Slide 118: Karnaugh Maps-(Don’t Cares)
- Think About It
- Minimize using K-Maps
- K-Maps

**1.f (a, b) = Σ(0, 1, 2, 3)**

**2.f (a, b, c, d ) =Σ(0, 1, 5, 7, 15, 14, 10)**
- Minimize using

### Slide 119: Karnaugh Maps-(Don’t Cares)

**MCQs**

**1. In a four-input K-Map, which pairs of squares are adjacent due to**
- wrap-around?
- A) Only left and right squares
- B) Only top and bottom squares
- C) Both left-right AND top-bottom squares are adjacent (wrap-around
- applies to both rows and columns)
- D) No squares wrap around in a four-input K-Map
- Correct Answer
- Option C

### Slide 120: Karnaugh Maps-(Don’t Cares)

**MCQs**

**2. What does an "X" (don't care) in a K-Map or truth table represent?**
- A) An output that is always 0
- B) An output that is always 1
- C) An output whose value is unspecified/irrelevant, which can be
- treated as either 0 or 1, whichever gives the smaller formula
- D) An invalid input combination that always causes an error
- Correct Answer
- Option C

### Slide 121: Karnaugh Maps-(Don’t Cares)

**MCQs**

**3. In the example of a three-input circuit whose inputs can never all be**
- 1 simultaneously, why do don't-care values help simplify the formula?
- A) Because don't cares always force the output to 0
- B) Because input combinations guaranteed never to occur can be
- assigned whichever output value (0 or 1) yields a smaller/simpler
- formula
- C) Because don't cares eliminate the need for a K-Map entirely
- D) Because don't cares only apply to four-input functions
- Correct Answer
- Option B

### Slide 124: Building Blocks
- OUTLINE
- Combinational logic is often grouped into larger building blocks
- to build more complex systems.
- This is an application of the principle of abstraction, hiding the
- unnecessary gate-level details to emphasize the function of the
- building block.
- Commonly used building blocks: Multiplexers , Decoders

### Slide 125: Building Blocks
- Multiplexer (Mux)
- Multiplexers are among the most commonly used combinational circuits.
- A Multiplexer is a digital switch that selects one of several inputs and
- forwards it to a single output.
- They choose an output from among several possible inputs based on the
- value of a select signal. A multiplexer is sometimes affectionately called a
- mux.
- Multiplexers reduce hardware and simplify circuit design.

### Slide 126: Building Blocks
- **2:** 1 Multiplexer
- Multiplexer (Mux)
- Selects between one of N inputs to
- connect to output
- log2N-bit select input – control input

**Example:**
- Symbol and Truth Table
- S is called Control Signal/Select input

### Slide 127: Building Blocks
- Select Lines

### Slide 128: Building Blocks
- Two different ways to implement a 2:1 Multiplexer:

**2. Tristates**

**1. Logic gates**
- Multiplexer using tristate buffers
- Sum-of-products form
- For an N-input mux, use N
- tristates
- Turn on exactly one to select
- the appropriate input

### Slide 129: Building Blocks
- A tri-state buffer has three output
- **states:** 0, 1, and High Impedance (Z).
- In a tri-state MUX, only one buffer is
- enabled at a time, ensuring that only
- the selected input reaches the output
- while all others remain disconnected
- (Z).
- How does the Tri-state MUX work?
- **For a 2:** 1 MUX:
- The select signal controls which buffer is
- enabled.
- **If S = 0:** 
- D₀ buffer is enabled.
- D₁ buffer outputs Z.
- So, Y = D₀.
- **If S = 1:** 
- D₁ buffer is enabled.
- D₀ buffer outputs Z.
- So, Y = D₁.
- Only one buffer drives the output at a time.

### Slide 130: Building Blocks
- **4:** 1 Mux
- S1 S0 Output
- ----- -------00 → D0
- 01 → D1
- 10 → D2
- 11 → D3
- **4:** 1 multiplexer implementations:
- (a) two-level logic, (b) tristates, (c) hierarchical

### Slide 131: Building Blocks
- Logic using Multiplexers
- Multiplexers can be used as lookup tables to perform logic functions.
- Using the mux as a lookup table to implement AND gate.
- **4:** 1 multiplexer
- implementation of two-input AND
- Function
- The inputs, A and B, serve as select lines. The
- multiplexer data inputs are connected to 0 or 1
- according to the corresponding row of the truth
- table.

### Slide 132: Building Blocks
- Logic using Multiplexers- (AND implementation)
- we can cut the multiplexer size in half, using only a 2 N–1 -input multiplexer to
- perform any N-input logic function. The strategy is to provide one of the literals,
- as well as 0’s and 1’s, to the multiplexer data inputs.
- For example, in the case
- Reducing the size of the mux (2:1 Mux)
- of AND,
- when A = 0, Y = 0,
- regardless of B.
- When A = 1, Y = 0 if B = 0
- and Y = 1 if B = 1, so Y =

**B. We then use the**
- multiplexer as a lookup
- table according to the
- new, smaller truth table.

### Slide 133: Building Blocks
- Logic using Multiplexers - XOR
- Reducing the size of the mux

### Slide 135: Building Blocks
- Logic using Multiplexers - OR ?
- Y(A+B)
- **Assume:** 
- Select line (S) = A
- Data inputs = I₀ and I₁
- Y(A+B)
- B-I0
- B-I0
- 1-I1
- 1-I1
- Look only at the rows where A = 0.
- Look only at the rows where A = 1.
- Output
- Output
- The output follows B.
- So,
- I₀ = B
- Draw the figure
- The output is always 1.
- So,
- I₁ = 1

### Slide 136: Building Blocks
- Logic using Multiplexers
- Alyssa P. Hacker needs to implement the
- function Y = AB’+B’C’ + A’BC to finish her
- senior project, but when she looks in her
- lab kit, the only part she has left is an 8:1
- multiplexer. How does she implement the
- function?

### Slide 137: Building Blocks
- Logic using Multiplexers
- Alyssa turns on her circuit one more time
- before the final presentation and blows up
- **the 8:** 1 multiplexer. (She accidently
- powered it with 20 V instead of 5 V after
- not sleeping all night.) She begs her friends
- for spare parts and they give her a 4:1
- multiplexer and an inverter.
- Can she build her circuit with only these
- parts?
- Y = AB’+B’C’ + A’BC

### Slide 138: Building Blocks
- Implement the function

**1. Y=A′B+A′C+AB′**
- **using a 4:** 1 MUX.

**2. Implement a 3-variable function using a 4:1**
- MUX
- **Consider:** 
- F(A,B,C)=Σm(1,2,5,7)
- **Also implement using 2:** 1 Mux

### Slide 139: Building Blocks
- **How many 2:** 1 Mux’s are required to implement

**1. 4:1**

**2. 8:1**

**3. 16:1 and so on**
- **How many 4:** 1 Mux’s are required to implement

**4. 8:1**

**5. 16:1**

**6. 64:1 and so on**

### Slide 140: Step 1: First level
- Building Blocks
- **Build an 8:** 1 MUX
- Now we have 8 inputs.
- First level
- **We need:** 
- 8→4
- **So we need 4 × 2:** 1 MUXes.
- Second level
- Those 4 outputs need to become 2 outputs.
- **So we need 2 × 2:** 1 MUXes.
- Third level
- Finally, 2 outputs need to become 1.
- **So we need 1 × 2:** 1 MUX.
- **Therefore:** 
- **4+2+1=7 8:** 1=7 two-to-one MUXes​
- **So the general formula is:** 
- **2n:** 1 MUX requires (2n−1) 2:1 MUXes​
- **A 64:** 1 MUX has 64 inputs.
- **Each 4:** 1 MUX can reduce 4 inputs to 1 output.
- **So:** 
- 64/4=16​
- **We need 16 - 4:** 1 MUXes.

**Step 2: Second level**
- Now we have 16 outputs.
- **Each 4:** 1 MUX can take 4 of these:
- 16​/4=4
- **So we need 4 - 4:** 1 MUXes.

**Step 3: Third level**
- Now we have 4 outputs.
- **One 4:** 1 MUX can combine them:
- 4/4​=1
- **So we need 1 -4:** 1 MUX.
- Total
- 16+4+1=21
- General formula

### Slide 141: Building Blocks
- Decoders
- N inputs, 2N outputs
- It asserts exactly one of its outputs
- depending on the input
- combination.
- **One-hot outputs:** only one output
- HIGH at once

### Slide 142: Building Blocks
- **2:** 4 Decoder Implementation

### Slide 143: Building Blocks
- Logic Using Decoders
- Decoders can be
- combined with OR
- gates to build logic
- functions.
- **Ex:** Fig shows the
- two-input XNOR
- **function using a 2:** 4
- decoder and a single
- OR gate.

### Slide 144: Building Blocks
- Implementing Logic Functions Using Decoders
- A Boolean function can be represented using a Truth Table or Canonical
- Sum-of-Products (SOP) form.
- An N-input Boolean function requires an N : 2ᴺ Decoder.
- The decoder generates all possible minterms.
- Each decoder output represents one minterm.
- If the function has M output 1's in its truth table:
- Connect the corresponding M minterm outputs of the decoder to
- an M-input OR gate.
- **General Structure:** 
- **N Inputs → N:** 2ᴺ Decoder → Selected Minterms → M-input OR Gate →
- Function Output

### Slide 146: Building Blocks
- Encoder
- An encoder is a digital combinational circuit that converts multiple input signals
- into a binary code. It typically has one active input at a time and generates a
- binary output representing the position of that active input.
- The number of inputs is usually 2n, with n output lines.
-  Inputs are usually active high, meaning high voltage represents an active signal.
-  Binary-weighted encoders assign codes based on input position using binary values.
-  Encoders help convert parallel inputs into compact binary formats for processing.
-  Encoders are useful in digital systems for data compression and efficient
- transmission.
-  For example, a 4-to-2 encoder has four inputs and produces a 2-bit output code.

### Slide 147: Building Blocks
- The number of inputs is usually 2n, with n output lines.

### Slide 148: Building Blocks
- Types of Encoders

**1. 4 to 2 Encoder**

**2. Octal to Binary Encoder (8 to 3 Encoder)**

**3. Decimal to BCD Encoder**

**4. Priority Encoder**

### Slide 149: Building Blocks

**1. 4 to 2 Encoder**
- The 4 to 2 Encoder consists of four inputs Y3, Y2, Y1 &
- Y0, and two outputs A1 & A0. At any time, only one of
- these 4 inputs can be ‘1’ in order to get the respective
- binary code at the output.
- Truth Table
- Logical expression
- **for A1 and A0:** 
- A1 = Y 3 + Y2
- A0 = Y 3 + Y1
- INPUTS(Y Y Y Y )
- OUTPUTS(A A )
- Logic symbol of the 4 to 2 encoder.
- Circuit Diagram

### Slide 150: Building Blocks

**2. Octal to Binary Encoder (8 to 3 Encoder)**
- The 8 to 3 Encoder or octal to Binary encoder consists of 8 inputs: Y 7 to
- **Y0 and 3 outputs:** A2, A1 & A0. Each input line corresponds to each octal
- digit value and three outputs generate corresponding binary code.
- Truth Table
- Logical expression
- **for A2, A1, and A0:** 
- A2 = Y7 + Y6 + Y5 + Y4
- A1 = Y7 + Y6 + Y3 + Y2
- A0 = Y7 + Y5 + Y3 + Y1
- INPUTS(Y7Y6Y5Y4Y3Y2Y1Y0)
- OUTPUTS(A 2A1
- A0)
- Logic symbol of the Octal or 8 to 3 encoder.
- Circuit Diagram

### Slide 151: Building Blocks

**3. Decimal to BCD Encoder**
- The decimal-to-binary encoder usually consists of 10 input lines and 4
- output lines. Each input line corresponds to each decimal digit and 4
- outputs correspond to the BCD code.
- Truth Table
- Logical expression for
- **A3, A2, A1, and A0:** 
- A3 = Y9 + Y8
- A2 = Y7 + Y6 + Y5 +Y4
- A1 = Y7 + Y6 + Y3 +Y2
- A0 = Y9 + Y7 +Y5 +Y3 + Y1
- NPUTS(Y9Y8Y7Y6Y5Y4Y3Y2Y1Y0)
- OUTPUTS(A3A2A1
- A 0)
- Logic symbol of the BCD encoder.
- Circuit Diagram

### Slide 152: Building Blocks
- What is an ordinary encoder?
- An encoder converts one active input into a binary code.
- For example, a 4-to-2 encoder has 4 inputs and 2 outputs:
- INPUTS(Y Y Y Y )
- OUTPUTS(A A )

**2. What is the problem? (NEED OF PRIORITY ENCODER)**
- **Suppose two inputs become 1:** 
- Y3 Y2 Y1 Y0
- Which one should the encoder represent?
- An ordinary encoder cannot decide because D₂ and D₁ are
- both active.
- This is where the priority encoder comes in.
- Here we assume only one input is 1 at a time.
- **For example:** 
- Y3 Y2 Y1 Y0
- 0 1 0 0 → 10
- So, input Y₂ is active, and the encoder produces binary 10.

### Slide 153: Building Blocks

**4. Priority Encoder**
- A 4 to 2 priority encoder has 4 inputs: Y3, Y2, Y1 & Y0, and 2 outputs: A 1 & A0. Here, the input,
- Y3 has the highest priority
- Y0 has the lowest priority.
- In this case, even if more than one input is ‘1’ at the same time, the output will be the (binary)
- code corresponding to the input, which is having higher priority.
- Truth Table (Here X means “don't care”)
- INPUTS(Y3Y2Y1Y0)
- OUTPUTS(A 1A0V)
- XX0
- 001X
- 01XX
- 1XXX
- **Case 1:** 
- Y3 Y2 Y1 Y0
- Only Y₀ is active.
- **Output:** 
- A1 A0 = 00
- **Case 2:** 
- Y3 Y2 Y1 Y0
- 0 0 1 X
- Only Y1 is active.
- **Output:** 
- A1 A0 = 01
- **Case 3:** 
- Y3 Y2 Y1 Y0
- 0 1 X X
- Only Y2 is active.
- **Output:** 
- A1 A0 = 10
- **Case 4:** 
- Y3 Y2 Y1 Y0
- 1 X X X
- Only Y3 is active.
- **Output:** 
- A1 A0 = 11

### Slide 156: Building Blocks

**4. Priority Encoder**
- Truth Table (Here X means “don't care”)
- INPUTS(Y3Y2Y1Y0)
- OUTPUTS(A 1A0V)
- XX0
- 001X
- 01XX
- 1XXX
- Why do we need the Valid output(V)?
- Just to mention no input is high V=0
- All other cases V=1
- Circuit Diagram

### Slide 158: Building Blocks

**MCQ 1**
- **Q1. A 4:** 1 Multiplexer requires how many select lines?
- A) 1
- B) 2
- C) 3
- D) 4

### Slide 160: Building Blocks

**MCQ 3**
- Q3. In a decoder, the outputs are called one-hot because
- A) All outputs are HIGH simultaneously.
- B) Exactly one output is HIGH for any input combination.
- C) All outputs are LOW.
- D) Outputs keep changing randomly.
- **Answer:** B) Exactly one output is HIGH for any input
- combination.
- **Explanation:** 
- For every valid input, only one decoder output becomes
- HIGH while all others remain LOW.

### Slide 162: Latches, Flip-flops

### Slide 163: Digital Logic and
- Computer Design
- Latches, Flip-flops

### Slide 164: LATCHES, FLIP-FLOPS
-  Combinational logic design
-  Sequential logic design
- Latches, Flip-flops

### Slide 165: LATCHES, FLIP-FLOPS
- How does Sequential Logic differ from Combinational Logic?
- Previously we analysed and designed combinational logic.
- The output of combinational logic depends only on current
- input values. Given a specification in the form of a truth
- table or Boolean equation, we can create an optimized
- circuit to meet the specification.
- Now we will analyse and design sequential logic. The
- outputs of sequential logic depend on both current and
- prior input values.

### Slide 166: Sequential Circuits
- It consists of a combinational circuit to which storage elements are connected
- to form a feedback path.
- The storage elements are devices capable of storing binary information.
- The binary information stored in these elements at any given time defines the
- state of the sequential circuit at that time.
- The sequential circuit receives binary information from external inputs that,
- together with the present state of the storage elements, determine the binary
- value of the outputs.
- These external inputs also determine the condition for changing the state in the
- storage elements.
- The next state of the storage elements is also a function of external inputs and
- the present state.

### Slide 167: Types of Sequential Circuits
- There are two main types of sequential circuits, and their classification
- is a function of the timing of their signals.
-  A synchronous sequential circuit is a system whose behavior can
- be defined from the knowledge of its signals at discrete instants of
- time.
-  The behavior of an asynchronous sequential circuit depends upon
- the input signals at any instant of time and the order in which the
- inputs change.

### Slide 168: Two Memory Elements
- LATCH
- FLIPFLOP

### Slide 169: How to Implement Memory?
- ● The inverter is essentially the
- simplest logic gate
- ● What happens when we connect
- its output to input, forming a
- loop?
- ● Inverter loop is thus not in a stable
- state
- ● Hence, a single inverter loop
- cannot store a stable bit.
- ●
- ●
- ●
- ●
- How about a loop of two inverters?
- A two-inverter loop can be in one of
- two stable states.
- A bit can have one of two different
- values.
- Thus, a two-inverter loop can store (or
- “remember”) a single bit.
- But how can we change the bit stored
- or the stable state?

### Slide 170: How to Implement Memory?
- How do we CHANGE the stored bit?
- This is the crucial problem.
- Suppose the circuit currently stores:
- A=0, B=1​
- The feedback keeps reinforcing this state.
- How can we force it to become:
- A=1, B=0​
- We need some external control mechanism to temporarily
- override the feedback.
- So we need cross coupled inverters

### Slide 171: LATCHES, FLIP-FLOPS
- Latches and Flip Flops
- The fundamental building block of memory is a bistable element, an element
- with two stable states.
- The inverters are cross-coupled, meaning that the input of I1 is the output of I2
- and vice versa.

### Slide 172: LATCHES, FLIP-FLOPS
- Latches and Flip Flops
- Bistable operation of cross-coupled inverters
- **Case I:** Q = 0
- As shown in Figure (a), I2 receives a FALSE input, Q, so
- it produces a TRUE output on Q' I1 receives a TRUE
- input, Q’ so it produces a FALSE output on Q. This is
- consistent with the original assumption that Q = 0, so
- the case is said to be stable.
- The cross-coupled inverters
- have two stable states, Q = 0
- and Q = 1, so the circuit is
- said to be bistable.
- **Case II:** Q = 1
- As shown in Figure (b), I2 receives a TRUE input and
- produces a FALSE output on Q’. I1 receives a FALSE
- input and produces a TRUE output on Q. This is again
- stable.

### Slide 173: LATCHES, FLIP-FLOPS
- Latches and Flip Flops
- Problem with cross coupled inverters
- Although the cross-coupled inverters can store a bit of
- information, they are not practical because the user has no
- inputs to control the state.
- However, other bistable elements, such as latches and flipflops, provide inputs to control the value of the state
- variable. The remainder of this section considers these
- circuits.

### Slide 174: LATCHES, FLIP-FLOPS
- Latches and Flip Flops
- Although the cross-coupled inverters can store a bit of information, they are not
- practical because the user has no inputs to control the state.
- However, other bistable elements, such as latches and flip-flops, provide inputs to
- control the value of the state variable.
- Latch
- A latch is a 1-bit memory element that stores a value and can change
- its output as long as its enable/control signal is active.
- **In simple terms:** 
- Latch = level-sensitive memory
- For example, an Enable signal controls the latch:
- Enable = 1 → latch can change/update
- Enable = 0 → latch holds the previous value

### Slide 175: LATCHES, FLIP-FLOPS
- Latches and Flip Flops

### Slide 176: LATCHES, FLIP-FLOPS
- SR Latch
- One of the simplest sequential circuits is the SR latch, which is composed of two crosscoupled NOR gates. The SR latch is similar to the cross-coupled inverters, but its state can
- be controlled through the S and R inputs, which set and reset the output Q.
- Cross-coupled inverters + control inputs = SR latch

### Slide 177: LATCHES, FLIP-FLOPS
- SR Latch
- SR Latch Operation when S=R=0
- a) Q=0 and Q’=1
- b) Q=1 and Q’=0

### Slide 178: LATCHES, FLIP-FLOPS
- SR Latch
- Like the cross-coupled inverters, the SR latch is a bistable element with one bit of
- state stored in Q.
- However, the state can be controlled through the S and R inputs. When R is
- asserted, the state is reset to 0.
- When S is asserted, the state is set to 1. When neither is asserted, the state retains
- its old value.
- No matter what pattern of setting and resetting occurred in the past, all that is
- needed to predict the future behavior of the SR latch is whether it was most
- recently set or reset.
- S=1 → Q becomes 1
- S=0,R=0 → Q stays 1
- R=1 → Q becomes 0
- S=0,R=0 → Q stays 0
- S=1 → Q becomes 1

### Slide 179: LATCHES, FLIP-FLOPS
- Problems with SR Latch

**1. Problem with the SR latch**
- **In an SR latch:** 
- S tells us what to store → Q=1
- R tells us what to store → Q=0
- But they also directly cause the
- change.
- **For example:** 
- S=1 ⇒ Q becomes 1
- There is no separate signal saying:
- "Change now."
- So what to store and when to change
- are mixed together.

**2. The problem with both S and R**
- **For the SR latch:** 
- Action
- Hold
- Reset → (Q=0)
- Set → (Q=1)
- Invalid
- ❌
- The S=R=1 case is awkward.
- So we want a simpler memory element where
- we don't have to separately worry about Set
- and Reset.

### Slide 180: LATCHES, FLIP-FLOPS
- D Latch
- Designing circuits becomes easier when these questions of
- what and when are separated.
- D latch solves these problems.
- It has two inputs. The data input, D, controls what the next
- state should be. The clock input, CLK, controls when the
- state should change.
- **So:** 
- D=WHAT to store​
- **So:** 
- CLK=WHEN to change​

### Slide 181: LATCHES, FLIP-FLOPS
- D Latch
- When CLK = 1, the latch is transparent(open). The data at D flows through to Q as if the
- latch were just a buffer. When CLK = 0, the latch is opaque(closed).
- It blocks the new data from flowing through to Q, and Q retains the old value. Hence,
- the D latch is some- times called a transparent latch or a level-sensitive latch.
- The circuit guarantees that S and R can never both be 1.

### Slide 182: LATCHES, FLIP-FLOPS
- Problem with latch (Need of Flipflop)
- The problem with the latch is that it responds to a change in the level of a clock pulse.
- As shown in Fig. 5.8 (a), a positive level
- response in the enable input allows
- changes in the output when the D input
- changes while the clock pulse stays at logic

**1. The result is an unpredictable situation,**
- since the state of the latches may keep
- changing for as long as the clock pulse
- stays at the active level. The key to the
- proper operation of a flip-flop is to trigger it
- only during a signal transition .

### Slide 183: LATCHES, FLIP-FLOPS
- Problem with latch (Need of Flipflop)

**1.Problem with the latch (fig 5.8a)**
- **CLK = 1 D changes:** 
- **D:** 0 ─── 1 ─── 0 ─── 1
- ↓ ↓ ↓
- **Q:** 0 ─── 1 ─── 0 ─── 1
- While CLK is HIGH, every change in
- D can potentially change Q.
- So if D changes many times while:
- CLK=1
- then Q can also change many times.
- This is unpredictable because the
- final state can depend on exactly
- when the input changes during the
- active level.

**2. What do we really want?**
- We want the memory element to say:
- "I will look at D only at one particular
- instant."
- **Not:** 
- "I will keep looking at D for the entire HIGH
- period."
- That particular instant is called an edge.

**3. What is an edge?**
- A clock signal has two transitions:
- Rising edge (fig 5.8b)
- 0→1​
- This is also called the positive edge or
- positive-going edge.
- Falling edge (fig 5.8c)
- 1→0​This is the negative edge or negativegoing edge.
- Flip-flop changes only at the edge
- This is the fundamental difference:
- Latch
- Level sensitive​
- **For positive-level latch:** 
- CLK=1⇒Q may change
- Flip-flop
- Edge sensitive​
- **For positive-edge flip-flop:** 
- **CLK:** 0→1⇒Q changes
- only at that instant.

### Slide 184: Difference b/w Latches & Flip-Flops
- Latches
- Flip-Flops
- Latches are building blocks of sequential
- circuits, these can be built from logic gates
- Flip flops are also building blocks of sequential circuits. But, these
- can be built from the latches.
- Latch continuously checks its inputs and
- changes its output correspondingly.
- Flip flop continuously checks its inputs and changes its output
- correspondingly only at times determined by clocking signal
- The latch is sensitive to the duration of the
- pulse and can send or receive the data when
- the switch is on.
- Flipflop is sensitive to a signal change. They can transfer data only
- at the single instant and data cannot be changed until next signal
- change.Flip flops are used as a register.
- It is based on the enable function input.
- It works on the basis of clock pulses.
- It is a level triggered, it means that the output
- of the present state and input of the next state
- depends on the level that is binary input 1 or

**0. (asynchronous circuits)**
- It is an edge triggered, it means that the output and the next state
- input changes when there is a change in clock pulse whether it may
- a+ve or-ve clock pulse.(synchronous circuits)

### Slide 185: Difference b/w Latches & Flip-Flops

**Example: Traffic Light Controller**
- **Scenario:** 
- A city traffic light controller uses digital storage elements to decide when to change from Green
- → Yellow → Red.
- Using a Latch (Level-triggered)
- Suppose the system uses a latch to store the current state of the traffic light.
- Since a latch is level-sensitive, whenever the clock/enable signal is high, the latch is
- “transparent” — it immediately passes input changes to the output.
- **Problem:** If there is noise or a small glitch during the enable-high period, the latch will capture
- it. This could cause the traffic light to change state unexpectedly (e.g., Green jumps to Red
- without Yellow).
- Application-level interpretation: Not safe for traffic control, because continuous input changes
- during the active level may corrupt the output.

### Slide 186: Difference b/w Latches & Flip-Flops

**Example: Traffic Light Controller**
- **Scenario:** 
- A city traffic light controller uses digital storage elements to decide when to change from Green
- → Yellow → Red.
- Using a Flip-Flop (Edge-triggered)
- If the system uses a Flip-Flop, the light state is updated only at the clock’s rising (or falling)
- edge.
- Input changes happening in between edges are ignored until the next edge.
- **Advantage:** The traffic light changes state in a controlled manner (e.g., every 30 seconds on the
- rising clock edge). Even if input glitches occur while the clock is low, they won’t affect the state.
- Application-level interpretation: Much safer and reliable for real-world sequential control
- (traffic lights, elevators, etc.).

### Slide 187: Difference b/w Latches & Flip-Flops
- **https:** //www.youtube.com/watch?v=LTtuY
- eSmJ2g

### Slide 188: LATCHES, FLIP-FLOPS
- What is Flipflop and how to build it?
- There are two ways that a latch can be modified to form a flip-flop.
- One way is to employ two latches in a special configuration that isolates the output
- of the flip-flop and prevents it from being affected while the input to the flip-flop is
- changing – Example-D flipflop
- Another way is to produce a flip-flop that triggers only during a signal transition (from
- 0 to 1 or from 1 to 0) of the synchronizing signal (clock) and is disabled during the rest
- of the clock pulse.

### Slide 189: LATCHES, FLIP-FLOPS
- D FIip-Flop
- A D flip-flop can be built from two back-to-back D latches controlled by complementary
- clocks
- The first latch, L1, is called the master. The second latch, L2, is
- called the slave. The node between them is named N1.
- When CLK = 0, the master latch is transparent and the slave is
- opaque. Therefore, whatever value was at D propagates through
- to N1.
- When CLK = 1, the master goes opaque and the slave becomes
- transparent.

### Slide 190: LATCHES, FLIP-FLOPS
- D FIip-Flop
- A D flip-flop can be built from two back-to-back D latches controlled by complementary
- clocks
- Hence, whatever value was at D immediately before the clock
- rises from 0 to 1 gets copied to Q immediately after the clock
- rises.
- At all other times, Q retains its old value, because there is always
- an opaque latch blocking the path between D and Q.
- In other words, a D flip-flop copies D to Q on the rising edge of
- the clock, and remembers its state at all other times.
- The rising edge of the clock is often just called the clock edge for
- brevity. The D input specifies what the new state will be.

### Slide 191: LATCHES, FLIP-FLOPS
- D FIip-Flop
- A D flip-flop is also known as a master-slave flip-flop, an edge-triggered flip-flop, or a
- positive edge-triggered flip-flop. The triangle in the symbols denotes an edge-triggered
- clock input. The Q output is often omitted when it is not needed.
- **The main idea is:** 
- When the clock triggers the flip-flop, whatever is present at D gets stored in Q.
- **So we can remember it as:** 
- Q(next) = D
- Clock event
- Q(next)
- ↑
- ↑
- Here ↑ means the rising edge of the clock.

### Slide 192: Flip-Flops(2ND METHOD)
- Flip-Flops have following representation:
- ● Function table- output Q and Q`
- ● Characteristic table- They define next state
- ● Characteristic equation-solve using K map- The logical properties of a flipflop, as described in the characteristic table, can be expressed algebraically
- with a characteristic equation.
- ● Excitation table- predict the i/p based on current state and next state to build
- state diagram

### Slide 193: Characteristic table & Excitation Table
- The easiest way to remember it is:
- Characteristic table = What the flip-flop DOES
- Excitation table = What we MUST GIVE to the flip-flop to make it DO
- what we want

### Slide 194: SR Flip-Flops Characteristic table and Characteristic equation
- Characteristic table
- Characteristic equation by simplifying using K maps
- Qn+1= S +R`Qn

### Slide 195: Excitation Table and State Diagram
- Characteristic Table of SR
- State Diagram

### Slide 196: D Flip-Flop-Data FF

### Slide 197: D Flip-Flop
- Characterstic Table
- Excitation table
- Q(n+1)
- Qn+1
- Simplifying using K mapscharacteristic equation is

### Slide 198: JK Flip-Flop
- A JK flip-flop is required mainly to overcome the limitations of the SR flip-flop and to
- provide a more versatile storage element in sequential circuits.
- In an SR flip-flop, when S=1 and R=1 simultaneously, the output becomes indeterminate
- (invalid).

### Slide 199: JK Flip-Flop-function table/Truth table
- Clk
- Memory
- Toggle
- race around condition

### Slide 200: JK Flip-Flop
- Truth Table
- Clk
- **Solve using K map:** 
- J= Qn+1
- K = Q’n+1
- Solve using K map to get
- **characterstic equation:** 
- Q = Q K` + Q `J

### Slide 202: T Flip-Flop (Toggle Flip-Flop)
- Truth table- if clk=0
- then previous state
- Characterstic Table
- Excitation table
- Qn+1
- Qn+1

### Slide 203: Flip-Flops
- JK flip-flop can function as:
- SR flip-flop (J = S, K = R)
- T flip-flop (J=K=1 → toggles)
- D flip-flop (J=D, K=¬D)
- Hence, it’s a universal flip-flop that can emulate other
- types.

### Slide 204: Characteristics Table -summary

### Slide 205: Characteristics Equations-summary

### Slide 206: Steps for Flipflop Conversion

### Slide 207: JK to D FF (b)
- STEP1-Identify available and required FF
- Available is JK and required is D
- Step-2 Make characteristic table of
- required FF
- Step-3- Make Excitation table of
- available FF

### Slide 208: JK to D FF
- STEP-4-write Boolean Expression for Available FF(JK) using required FF (D)
- STEP-5 Write the circuit diagram

### Slide 209: 2. D to JK FF (a)

### Slide 211: D to JK FF

### Slide 212: Exercise 3.10

### Slide 213: Solve it.
- (c) Construct a T flip-flop using a JK flip-flop

### Slide 214: LATCHES, FLIP-FLOPS
- Registers
- An N-bit register is a bank of N flip-flops that share a common CLK input,
- so that all bits of the register are updated at the same time.
- Registers are the key building block of most sequential circuits.
- **Figure A 4-bit register:** 
- (a) schematic and (b) symbol
- Four-bit register with inputs D3:0
- **and outputs Q3:** 0. D3:0 and Q3:0
- are both 4-bit buses.

### Slide 215: LATCHES, FLIP-FLOPS
- Registers
- How much information can a N-bit register store?
- Each flip-flop stores either 0 or 1.
- Four flip-flops can therefore store:
- 24=16 different combinations.
- **From:** 
- **to:** 
- So a 4-bit register can store 16 different values.
- Hence N bit register = N Flip flops and can store 2 N different combinations.
- "N-bit register stores N bits, but it can represent 2 N different values."

### Slide 216: LATCHES, FLIP-FLOPS
- Enabled Flip-Flop
- An enabled flip-flop adds another input called EN or ENABLE to determine whether
- data is loaded on the clock edge.
- When EN is TRUE, the enabled flip-flop behaves like an ordinary D flip-flop.
- When EN is FALSE, the enabled flip-flop ignores the clock and retains its state
- Enabled flip-flops are useful when we wish to load a new value into a flip-flop only
- some of the time, rather than on every clock edge.

### Slide 217: LATCHES, FLIP-FLOPS
- Enabled Flip-Flop
- In Figure 3.10(a), an input multiplexer chooses whether to pass the value at D, if EN is
- TRUE, or to recycle the old state from Q, if EN is FALSE.
- In Figure 3.10(b), the clock is gated.
- If EN is TRUE, the CLK input to the flip-flop toggles normally.
- If EN is FALSE, the CLK input is also FALSE and the flip-flop retains its old value.
- EN must not change while CLK = 1, let the flip-flop see a clock glitch(switch at an
- incorrect time).

### Slide 218: LATCHES, FLIP-FLOPS
- Enabled Flip-Flop
- EN = 1 → LOAD
- **When:** 
- EN=1
- the flip-flop behaves like a normal D flip-flop.
- **At the clock edge:** 
- Qnext​=D​

**Example**
- **Suppose:** 
- Q=0
- D=1
- EN = 1
- **When the clock edge arrives:** 
- The new data 1 is loaded
- So output Q=1
- EN = 0 → HOLD
- **Now suppose:** 
- Q=1
- D=0
- **but:** 
- EN = 0
- When the clock edge arrives, the flip-flop says:
- "EN is 0. I am not allowed to load D."
- **Therefore:** 
- Qnext​=Q​
- **So Q remains:** 
- Q=1 Even though D is 0.
- i.e. (the new data D is not loaded to Q)
- An enabled flip-flop loads new data only when EN = 1; when EN = 0, it ignores the clock
- edge and keeps its previous value.

### Slide 219: LATCHES, FLIP-FLOPS
- Resettable Flip-Flop
- A resettable flip-flop adds another input called RESET. When RESET is FALSE, the
- resettable flip-flop behaves like an ordinary D flip-flop.
- When RESET is TRUE, the resettable flip-flop ignores D and resets the output to 0.
- Resettable flip-flops are useful when we want to force a known state (i.e., 0) into all
- the flip-flops in a system when we first turn it on.
- Such flip-flops may be synchronously or asynchronously resettable.
- Synchronously resettable flip-flops reset themselves only on the rising edge of CLK.
- Asynchronously resettable flip-flops reset themselves as soon as RESET becomes
- TRUE, independent of CLK.

### Slide 220: LATCHES, FLIP-FLOPS
- Resettable Flip-Flop
- Figure 3.11(a) shows how to construct a synchronously
- resettable flip-flop from an ordinary D flip-flop and an
- AND gate.
- When RESET` is FALSE, the AND gate forces a 0 into the
- input of the flip-flop. When RESET` is TRUE, the AND
- gate passes D to the flip-flop.
- RESET` is an active low signal
- Asynchronously resettable flip-flops require modifying
- the internal structure of the flip-flop settable flip-flops
- are also occasionally used.
- They load a 1 into the flip-flop when SET is asserted
- Resettable and settable flip-flops may also have an
- enable input and may be grouped into N-bit registers.

### Slide 221: LATCHES, FLIP-FLOPS
- Resettable Flip-Flop
- Normal D Flip-Flop
- **A normal D flip-flop does:** 
- Qnext​=D​
- at the active clock edge.
- **For example:** 
- D = 1 → clock edge → Q = 1
- Add RESET
- **Now we add another input:** 
- D + CLK + RESET
- RESET has higher priority than D.
- **Think of it like this:** 
- IF RESET = 0 → behave normally
- IF RESET = 1 → forget D and make Q = 0
- **So the basic behavior is:** 
- RESET
- Clock edge
- Q(next)
- ↑
- ↑
- ↑
- Here X means "don't care."
- When RESET = 1, we don't care whether D is 0 or 1.

### Slide 222: LATCHES, FLIP-FLOPS
- Flip Flop and Latch Comparison
- Latches and flip-flops are the fundamental building blocks of sequential circuits.
- Remember that a D latch is level-sensitive, whereas a D flip-flop is edgetriggered.
- The D latch is transparent when CLK = 1, allowing the input D to flow through
- to the output Q.
- The D flip-flop copies D to Q on the rising edge of CLK. At all other times,
- latches and flip-flops retain their old state.
- A register is a bank of several D flip-flops that share a common CLK signal.

### Slide 224: LATCHES, FLIP-FLOPS
- Flip-Flop and Latch Comparison
- Ben Bitdiddle applies the D and CLK inputs shown in Figure 3.14 to a D latch and
- a D flip-flop. Help him determine the output, Q, of each device.

### Slide 226: LATCHES, FLIP-FLOPS

**MCQs**
- **Q1:** Why can a loop of two cross-coupled inverters store one bit of
- information?
- A) Because it has two outputs
- B) Because it consumes low power
- C) Because it can settle into one of two stable states, matching the
- two values a bit can take
- D) Because it uses NAND gates only

### Slide 228: LATCHES, FLIP-FLOPS

**MCQs**
- **Q2:** In a NOR-gate SR latch, what happens when both inputs S = 1 and
- R = 1?
- A) The latch remembers the previous state
- B) The output q is set to 1
- C) Both outputs q and q' become 0 — an invalid state since they're no
- longer complementary
- D) The output is reset to q = 0

### Slide 230: LATCHES, FLIP-FLOPS

**MCQs**
- **Q3:** Why is the NAND-gate based SR latch sometimes called an S'R'
- latch?
- A) Because it uses only NOR gates internally
- B) Because its input signals are complemented (active-low) compared
- to the NOR latch
- C) Because it stores complemented data only
- D) Because S' and R' represent set and reset simultaneously

### Slide 233: DIGITAL LOGIC AND
- COMPUTER DESIGN
- Synchronous Sequential Logic Circuits

### Slide 234: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Combinational logic design
- Sequential logic design
- Synchronous Sequential Logic Circuits

### Slide 235: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Potential Problems with Sequential Logic Circuits
- logic circuits do not
- contain loops or cyclic paths but
- sequential logic circuits do
- Loops can cause problems
- Memory elements can suffer from
- race conditions
- clk1
- d q
- clk2
- Output is unstable
- Output depends upon input sequence

### Slide 236: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Sequential Logic Circuits
- Cyclic paths are broken by inserting flip-flops in them
- Cyclic paths can be broken by converting combinational ckts and
- register(synchronize with clock)
- Flip-flops are synchronized by connecting them to a common clock
- Race conditions are eliminated if the clock time period is long enough
- clk2 clk1
- d q
- d q

### Slide 237: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Sequential Logic Circuits
- Cyclic paths are broken by inserting flip-flops in them
- clk
- q d
- Flip-flops are synchronized by connecting them to a common clock
-  Race conditions are eliminated if the clock time period is long enough
- clk2 clk1
- d q
- d q

### Slide 238: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Sequential Logic Circuits
- Cyclic paths are broken by inserting flip-flops in them
- clk
- q d
- Flip-flops are synchronized by connecting them to a common clock
-  Race conditions are eliminated if the clock time period is long enough
- clk
- d q

### Slide 239: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Potential Problems with Sequential Logic Circuits
- ASTABLE CIRCUITS
- Alyssa P. Hacker encounters three misbegotten inverters who have tied themselves
- in a loop, as shown in Figure 3.16. The output of the third inverter is fed back to
- the first inverter. Each inverter has a propagation delay of 1 ns. Determine what
- the circuit does.

### Slide 240: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Potential Problems with Sequential Logic Circuits
- Suppose node X is initially 0. Then Y = 1, Z = 0, and hence X = 1,
- which is inconsistent with our original assumption. The circuit has
- no stable states and is said to be unstable or astable.
- Figure 3.17 shows the behavior of the circuit. If X rises at time 0, Y
- will fall at 1 ns, Z will rise at 2 ns, and X will fall again at 3 ns.
- In turn, Y will rise at 4 ns, Z will fall at 5 ns, and X will rise again at
- 6 ns, and then the pattern will repeat.
- Each node oscillates between 0 and 1 with a period (repetition
- time) of 6 ns. This circuit is called a ring oscillator.
- Figure 3.16 Three-inverter loop

### Slide 241: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Potential Problems with Sequential Logic Circuits
- RACE CONDITIONS
- Ben Bitdiddle designed a new D latch that
- he claims is better than the one because
- it uses fewer gates. He has written the
- truth table to find the output, Q, given
- the two inputs, D and CLK, and the old
- state of the latch, Qprev.
- Based on this truth table, he has derived
- Boolean equations.
- He obtains Qprev by feeding back the
- output, Q in his design.
- Does his latch work correctly,independent
- of the delays of each gate?

### Slide 242: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Potential Problems with Sequential Logic Circuits
- This is an example of asynchronous
- circuit design in which outputs are
- directly fed back to inputs.
- Asynchronous circuits are infamous for
- having race conditions where the
- behaviour of the circuit depends on
- which of two paths through logic gates is
- fastest.

### Slide 243: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Problem with Cyclic Paths
- Sequential circuits contain feedback (cyclic) paths.
- These paths can cause race conditions and unstable behavior.
- Analyzing such circuits is difficult and may lead to design errors.
- Solution
- Insert registers in the feedback path.
- Registers store the system state and update only on the clock edge.
- This converts the design into combinational logic + registers, eliminating races.
- Synchronous Sequential Circuit
-  State changes only at the rising edge of the clock.
- **Uses:** 
- Current State – Present state of the system.
- Next State – State after the next clock edge.
- If the clock is slow enough for signals to settle, the circuit operates reliably.
- Registers synchronize state changes with the clock, preventing race conditions and
- ensuring reliable sequential circuit operation.

### Slide 244: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Rules of Synchronous Sequential Circuit Composition
- **A circuit is synchronous if:** 
- Every circuit element is either a Register or Combinational Logic.
- The circuit contains at least one register.
- All registers share the same clock signal.
- Every feedback (cyclic) path contains at least one register.
- Asynchronous Sequential Circuit
- Sequential circuits that do not follow these rules are called Asynchronous Circuits.
- They are more prone to race conditions and unpredictable behavior.
- **Flip-Flop:** Basic Synchronous Sequential Circuit
- A Flip-Flop is the simplest synchronous sequential circuit.
- **Inputs:** D (Data), CLK (Clock)
- **Output:** Q
- **States:** {0, 1}
- **Function:** On every clock edge, the next state = D, and Q represents the current state.
- ✅
- Synchronous circuits use registers and a common clock to ensure predictable, stable, and reliable operation.

### Slide 246: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Rules of Synchronous Sequential Circuit Composition
- Circuit (a) is combinational, not sequential, because it has no registers.
- (b) is a simple sequential circuit with no feedback.
- (c) is neither a combinational
- circuit nor a synchronous sequential circuit, because it has a latch that is neither
- a register nor a combinational circuit.
- (d) and (e) are synchronous sequential logic;
- (f) is neither combinational nor synchronous sequential, because it has a cyclic
- path from the output of the combinational logic back to the input of the same
- logic but no register in the path.
- (g) is synchronous sequential logic in the form of a pipeline
- (h) is not, strictly speaking, a synchronous sequential circuit, because the second register receives a different clock
- signal than the first, delayed by two inverter delays.

### Slide 247: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Asynchronous vs. Synchronous Circuit Design
- Asynchronous vs. Synchronous Circuit Design
- Asynchronous circuits are more general and flexible since they are not restricted by a global
- clock.
- Similar to analog circuits, they can use arbitrary feedback and timing.
- Synchronous circuits are easier to design, verify, and implement, making them the preferred
- choice in digital systems.
- Asynchronous circuits are mainly used for:
- Communication between different clock domains.
- Handling inputs arriving at unpredictable times.
- Research in asynchronous design continues to provide innovative techniques that also benefit
- synchronous systems.
- Despite decades of research, nearly all modern digital systems are predominantly synchronous
- due to their simplicity and reliability.

### Slide 248: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS
- Think About It
- Classify the following logic circuits as combinational or synchrnous
- sequential or neither
- AND gate (output not connected to any input)
- AND gate (output connected to an input)
- D flip-flop
- SR latch
- Series of D flip-flops (with common clock) with output of one connected to the input
- of the next via an inverter

### Slide 250: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

**MCQs**

**1. In a sequential logic circuit with an unresolved race condition, why is the**
- output described as "unstable"?
- A) Because the circuit consumes too much power
- B) Because the flip-flops are not connected to any clock at all
- C) Because the output depends on the order/timing of inputs rather than
- settling to one well-defined value
- D) Because combinational gates need more chip area

### Slide 252: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

**MCQs**

**2. Race conditions are eliminated when flip-flops are synchronized to a**
- **common clock, provided that:** 
- A) The clock is asynchronous
- B) There is no clock signal
- C) Multiple independent clocks are used
- D) The clock time period is long enough

### Slide 254: SYNCHRONOUS SEQUENTIAL LOGIC CIRCUITS

**MCQs**

**3. An AND gate whose output is fed back into one of its own inputs, with no**
- flip-flop breaking the loop, would be classified as:
- A) Synchronous sequential logic
- B) Combinational logic
- C) Neither combinational nor synchronous sequential (unbroken feedback
- loop, no clock)
- D) A flip-flop


---

<a id="res-2"></a>
## Synthesized Resource 2: DLCD_Unit_1_Question_Bank.md
**Source File**: `resources/DLCD_Unit_1_Question_Bank.md`

# Unit 1: Question Bank (Comprehensive & Deduplicated)

## Section A: Descriptive Questions with Detailed Solutions

### Q1. Define a digital circuit. Explain the functional specification and timing specification of a digital circuit. Distinguish between input, output and internal nodes.

**Solution:**
A digital circuit is a network of elements that processes discrete-valued variables, generally represented using binary values 0 and 1.A digital circuit can be viewed as a black box having:1. One or more input terminals2. One or more output terminals3. A functional specification4. A timing specificationFunctional specification describes the relationship between inputs and outputs. For example, for an AND function, Y = AB. The output is 1 only when both inputs are 1.Timing specification describes how long the output takes to respond after an input changes. Thus, two circuits may implement the same Boolean function but have different delays.A node is a wire that carries a digital signal. An input node receives information from outside the circuit, an output node sends information to another circuit/system, and an internal node connects elements inside the circuit.Therefore, a digital circuit must be analyzed from both functional and timing perspectives.

### Q2. A digital control system has three inputs A, B, C. The output Y must be HIGH whenever at least two of the inputs are HIGH. Obtain the truth table and derive the Boolean equation in sum-of-products form.

**Solution:**
Since the output is HIGH whenever at least two inputs are HIGH, the required input combinations are 011, 101, 110, and 111.Truth table:A B C | Y0 0 0 | 00 0 1 | 00 1 0 | 00 1 1 | 11 0 0 | 01 0 1 | 11 1 0 | 11 1 1 | 1The corresponding minterms are:m3 = A'BCm5 = AB'Cm6 = ABC'm7 = ABCTherefore:Y = A'BC + AB'C + ABC' + ABCorY = Σ(3,5,6,7).This demonstrates obtaining a Boolean equation directly from a truth table in canonical sum-of-products form.

### Q3. For the Boolean function F(A,B,C) = Σ(1,3,5,7), obtain the canonical sum-of-products expression and simplify it using a K-map.

**Solution:**
The minterms are:1 = 0013 = 0115 = 1017 = 111Hence the canonical SOP expression is:F = A'B'C + A'BC + AB'C + ABCFactor C:F = C(A'B' + A'B + AB' + AB)The expression in brackets contains all possible combinations of A and B:A'B' + A'B + AB' + AB = 1Therefore:F = CHence:F = C.A K-map gives the same result by grouping the four 1s corresponding to C = 1.

### Q4. Explain the difference between sum-of-products and product-of-sums canonical forms. Give a suitable example for each.

**Solution:**
In Sum-of-Products (SOP) form, the function is represented as an OR of product terms. Each product term corresponds to a row where the output is 1.Example:F(A,B) = Σ(1,3)F = A'B + ABIn Product-of-Sums (POS) form, the function is represented as an AND of sum terms. Each maxterm corresponds to a row where the output is 0.Example:F = Π(0,2)F = (A+B)(A'+B)Difference:SOP is an OR of AND terms and is based on output-1 rows (minterms). POS is an AND of OR terms and is based on output-0 rows (maxterms). SOP uses Σ notation, while POS uses Π notation.

### Q5. A safety system produces output 1 for minterms 2, 3, 6, 7. Write the canonical SOP expression and explain how the resulting equation can be used to implement the circuit.

**Solution:**
For three variables A, B, C:2 = 0103 = 0116 = 1107 = 111Therefore:F = A'BC' + A'BC + ABC' + ABCFactor B:F = A'B(C'+C) + AB(C'+C)Since C'+C = 1:F = A'B + ABF = B(A'+A)F = BTherefore:F = B.Implementation: instead of implementing four minterms using multiple gates, the minimized circuit can simply connect B to F. This reduces gate count, hardware complexity, and propagation delay.

### Q6. A digital system has the following functional requirement: the output should be HIGH when the input combination is 0, 2, 4, or 6. Derive the Boolean function and explain how a K-map can be used to minimize it.

**Solution:**
Assume three inputs A, B, C.The required minterms are:F = Σ(0,2,4,6)Canonical SOP:F = A'B'C' + A'BC' + AB'C' + ABC'Every selected minterm has C = 0. Therefore, on the K-map the four 1s form a group of four. Within this group A and B change, while C remains 0.Thus:F = C'Therefore:F = C'.

### Q7. Explain the procedure for minimizing a Boolean function using a four-variable Karnaugh map. State the rules that must be followed while forming groups.

**Solution:**
A Karnaugh map is a graphical method for simplifying Boolean functions. A four-variable K-map contains 2^4 = 16 cells.Procedure:1. Draw the four-variable K-map.2. Enter 1s corresponding to the specified minterms.3. Enter X for don't-care conditions if given.4. Identify adjacent 1s.5. Form groups containing 1, 2, 4, 8, ... cells.6. Make groups as large as possible.7. Groups may wrap around the edges.8. A cell may belong to more than one group when useful.9. Obtain the implicant corresponding to each group.10. OR all required implicants.The objective is to obtain a minimal expression using the fewest/largest valid groups.

### Q8. Minimize the following function using a four-variable K-map: F(A,B,C,D) = Σ(0,1,2,3,8,9,10,11).

**Solution:**
The minterms are 0, 1, 2, 3, 8, 9, 10, and 11. These eight cells form one group of eight.Throughout this group:B = 0while A, C, and D vary.Therefore the only remaining variable is B'.Hence:F = B'.

### Q9. Minimize F(A,B,C,D) = Σ(1,3,5,7,9,11,13,15) using a K-map. Explain your grouping.

**Solution:**
All the specified minterms are odd. In binary, every odd number has D = 1.Therefore, all eight cells corresponding to D = 1 can be grouped together. A, B, and C vary within the group, while D remains constant.Hence:F = D.Thus the minimized function is:F = D.

### Q10. Minimize F(A,B,C,D) = Σ(0,2,8,10,11,14,15) using a four-variable K-map.

**Solution:**
Form the largest possible groups.Group 1: minterms 0, 2, 8, 10 form a group of four. For this group B = 0 and D = 0, giving:B'D'Group 2: minterms 10, 11, 14, 15 form a group of four. For this group A = 1 and C = 1, giving:ACTherefore:F = B'D' + AC.The key point is to prefer maximum-sized valid groups so that the resulting expression contains fewer literals.

### Q11. What are don't-care conditions? Explain how they help in K-map minimization.

**Solution:**
A don't-care condition occurs when the output of a circuit does not matter for a particular input combination. It is represented by X.In a K-map, an X can be treated as either 0 or 1 depending on which choice produces a simpler expression.For example, if a circuit uses only decimal inputs 0–9, inputs 10–15 are invalid. Their outputs can therefore be treated as don't-cares.A don't-care should be included in a group when it helps form a larger group. If it does not help, it can be ignored.Advantages include fewer product terms, fewer literals, fewer gates, and simpler hardware.

### Q12. A seven-segment display receives a 4-bit input representing decimal digits 0–9. Inputs 10–15 are never used. Explain how these unused inputs can be exploited during K-map minimization.

**Solution:**
Since inputs 10–15 never occur during normal operation, their corresponding output values are irrelevant. They can be marked X in the K-map.While grouping required 1s, these Xs may be included whenever they help produce a larger group. For example, a group of 2 may become a group of 4, or a group of 4 may become a group of 8.Larger groups eliminate more variables, producing fewer gates and a simpler circuit.Thus, unused input combinations can be exploited as don't-care conditions during K-map minimization.

### Q13. Why is the minimal K-map expression not necessarily unique? Explain with reference to prime implicants.

**Solution:**
A Boolean function can sometimes be minimized in more than one valid way. This happens when a particular 1-cell can be included in more than one equally large prime implicant.A prime implicant is an implicant that cannot be combined further to remove another literal.If two different valid groupings cover all required 1s and each produces an expression with the same minimum cost, both expressions are minimal.Therefore, the minimal expression of a Boolean function is not necessarily unique. What matters is that the expression is logically equivalent to the original function and meets the desired minimization criterion.

### Q14. Explain the operation of a 2:1 multiplexer. Derive its Boolean equation and explain its truth table.

**Solution:**
A 2:1 multiplexer has two data inputs D0 and D1, one select input S, and one output Y.Operation:S = 0 -> Y = D0S = 1 -> Y = D1Therefore:Y = S'D0 + SD1When S = 0:Y = 1·D0 + 0·D1 = D0When S = 1:Y = 0·D0 + 1·D1 = D1Hence:Y = S'D0 + SD1.The multiplexer therefore selects one of several inputs and forwards the selected input to the output.

### Q15. Explain how a 4:1 multiplexer can be constructed using 2:1 multiplexers. Determine the number of 2:1 multiplexers required.

**Solution:**
A 4:1 MUX has D0, D1, D2, D3 and two select lines S1 and S0.First stage:- MUX 1 selects between D0 and D1 using S0.- MUX 2 selects between D2 and D3 using S0.Second stage:- MUX 3 selects between the outputs of MUX 1 and MUX 2 using S1.Therefore:3 two-to-one multiplexers are required.The first stage performs two selections in parallel, while the second stage selects between the resulting two signals.

### Q16. A processor needs to select one of eight possible data sources. Determine the type of multiplexer required and the number of select lines needed. Explain your answer.

**Solution:**
There are eight possible data inputs, so an 8:1 multiplexer is required.For an N:1 multiplexer, the number of select lines is:log2(N)For N = 8:log2(8) = 3Therefore:- Multiplexer required = 8:1- Select lines required = 3The three select bits provide 2^3 = 8 possible combinations, allowing each of the eight data sources to be selected.

### Q17. Implement F(A,B,C) = Σ(1,2,5,7) using an 8:1 multiplexer.

**Solution:**
An 8:1 MUX has three select inputs. Choose:S2 = A, S1 = B, S0 = C.The data inputs correspond to minterms 0 through 7. Since the function is 1 for minterms 1, 2, 5, and 7:D0 = 0D1 = 1D2 = 1D3 = 0D4 = 0D5 = 1D6 = 0D7 = 1Thus:D0=0, D1=1, D2=1, D3=0, D4=0, D5=1, D6=0, D7=1.With A, B, C connected to the select inputs, the MUX directly realizes the Boolean function.

### Q18. Explain the operation of a decoder. How is a decoder different from a multiplexer?

**Solution:**
A decoder converts an N-bit binary input into one of up to 2^N outputs. For example, a 2-to-4 decoder has two inputs and four outputs. For each input combination, exactly one output is asserted.Difference:Multiplexer: many data inputs -> one output. It selects one input according to select lines.Decoder: binary input -> one selected output. It identifies or activates an output according to the input code.Thus, a MUX is primarily a data-selection circuit, whereas a decoder is primarily a code-to-one-of-many-output circuit.

### Q19. A memory system contains eight memory modules. A 3-bit address is used to select exactly one module at a time. Explain how a decoder can be used for module selection.

**Solution:**
A 3-bit address has 2^3 = 8 possible combinations. Therefore, a 3:8 decoder can be used.The three address bits are connected to the decoder inputs. Each decoder output corresponds to one memory module:000 -> M0001 -> M1010 -> M2011 -> M3100 -> M4101 -> M5110 -> M6111 -> M7Only the selected decoder output is asserted, enabling the corresponding memory module. Thus, the decoder performs address decoding and ensures that one module is selected for each address.

### Q20. Differentiate between combinational and sequential logic. Explain the role of memory/state in sequential circuits.

**Solution:**
In a combinational circuit, the output depends only on the current inputs:Y = f(X)There is no memory of previous inputs. Examples include multiplexers and decoders.In sequential logic, the output depends on current inputs and previous state:Y = f(X,Q)where Q represents stored state.The state stores information about past events. Therefore, sequential circuits can perform functions such as counting, storing data, and controlling a sequence of operations.The key distinction is that combinational logic has no memory, whereas sequential logic has state/memory.

### Q21. Given the input waveforms of an SR latch, explain how the output Q is determined. Discuss the SET, RESET and HOLD conditions.

**Solution:**
An SR latch has two inputs: S (Set) and R (Reset).For an active-high SR latch:S=0, R=0 -> HOLDS=0, R=1 -> RESETS=1, R=0 -> SETS=1, R=1 -> invalid/forbiddenSet: when S=1 and R=0, Q becomes 1.Reset: when S=0 and R=1, Q becomes 0.Hold: when S=0 and R=0, the latch retains its previous state.The important feature is memory: during HOLD, the current output depends on the previous state.

### Q22. A D latch is transparent when CLK=1. If D during a HIGH clock period is 0 -> 1 -> 0 -> 1, explain the output sequence. What happens when the clock becomes LOW?

**Solution:**
A D latch is level-sensitive. When CLK=1, it is transparent, so Q follows D.Therefore, during the HIGH clock period:D: 0 -> 1 -> 0 -> 1Q: 0 -> 1 -> 0 -> 1When CLK becomes 0, the latch becomes opaque and holds its last value.Therefore, after the clock goes LOW:Q = 1Even if D subsequently changes while CLK remains LOW, Q does not change until the latch becomes transparent again.

### Q23. Compare a D latch and a positive-edge-triggered D flip-flop for the same changing input signal. Explain why the two devices can produce different outputs.

**Solution:**
A D latch is level-sensitive. When its active clock level is present, changes in D can propagate to Q.A positive-edge-triggered D flip-flop is edge-sensitive. It copies D to Q only at the rising clock edge.If D changes several times while CLK is HIGH:- A D latch can respond to all those changes.- A positive-edge-triggered D flip-flop captures only the value present at the rising edge.Therefore, the two devices can produce different output waveforms for the same input sequence.This difference is fundamental: a latch is transparent during an active level, while a flip-flop samples at a clock edge.

### Q24. Construct a T flip-flop using a D flip-flop and logic. Derive the required D input equation.

**Solution:**
A T flip-flop toggles when T=1 and holds its state when T=0.Truth table:T Q | Q+0 0 | 00 1 | 11 0 | 11 1 | 0Therefore:Q+ = T XOR QFor a D flip-flop:Q+ = DHence:D = T XOR QSo the implementation is:1. Feed T and the current Q into an XOR gate.2. Connect the XOR output to D.3. Use the same clock for the D flip-flop.Thus:D = T ⊕ Q.

### Q25. A JK flip-flop is to be implemented using a D flip-flop. Derive the expression for D in terms of J, K and Q.

**Solution:**
The JK flip-flop has:J=0, K=0 -> HoldJ=0, K=1 -> ResetJ=1, K=0 -> SetJ=1, K=1 -> ToggleIts characteristic equation is:Q+ = JQ' + K'QFor a D flip-flop:Q+ = DTherefore:D = JQ' + K'QHence, a D flip-flop can implement a JK flip-flop by connecting the output of combinational logic implementing JQ' + K'Q to D.

### Q26. Explain the operation of an N-bit register. Why are multiple flip-flops required?

**Solution:**
An N-bit register stores an N-bit binary value. It is constructed using N flip-flops, normally D flip-flops, with a common clock.For a 4-bit register:Inputs: D3, D2, D1, D0Outputs: Q3, Q2, Q1, Q0At the active clock edge, all flip-flops capture their corresponding inputs simultaneously.Therefore:Q3:0+ = D3:0Multiple flip-flops are required because each flip-flop stores one bit. Thus N bits require N storage elements.A register is therefore a bank of flip-flops sharing a common clock.

### Q27. A processor register should load new data only when ENABLE is HIGH. When ENABLE is LOW, it must retain its previous value even when clock edges occur. Explain how an enabled flip-flop achieves this requirement.

**Solution:**
An enabled flip-flop has D, CLK, EN, and Q.Its operation is:EN=1 -> at the active clock edge, Q loads D.EN=0 -> at the active clock edge, Q retains its old value.Therefore:Q+ = D, when EN=1Q+ = Q, when EN=0A MUX can be placed before the D input:DFF = EN·D + EN'·QWhen EN=1:DFF = DWhen EN=0:DFF = QThus the old output is fed back and retained when the register is disabled.

### Q28. A digital system requires a flip-flop to return to a known state whenever RESET is asserted. Explain the purpose of a resettable flip-flop and distinguish between resetting the state and loading normal data.

**Solution:**
A resettable flip-flop contains an additional RESET input. When RESET is asserted, the flip-flop is forced to a known state, generally Q=0.This is important because sequential circuits need a known starting state.During normal operation, when RESET is inactive, the flip-flop captures D at the active clock edge:Q+ = DWhen RESET is asserted:Q -> 0Thus, RESET is used for initialization or recovery to a known state, while D is used for normal data storage.

### Q29. A ring oscillator consists of three identical inverters connected in a loop. Each inverter has a propagation delay of 2 ns. Determine the oscillation period and frequency. Explain why the circuit is not a stable combinational circuit.

**Solution:**
There are N=3 inverters and each has propagation delay tp=2 ns.For a ring oscillator:T = 2NtpTherefore:T = 2(3)(2 ns)T = 12 nsFrequency:f = 1/T  = 1/(12 × 10^-9)  ≈ 83.33 MHzThe circuit is not a stable combinational circuit because the output of each inverter is fed back into the input of another. The feedback prevents a stable Boolean assignment and causes the signal to continually propagate around the loop, producing oscillation.

### Q30. An elevator controller is designed for a building containing 25 floors, but floor 13 does not exist. The controller must remember the current floor. Determine the minimum number of state bits required and explain your reasoning.

**Solution:**
The controller must represent 25 valid floor positions.The number of state bits N must satisfy:2^N >= 25For 4 bits:2^4 = 16 < 25Therefore 4 bits are insufficient.For 5 bits:2^5 = 32 >= 25Hence:N = 5 state bitsTherefore, at least 5 bits of state are required to uniquely represent all 25 valid floor positions. The unused state encodings can be treated as invalid/unreachable states and handled appropriately in the controller design.


---
## Section B: Additional Curated Practice & Review Questions

1. Differentiate between combinational and sequential logic circuits. Support your answer with two real-life analogies other than the automatic-door and ATM examples.

2. Explain the rules that must be satisfied for a circuit to be considered a combinational circuit. In particular, discuss why cyclic paths are not permitted.

3. State and explain the three rules that must simultaneously hold for a circuit to be classified as combinational.

4. Explain why a circuit containing a cyclic feedback path cannot be classified as combinational, even if every individual element within it is itself combinational.

5. A circuit is built from three combinational elements E1, E2, and E3, where E3 begins computing only after the outputs of both E1 and E2 become valid. Given Delay(E1), Delay(E2), and Delay(E3), derive a general formula for the worst-case propagation delay of the overall circuit, and explain your reasoning.

6. Define the terms Literal, Implicant, Minterm, and Maxterm, giving one worked example of each for a 3-variable function with inputs a, b, c.

7. Implement the Boolean function F = xy + x’y’ + y’z (a) With AND, OR, and inverter gates (b)  With OR and inverter gates (c) With AND and inverter gates (d) (e) With NAND and inverter gates With NOR and inverter gates.

8. Express the following function as a sum of minterms and as a product of maxterms: F(A, B, C, D) = B’D + A’D + BD.

9. Express the complement of the following functions in sum‐of‐minterms form: ( a ) F(A,B ,C, D) = g(2, 4, 7, 10, 12, 14) (b) F ( x, y, z ) = w(3, 5, 7).

10. Starting from y = a′bc + ab′c′ + abc′ + abc, minimize the expression using only Boolean algebra laws (distributive, complement, and identity laws). Show every intermediate step and name the law used at each stage.

11. Convert the POS expression y = (a + b + c)(a + b′ + c)(a′ + b + c′) into its equivalent canonical SOP form, and then convert that SOP form back into POS, showing every step so that the two final expressions match.

12. What is meant by "logic minimization"? Describe at least three different metrics that can be used to judge the quality of a Boolean expression or its circuit realization, and state which specific metric is adopted as the standard in this course.

13. For a three-variable Boolean function, explain how a truth table is converted into canonical SOP form. Include the construction of minterms and Σ-notation.

14. For a three-variable Boolean function, explain how canonical POS form is obtained from the rows where the output is 0. Include maxterms and Π-notation.

15. Given a Boolean equation containing several product terms, simplify it using Boolean identities. Explain at every stage which identity is being applied and compare the gate count before and after minimization.

16. State the Complement law, Identity law, and Distributive law used in Boolean minimization, and prove each using a truth table. Then apply all three, in sequence, to minimize y = xy′z + xyz + xyz′.

17. Convert each of the following expressions into sum of products and product of sums: ( a ) ( u + xw )( x + u’v ) (b) x’ + x(x + y’)(y + z’)

18. Show that the dual of the exclusive‐OR is equal to its complement.

19. Show that a positive logic NAND gate is a negative logic NOR gate and vice versa.

20. Write the Boolean equations and draw the logic diagram of the circuit whose outputs are defined by the following truth table:

21. Determine whether the following Boolean equation is true or false. 
x’y’ + x’z + x’z’ = x’z’ + y’z’ + x’z .

22. Write the following Boolean expressions in sum of products form: (b+d)(a’ +b’ +c).

23. Write the following Boolean expression in product of sums form: a’b +a’c’ +abc.

24. Simplify the Boolean function F (x, y, z) = Σ(3, 4, 6, 7).

25. Explain why Boolean-algebra-based minimization becomes increasingly difficult and error-prone as the number of variables in a function increases, and describe how the K-map method overcomes this limitation.

26. Explain why Karnaugh-map rows and columns are arranged in Gray-code order rather than ordinary binary order. Demonstrate how this ordering guarantees that adjacent cells differ in only one variable.

27. A student groups three cells together in a K-Map because all three cells contain 1. Explain why this grouping is invalid. State the rules governing the number and shape of cells in a valid K-Map group.

28. Construct a 3-variable K-Map for   F(A,B,C)=Σ(0,1,2,4,5,6)  and obtain the minimum SOP expression. Clearly identify the groups and explain which variables are eliminated.

29. Explain the difference between an implicant, prime implicant, and essential prime implicant. Illustrate the difference using a suitable K-Map.

30. T Clock A sequential circuit has two JK flip-flops A and B and one input x . The circuit is described by the following flip-flop input equations: JA = x KA= B JB = x KB= A’ (a) Derive the state equations A ( t + 1) and B ( t + 1) by substituting the input equations for the J and K variables. (b) Draw the state diagram of the circuit.

31. Starting from state a, and the input sequence 01110010011, determine the output sequence for (a) The state table of the previous problem. (b) The reduced state table from the previous problem. Show that the same output sequence is obtained for both.

32. Minimize F(A,B,C)=Σ(0,2,3,4,6,7)  using a K-Map. Identify all useful prime implicants and determine which are essential.

33. What is the main difference between an initial statement and an always statement in Verilog HDL?

34. Explain K-Map wrap-around adjacency. Demonstrate how cells at opposite edges of a K-Map can form a valid group.

35. Explain the concept of don't-care conditions. Why can a don't-care cell be treated as either 0 or 1 during minimization? Give an example where assigning a don't-care as 1 produces a substantially simpler expression.

36. A seven-segment display accepts a 4-bit input representing decimal digits 0–9. Inputs 10–15 are invalid. Construct the truth table and use K-Maps to derive the simplified equation for segment Sa​.

37. Minimize f(a, b, c, d) = Σ(0, 1, 2, 3, 8, 9, 10, 11) using a 4-variable K-map. Derive the simplest SOP expression and explain the reasoning behind every grouping used.

38. A PN flip-flop has four operations: clear to 0, no change, complement, and set to 1, when inputs P and N are 00, 01, 10, and 11, respectively. (a) Tabulate the characteristic table. (b)  Derive the characteristic equation. (c) Tabulate the excitation table. (d) Show how the PN flip-flop can be converted to a D flip-flop.

39. For the following state table 
    (a) Draw the corresponding state diagram.
    (b)  Tabulate the reduced state table. 
    (c) Draw the state diagram corresponding to the reduced state table.

40. Explain the differences among a truth table, a state table, a characteristic table, and an excitation table. Also, explain the difference among a Boolean equation, a state equation, a characteristic equation, and a flip-flop input equation.

41. A sequential circuit has one flip-flop Q, two inputs x and y, and one output S . It consists of a full-adder circuit connected to a D flip-flop, as shown in Fig . Derive the state table and state diagram of the sequential circuit.

42. Explain why a group of 8 cells eliminates three variables, a group of 4 eliminates two variables, and a group of 2 eliminates one variable. Derive this rule logically rather than merely stating it.

43. Given a 4-variable K-Map with several 1s and don't-care cells, describe a systematic algorithm for obtaining the minimum SOP expression, starting from identifying the largest possible groups and ending with the selection of required groups.

44. A sequential circuit has three flip-flops A, B, C ; one input x_in ; and one output y_out . The state diagram is shown in Fig below . The circuit is to be designed by treating the unused states as don’t-care conditions. Analyze the circuit obtained from the design to determine the effect of the unused states. (a)Use D flip-flops in the design. (b) Use JK flip-flops in the design.

45. Design the sequential circuit specified by the state diagram of Figure, using T flip-flops.

46. Explain the operation of a 2:1 multiplexer using its block diagram, truth table, Boolean equation, and gate-level implementation.

47. Derive the relationship between the number of inputs and select lines for a multiplexer. Determine the number of select lines required for 2:1, 4:1, 8:1, 16:1, and 32:1 MUXes. Explain three different ways of implementing a 4:1 multiplexer:
    i. two-level logic,
    ii. tri-state buffers,
    iii. hierarchical composition of smaller MUXes.Compare their structures.

48. Implement Y=A+B using a 2:1 multiplexer. Use one variable as the select input and derive the required data inputs systematically from the truth table.

49. Explain the concept of a multiplexer (mux). Derive the general relationship between the number of data inputs N and the number of select lines required (log₂N), and tabulate this relationship for N = 2, 4, 8, and 16.

50. Implement Y=A⊕B using a 2:1 multiplexer. Explain why your selected data-input connections produce XOR.

51. Explain how a multiplexer can be used as a lookup table to implement an arbitrary Boolean function. Demonstrate the process using a three-variable function and an 8:1 MUX.

52. Implement a three-variable Boolean function using an 8:1 MUX. Determine the eight data-input values directly from the function's truth table and explain the mapping.

53. Implement F(A,B,C)=Σ(1,3,5,7) using a 3:8 decoder and an OR gate. Clearly identify which decoder outputs must be connected to the OR gate and explain why the implementation works.

54. Compare implementing a Boolean function using a multiplexer versus implementing it using a decoder + OR gate. Discuss the selection mechanism, number of components, flexibility, and how the Boolean function maps onto the hardware.

55. Explain the operation of an N-input decoder and why it produces 2N outputs. Explain the meaning of one-hot output and show how decoder outputs correspond to minterms.

56. Implement F(A,B,C,D)=Σ(1,3,4,7,9,11,12,15) using a 4:16 decoder and external OR gates. Determine which decoder outputs must be connected.

57. Implement F(A,B,C)=A′B+AC using a 2:1 MUX. You are allowed to use one inverter. Determine:select input,I0,I1,inverter connection. Then verify your circuit using the truth table.

58. A decoder is constructed using two levels of logic gates. The first level has a propagation delay of 20ns, and the second level has a propagation delay of 30ns. Determine:
    i. the propagation delay,
    ii. the critical path,
    iii. the contamination delay if the corresponding gate contamination delays are given.

59. Explain why the longest path determines propagation delay.The textbook includes decoder design problems specifically involving critical path, propagation delay, and contamination delay

60. Implement the following three Boolean functions using a single 3-to-8 decoder: F1​(A,B,C)=Σ(1,3,5) F2​(A,B,C)=Σ(0,2,6,7) F3​(A,B,C)=Σ(2,3,6) Determine the decoder-output connections required for each function. Design an 8:1 multiplexer with the shortest possible delay from the data inputs to the output. You are given the available gate types and their propagation/contamination delays. Your answer must include:
    i. circuit structure,
    ii. critical path,
    iii. propagation delay,
    iv. contamination delay,
Justify why your architecture is faster than alternative 	implementations.

61. A Boolean function is given by F(A,B,C,D)=Σ(0,2,3,6,7,8,10,14,15). Implement it using a 4:1 MUX with the minimum number of additional gates. You must:
    i. select appropriate select variables,
    ii. derive each data input,
    iii. simplify each data input,
    iv. identify the additional gates required,
    v. draw the final implementation.

62. The D latch of Figure is constructed with four NAND gates and an inverter. 

Consider the following three other ways for obtaining a D latch. In each case, draw the logic diagram and verify the circuit operation.
(a) Use NOR gates for the SR latch part and AND gates for the other two. An inverter may be needed.
(b) Use NOR gates for all four gates. Inverters may be needed.
(c) Use four NAND gates only (without an inverter). This can be done by connecting the output of the upper gate in Figure (the gate that goes to the SR latch) to the input of the lower gate (instead of the inverter output).

63. Given the input wave-forms shown in the Figure, sketch the output, Q, of an SR latch.

64. Design an asynchronously resettable D latch using logic gates.

65. A sequential circuit with two D flip-flops A and B, two inputs, x and y ; and one output z is specified by the following next-state and output equations:
A(t + 1) = xy’+ xB
B(t + 1) = xA + xB’
z = A
(a) Draw the logic diagram of the circuit.
(b) List the state table for the sequential circuit.
(c) Draw the corresponding state diagram.

66. 73.  Derive the state table and the state diagram of the sequential circuit shown in the Figure.Explain the function that the circuit performs.

67. For the circuit described by the state diagram of the Figure ,

(a) Determine the state transitions and output sequence that will be generated when an input sequence of 010110111011110 is applied to the circuit and it is initially in the state 00.
(b) Find all of the equivalent states in the Figure and draw a simpler, but equivalent, state diagram.
(c) Using D flip-flops, design the equivalent machine (including its logic diagram) described by the state diagram in (b).

68. Design a sequential circuit with two D flip-flops A and B, and one input x_in .
(a) When x_in = 0, the state of the circuit remains the same. When x_in = 1, the circuit goes through the state transitions from 00 to 01, to 11, to 10, back to 00, and repeats.
(b) When x_in = 0, the state of the circuit remains the same. When x_in =1, the circuit goes through the state transitions from 00 to 11, to 01, to 10, back to 00, and repeats.

69. Which of the circuits in the Figure  are synchronous sequential circuits? Explain.

70. Implement a full adder with two 4x1 multiplexers.

71. Design a combinational circuit with three inputs, x, y, and z, and three outputs, A, B, and C. When the binary input is 0, 1, 2, or 3, the binary output is one greater than the input. When the binary input is 4, 5, 6, or 7, the binary output is two less than the input.

72. A majority circuit is a combinational circuit whose output is equal to 1 if the input variables have more 1's than 0's. The output is 0 otherwise. (a)* Design a 3-input majority circuit by finding the circuit's truth table, Boolean equation, and a logic diagram. (b) Write and verify a Verilog gate-level model of the circuit.

73. Design a four-bit combinational circuit 2's complementer. (The output generates the 2's complement of the input binary number.) Show that the circuit can be constructed with exclusive-OR gates. Can you predict what the output functions are for a five-bit 2's complementer?

74. In an SR latch, both S and R are accidentally asserted high at the same time due to a wiring fault. Predict the resulting outputs Q and Q', and explain why this condition is considered invalid or problematic for circuit design.

75. You are designing a circuit and need the stored value to change immediately whenever the data input changes, as long as the clock is high. Would you choose a D latch or a D flip-flop for this requirement? Justify your choice.

76. Two flip-flops in a circuit are accidentally connected to two different clock signals, clk1 and clk2, instead of a shared clock. Explain what problems this could cause in a supposedly synchronous system, and how you would fix it.

77. A system needs all its flip-flops to start from a known state (0) the moment power is turned on, without waiting for a clock edge. Which type of flip-flop input would you use, and how would its internal circuit differ from a standard resettable flip-flop?

78. A ring oscillator is built using five inverters instead of three, each with a propagation delay of 1 ns. Derive the oscillation period of this circuit and generalize a formula for an odd-numbered inverter loop, explaining why an even number of inverters would not oscillate in the same way.

79. Ben Bitdiddle has designed the circuit in the Figure  to compute a registered four-input XOR function. Each two-input XOR gate has a propagation delay of 100 ps and a contamination delay of 55 ps. Each flip-flop has a setup time of 60 ps, a hold time of 20 ps, a clock-to-Q maximum delay of 70 ps, and a clock-to-Q minimum delay of 50 ps.
(a) If there is no clock skew, what is the maximum operating 	frequency of the circuit?
(b) How much clock skew can the circuit tolerate if it must operate 	at 2 GHz?
(c) How much clock skew can the circuit tolerate before it might 	experience a hold time violation?

80. Alyssa P. Hacker points out that she can redesign the combinational logic between the registers to be faster and tolerate more clock skew. Her improved circuit also uses three two-input XORs, but they are arranged differently. What is her circuit? What is its maximum frequency if there is no clock skew? How much clock skew can the circuit tolerate before it might experience a hold time violation?

81. Two D flip-flops are connected back-to-back (output of the first feeding the input of the second) and share the same clock signal, but a buffer introduces a small delay between the clock reaching the first and second flip-flop. Analyze whether this circuit will function correctly as a synchronous shift register, and identify the potential failure mode this delay could introduce (hint: consider hold-time violations).

82. You are asked to design a resettable, enabled D flip-flop that must also synchronously load new data only when EN is high, and reset to 0 regardless of D when RESET is high, without introducing clock glitches. Draw a gate-level design combining the enable and reset logic, and justify the order in which the reset and enable conditions should be prioritized.

83. What is the difference between a latch and a flip-flop? Under what circumstances is each one preferable?

84. A combinational circuit's output is mistakenly fed back into one of its own inputs without any register in the path, but the designer argues the circuit is "fast and works fine in simulation." Explain, using the concept of race conditions and propagation delay, why this design is unsafe for real hardware even if simulation shows no errors.

85. Given a synchronous circuit with a feedback path containing exactly one register, and a clock period that is deliberately shortened until errors appear, explain — in terms of combinational propagation delay and setup time — what determines the minimum safe clock period, and derive a general inequality relating clock period, propagation delay, and setup time for correct operation.

86. Ben Bitdiddle has hundreds of friends coming to his party and needs to bake cookies faster. He is considering using spatial and/or temporal parallelism.
    a) Spatial Parallelism: Ben asks Alyssa P. Hacker to help out. She has her own cookie tray and oven.
    b) Temporal Parallelism: Ben gets a second cookie tray. Once he puts one cookie tray in the oven, he starts rolling cookies on the other tray rather than waiting for the first tray to bake.
    c) What is the throughput and latency using spatial parallelism? Using temporal parallelism? Using both?

87. Explain why combinational logic circuits cannot "remember" data, and describe how breaking the no-feedback restriction enables storage elements.

88. Describe the bistable operation of a cross-coupled inverter loop and explain why it is not practical as a usable memory element.

89. With the help of a circuit diagram, explain the working of an SR latch built from two cross-coupled NOR gates, and describe the significance of its invalid state.

90. Why is the SR latch considered "awkward," and how does the D latch resolve this problem by separating the concepts of "what" and "when"?

91. Explain the transparent (level-sensitive) behavior of a D latch when CLK = 1 and CLK = 0.

92. Describe how a D flip-flop is constructed from two back-to-back D latches (master-slave configuration), and explain its operation on the rising clock edge.

93. Differentiate between a latch and a flip-flop in terms of triggering mechanism, with relevant examples.

94. Explain the working of an enabled flip-flop and describe two different circuit techniques used to implement it.

95. Describe the difference between a synchronously resettable and an asynchronously resettable flip-flop, with the help of a circuit diagram.

96. What is an N-bit register? Explain its structure and significance as a building block of sequential circuits.

97. Explain how race conditions arise in sequential circuits containing cyclic feedback paths, and describe how inserting registers eliminates them.

98. With reference to the three-inverter loop example, explain what an astable circuit (ring oscillator) is and describe its output behavior over time.

99. State and explain the four rules that a circuit must satisfy to be classified as a synchronous sequential circuit.

100. Differentiate between synchronous and asynchronous circuit design, and explain why most modern digital systems favor synchronous design.

101. Analyze the classification of different example circuits (combinational, synchronous sequential, or neither) based on the presence of registers and feedback paths.

102. A cross-coupled NAND-based SR latch (S'R' latch) is used in a circuit where both inputs are inadvertently pulled low (S'=0, R'=0) briefly during a glitch. Predict the resulting state of Q and Q', and explain why this differs from the invalid condition of the NOR-based SR latch.

103. You are given a black-box sequential element and told only that its output changes multiple times while the clock is held high. Determine, with reasoning, whether this element is a latch or a flip-flop, and describe an experiment (input pattern) you could apply to confirm your answer.

104. A 4-bit register is built from four D flip-flops sharing a common clock, but one flip-flop's clock line has a broken trace causing it to receive a stuck-low signal. Predict the observable behavior of the register's output bus D3:0 → Q3:0, and explain how this fault could be diagnosed using only input/output waveforms.

105. In a synchronously resettable flip-flop built using an AND gate ahead of the D input, the RESET signal glitches briefly HIGH for a duration shorter than the clock period, occurring while CLK = 0. Explain whether this glitch will affect the stored state, and contrast this with what would happen in an asynchronously resettable design under the same glitch.

106. A designer cascades two enabled flip-flops (Flip-Flop A's output feeds Flip-Flop B's D input) and toggles EN on Flip-Flop A while CLK is HIGH, violating the stated design rule. Explain, using the concept of clock gating, what specific hazard this could introduce into the circuit's behavior.

107. A digital system needs to load a new value into a flip-flop only once every 4 clock cycles, otherwise retain its current value. Design the required circuit modification and explain how it behaves using a timing diagram.

108. You are given a D flip-flop and a D latch, both fed the same D and CLK waveforms containing glitches while CLK = 1. Sketch and justify the resulting Q output for each device, explaining why their behavior differs.

109. A synchronous sequential circuit is composed of combinational logic blocks and registers, but a designer accidentally omits a register on one of the feedback paths while keeping registers on all others. Explain why this circuit fails the formal definition of a synchronous sequential circuit, and predict what kind of behavioral problems could result during operation.

110. Consider a system with two independent clock domains, each synchronous internally, that need to exchange a single data bit. Using the asynchronous-vs-synchronous design concepts discussed, explain why directly connecting a flip-flop output from one clock domain to a flip-flop input in the other domain is risky, and propose a safer approach at a conceptual level.


---

<a id="res-3"></a>
## Synthesized Resource 3: DLCD_Unit_1_MCQs.md
**Source File**: `resources/DLCD_Unit_1_MCQs.md`

# Unit 1: Multiple Choice Questions (Deduplicated with Explanations)

**Q1. Why must all registers in a synchronous sequential circuit share the same clock signal?**
- A. So that all state updates happen at the same instant, avoiding race conditions between registers
- B. To reduce the total number of gates in the circuit
- C. Because registers cannot function without a shared clock wire physically touching
- D. It is only a convention with no functional purpose
**Explanation:** In synchronous sequential design, a shared global clock ensures that all state updates occur simultaneously at the active clock edge. This avoids race conditions and timing hazards between cascading registers.

**Q2. An essential prime implicant is a prime implicant that:**
- A. Covers the maximum possible number of squares in the map
- B. Contains at least one square (minterm) that is not covered by any other prime implicant
- C. Is always adjacent to a don't-care square
- D. Must always contain exactly two literals
**Explanation:** An Essential Prime Implicant (EPI) covers at least one 1 (minterm) that is not covered by any other prime implicant. Because that minterm must be satisfied, the EPI must be included in every minimal SOP cover.

**Q3. In Product-of-Sums (POS) form, the Boolean formula is constructed as:**
- A. Sum of all minterms corresponding to a 1 output
- B. Product of all maxterms corresponding to a 0 output
- C. Product of all minterms corresponding to a 1 output
- D. Sum of all maxterms corresponding to a 0 output
**Explanation:** The canonical Product-of-Sums (POS) form is formed by taking the product (AND) of all maxterms for which the truth table output is 0. Formally, $F = \prod M(i)$ where $f(i) = 0$.

**Q4. What is the key structural difference between a D latch and a D flip-flop?**
- A. A flip-flop has no clock input at all
- B. A flip-flop is built from two back-to-back latches (master-slave) and changes state only on a clock edge, unlike the level-sensitive latch
- C. A latch always requires two separate clocks
- D. There is no real difference - the terms are interchangeable
**Explanation:** A D latch is level-sensitive (transparent whenever CLK=1). A D flip-flop is edge-triggered, constructed from two cascaded latches (master-slave with inverted clocks) or an edge-detecting latch circuit, sampling D only at clock transitions.

**Q5. How many select lines does a 4:1 multiplexer require?**
- A. 1
- B. 2
- C. 3
- D. 4
**Explanation:** A multiplexer with $N$ inputs requires $k = \lceil \log_2 N \rceil$ select lines. For $N = 4$, $\log_2(4) = 2$ select lines ($S_1, S_0$).

**Q6. An AND gate whose output is fed back to one of its own inputs, with no flip-flop in the loop, is classified as:**
- A. Combinational logic
- B. Synchronous sequential logic
- C. Neither combinational nor synchronous sequential
- D. A D flip-flop
**Explanation:** Combinational logic strictly prohibits cyclic (feedback) paths. Synchronous sequential logic requires every cyclic path to contain at least one clocked register. Therefore, an unclocked feedback loop is asynchronous and violates both rules.

**Q7. The same D and CLK waveform is applied to both a D latch and a D flip-flop, where D changes value more than once while CLK = 1. Which statement correctly compares their outputs Q?**
- A. Both outputs will be identical at all times
- B. The D latch's Q will track every change in D while CLK = 1 (transparent), while the D flip-flop's Q updates only once, at the rising edge of CLK
- C. The D flip-flop updates continuously while CLK = 1, and the D latch updates only at the rising edge
- D. Neither device changes state until CLK falls to 0
**Explanation:** The D latch is transparent throughout the high duration of CLK ($CLK = 1$), so its output follows every change in D. The D flip-flop is edge-triggered and samples D only at the instantaneous rising edge of CLK.

**Q8. When a digital circuit is viewed as a 'black box,' it is completely described by its input terminals, output terminals, and:**
- A. Only a functional specification
- B. A functional specification and a timing specification
- C. Only a timing specification
- D. A list of the gates used inside
**Explanation:** In abstraction-based digital design (Harris & Harris), a black box is completely specified by its input terminals, output terminals, functional specification (relationship between inputs and outputs), and timing specification (delays).

**Q9. A 'minterm' for a Boolean function of 3 variables is:**
- A. Any single literal
- B. A sum of two or more literals
- C. A product term that includes all three input variables
- D. A product term with only one input variable
**Explanation:** A minterm (standard product) for an $n$-variable function is a product term that contains each of the $n$ variables exactly once in either complemented or uncomplemented form.

**Q10. The output equation of a 2:1 multiplexer with data inputs D0, D1 and select line S is:**
- A. $Y = D_0 S + D_1 S$
- B. $Y = D_0 S' + D_1 S$
- C. $Y = D_0 + D_1 + S$
- D. $Y = (D_0 + S)(D_1 + S)$
**Explanation:** When $S = 0$, $Y = D_0$; when $S = 1$, $Y = D_1$. This is expressed in Boolean form as $Y = S' D_0 + S D_1$.

**Q11. In the minimization step $y = bc(a' + a) + ac(b' + b) \implies y = bc(1) + ac(1)$, which law has been applied?**
- A. Distributive law
- B. Identity law
- C. Complement law
- D. De Morgan's law
**Explanation:** The Complement Law states that $x + x' = 1$. Replacing $(a' + a)$ and $(b' + b)$ with $1$ is an application of the complement law.

**Q12. A combinational circuit has three elements: Delay(E1) = 5 ns, Delay(E2) = 8 ns, Delay(E3) = 4 ns. E3 begins computation only after both E1 and E2 outputs become valid. What is the worst-case propagation delay of the circuit?**
- A. 8 ns
- B. 12 ns
- C. 13 ns
- D. 17 ns
**Explanation:** E1 and E2 operate in parallel. E3 must wait for both to finish, which takes $\max(5\text{ ns}, 8\text{ ns}) = 8\text{ ns}$. Then E3 takes 4 ns. Total worst-case propagation delay = $8 + 4 = 12\text{ ns}$.

**Q13. As per the rules of combinational composition, what happens if a circuit contains a cyclic (feedback) path with no register in it?**
- A. It is still combinational if the loop has an even number of gates
- B. It cannot be classified as combinational
- C. It automatically becomes a flip-flop
- D. It becomes combinational only at high clock speeds
**Explanation:** A combinational circuit must have an acyclic schematic (no feedback loops). Any unclocked cyclic path creates memory, oscillation, or race conditions, disqualifying it from being combinational.

**Q14. A Boolean function of n input variables has how many possible minterms?**
- A. $n$
- B. $2n$
- C. $2^n$
- D. $n^2$
**Explanation:** Each of the $n$ binary variables can appear either complemented or uncomplemented (2 choices). Hence, there are $2^n$ unique minterm combinations.

**Q15. Which set contains only combinational circuits?**
- A. Adder, Multiplexer, Decoder
- B. Counter, Register, Flip-Flop
- C. Decoder, Counter, Encoder
- D. Comparator, Register, Multiplexer
**Explanation:** Adders, multiplexers, and decoders contain no internal storage or feedback loops; outputs depend solely on current inputs. Counters, registers, and flip-flops are sequential circuits.

**Q16. Minimize $y = a'bc + ab'c + abc' + abc$ using the distributive, complement, and identity laws. What is the minimized SOP expression?**
- A. $bc + ac$
- B. $ab + bc$
- C. $ab + ac$
- D. $ab' + bc$
**Explanation:** Group terms: $(a'bc + abc) + (ab'c + abc) = bc(a' + a) + ac(b' + b) = bc(1) + ac(1) = bc + ac$ (or by K-map).

**Q17. Ben won't enjoy his picnic if it rains (R) or if there are ants (A). His enjoyment E expressed in SOP form is:**
- A. $E = A + R$
- B. $E = A' R'$
- C. $E = A' + R'$
- D. $E = A R$
**Explanation:** Ben enjoys his picnic ($E = 1$) only when it is NOT raining ($R = 0$) AND there are NO ants ($A = 0$). By De Morgan's Law: $E = (A + R)' = A' R'$.

**Q18. In an unresolved race condition, why is the circuit's output described as 'unstable'?**
- A. Because the circuit consumes too much power
- B. Because the flip-flops aren't connected to any clock at all
- C. Because the output depends on the order/timing of inputs rather than settling to one well-defined value
- D. Because combinational gates need more chip area
**Explanation:** A race condition occurs when multiple signal paths compete, causing the final output state to depend unpredictably on microscopic gate delays and arrival order rather than logical design.

**Q19. Given the truth table for a 3-input function: $(a,b,c) = (000,0), (001,1), (010,0), (011,1), (100,1), (101,1), (110,1), (111,1)$. Using a K-map, what is the minimal Boolean expression for y?**
- A. $y = a + c$
- B. $y = a' c$
- C. $y = a' c + a c$
- D. $y = a + b' c$
**Explanation:** Minterms are $m(1, 3, 4, 5, 6, 7)$. A group of four 1s $\{4, 5, 6, 7\}$ gives $a$. A group of four 1s $\{1, 3, 5, 7\}$ gives $c$. Thus, the minimal expression is $y = a + c$.

**Q20. Decoder outputs are called 'one-hot' because:**
- A. All outputs are HIGH simultaneously
- B. Exactly one output is HIGH for any valid input combination, all others LOW
- C. All outputs are always LOW
- D. Outputs toggle randomly
**Explanation:** In an active-high decoder, for every unique $N$-bit binary input pattern, exactly one corresponding output out of $2^N$ becomes active (HIGH = 1) while all other outputs remain 0 (inactive).

**Q21. What does the reset input on a resettable flip-flop do?**
- A. It forces Q to 0 regardless of the current D input, overriding normal operation
- B. It permanently disables the flip-flop
- C. It doubles the clock frequency
- D. It has no effect on Q, only on D
**Explanation:** When RESET is asserted, it forces the state output $Q$ to 0 (cleared state), overriding the data input $D$ to initialize the circuit to a known state.

**Q22. A 3-input circuit is designed so that inputs can never have all three variables = 1 simultaneously (so row 111 is a don't care). Given truth table: $(000,1), (001,1), (010,0), (011,0), (100,1), (101,1), (110,1), (111,X)$. Treating the don't care to minimize the formula, which expression correctly represents y?**
- A. $y = a + b'$
- B. $y = a' b'$
- C. $y = a b'$
- D. $y = a' + b$
**Explanation:** Minterms: $\{0, 1, 4, 5, 6\}$ and $d(7)$. By grouping $\{0, 1, 4, 5\}$, we get $b'$. By grouping $\{4, 5, 6, 7\}$ (using the $X$ at 7), we get $a$. Thus, $y = a + b'$.

**Q23. A tristate buffer has three possible output states, namely:**
- A. 0, 1 and X
- B. 0, 1 and High Impedance (Z)
- C. High, Low and Don't Care
- D. Set, Reset and Hold
**Explanation:** A tristate buffer provides logic 0 (Low), logic 1 (High), and High Impedance ($Z$), where the output is electrically disconnected from the wire, allowing multiple drivers to share a bus.

**Q24. The Sum-of-Products (SOP) form of a Boolean function is constructed by:**
- A. ANDing all maxterms where the output is 0
- B. ORing all minterms where the output is TRUE
- C. ORing all maxterms
- D. Complementing the truth table
**Explanation:** Canonical Sum-of-Products (SOP) is formed by taking the logical OR (sum) of all minterms (products) for which the function output is 1.

**Q25. In a master-slave D flip-flop built from two D latches with complementary clocks, when CLK = 0:**
- A. The master is transparent and the slave is opaque
- B. The master is opaque and the slave is transparent
- C. Both latches are transparent
- D. Both latches are opaque
**Explanation:** When $CLK = 0$, the inverted clock $CLK' = 1$ enables the master latch (transparent, sampling D), while the slave latch receives $CLK = 0$ (opaque, holding the previous output Q).

**Q26. Why are K-Map rows/columns labeled in the order 00, 01, 11, 10 instead of 00, 01, 10, 11?**
- A. It matches decimal counting order
- B. So that any two adjacent squares differ in exactly one literal (Gray code order)
- C. It is purely a drawing convention with no logical basis
- D. To prevent wrap-around
**Explanation:** Gray code ordering ensures that adjacent squares (and wrap-around edges) differ by exactly one variable bit, which allows applying the adjacency rule $A B + A B' = A$ to eliminate variables.

**Q27. An 'X' (don't care) entry in a K-Map/truth table represents:**
- A. An output that is always 0
- B. An output that is always 1
- C. An output whose value is unspecified - it can be treated as either 0 or 1, whichever gives the smaller formula
- D. An invalid input combination that must be deleted before minimization
**Explanation:** A don't-care condition corresponds to an input pattern that can never occur or whose output does not matter. The designer can treat it as 1 to enlarge groups or 0 to avoid creating extra groups.

**Q28. A D latch is described as transparent when:**
- A. CLK = 0
- B. CLK = 1
- C. D = 0
- D. Only at the rising edge of CLK
**Explanation:** For an active-high D latch, when $CLK = 1$, the latch is in transparent mode, meaning the output $Q$ directly tracks any changes on data input $D$.

**Q29. For an N:2^N decoder, how many total output lines does it have?**
- A. $N$
- B. $N \times 2$
- C. $2^N$
- D. $N^2$
**Explanation:** An $N$-to-$2^N$ decoder takes $N$ binary input lines and decodes them into $2^N$ distinct output lines (one for each possible minterm).

**Q30. A literal in Boolean algebra is:**
- A. A product of two or more variables
- B. A Boolean variable or its complement
- C. A sum involving all input variables
- D. Only an uncomplemented variable
**Explanation:** A literal is defined as a variable in its true (uncomplemented, e.g., $A$) or complemented (inverted, e.g., $A'$) form.

**Q31. 'Wrap-around' in a K-Map means:**
- A. The map can be rotated 90 degrees
- B. The far-left and far-right (and top/bottom, in 4-variable maps) squares are considered adjacent
- C. It only applies when using POS form
- D. Squares in different rows are never adjacent
**Explanation:** Due to Gray code reflection, the outer columns ($00$ and $10$) differ by only 1 bit, as do the outer rows ($00$ and $10$). Therefore, the edges of the K-map wrap around toroidally and are logically adjacent.

**Q32. A worked example produced two equally minimal answers, $f = b'c + bc' + ca$ and $f = b'c + bc' + ab$. This illustrates that:**
- A. K-Maps always give a unique minimal solution
- B. The minimal SOP form is not always unique
- C. POS form must be used instead
- D. The K-Map method has failed
**Explanation:** When non-essential prime implicants can cover the remaining minterms equally well with the same number of terms and literals, multiple distinct but equally minimal SOP equations exist.

**Q33. What is the key difference between a combinational and a sequential logic circuit?**
- A. Combinational circuits have memory, sequential circuits don't
- B. A combinational circuit's output depends only on current inputs; a sequential circuit's output also depends on past inputs
- C. Sequential circuits use only NAND gates
- D. There is no real difference between them
**Explanation:** Combinational circuits are memoryless ($Y = f(X)$). Sequential circuits possess internal memory elements (state), meaning outputs depend on both current inputs and past history ($Y = f(X, \text{State})$).

**Q34. For a three-input function with inputs a, b, c, the maxterm M6 is:**
- A. $a' + b' + c$
- B. $a + b + c'$
- C. $a' + b + c'$
- D. $a + b' + c$
**Explanation:** Decimal $6 = 110_2$ in binary. In maxterm notation, a variable with bit 1 appears complemented and bit 0 appears uncomplemented. Thus, $M_6 = a' + b' + c$.

**Q35. A Boolean function has four inputs (A, B, C, D) and is TRUE only for minterms m(3, 7, 11, 15). Which characteristic do all these minterms share?**
- A. $A = 1$
- B. $C = 1$ and $D = 1$
- C. $C = 0$
- D. $B = 1$
**Explanation:** In binary: $3 = 0011, 7 = 0111, 11 = 1011, 15 = 1111$. In all four terms, the lowest two bits ($C$ and $D$) are both 1, giving the minimized expression $F = C D$.

**Q36. According to Moore's Law, approximately every 18 months the number of transistors per unit chip area:**
- A. Halves
- B. Remains constant
- C. Doubles
- D. Increases by 10%
**Explanation:** Gordon Moore observed in 1965 that the number of transistors integrated on a microchip doubles roughly every 18 to 24 months, driving exponential performance gains.

**Q37. For a circuit to be classified as a synchronous sequential circuit, which condition must hold?**
- A. It must contain only combinational gates
- B. Every feedback (cyclic) path must contain at least one register, and all registers share a common clock
- C. It must have no registers at all
- D. Each register may run off its own independent clock
**Explanation:** The strict compositional rule of synchronous sequential circuits mandates that every cyclic feedback loop must contain at least one clocked register, and all registers must be driven by the same periodic clock.

**Q38. To implement any three-input Boolean function using a decoder and an OR gate, the decoder required is:**
- A. 2:4 decoder
- B. 3:8 decoder
- C. 8:3 encoder
- D. 4:16 decoder
**Explanation:** A 3-variable function has up to 8 minterms ($m_0$ to $m_7$). A 3:8 decoder generates all 8 minterms, which can then be ORed together to realize any arbitrary 3-input function.

**Q39. In a 4-variable K-map, the total set of 1s is exactly {0, 1, 4, 5, 6, 7}. Group G1 covers squares {0, 1, 4, 5} and group G2 covers squares {4, 5, 6, 7}; both are valid maximal (prime) groupings. Which group(s) must be classified as essential prime implicants?**
- A. Only G1
- B. Only G2
- C. Both G1 and G2, since squares 0/1 are covered only by G1 and squares 6/7 are covered only by G2
- D. Neither, because they overlap on squares 4 and 5
**Explanation:** Squares 0 and 1 are covered solely by G1, making G1 essential. Squares 6 and 7 are covered solely by G2, making G2 essential. Therefore, both G1 and G2 are essential prime implicants.

**Q40. Why can a loop of two cross-coupled inverters store one bit of information?**
- A. Because it has two outputs
- B. Because it consumes low power
- C. Because it can settle into one of two stable states, matching the two values a bit can take
- D. Because it uses NAND gates only
**Explanation:** Cross-coupled inverters form a bistable element with positive feedback. It possesses two stable equilibrium operating points (Output $Q=1, Q'=0$ or $Q=0, Q'=1$), allowing it to store 1 bit of memory.

**Q41. In a four-variable K-Map, a valid group of 8 adjacent 1s reduces to a product term containing:**
- A. 1 literal
- B. 2 literals
- C. 3 literals
- D. 4 literals
**Explanation:** A group of size $2^k$ in an $n$-variable map eliminates $k$ variables. In a 4-variable map with an octet ($2^3 = 8$), $k = 3$ variables are eliminated, leaving $4 - 3 = 1$ literal.

**Q42. A prime implicant is:**
- A. Any implicant containing exactly one square
- B. The largest possible grouping of adjacent 1's that cannot be enlarged further while following K-map rules
- C. An implicant derived only using Boolean algebra, never a K-map
- D. An implicant that covers every square in the map
**Explanation:** A Prime Implicant is an implicant (group of $1, 2, 4, 8, \dots$ adjacent 1s) that cannot be combined with another adjacent group to form a larger group (i.e. cannot eliminate any more literals).

**Q43. A 3-input Boolean function is TRUE for minterms m(1, 3, 6). To implement this using an N:2^N decoder and an OR gate, what is the correct hardware structure?**
- A. A 3:8 decoder whose outputs 1, 3, and 6 are connected to a 3-input OR gate
- B. A 3:8 decoder whose outputs 0, 2, 4, 5, 7 are connected to a 5-input OR gate
- C. An 8:3 encoder with all outputs ANDed together
- D. A single 2:1 multiplexer with select line tied to the function output
**Explanation:** A 3:8 decoder generates all minterms $Y_0$ to $Y_7$. By connecting the active-high output pins 1, 3, and 6 to a 3-input OR gate, the circuit computes $F = Y_1 + Y_3 + Y_6 = m_1 + m_3 + m_6$.

**Q44. An SR latch is most commonly constructed from:**
- A. Two cross-coupled NOR gates
- B. Two cascaded AND gates
- C. Three inverters in a loop
- D. A single XOR gate
**Explanation:** The classical active-high SR latch is constructed from two cross-coupled NOR gates where the output of each gate feeds back into an input of the opposite gate.

**Q45. A 'maxterm' is defined as:**
- A. A product of literals corresponding to a 1 output
- B. A sum term that includes all input variables of the function
- C. A single input variable
- D. The final minimized SOP expression
**Explanation:** A maxterm (standard sum) is a sum term containing every input variable of the function exactly once in either true or complemented form, evaluating to 0 for exactly one input combination.

**Q46. Three inverters are connected in a feedback loop (ring oscillator), each with a propagation delay of 1 ns. What is the oscillation period of this circuit?**
- A. 2 ns
- B. 3 ns
- C. 6 ns
- D. 9 ns
**Explanation:** A signal transition takes $N \times t_{\text{pd}}$ to traverse the loop once, inverting the state. A full cycle requires two traversals (low-to-high and high-to-low). $T = 2 \times N \times t_{\text{pd}} = 2 \times 3 \times 1\text{ ns} = 6\text{ ns}$.

**Q47. In a NOR-gate based SR latch, what happens when both S = 1 and R = 1?**
- A. The latch remembers its previous state
- B. The output Q is set to 1
- C. Both Q and Q' become 0 - an invalid state since they are no longer complementary
- D. The output resets to Q = 0
**Explanation:** In a NOR SR latch, an input of 1 forces the NOR output to 0. When both $S = 1$ and $R = 1$, both $Q$ and $Q'$ are forced to 0. This violates the definition of complementary outputs and causes an unpredictable race condition upon releasing.

**Q48. An N-bit register is best described as:**
- A. A bank of N D latches with independent clocks
- B. A bank of N flip-flops sharing a common CLK input
- C. A combinational circuit with N inputs
- D. N cross-coupled inverter pairs without a clock
**Explanation:** An $N$-bit synchronous register consists of an array of $N$ flip-flops sharing a common clock signal (and common control signals like enable/reset), storing an $N$-bit word simultaneously.

**Q49. Using a 2:1 multiplexer to implement a 2-input AND function (Y = A.B), with A connected to the select line S, what should the data inputs I0 and I1 be set to?**
- A. $I_0 = 1, I_1 = 0$
- B. $I_0 = 0, I_1 = B$
- C. $I_0 = B, I_1 = 0$
- D. $I_0 = A, I_1 = B$
**Explanation:** The 2:1 MUX equation is $Y = S' I_0 + S I_1$. With $S = A$, $Y = A' I_0 + A I_1$. For AND logic ($Y = A B$), when $A = 0$, $Y = 0 \implies I_0 = 0$. When $A = 1$, $Y = B \implies I_1 = B$.

**Q50. What is the definition of the register setup time (t_setup)?**
- A. The time taken for output Q to become stable after the clock edge
- B. The minimum time the data input D must remain valid and stable before the active clock edge
- C. The minimum time the clock must remain HIGH
- D. The delay introduced by combinational gates in the feedback loop
**Explanation:** Setup time ($t_{\text{setup}}$) is the required window of time immediately before the active clock edge during which the data input $D$ must remain stable to ensure reliable capture by the flip-flop.

**Q51. What is the definition of the register hold time (t_hold)?**
- A. The time the register can retain data without power
- B. The minimum time the data input D must remain valid and stable after the active clock edge
- C. The time between consecutive clock pulses
- D. The duration of the reset pulse
**Explanation:** Hold time ($t_{\text{hold}}$) is the minimum time following the active clock edge during which the data input $D$ must not change, preventing contamination of the internal master-slave transition.

**Q52. In a synchronous digital system with propagation delay t_pd through combinational logic, what is the fundamental setup timing constraint on the clock period Tc?**
- A. $T_c \ge t_{\text{pcq}} + t_{\text{pd}} + t_{\text{setup}}$
- B. $T_c \le t_{\text{pcq}} - t_{\text{setup}}$
- C. $T_c = t_{\text{pcq}} + t_{\text{hold}}$
- D. $T_c \ge t_{\text{ccq}} + t_{\text{cd}}$
**Explanation:** A signal launched from a flip-flop at a clock edge takes clock-to-Q delay ($t_{\text{pcq}}$), propagates through combinational logic ($t_{\text{pd}}$), and must arrive at the destination flip-flop at least $t_{\text{setup}}$ before the next clock edge. Hence $T_c \ge t_{\text{pcq}} + t_{\text{pd}} + t_{\text{setup}}$.

**Q53. Given t_pcq = 1.0 ns, t_pd,comb = 3.5 ns, and t_setup = 0.5 ns, what is the maximum clock frequency (f_max) at which this circuit can operate reliably?**
- A. 100 MHz
- B. 200 MHz
- C. 250 MHz
- D. 500 MHz
**Explanation:** Minimum clock period $T_{c,\text{min}} = t_{\text{pcq}} + t_{\text{pd}} + t_{\text{setup}} = 1.0 + 3.5 + 0.5 = 5.0\text{ ns}$. Maximum clock frequency $f_{\text{max}} = 1 / T_{c,\text{min}} = 1 / (5.0 \times 10^{-9}\text{ s}) = 200\text{ MHz}$.

**Q54. To prevent hold time violations in a synchronous sequential circuit, which timing relationship must hold?**
- A. $t_{\text{ccq}} + t_{\text{cd}} \ge t_{\text{hold}}$
- B. $t_{\text{pcq}} + t_{\text{pd}} \le t_{\text{hold}}$
- C. $T_c \ge t_{\text{hold}}$
- D. $t_{\text{setup}} + t_{\text{hold}} \ge T_c$
**Explanation:** Hold time failure occurs if newly launched data races through the logic too fast and corrupts the destination flip-flop before its hold time has elapsed. The fastest possible propagation is contamination delay: $t_{\text{ccq}} + t_{\text{cd}} \ge t_{\text{hold}}$.

**Q55. What happens if the input D to a flip-flop changes within the setup-and-hold aperture around the active clock edge?**
- A. The flip-flop permanently burns out
- B. The output Q may enter an unstable metastable state, hovering between 0 and 1 for an indeterminate period
- C. The clock frequency instantly drops to zero
- D. The flip-flop automatically converts into a latch
**Explanation:** Violating setup or hold time creates metastability: the internal cross-coupled bistable nodes balance near the threshold voltage, taking an unpredictable amount of time to resolve to a valid logic 0 or 1, leading to system failure.

**Q56. How can a Toggle (T) flip-flop be constructed using a standard D flip-flop and combinational logic?**
- A. By connecting $D = T \cdot Q$
- B. By connecting $D = T \oplus Q$
- C. By connecting $D = T + Q$
- D. By connecting $D = T'$
**Explanation:** A T flip-flop has characteristic equation $Q_{\text{next}} = T \oplus Q$. Since a D flip-flop satisfies $Q_{\text{next}} = D$, driving input $D = T \oplus Q$ (using a 2-input XOR gate) makes the D flip-flop function as a T flip-flop.

**Q57. In a synchronous register with a Load Enable (EN) input, how is the 'Hold' (disable load) state safely implemented without clock gating?**
- A. By disconnecting power to the flip-flop
- B. By placing a 2:1 multiplexer at each D input to feed back the current output Q when EN = 0 ($D_{\text{in}} = EN \cdot D + EN' \cdot Q$)
- C. By grounding the clock line
- D. By inverting the clock
**Explanation:** Gating the clock line introduces clock skew and glitches. A robust synchronous register feeds a continuous clock to all flip-flops and uses a 2:1 MUX on data inputs: when $EN = 1$, $D_{\text{in}} = D$ (load); when $EN = 0$, $D_{\text{in}} = Q$ (re-circulate/hold).

**Q58. What is the difference between a synchronous reset and an asynchronous reset on a flip-flop?**
- A. Synchronous reset affects Q immediately; asynchronous reset waits for the clock edge
- B. Synchronous reset takes effect only on the active clock edge; asynchronous reset clears Q immediately regardless of the clock
- C. Asynchronous reset requires an external crystal oscillator
- D. Synchronous reset only works when D = 1
**Explanation:** A synchronous reset is sampled at the active clock edge along with data. An asynchronous reset connects directly to internal gate overrides (clear inputs), resetting the flip-flop immediately upon assertion without waiting for a clock edge.

**Q59. What is the formula for the oscillation frequency f of an N-stage ring oscillator where each inverter has propagation delay t_pd?**
- A. $f = 1 / (N \cdot t_{\text{pd}})$
- B. $f = 1 / (2 \cdot N \cdot t_{\text{pd}})$
- C. $f = 2 \cdot N \cdot t_{\text{pd}}$
- D. $f = N / (2 \cdot t_{\text{pd}})$
**Explanation:** A signal transition takes $N \cdot t_{\text{pd}}$ to invert around the loop. A complete period $T$ requires two transitions (low-to-high and high-to-low), so $T = 2 N t_{\text{pd}}$. The frequency is $f = 1 / T = 1 / (2 N t_{\text{pd}})$.

**Q60. A 5-stage ring oscillator is constructed using CMOS inverters with t_pd = 200 ps. What is the frequency of oscillation?**
- A. 250 MHz
- B. 500 MHz
- C. 1 GHz
- D. 2 GHz
**Explanation:** Period $T = 2 \times N \times t_{\text{pd}} = 2 \times 5 \times 200\text{ ps} = 2000\text{ ps} = 2.0\text{ ns}$. Frequency $f = 1 / T = 1 / (2.0 \times 10^{-9}\text{ s}) = 500\text{ MHz}$.


---

# PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS

<a id="topic-1"></a>
## Topic Module 1: 01_digital-circuits-introduction.md
**Source File**: `docs/01_digital-circuits-introduction.md`

# 01. Digital Circuits — Introduction & Combinational vs Sequential Logic

> **Source:** Harris & Harris Ch. 1–2, Unit 1 Slides 2–12

---

## What is a Digital Circuit?

A **digital circuit** is a network that processes **discrete-valued variables** (binary 0/1). Unlike analog circuits that handle continuous signals, digital circuits operate on two well-defined voltage levels.

### Black-Box View

Every digital circuit can be viewed as a black box with:

| Component | Description |
|-----------|-------------|
| **Input Terminals** | Receive external signals (A, B, C, ...) |
| **Output Terminals** | Drive external loads (Y, Z, ...) |
| **Functional Specification** | Logical I/O relationship — Truth Table / Boolean Equation (e.g., `Y = A·B`) |
| **Timing Specification** | Propagation delay (`t_pd`) — time between input change and output response |

> **Key Insight:** Two circuits can have **identical functional specs** but **different timing specs**. Both compute `Y = A·B`, but one may be faster (lower `t_pd`) due to better layout, transistor sizing, or logic family.

---

## Nodes in a Circuit

| Type | Description | Example |
|------|-------------|---------|
| **Input** | Receives from outside | A, B, C |
| **Output** | Sends to outside | Y, Z |
| **Internal** | Connects elements inside | n₁ (output of first gate, input to second) |

---

## Combinational vs Sequential Logic

| Property | Combinational Logic | Sequential Logic |
|----------|---------------------|------------------|
| **Memory** | None (Memoryless) | Yes — stores state |
| **Output depends on** | Current inputs **only** | Current + **previous** inputs (state) |
| **Feedback** | Forbidden | Required (via registers) |
| **Examples** | Adder, MUX, Decoder, Encoder, Comparator | Register, Counter, Flip-flop, FSM, Memory |

### Combinational Circuit Definition

A circuit is **combinational** **iff** all three rules hold:

1. **Element Rule:** Every circuit element is itself combinational
2. **Node Rule:** Every node is either an input or connects to **exactly one** output terminal (no shorted outputs)
3. **Acyclic Rule:** **No cyclic paths** (feedback loops) — every path visits each node at most once

> **MCQ Trap:** A circuit with a cyclic path and **no register** is **NOT combinational** (it's either sequential or unstable/astable).

---

## Propagation Delay

### Key Formulas

```
Elements in PARALLEL:  delay = max(delay₁, delay₂, ...)
Elements in SERIES:    delay = delay₁ + delay₂ + ...
```

### Worked Example

```
E1 = 5 ns (parallel)     E2 = 8 ns (parallel)
              ↓
         E3 = 4 ns (series after both)
         
Total delay = max(5, 8) + 4 = 8 + 4 = 12 ns
```

### Timing Diagram
```
A ────────┐
          ├── E1 (5ns) ──┐
B ────────┤              ├── max(5,8)=8ns ──┐
          ├── E2 (8ns) ──┘                  ├── E3 (4ns) ── Y
C ────────┘                                     (12ns total)
```

---

## Voltage Thresholds & Noise Margins (Ch. 1)

For a 1.8V system:

| Parameter | Value | Description |
|-----------|-------|-------------|
| **V_OH** | ≥ 1.35V | Output HIGH min voltage |
| **V_OL** | ≤ 0.45V | Output LOW max voltage |
| **V_IH** | ≥ 1.26V | Input recognized as HIGH |
| **V_IL** | ≤ 0.54V | Input recognized as LOW |
| **NM_H** | V_OH − V_IH = 0.09V | HIGH noise margin |
| **NM_L** | V_IL − V_OL = 0.09V | LOW noise margin |

**Forbidden Zone:** 0.54V < V < 1.26V → undefined behavior

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| What are the two specifications of a digital circuit? | Functional + Timing |
| Combinational vs Sequential difference? | Memoryless vs Has memory/state |
| When is a circuit NOT combinational? | Cyclic path exists without register |
| Worst-case delay for parallel then series? | `max(parallel) + series` |
| What are the three combinational rules? | 1) All elements combinational 2) Each node driven by one output 3) No cyclic paths |

---

## Exam-Relevant MCQ Patterns

1. **Black-box specifications** — always both functional AND timing (Q8)
2. **Combinational classification** — cyclic path = NOT combinational (Q13)
3. **Delay calculation** — parallel = max, series = sum (Q12)
4. **Circuit type identification** — Adders/Mux/Decoder = combinational; Counter/Reg/FF = sequential (Q15)

---

## Key Formulas (Memorize)

```
Parallel delay = max(d₁, d₂, ...)
Series delay   = d₁ + d₂ + ...
Combinational  = no feedback loops
Sequential     = has memory/state
```

---

<a id="topic-2"></a>
## Topic Module 2: 02_boolean-equations.md
**Source File**: `docs/02_boolean-equations.md`

# 02. Boolean Equations — Minterms, Maxterms, SOP & POS Forms

> **Source:** Harris & Harris Ch. 2, Unit 1 Slides 13–42

---

## Key Terminology

| Term | Definition | Example (3 vars) |
|------|------------|------------------|
| **Literal** | A variable or its complement | `A`, `Ā`, `B`, `B̄` |
| **Implicant** | Product of one or more literals | `AB`, `ĀC`, `BC̄` |
| **Minterm (mᵢ)** | Product containing **ALL** input variables (exactly once each) | `ĀB̄C̄`, `ABC` (8 total for 3 vars) |
| **Maxterm (Mᵢ)** | Sum containing **ALL** input variables (exactly once each) | `A+B+C`, `Ā+B̄+C̄` |

> **Notation:**
> - **Minterm:** `mᵢ` where `i` = decimal value of binary input combination
> - **Maxterm:** `Mᵢ` where `i` = decimal value of binary input combination

---

## Truth Table → Minterms/Maxterms (3 Variables)

| A | B | C | Y | Minterm (mᵢ) | Maxterm (Mᵢ) |
|---|---|---|---|--------------|--------------|
| 0 | 0 | 0 | 0 | m₀ = ĀB̄C̄ | M₀ = A+B+C |
| 0 | 0 | 1 | 1 | m₁ = ĀB̄C | M₁ = A+B+C̄ |
| 0 | 1 | 0 | 0 | m₂ = ĀBC̄ | M₂ = A+B̄+C |
| 0 | 1 | 1 | 1 | m₃ = ĀBC | M₃ = A+B̄+C̄ |
| 1 | 0 | 0 | 1 | m₄ = AB̄C̄ | M₄ = Ā+B+C |
| 1 | 0 | 1 | 1 | m₅ = AB̄C | M₅ = Ā+B+C̄ |
| 1 | 1 | 0 | 0 | m₆ = ABC̄ | M₆ = Ā+B̄+C |
| 1 | 1 | 1 | 1 | m₇ = ABC | M₇ = Ā+B̄+C̄ |

**Key Observations:**
- **Minterm = 1** for exactly one input combination
- **Maxterm = 0** for exactly one input combination
- Minterm index = binary value of inputs (e.g., 011₂ = 3 → m₃)
- Maxterm index = binary value of inputs (e.g., 011₂ = 3 → M₃)

---

## Sum-of-Products (SOP) Form

### Canonical SOP
OR of all minterms where output = 1
```
F = Σ m(list of indices where Y=1)
```

**Example:** `Y = A'B + AB = Σ(1, 3)`

### Standard SOP (Minimized)
Not necessarily canonical — terms may not include all variables
```
F = A'B + AB = B(A' + A) = B
```

### Constructing SOP from Truth Table
1. Identify rows where output = 1
2. Write minterm for each (include all variables)
3. OR them together

---

## Product-of-Sums (POS) Form

### Canonical POS
AND of all maxterms where output = 0
```
F = Π M(list of indices where Y=0)
```

**Example:** `Y = (A+B)(A'+B) = Π(0, 2)`

### Standard POS (Minimized)
```
F = (A+B)(A'+B) = B
```

### Constructing POS from Truth Table
1. Identify rows where output = 0
2. Write maxterm for each (include all variables)
3. AND them together

---

## SOP ↔ POS Conversion

### Duality Principle
```
F = Σ m(indices)  ⇔  F = Π M(complement of indices)
```

**Example (3 variables):**
```
If F = Σ m(1, 3, 5)  →  F = Π M(0, 2, 4, 6, 7)
```

**Proof:** By De Morgan's Theorem
```
F = m₁ + m₃ + m₅
F' = m₀·m₂·m₄·m₆·m₇ = M₀·M₂·M₄·M₆·M₇
F = (F')' = M₀ + M₂ + M₄ + M₆ + M₇  ← Not quite right...
```

Actually: Complement of minterm is maxterm with same index
- `mᵢ' = Mᵢ` (by De Morgan)
- `F = Σ m(i) = (Π M(i)')' = Π M(i)` for i NOT in list

---

## Ben Bitdiddle Picnic Example (From Textbook)

> **Problem:** Ben enjoys picnic if **NOT** raining AND **NO** ants
> - A = ants (1 = yes), R = rain (1 = yes), E = enjoy
> - Only enjoys when A=0, R=0 → row 00 gives 1

**Truth Table:**
| A | R | E |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

**SOP:** `E = ĀR̄ = Σ m(0)` — only row 00 gives 1
**POS:** Rows 1,2,3 are 0 → `E = (A+R)(A'+R)(A'+R') = Π M(1,2,3)`

---

## Minterm/Maxterm Count

| Variables (n) | Minterms (2ⁿ) | Maxterms (2ⁿ) |
|---------------|---------------|---------------|
| 2 | 4 | 4 |
| 3 | 8 | 8 |
| 4 | 16 | 16 |
| n | 2ⁿ | 2ⁿ |

> **MCQ Pattern:** "How many minterms for 3 variables?" → **8** (Q14)

---

## Finding Shared Characteristics (MCQ Pattern)

**Question:** Minterms `m(3, 7, 11, 15)` for 4 variables (A,B,C,D) — what do they share?

| Index | Binary | A | B | C | D |
|-------|--------|---|---|---|---|
| 3 | 0011 | 0 | 0 | 1 | 1 |
| 7 | 0111 | 0 | 1 | 1 | 1 |
| 11 | 1011 | 1 | 0 | 1 | 1 |
| 15 | 1111 | 1 | 1 | 1 | 1 |

**Answer:** C=1, D=1 for all → `F = C·D` (Q35)

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| Minterm for 3 variables? | Product with all 3 variables (e.g., `ĀB̄C`) |
| Maxterm for 3 variables? | Sum with all 3 variables (e.g., `A+B+C̄`) |
| SOP uses which rows? | Output = 1 rows (minterms) |
| POS uses which rows? | Output = 0 rows (maxterms) |
| `M₆` for 3 vars (A,B,C)? | `Ā + B̄ + C` (binary 110) |
| `Σ m(1,3,5)` = Π M(?) | `Π M(0,2,4,6,7)` |

---

## Exam-Relevant MCQ Patterns

1. **Minterm definition** — product with ALL inputs (Q1, Q9, Q34)
2. **POS construction** — product of maxterms for 0 outputs (Q2, Q24)
3. **Minterm count** — `2ⁿ` for n variables (Q14)
4. **Shared characteristic** — find common bits in minterm list (Q35: `m(3,7,11,15)` all have `C=1, D=1`)

---

## Key Formulas (Memorize)

```
Minterms for n vars = 2ⁿ
Minterm index = binary value of inputs
Maxterm index = binary value of inputs
SOP: F = Σ(minterms where Y=1)
POS: F = Π(maxterms where Y=0)
```

---

<a id="topic-3"></a>
## Topic Module 3: 03_logic-minimization-kmaps-3var.md
**Source File**: `docs/03_logic-minimization-kmaps-3var.md`

# 03. Logic Minimization — Boolean Algebra & K-Maps (3-Variable)

> **Source:** Harris & Harris Ch. 2, Unit 1 Slides 33–93

---

## Boolean Algebra Minimization

### Laws Used (Memorize!)

| Law | Formula | Application |
|-----|---------|-------------|
| **Distributive** | `A(B+C) = AB + AC` | Factoring common terms |
| **Complement** | `A + Ā = 1` | Eliminate variable |
| **Identity** | `A·1 = A` | Cleanup after factoring |
| **Idempotent** | `A + A = A` | Remove duplicates |
| **Absorption** | `A + AB = A` | Remove redundant terms |
| **Consensus** | `AB + ĀC + BC = AB + ĀC` | Remove consensus term |
| **De Morgan** | `Ā + B̄ = Ā·B̄` | SOP ↔ POS, NAND/NOR |

### Step-by-Step Worked Example

**Minimize:** `Y = ĀBC + AB̄C̄ + ABC̄ + ABC`

```
Y = ĀBC + AB̄C̄ + ABC̄ + ABC
  = BC(Ā + A) + AC̄(B̄ + B)    [Distributive: factor BC from 1&4, AC̄ from 2&3]
  = BC(1) + AC̄(1)              [Complement: Ā+A=1, B̄+B=1]
  = BC + AC̄                    [Identity: X·1=X]
```

**Result:** 2 terms, 4 literals (vs original 4 terms, 12 literals)

---

## Why K-Maps? Limitations of Algebraic Minimization

| Aspect | Algebraic | K-Map |
|--------|-----------|-------|
| **Guarantee** | Heuristic — no optimal guarantee | **Algorithmic — guarantees minimum for ≤4 vars** |
| **Process** | Requires insight, trial-and-error | Systematic visual grouping |
| **Don't-cares** | Hard to handle | Natural fit — use as 0 or 1 |

> **Key Point:** K-maps provide **provably minimal** SOP/POS for ≤4 variables. For >4 vars, use Quine-McCluskey or CAD tools.

---

## Karnaugh Maps (3-Variable)

### Structure

```
        BC
       00  01  11  10
A  0   m0  m1  m3  m2
A  1   m4  m5  m7  m6
```

### Critical Properties

1. **Gray Code Order:** 00, 01, 11, 10 — **adjacent cells differ by exactly 1 bit**
2. **Wrap-Around:** Left ↔ Right edges are adjacent (m₀ adjacent to m₂, m₄ to m₆)

> **Why Gray Code?** Ensures adjacent squares differ by exactly 1 literal → valid grouping by Boolean algebra

---

## Key Definitions

| Term | Definition |
|------|------------|
| **Implicant** | Rectangle of 1s (size 1, 2, 4, 8...) — may include X's |
| **Prime Implicant (PI)** | **Largest** possible grouping (cannot be enlarged further) |
| **Essential PI (EPI)** | PI covering at least one 1 **not covered by any other PI** — **MUST include** |

---

## Minimization Algorithm (Guaranteed Optimal for ≤4 vars)

1. **Plot 1s** from truth table (and X's for don't-cares)
2. **Find ALL Prime Implicants** — identify largest valid rectangles (size 2ᵏ)
3. **Identify Essential PIs** — cover at least one 1 uniquely
4. **Select minimum non-EPIs** to cover remaining uncovered 1s
5. **Read equation** — variables **constant** across group (eliminate changing ones)

---

## Worked Examples

### Example 1: `F = Σ(3, 4, 6, 7)`

```
        BC
       00  01  11  10
A  0    0   0   1   0   (m₃=1)
A  1    0   1   1   1   (m₄,m₆,m₇=1)
```

**Step 1: Find all PIs**
- Group {m₃,m₇} vertical → **BC** (A changes, eliminated)
- Group {m₄,m₆} horizontal → **AC̄** (B changes, eliminated)

**Step 2: Essential PIs**
- m₃ only in {m₃,m₇} → **BC essential**
- m₄ only in {m₄,m₆} → **AC̄ essential**
- m₆ covered by both, m₇ covered by BC

**Result:** `F = BC + AC̄`

---

### Example 2: `F = Σ(0, 2, 3, 4, 6, 7)`

```
        BC
       00  01  11  10
A  0    1   0   1   1
A  1    1   0   1   1
```

**PIs:**
- {0,2,4,6} (cols 00,10) → **A** (B,C change)
- {3,7} → **C** (A,B change)
- {2,3,6,7} → **B̄C + BC̄** (not maximal)

**EPIs:**
- {0,2,4,6} covers m₀,m₄ uniquely → **A essential**
- {3,7} covers m₃ uniquely → **C essential**
- All 1s covered!

**Result:** `F = A + C` (minimal) or `F = A + B̄C + BC̄` (also minimal)

> **Non-Uniqueness:** Multiple equally minimal solutions possible (Q32, Q92)

---

### Example 3: Don't-Care Conditions

**Problem:** `F = Σ(0,1,4,5,6) + d(7)` — input 111 never occurs

```
        BC
       00  01  11  10
A  0    1   1   X   0
A  1    1   1   1   0
```

**Using X at m₇ to enlarge groups:**
- {0,1,4,5} → **B̄** (A,C change)
- {4,5,6,7} → **A** (B,C change, using X at m₇)

**Result:** `F = A + B̄`

> **Don't-Care Rule:** Treat X as 0 or 1 — **whichever gives larger groups**. Not mandatory to use all X's.

---

## POS Minimization Using K-Maps

### Procedure (Group the 0s)
1. Plot 0s from truth table
2. Group 0s into rectangles (size 2ᵏ)
3. Each group → Sum Term (variables **constant** = complemented)
4. AND the sum terms

### Example: Same `F = Σ(3,4,6,7)` → 0s at m₀,m₁,m₂,m₅

```
        BC
       00  01  11  10
A  0    0   0   1   0
A  1    0   1   1   1

0-groups: {m₀,m₁} → A+B    {m₁,m₅} → B̄+C    {m₀,m₂} → A+C̄
```

Wait, let's do this properly:

For 0s at m₀(000), m₁(001), m₂(010), m₅(101):
- {m₀,m₁} vertical → A=0,B=0 constant → **A+B**
- {m₁,m₅} diagonal? No, not adjacent
- {m₀,m₂} horizontal → A=0,C=0 constant → **A+C̄**

Actually: Let's check the groups:
- {m₀,m₁}: A=0,B=0 → A+B
- {m₂}: isolated → A+B̄+C̄
- {m₅}: isolated → Ā+B+C̄

POS = (A+B)(A+B̄+C̄)(Ā+B+C̄) — not minimal, confirms SOP is better here.

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| K-map order? | Gray code: 00, 01, 11, 10 |
| Wrap-around? | Left↔right (and top↔bottom for 4-var) adjacent |
| Prime Implicant? | Largest valid grouping of 1s |
| Essential PI? | Covers a 1 no other PI covers |
| Don't-care (X)? | Treat as 0 or 1 to maximize groups |
| POS vs SOP? | Group 0s for POS, group 1s for SOP |

---

## Exam-Relevant MCQ Patterns

1. **Gray code reason** — adjacent squares differ by 1 literal (Q26)
2. **Wrap-around** — both horizontal and vertical edges (Q31, Q119)
3. **EPI identification** — unique coverage makes it mandatory (Q10, Q39)
4. **Non-unique minimum** — different non-EPI choices = equally valid (Q32)
5. **Don't-care usage** — assign to simplify, not mandatory (Q11, Q27)
6. **Group size → literals** — 8 cells→1 lit, 4→2, 2→3, 1→4 (Q41)

---

## Key Formulas (Memorize)

```
Group of 2ᵏ cells in n-var K-map → eliminates k variables → (n-k) literals

3-var:  1 cell=3 lits,  2=2,  4=1,  8=0 (constant 1)
4-var:  1 cell=4 lits,  2=3,  4=2,  8=1,  16=0
```

---

<a id="topic-4"></a>
## Topic Module 4: 04_kmaps-4var-seven-segment.md
**Source File**: `docs/04_kmaps-4var-seven-segment.md`

# 04. K-Maps (4-Variable) & Seven-Segment Decoder

> **Source:** Harris & Harris Ch. 2, Unit 1 Slides 94–123

---

## 4-Variable K-Map Structure

```
        CD
       00  01  11  10
AB 00  m0  m1  m3  m2
AB 01  m4  m5  m7  m6
AB 11  m12 m13 m15 m14
AB 10  m8  m9  m11 m10
```

### Critical Properties

1. **Rows & Columns:** Gray code (00, 01, 11, 10) — adjacent differ by 1 bit
2. **Wrap-Around:** **Left↔Right AND Top↔Bottom** — torus topology
   - m₀ adjacent to m₂, m₈, m₄
   - m₁₅ adjacent to m₁₃, m₇, m₁₄

> **MCQ Trap:** 4-var K-map wraps in **both** dimensions (Q119)

---

## Worked Examples

### Example 1: `F = Σ(5, 7, 13, 15)`

```
        CD
       00  01  11  10
00    0   0   0   0
01    0   1   1   0
11    0   1   1   0
10    0   0   0   0
```

**Groups:**
- {5,7,13,15} — columns 01&11, rows 01&11 → **BD** (A,C change)
- {5,7} vertical? No, need 4-cell groups for max simplification
- Actually: {5,7,13,15} = columns where C=1,D=1? Let's check:
  - 5=0101, 7=0111, 13=1101, 15=1111 → C=1, D=1, A/B vary → **CD**

Wait, let me recalculate:
- m₅ = 0101 (A=0,B=1,C=0,D=1)
- m₇ = 0111 (A=0,B=1,C=1,D=1)
- m₁₃ = 1101 (A=1,B=1,C=0,D=1)
- m₁₅ = 1111 (A=1,B=1,C=1,D=1)

Common: B=1, D=1 → **BD** ✓

**From slides:** Required PIs = `bd, b'd'` — two groups of 4
- Group 1: {m₁,m₃,m₉,m₁₁} → B=0,D=0 → **B̄D̄**
- Group 2: {m₅,m₇,m₁₃,m₁₅} → B=1,D=1 → **BD**

---

### Seven-Segment Display Decoder (4-bit input D₃:₀)

Each segment Sₐ–S₉ is a function of 4 inputs.

#### Without Don't-Cares (0–9 only, 10–15 = 0)
```
Sa = D3'D1 + D3'D2D0 + D2'D1'D0' + D3D2'D1'
Sb = D3'D2' + D2'D1' + D3'D1D0 + D3'D1'D0'
Sc = D3'D0 + D3'D2 + D2'D1'
Sd = D3'D2'D1 + D3'D2D1'D0 + D2'D1'D0' + D3'D1D0
Se = D3'D1D0' + D2'D1'D0'
Sf = D3'D2D0' + D3'D2D1' + D3D2'D1' + D3'D1'D0'
Sg = D3'D1D0' + D3'D2'D1 + D3'D2D1' + D3D2'D1'
```

#### With Don't-Cares (10–15 = X)
**Significantly simpler!**
```
Sa = D3 + D2D0 + D2'D0' + D1
Sb = D2' + D1'D0' + D1D0
Sc = D0 + D2 + D1'
Sd = D1D0' + D2'D1 + D0'D2' + D2D1'D0
Se = D1D0' + D2'D0'
Sf = D3 + D2D0' + D2D1' + D1'D0'
Sg = D3 + D1D0' + D2'D1 + D2D1'
```

> **Key Insight:** Don't-cares allow **larger groups** → fewer terms, fewer literals.

---

## Think About It Exercises (From Slides)

| # | Function | Minimized Result |
|---|----------|------------------|
| 1 | `f(a,b,c) = Σ(0, 3, 5)` | `a'b'c' + a'bc + ab'c` |
| 2 | `f(a,b,c) = Σ(0, 1, 2, 4, 5, 6)` | `a' + b'c'` or similar |
| 3 | `f(a,b,c) = Σ(0, 2, 3, 4, 6, 7)` | `a + c` |
| 4 | `f(a,b) = Σ(0, 1, 2, 3)` | `1` (all 1s) |
| 5 | `f(a,b,c,d) = Σ(0, 1, 5, 7, 15, 14, 10)` | Use K-map with X |

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| 4-var K-map wrap-around? | Both horizontal AND vertical |
| 7-seg without don't-cares? | 10–15 produce blank (0) |
| 7-seg with don't-cares? | 10–15 = X, simpler equations |
| Group of 8 in 4-var? | Eliminates 3 vars → 1 literal |

---

## Exam-Relevant MCQ Patterns

1. **4-var wrap-around** — both row and column edges (Q119)
2. **Don't-care meaning** — unspecified, use for larger groups (Q120)
3. **Don't-care benefit** — impossible inputs can be 0 or 1 (Q121)
4. **7-segment decoder** — classic 4-var K-map application

---

## Key Formulas (Memorize)

```
4-var K-map: 16 cells (m0-m15)
Group sizes: 1, 2, 4, 8, 16
Literals remaining = 4 - log₂(group_size)
Don't-care (X): can be 0 or 1
```

---

<a id="topic-5"></a>
## Topic Module 5: 05_combinational-building-blocks.md
**Source File**: `docs/05_combinational-building-blocks.md`

# 05. Combinational Building Blocks — Mux, Decoder, Encoder

> **Source:** Harris & Harris Ch. 2, Unit 1 Slides 124–160

---

## Multiplexer (MUX)

### 2:1 MUX
- **Select (S):** 1 bit → chooses D₀ (S=0) or D₁ (S=1)
- **Equation:** `Y = S̄·D₀ + S·D₁`

**Two Implementations:**
1. **Logic Gates** (AND-OR): 2 AND, 1 OR, 1 NOT
2. **Tristate Buffers** — only one enabled at a time (outputs Z = high-Z)

### 4:1 MUX
- **Select:** S₁, S₀ (2 bits)
- **Truth Table:**

| S₁ | S₀ | Y |
|----|----|---|
| 0  | 0  | D₀ |
| 0  | 1  | D₁ |
| 1  | 0  | D₂ |
| 1  | 1  | D₃ |

### MUX as Lookup Table (Implementing Logic)

**Full Size (2ᴺ:1):**
- Connect select lines to N inputs
- Connect data inputs to truth table outputs (0/1)

**Example: AND gate with 4:1 MUX (A,B as selects)**

| A | B | Y | D₀ | D₁ | D₂ | D₃ |
|---|---|---|----|----|----|----|
| 0 | 0 | 0 | 0  |    |    |    |
| 0 | 1 | 0 |    | 0  |    |    |
| 1 | 0 | 0 |    |    | 0  |    |
| 1 | 1 | 1 |    |    |    | 1  |

→ `D₀=0, D₁=0, D₂=0, D₃=1`

---

## Reduced MUX Size (Shannon Expansion)

Use one variable as **data input** instead of select:
- **N-input function** → **2ᴺ⁻¹:1 MUX**

**Example: 3-var AND with 2:1 MUX**
- A = select, B = data input
- `F(0,B) = 0` → I₀ = 0
- `F(1,B) = B` → I₁ = B
- Circuit: S=A, I₀=0, I₁=B

---

## MUX Cascading (Building Larger MUXes)

| Target | Using 2:1 MUXes | Formula |
|--------|------------------|---------|
| 4:1    | 3                | 2+1     |
| 8:1    | 7                | 4+2+1   |
| 16:1   | 15               | 8+4+2+1 |
| 2ᴺ:1   | 2ᴺ - 1           | Σ 2ⁱ    |

| Target | Using 4:1 MUXes | Formula |
|--------|------------------|---------|
| 8:1    | 3                | 2¹ + 2⁰ |
| 16:1   | 5                | 4¹ + 4⁰ |
| 64:1   | 21               | 4²+4¹+4⁰ |

---

## Decoder (N:2ᴺ)

### Operation
- **N inputs** → **2ᴺ outputs** (one-hot)
- Exactly **one output HIGH** per input combination
- Outputs = **minterms** of inputs

### 2:4 Decoder

| A₁ | A₀ | Y₀ | Y₁ | Y₂ | Y₃ |
|----|----|----|----|----|----|
| 0  | 0  | 1  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  | 0  | 0  |
| 1  | 0  | 0  | 0  | 1  | 0  |
| 1  | 1  | 0  | 0  | 0  | 1  |

### Logic Using Decoders
- Generate all minterms via decoder
- OR required minterms for function
- **N-input function** → **N:2ᴺ decoder + M-input OR gate**

---

## Encoder

### Types

| Encoder | Inputs | Outputs | Notes |
|---------|--------|---------|-------|
| 4:2     | 4      | 2       | One-hot input |
| 8:3 (Octal) | 8   | 3       | Binary code out |
| 10:4 (BCD) | 10  | 4       | Decimal→BCD |
| **Priority** | 2ᴺ | N       | Highest priority wins |

### Priority Encoder (4:2)

| Y₃ | Y₂ | Y₁ | Y₀ | A₁ | A₀ | V |
|----|----|----|----|----|----|---|
| 0  | 0  | 0  | 1  | 0  | 0  | 1 |
| 0  | 0  | 1  | X  | 0  | 1  | 1 |
| 0  | 1  | X  | X  | 1  | 0  | 1 |
| 1  | X  | X  | X  | 1  | 1  | 1 |
| 0  | 0  | 0  | 0  | X  | X  | 0 |

- **V (Valid)** = 1 if any input active, else 0
- **Y₃ highest priority**, Y₀ lowest

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| 4:1 MUX select lines? | 2 (log₂4) |
| 2:1 MUX equation? | `Y = S̄D₀ + SD₁` |
| Decoder outputs? | One-hot (exactly one HIGH) |
| 3:8 decoder for 3-var function? | Connect minterm outputs to OR |
| Priority encoder purpose? | Resolve multiple active inputs |

---

## Exam-Relevant MCQ Patterns

1. **MUX select lines** — log₂N (Q5, Q29)
2. **2:1 MUX equation** — `S̄D₀ + SD₁` (Q10)
3. **Decoder one-hot** — exactly one output HIGH (Q20, Q160)
4. **Decoder + OR for logic** — N:2ᴺ decoder generates all minterms (Q38)
5. **Tristate MUX** — 0, 1, Z states (Q23)
6. **MUX as lookup** — data inputs = truth table outputs
7. **Cascading formula** — 2ᴺ:1 needs 2ᴺ-1 two-to-one MUXes

---

## Key Formulas (Memorize)

```
MUX: N inputs → log₂N select lines
2:1 MUX: Y = S̄D₀ + SD₁
Decoder: N inputs → 2ᴺ outputs (one-hot)
N:2ᴺ Decoder + OR gate = any N-input function
Priority Encoder: V=0 only when all inputs=0
```

---

<a id="topic-6"></a>
## Topic Module 6: 06_sequential-basics-latches.md
**Source File**: `docs/06_sequential-basics-latches.md`

# 06. Sequential Logic Basics — Latches, SR Latch, D Latch

> **Source:** Harris & Harris Ch. 3, Unit 1 Slides 162–186

---

## Combinational vs Sequential

| Property | Combinational | Sequential |
|----------|---------------|------------|
| Memory | None | Yes (state) |
| Output depends on | Current inputs only | Current + past inputs |
| Example | Adder, MUX, Decoder | Register, Counter, FF |

---

## Memory Elements

### Bistable Element (Cross-Coupled Inverters)
- Two stable states: `Q=0, Q̄=1` or `Q=1, Q̄=0`
- **Problem:** No inputs to control state

---

### SR Latch (NOR-based)

```
     S ──┐      ┌── Q
         NOR──┘
     R ──┘      ┌── Q̄
         NOR──┘
```

| S | R | Action | Q | Q̄ |
|---|---|--------|---|---|
| 0 | 0 | Hold   | Q | Q̄ |
| 0 | 1 | Reset  | 0 | 1  |
| 1 | 0 | Set    | 1 | 0  |
| 1 | 1 | **Invalid** | 0 | 0 |

- **S=R=1 invalid:** Q=Q̄=0 (not complementary), race on release
- **Awkward:** "What to store" and "When to change" mixed

**NAND Implementation (`S̄ R̄` Latch):** Active Low. Forbidden: `S̄=R̄=0`.

---

### Gated D Latch (Solves SR Problems)

| D | CLK | Action | Q |
|---|-----|--------|---|
| X | 0   | Hold   | Q |
| 0 | 1   | Reset  | 0 |
| 1 | 1   | Set    | 1 |

- **D = WHAT to store**
- **CLK = WHEN to change**
- **Transparent** when CLK=1 (Q follows D)
- **Opaque** when CLK=0 (holds value)
- Guarantees S≠R internally

---

## D Latch vs D Flip-Flop

| Property | D Latch | D Flip-Flop |
|----------|---------|-------------|
| Triggering | Level-sensitive | Edge-triggered |
| Transparent | CLK=1 | Only at edge |
| Symbol | No triangle | Triangle at CLK |
| Symbol (pos-edge) | — | `CLK ▷` |

**Problem with latch:** While CLK=1, D changes → Q changes unpredictably
**Solution:** Flip-flop samples **only at clock edge**

---

## Clock Edges

| Edge | Transition | Name |
|------|------------|------|
| Rising | 0→1 | Positive edge |
| Falling | 1→0 | Negative edge |

---

## Traffic Light Example

| Element | Behavior | Problem |
|---------|----------|---------|
| **Latch** | Transparent during CLK=1 | Glitch during HIGH → wrong state |
| **Flip-Flop** | Updates only at edge | Glitches ignored until next edge |

> **Flip-flop preferred** for reliable sequential control

---

## Quick Self-Test

| Question | Answer |
|----------|--------|
| SR latch invalid state? | S=1, R=1 → Q=Q̄=0 |
| D latch transparent when? | CLK=1 |
| D latch holds when? | CLK=0 |
| Latch vs FF difference? | Level vs edge triggered |
| Why FF better for traffic light? | Ignores glitches between edges |

---

## Exam-Relevant MCQ Patterns

1. **SR latch invalid** — S=R=1 gives Q=Q̄=0 (Q47)
2. **D latch transparency** — CLK=1 means transparent (Q28)
3. **Latch vs FF** — level vs edge sensitive (Q4, Q7, Q183-186)
4. **Cross-coupled inverters** — two stable states = 1 bit storage (Q40)
5. **Ring oscillator** — 3 inverters loop, period = 2·N·tₚd (Q46, Q59, Q60)

---

## Key Formulas (Memorize)

```
Ring oscillator: T = 2 × N × tₚd,  f = 1/T
SR latch: S=1→Set, R=1→Reset, S=R=1→Invalid
D latch: CLK=1→Transparent (Q=D), CLK=0→Hold
```

---

<a id="topic-7"></a>
## Topic Module 7: 07_flipflops-timing-metastability.md
**Source File**: `docs/07_flipflops-timing-metastability.md`

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

---

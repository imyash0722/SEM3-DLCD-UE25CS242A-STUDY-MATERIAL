# DLCD Complete Exam Preparation Master Package (Unit 1 & Unit 2)
> **Comprehensive, Cleaned, and Deduplicated Resource Package**
> - **Source Material Included:** Lecture Slides (Unit 1 & 2), Question Banks with Full Solutions (`U1QB_soln.docx` & `U2QB_soln.docx`), Curated Problem Sets (`QB.doc` & `U2QB.docx`), and All MCQs with Explanations (`U1U2MCQs.html`, `U2MCQ1.docx`, `U2MCQ2.docx`, `U2MCQ3.pdf`).
> - **Cleaned:** All duplicate animation frames, PowerPoint watermark artifacts, and isolated diagram tokens have been eliminated.
> - **Deduplicated:** All 25+ redundant questions in the Question Bank and all duplicate MCQs across datasets have been merged.

---

# PART 1: UNIT 1 COMPREHENSIVE STUDY MATERIAL
(Combinational and Sequential Logic Design)

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

# PART 2: UNIT 2 COMPREHENSIVE STUDY MATERIAL
(Finite State Machines & Digital Building Blocks)

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


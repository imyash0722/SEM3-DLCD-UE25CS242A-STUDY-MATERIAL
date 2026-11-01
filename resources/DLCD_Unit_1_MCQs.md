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

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

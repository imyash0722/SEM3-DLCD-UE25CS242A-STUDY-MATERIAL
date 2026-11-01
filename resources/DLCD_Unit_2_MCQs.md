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

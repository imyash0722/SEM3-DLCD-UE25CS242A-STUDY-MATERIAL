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

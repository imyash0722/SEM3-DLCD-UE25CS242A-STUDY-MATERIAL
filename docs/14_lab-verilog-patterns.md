# 14. Lab Code Patterns — Verilog Examples

> **Source:** Lab Week 8 (Prefix Adder, Comparator) | Textbook: Harris & Harris Ch. 4–5

---

## Prefix Adder (4-bit)

```verilog
module prefix_adder(
    input  [3:0] a, b,
    input        cin,
    output [3:0] sum,
    output       cout
);
    wire [3:0] p, g, c;

    // Generate & Propagate
    assign p = a ^ b;        // Pᵢ = Aᵢ ⊕ Bᵢ
    assign g = a & b;        // Gᵢ = Aᵢ · Bᵢ

    // Prefix carry computation
    assign c[0] = cin;
    assign c[1] = g[0] | (p[0] & c[0]);
    assign c[2] = g[1] | (p[1] & g[0]) | (p[1] & p[0] & c[0]);
    assign c[3] = g[2] | (p[2] & g[1]) | (p[2] & p[1] & g[0]) | (p[2] & p[1] & p[0] & c[0]);
    assign cout = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) | (p[3] & p[2] & p[1] & g[0]) | (p[3] & p[2] & p[1] & p[0] & c[0]);

    // Sum = P ⊕ C
    assign sum = p ^ c;
endmodule
```

### Key Patterns
| Pattern | Code |
|---------|------|
| Generate | `g = a & b` |
| Propagate | `p = a ^ b` |
| Carry chain | `c[i] = g[i-1] | (p[i-1] & c[i-1])` |
| Sum | `sum = p ^ c` |

---

## Prefix Adder Testbench

```verilog
module prefix_adder_tb;
    reg  [3:0] a, b;
    reg        cin;
    wire [3:0] sum;
    wire       cout;

    prefix_adder uut(a, b, cin, sum, cout);

    initial begin
        $dumpfile("prefix_adder.vcd");
        $dumpvars(0, prefix_adder_tb);

        $monitor($time, " a=%b b=%b cin=%b | sum=%b cout=%b", a, b, cin, sum, cout);

        a = 4'b0000; b = 4'b0000; cin = 1'b0;
        #20 a = 4'b0101; b = 4'b0011; cin = 1'b0;   // 5+3=8
        #20 a = 4'b1111; b = 4'b0001; cin = 1'b0;   // 15+1=16 (cout=1)
        #20 a = 4'b1010; b = 4'b0101; cin = 1'b1;   // 10+5+1=16
        #20 a = 4'b1111; b = 4'b1111; cin = 1'b0;   // 15+15=30
        #20 a = 4'b1111; b = 4'b1111; cin = 1'b1;   // 15+15+1=31
        #20 $finish;
    end
endmodule
```

### Testbench Patterns
| Pattern | Code |
|---------|------|
| VCD dump | `$dumpfile`, `$dumpvars` |
| Monitor | `$monitor($time, "fmt", signals)` |
| Stimulus | `#delay` assignments |
| Finish | `$finish` |

---

## Comparator (4-bit)

```verilog
module comparator(
    input  [3:0] a, b,
    output       greater, equal, less
);
    assign greater = (a > b);
    assign equal   = (a == b);
    assign less    = (a < b);
endmodule
```

### Behavioral vs Structural
- **Behavioral:** Uses `>`, `==`, `<` operators (synthesizable)
- **Structural:** Would build from XNOR + AND for equality, MSB-first chain for magnitude

---

## Common Verilog Patterns for DLCD

### D Flip-Flop
```verilog
module dff(
    input  clk, reset, d,
    output reg q
);
    always @(posedge clk or posedge reset) begin
        if (reset) q <= 1'b0;
        else       q <= d;
    end
endmodule
```

### Enabled D Flip-Flop (No Clock Gating!)
```verilog
module dff_en(
    input  clk, reset, en, d,
    output reg q
);
    always @(posedge clk or posedge reset) begin
        if (reset) q <= 1'b0;
        else if (en) q <= d;
    end
endmodule
```

### 2:1 MUX
```verilog
module mux21(
    input  s, d0, d1,
    output y
);
    assign y = s ? d1 : d0;
endmodule
```

### Parameterized N-bit Register
```verilog
module reg_n #(parameter N=8)(
    input  clk, reset,
    input  [N-1:0] d,
    output reg [N-1:0] q
);
    always @(posedge clk or posedge reset) begin
        if (reset) q <= {N{1'b0}};
        else       q <= d;
    end
endmodule
```

### FSM Template (Moore)
```verilog
module fsm_moore(
    input  clk, reset, x,
    output reg y
);
    localparam S0 = 2'b00, S1 = 2'b01, S2 = 2'b10, S3 = 2'b11;
    reg [1:0] state, next_state;

    always @(posedge clk or posedge reset) begin
        if (reset) state <= S0;
        else       state <= next_state;
    end

    always @(*) begin
        case (state)
            S0: next_state = x ? S1 : S0;
            S1: next_state = x ? S2 : S0;
            S2: next_state = x ? S3 : S0;
            S3: next_state = x ? S3 : S0;
            default: next_state = S0;
        endcase
    end

    always @(*) begin
        y = (state == S3);  // Moore output
    end
endmodule
```

### FSM Template (Mealy)
```verilog
module fsm_mealy(
    input  clk, reset, x,
    output reg y
);
    localparam S0 = 1'b0, S1 = 1'b1;
    reg state, next_state;

    always @(posedge clk or posedge reset) begin
        if (reset) state <= S0;
        else       state <= next_state;
    end

    always @(*) begin
        case (state)
            S0: begin
                next_state = x ? S1 : S0;
                y = 1'b0;
            end
            S1: begin
                next_state = x ? S1 : S0;
                y = x;  // Mealy output on transition
            end
        endcase
    end
endmodule
```

---

## Quick Reference

| Construct | Syntax |
|-----------|--------|
| Non-blocking | `<=` (sequential) |
| Blocking | `=` (combinational) |
| Case | `case (sig) ... endcase` |
| If-else | `if (cond) ... else ...` |
| Concatenation | `{a, b, c}` |
| Replication | `{N{val}}` |
| Parameter | `#(param=val)` |

---

## Exam-Relevant Code Patterns

1. **Prefix adder carry** — explicit prefix equations
2. **FSM two-process** — state reg + next-state comb
3. **Default case** — safe recovery
4. **Non-blocking in seq** — `<=` always
5. **Enabled FF** — `if (en) q <= d` not clock gating
6. **Parameterized modules** — `#(parameter N=8)`

---

## Key Verilog Rules (Memorize)

```
Sequential:   always @(posedge clk)  q <= d;
Combinational: always @(*)           y = a & b;
FSM:          State reg (non-block) + Next-state comb (block)
Reset:        Sync or async (posedge reset)
Default:      Always in case for synthesis safety
```
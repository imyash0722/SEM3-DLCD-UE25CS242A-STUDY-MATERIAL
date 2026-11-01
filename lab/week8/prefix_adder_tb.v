module prefix_adder_tb;
    reg [3:0] a, b;
    reg cin;
    wire [3:0] sum;
    wire cout;

    prefix_adder uut(a, b, cin, sum, cout);

    initial begin
        $dumpfile("prefix_adder.vcd");
        $dumpvars(0, prefix_adder_tb);

        $monitor($time, " a=%b b=%b cin=%b | sum=%b cout=%b", a, b, cin, sum, cout);

        a = 4'b0000; b = 4'b0000; cin = 1'b0;
        #20 a = 4'b0101; b = 4'b0011; cin = 1'b0;
        #20 a = 4'b1111; b = 4'b0001; cin = 1'b0;
        #20 a = 4'b1010; b = 4'b0101; cin = 1'b1;
        #20 a = 4'b1111; b = 4'b1111; cin = 1'b0;
        #20 a = 4'b1111; b = 4'b1111; cin = 1'b1;
        #20 $finish;
    end
endmodule
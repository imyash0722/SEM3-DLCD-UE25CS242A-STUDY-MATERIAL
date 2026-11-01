module comparator_tb;
    reg [3:0] a, b;
    wire greater, equal, less;

    comparator uut(a, b, greater, equal, less);

    initial begin
        $dumpfile("comparator.vcd");
        $dumpvars(0, comparator_tb);

        $monitor($time, " a=%b b=%b | greater=%b equal=%b less=%b", a, b, greater, equal, less);

        a = 4'b0000; b = 4'b0000;
        #20 a = 4'b0101; b = 4'b0011;
        #20 a = 4'b0010; b = 4'b0110;
        #20 a = 4'b1000; b = 4'b1000;
        #20 a = 4'b1111; b = 4'b0001;
        #20 a = 4'b0100; b = 4'b1100;
        #20 a = 4'b1010; b = 4'b1010;
        #20 $finish;
    end
endmodule

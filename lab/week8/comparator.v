module comparator(
    input [3:0] a, b,
    output greater, equal, less
);
    assign greater = (a > b);
    assign equal = (a == b);
    assign less = (a < b);
endmodule

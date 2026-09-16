def carrysave_adder(a, b, c, final_adder=ripple_add):
    a, b, c = libutils.match_bitwidth(a, b, c)
    partial_sum = a ^ b ^ c
    shift_carry = (a | b) & (a | c) & (b | c)
    return pyrtl.concat(final_adder(partial_sum[1:], shift_carry),
        partial_sum[0])
def fused_multiply_adder(mult_A, mult_B, add, signed=False, reducer=adders.
    wallace_reducer, adder_func=adders.kogge_stone):
    return generalized_fma(((mult_A, mult_B),), (add,), signed, reducer,
        adder_func)
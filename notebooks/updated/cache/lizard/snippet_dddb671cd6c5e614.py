def op_decanonicalize(op_name, canonical_op):
    global DECANONICALIZE_METHODS
    if op_name not in DECANONICALIZE_METHODS:
        return canonical_op
    else:
        return DECANONICALIZE_METHODS[op_name](canonical_op)
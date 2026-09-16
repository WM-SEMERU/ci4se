def _bin_op(instance, opnode, op, other, context, reverse=False):
    if reverse:
        method_name = protocols.REFLECTED_BIN_OP_METHOD[op]
    else:
        method_name = protocols.BIN_OP_METHOD[op]
    return functools.partial(_invoke_binop_inference, instance=instance, op
        =op, opnode=opnode, other=other, context=context, method_name=
        method_name)
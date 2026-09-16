def reduce_log_sum_exp(attrs, inputs, proto_obj):
    keep_dims = True if 'keepdims' not in attrs else attrs.get('keepdims')
    exp_op = symbol.exp(inputs[0])
    sum_op = symbol.sum(exp_op, axis=attrs.get('axes'), keepdims=keep_dims)
    log_sym = symbol.log(sum_op)
    return log_sym, attrs, inputs
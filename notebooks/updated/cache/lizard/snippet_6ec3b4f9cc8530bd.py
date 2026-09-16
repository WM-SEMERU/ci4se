def resolve_broadcast_params(inputs, function_proto, batch_size):
    f = function_proto
    negative_count = 0
    for d in f.broadcast_param.shape.dim:
        if d < 0:
            negative_count += 1
    if negative_count > 1:
        raise ValueError('Reshape: shape has multiple negative number.')
    shape = tuple([(d if d >= 0 else batch_size) for d in f.broadcast_param
        .shape.dim])
    return shape
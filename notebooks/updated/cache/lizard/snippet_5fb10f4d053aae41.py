def split_backward(layers):
    backward = []
    forward = [sink_return(op.begin_update, backward.append) for op in layers]
    return forward, backward
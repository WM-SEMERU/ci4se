def _merge_multi_context(outputs, major_axis):
    rets = []
    for tensors, axis in zip(outputs, major_axis):
        if axis >= 0:
            if len(tensors) == 1:
                rets.append(tensors[0])
            else:
                rets.append(nd.concat(*[tensor.as_in_context(tensors[0].
                    context) for tensor in tensors], dim=axis))
        else:
            rets.append(tensors[0])
    return rets
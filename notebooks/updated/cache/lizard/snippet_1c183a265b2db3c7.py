def split_and_load(data, ctx_list, batch_axis=0, even_split=True):
    if not isinstance(data, ndarray.NDArray):
        data = ndarray.array(data, ctx=ctx_list[0])
    if len(ctx_list) == 1:
        return [data.as_in_context(ctx_list[0])]
    slices = split_data(data, len(ctx_list), batch_axis, even_split)
    return [i.as_in_context(ctx) for i, ctx in zip(slices, ctx_list)]
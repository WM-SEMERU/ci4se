def replace_dimensions(tensor_or_shape, old_dim_or_dims, new_dim_or_dims):
    if isinstance(tensor_or_shape, Tensor):
        return reshape(tensor_or_shape, replace_dimensions(tensor_or_shape.
            shape, old_dim_or_dims, new_dim_or_dims))
    if not isinstance(tensor_or_shape, Shape):
        raise ValueError('tensor_or_shape must be a Tensor or Shape got %s' %
            (tensor_or_shape,))
    in_dims = tensor_or_shape.dims
    if isinstance(old_dim_or_dims, Dimension):
        old_dim_or_dims = [old_dim_or_dims]
    if isinstance(new_dim_or_dims, Dimension):
        new_dim_or_dims = [new_dim_or_dims]
    if not isinstance(old_dim_or_dims, list) or not old_dim_or_dims:
        raise ValueError(
            'old_dim_or_dims must be a Dimension or a list of Dimension got %s'
             % (old_dim_or_dims,))
    if not isinstance(new_dim_or_dims, list) or not new_dim_or_dims:
        raise ValueError(
            'new_dim_or_dims must be a Dimension or a list of Dimension got %s'
             % (new_dim_or_dims,))
    try:
        positions = [in_dims.index(d) for d in old_dim_or_dims]
        pos = positions[0]
        if positions != list(range(pos, pos + len(positions))):
            raise ValueError()
    except ValueError:
        raise ValueError(
            "old_dim_or_dims must be a subsequence of the input's dimensions old_dim_or_dims=%s input's dimensions=%s"
             % (old_dim_or_dims, in_dims))
    return Shape(in_dims[:pos] + new_dim_or_dims + in_dims[pos + len(
        old_dim_or_dims):])
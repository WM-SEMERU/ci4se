def assign(var, new_val, assign_fn=assign_slice):
    if isinstance(var, Tensor):
        var = var.operation
    if not isinstance(var, Variable):
        raise ValueError('var must be a mtf.Variable or its output Tensor.')
    return Assign([var], [new_val], assign_fn=assign_fn)
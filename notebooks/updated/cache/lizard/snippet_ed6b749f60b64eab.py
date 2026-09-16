def uniform_discr_fromspace(fspace, shape, dtype=None, impl='numpy', **kwargs):
    if not isinstance(fspace, FunctionSpace):
        raise TypeError('`fspace` {!r} is not a `FunctionSpace` instance'.
            format(fspace))
    if not isinstance(fspace.domain, IntervalProd):
        raise TypeError(
            'domain {!r} of the function space is not an `IntervalProd` instance'
            .format(fspace.domain))
    if dtype is None:
        dtype = fspace.out_dtype
    else:
        dtype, dtype_in = np.dtype(dtype), dtype
        if not np.can_cast(fspace.scalar_out_dtype, dtype, casting='safe'):
            raise ValueError(
                'cannot safely cast from output data {} type of the function space to given data type {}'
                .format(fspace.out, dtype_in))
    if fspace.field == RealNumbers() and not is_real_dtype(dtype):
        raise ValueError(
            'cannot discretize real space {} with non-real data type {}'.
            format(fspace, dtype))
    elif fspace.field == ComplexNumbers() and not is_complex_floating_dtype(
        dtype):
        raise ValueError(
            'cannot discretize complex space {} with non-complex-floating data type {}'
            .format(fspace, dtype))
    nodes_on_bdry = kwargs.pop('nodes_on_bdry', False)
    partition = uniform_partition_fromintv(fspace.domain, shape, nodes_on_bdry)
    return uniform_discr_frompartition(partition, dtype, impl, **kwargs)
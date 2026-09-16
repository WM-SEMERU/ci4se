def _conversion_function(pt_wrapper, dtype=None, name=None, as_ref=False):
    _ = name, as_ref
    t = pt_wrapper.tensor
    if dtype and not dtype.is_compatible_with(t.dtype):
        raise ValueError(
            'Tensor conversion requested dtype %s for Tensor with dtype %s: %r'
             % (dtype, t.dtype, t))
    return t
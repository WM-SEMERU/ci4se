def window_from_array(array):
    from ...utils.lal import find_typed_function
    dtype = array.dtype
    seq = find_typed_function(dtype, 'Create', 'Sequence')(array.size)
    seq.data = array
    return find_typed_function(dtype, 'Create', 'WindowFromSequence')(seq)
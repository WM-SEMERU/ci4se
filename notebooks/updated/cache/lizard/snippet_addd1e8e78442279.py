def find_common_dtype(*args):
    dtypes = []
    for arg in args:
        if type(arg) is numpy.ndarray or isspmatrix(arg) or isinstance(arg,
            LinearOperator):
            if hasattr(arg, 'dtype'):
                dtypes.append(arg.dtype)
            else:
                warnings.warn('object %s does not have a dtype.' % arg.__repr__
                    )
    return numpy.find_common_type(dtypes, [])
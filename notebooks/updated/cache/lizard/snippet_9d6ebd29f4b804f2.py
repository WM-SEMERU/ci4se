def make_function(function, name, arity):
    if not isinstance(arity, int):
        raise ValueError('arity must be an int, got %s' % type(arity))
    if not isinstance(function, np.ufunc):
        if function.__code__.co_argcount != arity:
            raise ValueError(
                'arity %d does not match required number of function arguments of %d.'
                 % (arity, function.__code__.co_argcount))
    if not isinstance(name, str):
        raise ValueError('name must be a string, got %s' % type(name))
    args = [np.ones(10) for _ in range(arity)]
    try:
        function(*args)
    except ValueError:
        raise ValueError(
            'supplied function %s does not support arity of %d.' % (name,
            arity))
    if not hasattr(function(*args), 'shape'):
        raise ValueError(
            'supplied function %s does not return a numpy array.' % name)
    if function(*args).shape != (10,):
        raise ValueError(
            'supplied function %s does not return same shape as input vectors.'
             % name)
    args = [np.zeros(10) for _ in range(arity)]
    if not np.all(np.isfinite(function(*args))):
        raise ValueError(
            'supplied function %s does not have closure against zeros in argument vectors.'
             % name)
    args = [(-1 * np.ones(10)) for _ in range(arity)]
    if not np.all(np.isfinite(function(*args))):
        raise ValueError(
            'supplied function %s does not have closure against negatives in argument vectors.'
             % name)
    return _Function(function, name, arity)
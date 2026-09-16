def combinations(n, k, strength=1, vartype=BINARY):
    r
    if isinstance(n, abc.Sized) and isinstance(n, abc.Iterable):
        variables = n
    else:
        try:
            variables = range(n)
        except TypeError:
            raise TypeError('n should be a collection or an integer')
    if k > len(variables) or k < 0:
        raise ValueError('cannot select k={} from {} variables'.format(k,
            len(variables)))
    lbias = float(strength * (1 - 2 * k))
    qbias = float(2 * strength)
    bqm = BinaryQuadraticModel.empty(vartype)
    bqm.add_variables_from(((v, lbias) for v in variables), vartype=BINARY)
    bqm.add_interactions_from(((u, v, qbias) for u, v in itertools.
        combinations(variables, 2)), vartype=BINARY)
    bqm.add_offset(strength * k ** 2)
    return bqm
def generate_quadrature(order, domain, accuracy=100, sparse=False, rule='C',
    composite=1, growth=None, part=None, normalize=False, **kws):
    from ..distributions.baseclass import Dist
    isdist = isinstance(domain, Dist)
    if isdist:
        dim = len(domain)
    else:
        dim = np.array(domain[0]).size
    rule = rule.lower()
    if len(rule) == 1:
        rule = collection.QUAD_SHORT_NAMES[rule]
    quad_function = collection.get_function(rule, domain, normalize, growth
        =growth, composite=composite, accuracy=accuracy)
    if sparse:
        order = np.ones(len(domain), dtype=int) * order
        abscissas, weights = sparse_grid.sparse_grid(quad_function, order, dim)
    else:
        abscissas, weights = quad_function(order)
    assert len(weights) == abscissas.shape[1]
    assert len(abscissas.shape) == 2
    return abscissas, weights
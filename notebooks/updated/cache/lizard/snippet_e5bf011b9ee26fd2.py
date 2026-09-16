def _mom(self, key, left, right, cache):
    if evaluation.get_dependencies(left, right):
        raise evaluation.DependencyError(
            'sum of dependent distributions not feasible: {} and {}'.format
            (left, right))
    if isinstance(left, Dist):
        left = evaluation.evaluate_moment(left, key, cache=cache)
    else:
        left = (numpy.array(left).T ** key).T
    if isinstance(right, Dist):
        right = evaluation.evaluate_moment(right, key, cache=cache)
    else:
        right = (numpy.array(right).T ** key).T
    return numpy.sum(left * right)
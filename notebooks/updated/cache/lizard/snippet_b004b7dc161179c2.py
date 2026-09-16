def intersect(self, other, strategy=_STRATEGY.GEOMETRIC, _verify=True):
    if _verify:
        if not isinstance(other, Surface):
            raise TypeError('Can only intersect with another surface',
                'Received', other)
        if self._dimension != 2 or other._dimension != 2:
            raise NotImplementedError('Intersection only implemented in 2D')
    if strategy == _STRATEGY.GEOMETRIC:
        do_intersect = _surface_intersection.geometric_intersect
    elif strategy == _STRATEGY.ALGEBRAIC:
        do_intersect = _surface_intersection.algebraic_intersect
    else:
        raise ValueError('Unexpected strategy.', strategy)
    edge_infos, contained, all_edge_nodes = do_intersect(self._nodes, self.
        _degree, other._nodes, other._degree, _verify)
    if edge_infos is None:
        if contained:
            return [self]
        else:
            return [other]
    else:
        return [_make_intersection(edge_info, all_edge_nodes) for edge_info in
            edge_infos]
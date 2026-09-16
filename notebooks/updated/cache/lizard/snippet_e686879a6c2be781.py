def compile(self, X, verbose=False):
    if self.feature >= X.shape[1]:
        raise ValueError(
            'term requires feature {}, but X has only {} dimensions'.format
            (self.feature, X.shape[1]))
    self.edge_knots_ = gen_edge_knots(X[:, (self.feature)], self.dtype,
        verbose=verbose)
    return self
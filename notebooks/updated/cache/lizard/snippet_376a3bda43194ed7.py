def _range(self, xloc, cache):
    uloc = numpy.zeros((2, len(self)))
    for dist in evaluation.sorted_dependencies(self, reverse=True):
        if dist not in self.inverse_map:
            continue
        idx = self.inverse_map[dist]
        xloc_ = xloc[idx].reshape(1, -1)
        uloc[:, (idx)] = evaluation.evaluate_bound(dist, xloc_, cache=cache
            ).flatten()
    return uloc
def potential_purviews(self, direction, mechanism, purviews=False):
    if purviews is False:
        purviews = self.network.potential_purviews(direction, mechanism)
        purviews = [purview for purview in purviews if set(purview).
            issubset(self.node_indices)]
    return irreducible_purviews(self.cm, direction, mechanism, purviews)
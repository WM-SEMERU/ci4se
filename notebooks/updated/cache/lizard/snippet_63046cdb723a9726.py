def cull_portals(self, stat, threshold=0.5, comparator=ge):
    comparator = self._lookup_comparator(comparator)
    dead = []
    for u in self.portal:
        for v in self.portal[u]:
            if stat in self.portal[u][v] and comparator(self.portal[u][v][
                stat], threshold):
                dead.append((u, v))
    self.remove_edges_from(dead)
    return self
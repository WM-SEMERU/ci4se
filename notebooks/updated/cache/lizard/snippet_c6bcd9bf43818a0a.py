def size(self, piecewise=False):
    if piecewise:
        return {k: v.size() for k, v in self.items()}
    return self.master_graph.size()
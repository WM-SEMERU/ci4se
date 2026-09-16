def edge_val_set(self, graph, orig, dest, idx, key, branch, turn, tick, value):
    if (branch, turn, tick) in self._btts:
        raise TimeError
    self._btts.add((branch, turn, tick))
    graph, orig, dest, key, value = map(self.pack, (graph, orig, dest, key,
        value))
    self._edgevals2set.append((graph, orig, dest, idx, key, branch, turn,
        tick, value))
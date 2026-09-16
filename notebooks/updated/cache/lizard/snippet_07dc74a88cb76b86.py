def eliminate(self, node, data):
    self.eliminated[node] = data
    others = self.checks[node]
    del self.checks[node]
    for check in others:
        check.check ^= data
        check.src_nodes.remove(node)
        if len(check.src_nodes) == 1:
            yield next(iter(check.src_nodes)), check.check
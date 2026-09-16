def match_seq(self, nodes, results=None):
    if len(nodes) != 1:
        return False
    return self.match(nodes[0], results)
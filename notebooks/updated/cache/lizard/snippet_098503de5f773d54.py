def all_nbrs(self, node):
    l = dict.fromkeys(self.inc_nbrs(node) + self.out_nbrs(node))
    return list(l)
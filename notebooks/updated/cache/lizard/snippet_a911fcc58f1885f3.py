def prune(self):
    pruned = []
    for c in self.children:
        c.prune()
        if c.isempty(False):
            pruned.append(c)
    for p in pruned:
        self.children.remove(p)
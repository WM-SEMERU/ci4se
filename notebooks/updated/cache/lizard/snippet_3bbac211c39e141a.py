def ladderize(self, direction=0):
    if not self.is_leaf():
        n2s = {}
        for n in self.get_children():
            s = n.ladderize(direction=direction)
            n2s[n] = s
        self.children.sort(key=lambda x: n2s[x])
        if direction == 1:
            self.children.reverse()
        size = sum(n2s.values())
    else:
        size = 1
    return size
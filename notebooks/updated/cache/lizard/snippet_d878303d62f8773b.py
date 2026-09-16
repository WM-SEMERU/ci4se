def remove_pane(self, pane):
    assert isinstance(pane, Pane)
    if pane in self.panes:
        if pane == self.active_pane:
            if self.previous_active_pane:
                self.active_pane = self.previous_active_pane
            else:
                self.focus_next()
        p = self._get_parent(pane)
        p.remove(pane)
        while len(p) == 0 and p != self.root:
            p2 = self._get_parent(p)
            p2.remove(p)
            p = p2
        while len(p) == 1 and p != self.root:
            p2 = self._get_parent(p)
            p2.weights[p[0]] = p2.weights[p]
            i = p2.index(p)
            p2[i] = p[0]
            p = p2
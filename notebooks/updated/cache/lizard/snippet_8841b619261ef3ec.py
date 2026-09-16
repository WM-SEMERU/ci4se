def add(self, pane):
    if isinstance(pane, list):
        initialised_panes = []
        for p in pane:
            initialised_panes.append(self.init_pane(p))
        self.panes.append(initialised_panes)
    else:
        pane = self.init_pane(pane)
        self.panes.append(pane)
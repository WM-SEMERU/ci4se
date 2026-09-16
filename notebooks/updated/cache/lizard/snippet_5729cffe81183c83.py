def enable(self):
    nwin = self.nwin.value()
    for label, xs, ys, nx, ny in zip(self.label[:nwin], self.xs[:nwin],
        self.ys[:nwin], self.nx[:nwin], self.ny[:nwin]):
        label.config(state='normal')
        xs.enable()
        ys.enable()
        nx.enable()
        ny.enable()
    for label, xs, ys, nx, ny in zip(self.label[nwin:], self.xs[nwin:],
        self.ys[nwin:], self.nx[nwin:], self.ny[nwin:]):
        label.config(state='disable')
        xs.disable()
        ys.disable()
        nx.disable()
        ny.disable()
    self.nwin.enable()
    self.xbin.enable()
    self.ybin.enable()
    self.sbutt.enable()
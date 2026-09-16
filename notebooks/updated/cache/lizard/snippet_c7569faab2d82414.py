def compute(self):
    self.setd = []
    self.satc = [False for cl in self.soft]
    self.solution = None
    self.bb_assumps = []
    self.ss_assumps = []
    if self.oracle.solve():
        self._filter_satisfied(update_setd=True)
        self._compute()
        self.solution = list(map(lambda i: i + 1, filter(lambda i: not self
            .satc[i], range(len(self.soft)))))
    return self.solution
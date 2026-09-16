def peirce_skill_score(self):
    n = float(self.table.sum())
    nf = self.table.sum(axis=1)
    no = self.table.sum(axis=0)
    correct = float(self.table.trace())
    return (correct / n - (nf * no).sum() / n ** 2) / (1 - (no * no).sum() /
        n ** 2)
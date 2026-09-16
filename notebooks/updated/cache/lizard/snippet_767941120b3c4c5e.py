def append(self, clause):
    self.nv = max([abs(l) for l in clause] + [self.nv])
    self.clauses.append(clause)
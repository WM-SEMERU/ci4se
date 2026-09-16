def to_binary(self, copy=False):
    if self.vartype is Vartype.BINARY:
        if copy:
            return self.copy()
        else:
            return self
    new = BinaryPolynomial({}, Vartype.BINARY)
    for term, bias in self.items():
        for t in map(frozenset, powerset(term)):
            newbias = bias * 2 ** len(t) * (-1) ** (len(term) - len(t))
            if t in new:
                new[t] += newbias
            else:
                new[t] = newbias
    return new
def reduce(self):
    support = frozenset(range(1, self.nvars + 1))
    new_clauses = set()
    for clause in self.clauses:
        vs = list(support - {abs(uniqid) for uniqid in clause})
        if vs:
            for num in range(1 << len(vs)):
                new_part = {(v if bit_on(num, i) else ~v) for i, v in
                    enumerate(vs)}
                new_clauses.add(clause | new_part)
        else:
            new_clauses.add(clause)
    return self.__class__(self.nvars, new_clauses)
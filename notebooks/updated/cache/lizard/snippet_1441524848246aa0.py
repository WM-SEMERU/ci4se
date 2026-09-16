def expressions(self):
    for s in self.statements:
        for expr_ in s.expressions:
            yield expr_
    yield self.next
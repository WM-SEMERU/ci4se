def parse_set(self):
    lineno = next(self.stream).lineno
    target = self.parse_assign_target()
    self.stream.expect('assign')
    expr = self.parse_tuple()
    return nodes.Assign(target, expr, lineno=lineno)
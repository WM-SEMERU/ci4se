def demorgan(self):
    expr = self.cancel()
    if expr.isliteral or not isinstance(expr, self.NOT):
        return expr
    op = expr.args[0]
    return op.dual(*(self.__class__(arg).cancel() for arg in op.args))
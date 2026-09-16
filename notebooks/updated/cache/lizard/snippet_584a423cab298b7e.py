def child_expressions(self):
    expressions = []
    for k in self.__slots__:
        v = getattr(self, k)
        if isinstance(v, IRExpr):
            expressions.append(v)
            expressions.extend(v.child_expressions)
    return expressions
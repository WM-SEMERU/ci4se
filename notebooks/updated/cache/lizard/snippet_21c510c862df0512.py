def _guess_name_of(self, expr):
    if isinstance(expr, ast.Var):
        return expr.value
    if isinstance(expr, ast.Resolve):
        return expr.rhs.value
    if isinstance(expr, ast.Select) and isinstance(expr.rhs, ast.Literal):
        name = self._guess_name_of(expr.lhs)
        if name is not None:
            return '%s_%s' % (name, expr.rhs.value)
    if isinstance(expr, ast.Apply) and isinstance(expr.func, ast.Var):
        return expr.func.value
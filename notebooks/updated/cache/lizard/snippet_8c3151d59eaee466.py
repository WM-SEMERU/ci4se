def is_constant(expression):
    if isinstance(expression, Wildcard):
        return False
    if isinstance(expression, Expression):
        return expression.is_constant
    if isinstance(expression, Operation):
        return all(is_constant(o) for o in op_iter(expression))
    return True
def concat_expr(operator, conditions):
    expr = ' {0} '.format(operator).join(conditions)
    return ['({0})'.format(expr)] if expr else []
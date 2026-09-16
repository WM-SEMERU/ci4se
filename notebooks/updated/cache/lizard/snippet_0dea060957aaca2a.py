def evaluate_rule(self, rule, value, target):

    def evaluate(expr):
        if expr in LOGICAL_OPERATORS.values():
            return expr
        rvalue = self.get_value_for_expr(expr, target)
        if rvalue is None:
            return False
        return expr['op'](value, rvalue)
    evaluated = [evaluate(expr) for expr in rule['exprs']]
    while len(evaluated) > 1:
        lhs, logical_op, rhs = (evaluated.pop(0) for _ in range(3))
        evaluated.insert(0, logical_op(lhs, rhs))
    return evaluated[0]
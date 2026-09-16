def get_value_for_expr(self, expr, target):
    if expr in LOGICAL_OPERATORS.values():
        return None
    rvalue = expr['value']
    if rvalue == HISTORICAL:
        history = self.history[target]
        if len(history) < self.history_size:
            return None
        rvalue = sum(history) / float(len(history))
    rvalue = expr['mod'](rvalue)
    return rvalue
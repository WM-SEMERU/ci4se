def _default_return_columns(self):
    return_columns = []
    parsed_expr = []
    for key, value in self.components._namespace.items():
        if hasattr(self.components, value):
            sig = signature(getattr(self.components, value))
            if len(set(sig.parameters) - {'args'}) == 0:
                expr = self.components._namespace[key]
                if not expr in parsed_expr:
                    return_columns.append(key)
                    parsed_expr.append(expr)
    return return_columns
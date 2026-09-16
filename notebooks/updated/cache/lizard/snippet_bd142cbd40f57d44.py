def _merge_expressions(self, other):
    new_inputs = tuple(set(self.inputs).union(other.inputs))
    new_self_expr = self._rebind_variables(new_inputs)
    new_other_expr = other._rebind_variables(new_inputs)
    return new_self_expr, new_other_expr, new_inputs
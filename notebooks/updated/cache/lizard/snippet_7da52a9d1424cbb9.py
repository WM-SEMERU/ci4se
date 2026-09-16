def _gather_variables(stack_def):
    variable_values = copy.deepcopy(stack_def.variables or {})
    return [Variable(k, v) for k, v in variable_values.items()]
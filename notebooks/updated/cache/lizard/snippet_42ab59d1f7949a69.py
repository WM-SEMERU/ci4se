def getInputOrder(ast, input_order=None):
    variables = {}
    for a in ast.allOf('variable'):
        variables[a.value] = a
    variable_names = set(variables.keys())
    if input_order:
        if variable_names != set(input_order):
            raise ValueError(
                "input names (%s) don't match those found in expression (%s)" %
                (input_order, variable_names))
        ordered_names = input_order
    else:
        ordered_names = list(variable_names)
        ordered_names.sort()
    ordered_variables = [variables[v] for v in ordered_names]
    return ordered_variables
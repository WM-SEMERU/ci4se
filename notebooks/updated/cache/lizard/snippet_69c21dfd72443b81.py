def _complete_parameters(param, variables):
    if isinstance(param, list):
        return [_complete_parameters(x, variables) for x in param]
    elif isinstance(param, dict):
        return {key: _complete_parameters(value, variables) for key, value in
            param.items()}
    elif isinstance(param, str):
        try:
            return Template(param).substitute(variables)
        except KeyError as exc:
            raise RecipeVariableNotPassed('Variable undefined in recipe',
                undefined_variable=exc.args[0])
    return param
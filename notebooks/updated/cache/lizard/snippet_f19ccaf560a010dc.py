def check_input_and_output_types(operator, good_input_types=None,
    good_output_types=None):
    if good_input_types is not None:
        for variable in operator.inputs:
            if type(variable.type) not in good_input_types:
                raise RuntimeError(
                    'Operator %s (type: %s) got an input %s with a wrong type %s. Only %s are allowed'
                     % (operator.full_name, operator.type, variable.
                    full_name, type(variable.type), good_input_types))
    if good_output_types is not None:
        for variable in operator.outputs:
            if type(variable.type) not in good_output_types:
                raise RuntimeError(
                    'Operator %s (type: %s) got an output %s with a wrong type %s. Only %s are allowed'
                     % (operator.full_name, operator.type, variable.
                    full_name, type(variable.type), good_output_types))
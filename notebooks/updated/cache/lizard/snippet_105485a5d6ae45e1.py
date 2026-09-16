def _get_hyperparameter_solution_size(meta_parameters):
    solution_size = 0
    for _, parameters in meta_parameters.iteritems():
        if parameters['type'] == 'discrete':
            num_values = len(parameters['values'])
            binary_size = helpers.binary_size(num_values)
        elif parameters['type'] == 'int':
            int_range = parameters['max'] - parameters['min'] + 1
            binary_size = helpers.binary_size(int_range)
        elif parameters['type'] == 'float':
            float_range = parameters['max'] - parameters['min']
            binary_size = helpers.binary_size(float_range * 1000)
        else:
            raise ValueError('Parameter type "{}" does not match known values'
                .format(parameters['type']))
        parameters['binary_size'] = binary_size
        solution_size += binary_size
    return solution_size
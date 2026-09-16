def logp_gradient_of_set(variable_set, calculation_set=None):
    logp_gradients = {}
    for variable in variable_set:
        logp_gradients[variable] = logp_gradient(variable, calculation_set)
    return logp_gradients
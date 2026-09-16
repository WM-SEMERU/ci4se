def disasters(value=disasters_array, params_of_mean=params_of_mean):
    val = params_of_mean[1] + params_of_mean[0] * arange(111)
    return poisson_like(value, val)
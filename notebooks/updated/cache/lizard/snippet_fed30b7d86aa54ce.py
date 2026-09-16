def maape(simulated_array, observed_array, replace_nan=None, replace_inf=
    None, remove_neg=False, remove_zero=False):
    simulated_array, observed_array = treat_values(simulated_array,
        observed_array, replace_nan=replace_nan, replace_inf=replace_inf,
        remove_neg=remove_neg, remove_zero=remove_zero)
    a = simulated_array - observed_array
    b = np.abs(a / observed_array)
    return np.mean(np.arctan(b))
def drel(simulated_array, observed_array, replace_nan=None, replace_inf=
    None, remove_neg=False, remove_zero=False):
    simulated_array, observed_array = treat_values(simulated_array,
        observed_array, replace_nan=replace_nan, replace_inf=replace_inf,
        remove_neg=remove_neg, remove_zero=remove_zero)
    a = ((simulated_array - observed_array) / observed_array) ** 2
    b = np.abs(simulated_array - np.mean(observed_array))
    c = np.abs(observed_array - np.mean(observed_array))
    e = ((b + c) / np.mean(observed_array)) ** 2
    return 1 - np.sum(a) / np.sum(e)
def _scaling_func_list(bdry_fracs, exponent):

    def scaling(factor):

        def scaling_func(x):
            return x * factor
        return scaling_func
    func_list = []
    for frac_l, frac_r in bdry_fracs:
        func_list_entry = []
        if np.isclose(frac_l, 1.0):
            func_list_entry.append(None)
        else:
            func_list_entry.append(scaling(frac_l ** (1 / exponent)))
        if np.isclose(frac_r, 1.0):
            func_list_entry.append(None)
        else:
            func_list_entry.append(scaling(frac_r ** (1 / exponent)))
        func_list.append(func_list_entry)
    return func_list
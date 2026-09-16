def chi_p_from_xi1_xi2(xi1, xi2):
    xi1, xi2, input_is_array = ensurearray(xi1, xi2)
    chi_p = copy.copy(xi1)
    mask = xi1 < xi2
    chi_p[mask] = xi2[mask]
    return formatreturn(chi_p, input_is_array)
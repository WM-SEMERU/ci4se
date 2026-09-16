def correct_rates(rates, opt_qes, combs):
    corrected_rates = np.array([(rate / opt_qes[comb[0]] / opt_qes[comb[1]]
        ) for rate, comb in zip(rates, combs)])
    return corrected_rates
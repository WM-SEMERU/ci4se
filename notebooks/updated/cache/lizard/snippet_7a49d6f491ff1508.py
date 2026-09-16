def cena_tau(imt, mag, params):
    if imt.name == 'PGV':
        C = params['PGV']
    else:
        C = params['SA']
    if mag > 6.5:
        return C['tau3']
    elif mag > 5.5 and mag <= 6.5:
        return ITPL(mag, C['tau3'], C['tau2'], 5.5, 1.0)
    elif mag > 5.0 and mag <= 5.5:
        return ITPL(mag, C['tau2'], C['tau1'], 5.0, 0.5)
    else:
        return C['tau1']
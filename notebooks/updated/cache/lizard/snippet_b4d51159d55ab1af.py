def get_phi_ss(imt, mag, params):
    C = params[imt]
    if mag <= 5.0:
        phi = C['a']
    elif mag > 6.5:
        phi = C['b']
    else:
        phi = C['a'] + (mag - 5.0) * ((C['b'] - C['a']) / 1.5)
    return phi
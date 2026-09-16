def seebeck_spb(eta, Lambda=0.5):
    from fdint import fdk
    return constants.k / constants.e * ((2.0 + Lambda) * fdk(1.0 + Lambda,
        eta) / ((1.0 + Lambda) * fdk(Lambda, eta)) - eta) * 1000000.0
def Fahien_Schriver(dp, voidage, vs, rho, mu, L=1):
    r
    Rem = dp * rho * vs / mu / (1 - voidage)
    q = exp(-voidage ** 2 * (1 - voidage) / 12.6 * Rem)
    f1L = 136 / (1 - voidage) ** 0.38
    f1T = 29 / ((1 - voidage) ** 1.45 * voidage ** 2)
    f2 = 1.87 * voidage ** 0.75 / (1 - voidage) ** 0.26
    fp = (q * f1L / Rem + (1 - q) * (f2 + f1T / Rem)) * (1 - voidage
        ) / voidage ** 3
    return fp * rho * vs ** 2 * L / dp
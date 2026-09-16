def dP_demister_dry_Setekleiv_Svendsen(S, voidage, vs, rho, mu, L=1):
    r
    term = 10.29 - 565.0 / (69.6 * S * L - (S * L) ** 2 - 779) - 74.9 / (
        160.9 - 4.85 * S * L)
    right = term + 45.33 * (mu * voidage * S ** 2 * L / rho / vs) ** 0.75
    return right * rho * vs ** 2 / voidage ** 2
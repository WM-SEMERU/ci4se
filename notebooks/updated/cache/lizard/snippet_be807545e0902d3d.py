def Nu_sphere_Churchill(Pr, Gr):
    r
    Ra = Pr * Gr
    Nu = 2 + 0.589 * Ra ** 0.25 / (1 + (0.469 / Pr) ** (9 / 16.0)) ** (4 / 9.0
        ) * (1 + 7.44e-08 * Ra / (1 + (0.469 / Pr) ** (9 / 16.0)) ** (16 / 9.0)
        ) ** (1 / 12.0)
    return Nu
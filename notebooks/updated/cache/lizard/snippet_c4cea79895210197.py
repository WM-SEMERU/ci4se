def Nu_vertical_plate_Churchill(Pr, Gr):
    r
    Ra = Pr * Gr
    Nu = (0.825 + 0.387 * Ra ** (1 / 6.0) / (1 + (0.492 / Pr) ** (9 / 16.0)
        ) ** (8 / 27.0)) ** 2
    return Nu
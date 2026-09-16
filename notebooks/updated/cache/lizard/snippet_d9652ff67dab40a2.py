def Schade(mp, rhop, dp, rhog, D):
    r
    B = (D / dp) ** 0.025 * (rhop / rhog) ** 0.34
    A = (g * D) ** 0.5
    C = mp / (rhog * pi / 4 * D ** 2)
    return (C ** 0.11 * B * A) ** (1 / 1.11)
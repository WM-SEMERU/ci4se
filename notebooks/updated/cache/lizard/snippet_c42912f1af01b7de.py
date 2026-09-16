def Flemmer_Banks(Re):
    r
    E = 0.383 * Re ** 0.356 - 0.207 * Re ** 0.396 - 0.143 / (1 + log10(Re) ** 2
        )
    Cd = 24.0 / Re * 10 ** E
    return Cd
def Buzzelli_2008(Re, eD):
    r
    B1 = (0.774 * log(Re) - 1.41) / (1 + 1.32 * eD ** 0.5)
    B2 = eD / 3.7 * Re + 2.51 * B1
    return (B1 - (B1 + 2 * log10(B2 / Re)) / (1 + 2.18 / B2)) ** -2
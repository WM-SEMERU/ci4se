def Nu_cylinder_Perkins_Leppert_1964(Re, Pr, mu=None, muw=None):
    r
    Nu = (0.31 * Re ** 0.5 + 0.11 * Re ** 0.67) * Pr ** 0.4
    if mu and muw:
        Nu *= (mu / muw) ** 0.25
    return Nu
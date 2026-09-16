def Kp_helical_ribbon_Rieger(D, h, nb, pitch, width, T):
    r
    c = 0.5 * (T - D)
    return 82.8 * h / D * (c / D) ** -0.38 * (pitch / D) ** -0.35 * (width / D
        ) ** 0.2 * nb ** 0.78
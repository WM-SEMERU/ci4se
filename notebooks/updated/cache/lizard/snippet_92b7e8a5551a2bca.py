def entrance_distance_45_Miller(Di, Di0):
    r
    t = 0.5 * (Di0 - Di)
    t_Di = t / Di
    if t_Di > 0.3:
        t_Di = 0.3
    return horner(entrance_distance_45_Miller_coeffs, 6.666666666666667 * (
        t_Di - 0.15))
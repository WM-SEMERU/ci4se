def diam_kolmogorov(EnergyDis, Temp, ConcAl, ConcClay, coag, material,
    DIM_FRACTAL):
    return material.Diameter * (eta_kolmogorov(EnergyDis, Temp).magnitude /
        material.Diameter * (6 * frac_vol_floc_initial(ConcAl, ConcClay,
        coag, material) / np.pi) ** (1 / 3)) ** (3 / DIM_FRACTAL)
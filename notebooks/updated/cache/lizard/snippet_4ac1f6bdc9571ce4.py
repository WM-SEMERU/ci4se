def diam_floc_vel_term(ConcAl, ConcClay, coag, material, DIM_FRACTAL,
    VelTerm, Temp):
    WaterDensity = pc.density_water(Temp).magnitude
    return material.Diameter * (18 * VelTerm * PHI_FLOC * pc.
        viscosity_kinematic(Temp).magnitude / (pc.gravity.magnitude * 
        material.Diameter ** 2) * (WaterDensity / (dens_floc_init(ConcAl,
        ConcClay, coag, material).magnitude - WaterDensity))) ** (1 / (
        DIM_FRACTAL - 1))
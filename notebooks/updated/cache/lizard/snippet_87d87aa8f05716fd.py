def dens_floc_init(ConcAluminum, ConcClay, coag, material):
    return conc_floc(ConcAluminum, ConcClay, coag
        ).magnitude / frac_vol_floc_initial(ConcAluminum, ConcClay, coag,
        material)
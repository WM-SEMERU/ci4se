def occipital_flatmap(cortex, radius=None):
    mdl = retinotopy_model('benson17', hemi=cortex.chirality)
    mp = mdl.map_projection
    if radius is not None:
        mp = mp.copy(radius=radius)
    return mp(cortex)
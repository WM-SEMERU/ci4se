def affine_initializer(fixed_image, moving_image, search_factor=20,
    radian_fraction=0.1, use_principal_axis=False, local_search_iterations=
    10, mask=None, txfn=None):
    if txfn is None:
        txfn = mktemp(suffix='.mat')
    veccer = [fixed_image.dimension, fixed_image, moving_image, txfn,
        search_factor, radian_fraction, int(use_principal_axis),
        local_search_iterations]
    if mask is not None:
        veccer.append(mask)
    xxx = utils._int_antsProcessArguments(veccer)
    libfn = utils.get_lib_fn('antsAffineInitializer')
    retval = libfn(xxx)
    if retval != 0:
        warnings.warn('ERROR: Non-zero exit status!')
    return txfn
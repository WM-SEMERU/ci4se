def error_perturbation(C, S):
    r
    if len(S.shape) == 2:
        return error_perturbation_single(C, S)
    elif len(S.shape) == 3:
        return error_perturbation_cov(C, S)
    else:
        raise ValueError('Sensitivity matrix S has to be a 2d or 3d array')
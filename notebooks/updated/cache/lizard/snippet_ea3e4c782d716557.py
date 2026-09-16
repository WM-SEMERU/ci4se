def _calc_covar_matrix(self, profile):
    corr = self._calc_corr(profile)
    std = self._calc_ln_std(profile)
    std *= randnorm.scale
    var = std ** 2
    covar = corr * std[:-1] * std[1:]
    mat = diags([covar, var, covar], [-1, 0, 1]).toarray()
    return mat
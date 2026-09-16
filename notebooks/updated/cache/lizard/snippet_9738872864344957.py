def convenience_calc_fisher_approx(self, params):
    placeholder_bhhh = np.diag(-1 * np.ones(params.shape[0]))
    return placeholder_bhhh
def minimize_sigmas(sigmas, weights, combs):

    def make_quality_function(sigmas, weights, combs):

        def quality_function(s):
            sq_sum = 0
            for sigma, comb, weight in zip(sigmas, combs, weights):
                sigma_sqsum = np.sqrt(s[comb[1]] ** 2 + s[comb[0]] ** 2)
                sq_sum += ((sigma - sigma_sqsum) * weight) ** 2
            return sq_sum
        return quality_function
    qfunc = make_quality_function(sigmas, weights, combs)
    s = np.ones(31) * 2.5
    bounds = [(0.0, 5.0)] * 31
    opt_sigmas = optimize.minimize(qfunc, s, bounds=bounds)
    return opt_sigmas
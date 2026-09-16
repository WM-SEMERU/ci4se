def power_under_cph(n_exp, n_con, p_exp, p_con, postulated_hazard_ratio,
    alpha=0.05):

    def z(p):
        return stats.norm.ppf(p)
    m = n_exp * p_exp + n_con * p_con
    k = float(n_exp) / float(n_con)
    return stats.norm.cdf(np.sqrt(k * m) * abs(postulated_hazard_ratio - 1) /
        (k * postulated_hazard_ratio + 1) - z(1 - alpha / 2.0))
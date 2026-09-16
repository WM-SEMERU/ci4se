def get_mean_DRAT(sum_ptrm_checks, sum_abs_ptrm_checks, n_pTRM, L):
    if not n_pTRM:
        return float('nan'), float('nan')
    mean_DRAT = old_div(1.0, n_pTRM) * old_div(sum_ptrm_checks, L) * 100
    mean_DRAT_prime = old_div(1.0, n_pTRM) * old_div(sum_abs_ptrm_checks, L
        ) * 100
    return mean_DRAT, mean_DRAT_prime
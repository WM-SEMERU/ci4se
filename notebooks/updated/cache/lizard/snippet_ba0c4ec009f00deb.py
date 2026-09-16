def crossvalidation_stats(errors1, errors2):
    import numpy as np
    import scipy.stats
    import warnings
    K = errors1.shape[0]
    if K < 30:
        warnings.warn(
            'The number of blocks is K<30 what is insufficient for conducting a t-Test to compare both models! K=40 is suggested.'
            )
    delta = errors1 - errors2
    mu = np.mean(delta)
    se = np.std(delta)
    tscore = mu / se
    pvalue = scipy.stats.t.sf(np.abs(tscore), K - 1) * 2
    return pvalue, tscore, se, mu
def ad_unif_inf(statistic):
    z = statistic
    if z < 2:
        return exp(-1.2337141 / z) / sqrt(z) * (2.00012 + (0.247105 - (
            0.0649821 - (0.0347962 - (0.011672 - 0.00168691 * z) * z) * z) *
            z) * z)
    else:
        return exp(-exp(1.0776 - (2.30695 - (0.43424 - (0.082433 - (
            0.008056 - 0.0003146 * z) * z) * z) * z) * z))
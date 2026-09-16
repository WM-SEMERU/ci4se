def patterson_fst(aca, acb):
    from allel.stats.admixture import patterson_f2, h_hat
    num = patterson_f2(aca, acb)
    den = num + h_hat(aca) + h_hat(acb)
    return num, den
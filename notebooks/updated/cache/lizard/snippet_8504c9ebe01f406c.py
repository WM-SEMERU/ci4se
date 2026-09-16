def overlap1d(l1, l2, PAx, PBx, gamma):
    total = 0
    for i in range(1 + int(floor(0.5 * (l1 + l2)))):
        total += binomial_prefactor(2 * i, l1, l2, PAx, PBx) * fact2(2 * i - 1
            ) / pow(2 * gamma, i)
    return total
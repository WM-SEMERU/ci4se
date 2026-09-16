def q_prior(q, m=1, gamma=0.3, qmin=0.1):
    if q < qmin or q > 1:
        return 0
    C = 1 / (1 / (gamma + 1) * (1 - qmin ** (gamma + 1)))
    return C * q ** gamma
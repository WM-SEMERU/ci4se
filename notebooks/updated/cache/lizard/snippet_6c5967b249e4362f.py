def get_step_f(step_f, lR2, lS2):
    mu, tau = 10, 2
    if lR2 > mu * lS2:
        return step_f * tau
    elif lS2 > mu * lR2:
        return step_f / tau
    return step_f
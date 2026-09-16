def _check_steps(a, b):
    if a.step != 1:
        raise ValueError('a.step must be equal to 1, got: %s' % a.step)
    if b.step != 1:
        raise ValueError('b.step must be equal to 1, got: %s' % b.step)
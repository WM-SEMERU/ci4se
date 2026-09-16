def weights(value):
    probs = probabilities(value)
    if abs(sum(probs) - 1.0) > PRECISION:
        raise ValueError('The weights do not sum up to 1: %s' % probs)
    return probs
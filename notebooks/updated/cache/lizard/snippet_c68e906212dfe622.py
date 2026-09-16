def compute(cls, observation, prediction):
    assert isinstance(observation, dict)
    assert isinstance(prediction, dict)
    p_mean = prediction['mean']
    p_std = prediction['std']
    o_mean = observation['mean']
    o_std = observation['std']
    try:
        p_n = prediction['n']
        o_n = observation['n']
        s = (((p_n - 1) * p_std ** 2 + (o_n - 1) * o_std ** 2) / (p_n + o_n -
            2)) ** 0.5
    except KeyError:
        s = (p_std ** 2 + o_std ** 2) ** 0.5
    value = (p_mean - o_mean) / s
    value = utils.assert_dimensionless(value)
    return CohenDScore(value)
def sample_without_replacement(n, k, num_trials=None, random_state=None):
    if n <= 0:
        raise ValueError('n must be greater than 0')
    if k > n:
        raise ValueError('k must be smaller than or equal to n')
    size = k if num_trials is None else (num_trials, k)
    random_state = check_random_state(random_state)
    r = random_state.random_sample(size=size)
    result = _sample_without_replacement(n, r)
    return result
def rand_int(start=1, end=10, seed=None):
    if seed is not None:
        random.seed(seed)
    return random.randint(start, end)
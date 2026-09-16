def strategize(generator):

    @functools.wraps(generator)
    def strategy_generator(random, args):
        candidate = generator(random, args)
        n = len(candidate)
        candidate.extend([random.random() for _ in range(n)])
        return candidate
    return strategy_generator
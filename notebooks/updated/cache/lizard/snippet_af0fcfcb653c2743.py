def drawUniform(N, bot=0.0, top=1.0, seed=0):
    RNG = np.random.RandomState(seed)
    if isinstance(bot, float) or isinstance(bot, int):
        draws = bot + (top - bot) * RNG.rand(N)
    else:
        draws = []
        for t in range(len(bot)):
            draws.append(bot[t] + (top[t] - bot[t]) * RNG.rand(N))
    return draws
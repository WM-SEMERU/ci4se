def pure_nash_brute_gen(g, tol=None):
    for a in np.ndindex(*g.nums_actions):
        if g.is_nash(a, tol=tol):
            yield a
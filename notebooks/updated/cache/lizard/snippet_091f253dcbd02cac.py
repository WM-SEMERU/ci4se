def random(cls, span=1, seed=None):
    if seed is not None:
        random.seed(seed)

    def rand_vect(min, max):
        return random.uniform(min, max), random.uniform(min, max
            ), random.uniform(min, max)
    while True:
        try:
            return cls(origin=rand_vect(-span, span), xDir=rand_vect(-1, 1),
                normal=rand_vect(-1, 1))
        except RuntimeError:
            continue
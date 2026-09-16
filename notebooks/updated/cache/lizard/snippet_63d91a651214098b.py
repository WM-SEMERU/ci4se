def get_random_number_generator_and_set_seed(seed=None):
    random.seed(seed)
    if seed is None:
        seed = random.randint(0, 2 ** 31 - 1)
    tf.set_random_seed(seed)
    numpy.random.seed(seed)
    return jax_random.get_prng(seed)
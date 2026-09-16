def random_from_alphabet(size, alphabet):
    import random
    return list(random.choice(alphabet) for _ in range(size))
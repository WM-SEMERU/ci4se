def cartesian_t(iterables, repeat):
    return Transformation('cartesian', lambda sequence: product(sequence, *
        iterables, repeat=repeat), None)
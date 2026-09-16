def each_cons(sequence, size):
    return zip(*(islice(it, start, None) for start, it in enumerate(tee(
        sequence, size))))
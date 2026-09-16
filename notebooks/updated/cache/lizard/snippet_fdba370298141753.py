def from_sequence(cls, seq):
    args = tuple(islice(seq, 4))
    if len(args) > 3:
        raise ValueError(
            'When creating a Point from sequence, it must not have more than 3 items.'
            )
    return cls(*args)
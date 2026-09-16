def leq(cls, lits, weights=None, bound=1, top_id=None, encoding=EncType.best):
    return cls._encode(lits, weights, bound, top_id, encoding, comparator='<')
def from_tuples(cls, tups):
    ivs = [Interval(*t) for t in tups]
    return IntervalTree(ivs)
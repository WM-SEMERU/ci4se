def from_versions(cls, versions):
    range = cls(None)
    range.bounds = []
    for version in dedup(sorted(versions)):
        lower = _LowerBound(version, True)
        upper = _UpperBound(version, True)
        bound = _Bound(lower, upper)
        range.bounds.append(bound)
    return range
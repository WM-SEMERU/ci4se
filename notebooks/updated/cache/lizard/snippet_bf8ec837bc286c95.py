def unique_deps(deps):
    deps.sort()
    return list(k for k, _ in itertools.groupby(deps))
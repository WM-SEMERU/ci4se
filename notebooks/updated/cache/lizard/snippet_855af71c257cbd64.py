def regex(self, *patterns, **kwargs):
    start = kwargs.pop('start', 0)
    stop = kwargs.pop('stop', None)
    keys_only = kwargs.pop('keys_only', False)
    flags = kwargs.pop('flags', 0)
    results = {pattern: [] for pattern in patterns}
    stop = stop if stop is not None else -1
    for i, line in enumerate(self[start:stop]):
        for pattern in patterns:
            grps = re.search(pattern, line, flags=flags)
            if grps and keys_only:
                results[pattern].append(i)
            elif grps and grps.groups():
                for group in grps.groups():
                    results[pattern].append((i, group))
            elif grps:
                results[pattern].append((i, line))
    if len(patterns) == 1:
        return results[patterns[0]]
    return results
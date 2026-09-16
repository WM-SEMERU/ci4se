def InterpolateGrouping(self, pattern):
    components = []
    offset = 0
    for match in GROUPING_PATTERN.finditer(pattern):
        components.append([pattern[offset:match.start()]])
        alternatives = match.group(1).split(',')
        components.append(set(alternatives))
        offset = match.end()
    components.append([pattern[offset:]])
    for vector in itertools.product(*components):
        yield ''.join(vector)
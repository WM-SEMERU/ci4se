def build_pattern(body, features):
    line_patterns = apply_features(body, features)
    return reduce(lambda x, y: [(i + j) for i, j in zip(x, y)], line_patterns)
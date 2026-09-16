def grade(adjective, suffix=COMPARATIVE):
    b = predicative(adjective)
    if suffix == SUPERLATIVE and b.endswith(('s', 'ß')):
        suffix = suffix[1:]
    return adjective[:len(b)] + suffix + adjective[len(b):]
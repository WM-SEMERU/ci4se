def fetch(index, tokens):
    if len(tokens) == 0:
        return set()
    return set.intersection(*[set(index.get(token, [])) for token in tokens])
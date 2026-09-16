def _namespace_to_ord(namespace):
    n = 0
    for i, c in enumerate(namespace):
        n += _LEX_DISTANCE[MAX_NAMESPACE_LENGTH - i - 1
            ] * NAMESPACE_CHARACTERS.index(c) + 1
    return n
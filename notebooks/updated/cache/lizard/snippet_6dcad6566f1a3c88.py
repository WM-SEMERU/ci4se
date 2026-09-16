def segment_into_tokens(utterance: str, token_inventory: Iterable[str]):
    if not isinstance(utterance, str):
        raise TypeError('Input type must be a string. Got {}.'.format(type(
            utterance)))
    token_inventory = set(token_inventory)
    max_len = len(sorted(list(token_inventory), key=lambda x: len(x))[-1])

    def segment_token(utterance):
        if utterance == '':
            return '', ''
        for i in range(max_len, 0, -1):
            if utterance[:i] in token_inventory:
                return utterance[:i], utterance[i:]
        return '', utterance[1:]
    tokens = []
    head, tail = segment_token(utterance)
    tokens.append(head)
    while tail != '':
        head, tail = segment_token(tail)
        tokens.append(head)
    tokens = [tok for tok in tokens if tok != '']
    return ' '.join(tokens)
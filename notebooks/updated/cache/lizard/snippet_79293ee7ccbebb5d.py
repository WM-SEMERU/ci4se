def decode(tokens):
    token_is_alnum = [(t[0] in _ALPHANUMERIC_CHAR_SET) for t in tokens]
    ret = []
    for i, token in enumerate(tokens):
        if i > 0 and token_is_alnum[i - 1] and token_is_alnum[i]:
            ret.append(' ')
        ret.append(token)
    return ''.join(ret)
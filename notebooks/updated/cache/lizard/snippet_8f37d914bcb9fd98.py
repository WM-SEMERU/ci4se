def _split_token_to_subtokens(token, subtoken_dict, max_subtoken_length):
    ret = []
    start = 0
    token_len = len(token)
    while start < token_len:
        for end in xrange(min(token_len, start + max_subtoken_length),
            start, -1):
            subtoken = token[start:end]
            if subtoken in subtoken_dict:
                ret.append(subtoken)
                start = end
                break
        else:
            raise ValueError(
                'Was unable to split token "%s" into subtokens.' % token)
    return ret
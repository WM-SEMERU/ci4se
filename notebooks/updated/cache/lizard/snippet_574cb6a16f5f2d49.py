def _auto_positive_symbol(tokens, local_dict, global_dict):
    result = []
    tokens.append((None, None))
    for tok, nextTok in zip(tokens, tokens[1:]):
        tokNum, tokVal = tok
        nextTokNum, nextTokVal = nextTok
        if tokNum == token.NAME:
            name = tokVal
            if name in global_dict:
                obj = global_dict[name]
                if isinstance(obj, (Basic, type)) or callable(obj):
                    result.append((token.NAME, name))
                    continue
            try:
                used_name = inv_name_alternatives[str(name)]
            except KeyError:
                used_name = str(name)
            result.extend([(token.NAME, 'Symbol'), (token.OP, '('), (token.
                NAME, repr(used_name)), (token.OP, ','), (token.NAME,
                'positive'), (token.OP, '='), (token.NAME, 'True'), (token.
                OP, ')')])
        else:
            result.append((tokNum, tokVal))
    return result
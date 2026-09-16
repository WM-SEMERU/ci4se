def obfuscatable_class(tokens, index, **kwargs):
    tok = tokens[index]
    token_type = tok[0]
    token_string = tok[1]
    if index > 0:
        prev_tok = tokens[index - 1]
    else:
        prev_tok = 54, '\n', (1, 1), (1, 2), '#\n'
    prev_tok_string = prev_tok[1]
    if token_type != tokenize.NAME:
        return None
    if token_string.startswith('__'):
        return None
    if prev_tok_string == 'class':
        return token_string
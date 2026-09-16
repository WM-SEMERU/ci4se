def _escape_token(token, alphabet):
    r
    token = token.replace('\\', '\\\\').replace('_', '\\u')
    ret = [(c if c in alphabet and c != '\n' else '\\%d;' % ord(c)) for c in
        token]
    return ''.join(ret) + '_'
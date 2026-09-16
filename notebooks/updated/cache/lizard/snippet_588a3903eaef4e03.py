def _escape_token(token, alphabet):
    if not isinstance(token, six.text_type):
        raise ValueError('Expected string type for token, got %s' % type(token)
            )
    token = token.replace('\\', '\\\\').replace('_', '\\u')
    ret = [(c if c in alphabet and c != '\n' else '\\%d;' % ord(c)) for c in
        token]
    return ''.join(ret) + '_'
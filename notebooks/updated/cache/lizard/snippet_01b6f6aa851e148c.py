def add_charset(charset, header_enc=None, body_enc=None, output_charset=None):
    if body_enc == SHORTEST:
        raise ValueError('SHORTEST not allowed for body_enc')
    CHARSETS[charset] = header_enc, body_enc, output_charset
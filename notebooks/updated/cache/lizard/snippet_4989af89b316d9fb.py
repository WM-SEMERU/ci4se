def encode(char_data, encoding='utf-8'):
    if type(char_data) is unicode:
        return char_data.encode(encoding, 'replace')
    else:
        return char_data
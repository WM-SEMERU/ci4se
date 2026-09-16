def _try_decode_list(content):
    result = list()
    for value in content:
        result.append(try_utf8_decode(value))
    return result
def is_HDN(text):
    if IPV4_RE.search(text):
        return False
    if text == '':
        return False
    if text[0] == '.' or text[-1] == '.':
        return False
    return True
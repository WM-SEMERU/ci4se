def find_end(self, text, start_token, end_token, ignore_end_token=None):
    if not text.startswith(start_token):
        raise MAVParseError('invalid token start')
    offset = len(start_token)
    nesting = 1
    while nesting > 0:
        idx1 = text[offset:].find(start_token)
        idx2 = text[offset:].find(end_token)
        if ignore_end_token:
            combined_token = ignore_end_token + end_token
            if text[offset + idx2:offset + idx2 + len(combined_token)
                ] == combined_token:
                idx2 += len(ignore_end_token)
        if idx1 == -1 and idx2 == -1:
            raise MAVParseError('token nesting error')
        if idx1 == -1 or idx1 > idx2:
            offset += idx2 + len(end_token)
            nesting -= 1
        else:
            offset += idx1 + len(start_token)
            nesting += 1
    return offset
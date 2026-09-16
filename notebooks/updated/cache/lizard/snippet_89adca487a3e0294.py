def _shift(tokens):
    after = tokens.peek(n=1, skip=_is_comment, drop=True)
    tok = tokens._buffer.popleft()
    return tok[0], tok[1], tok[2], after[0]
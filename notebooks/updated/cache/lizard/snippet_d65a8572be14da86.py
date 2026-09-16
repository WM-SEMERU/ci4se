def cycle_find(key, width=4):
    key_len = len(key)
    buf = ''
    it = deBruijn(width, 26)
    for i in range(key_len):
        buf += chr(ord('A') + next(it))
    if buf == key:
        return 0
    for i, c in enumerate(it):
        buf = buf[1:] + chr(ord('A') + c)
        if buf == key:
            return i + 1
    return -1
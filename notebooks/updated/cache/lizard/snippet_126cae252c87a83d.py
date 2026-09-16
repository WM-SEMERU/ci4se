def write_color_old(text, attr=None):
    u
    res = []
    chunks = terminal_escape.split(text)
    n = 0
    if attr is None:
        attr = 15
    for chunk in chunks:
        m = escape_parts.match(chunk)
        if m:
            for part in m.group(1).split(';'):
                if part == '0':
                    attr = 0
                elif part == '7':
                    attr |= 16384
                if part == '1':
                    attr |= 8
                elif len(part) == 2 and '30' <= part <= '37':
                    part = int(part) - 30
                    attr = attr & ~7 | (part & 1) << 2 | part & 2 | (part & 4
                        ) >> 2
                elif len(part) == 2 and '40' <= part <= '47':
                    part = int(part) - 40
                    attr = attr & ~112 | (part & 1) << 6 | (part & 2) << 4 | (
                        part & 4) << 2
            continue
        n += len(chunk)
        if chunk:
            res.append(('0x%x' % attr, chunk))
    return res
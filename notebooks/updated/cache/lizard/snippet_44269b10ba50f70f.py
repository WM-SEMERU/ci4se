def make_palette_chunks(palette):
    p = bytearray()
    t = bytearray()
    for x in palette:
        p.extend(x[0:3])
        if len(x) > 3:
            t.append(x[3])
    if t:
        return p, t
    return p, None
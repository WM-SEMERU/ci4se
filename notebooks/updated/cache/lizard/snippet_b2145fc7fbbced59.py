def chars2gloss(chars):
    out = []
    chars = gbk2big5(chars)
    for char in chars:
        tmp = []
        if char in _cd.TLS:
            for entry in _cd.TLS[char]:
                baxter = _cd.TLS[char][entry]['UNIHAN_GLOSS']
                if baxter != '?':
                    tmp += [baxter]
        out += [','.join(tmp)]
    return out
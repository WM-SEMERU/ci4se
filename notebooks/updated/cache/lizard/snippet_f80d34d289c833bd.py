def __trim_extensions_dot(exts):
    if exts is None:
        return None
    res = []
    for i in range(0, len(exts)):
        if exts[i] == '':
            continue
        res.append(__trim_extension_dot(exts[i]))
    return res
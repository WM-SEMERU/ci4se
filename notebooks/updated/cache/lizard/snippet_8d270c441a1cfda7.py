def mapping_get(uri, mapping):
    ln = localname(uri)
    for k, v in mapping.items():
        if k == uri:
            return v
    for k, v in mapping.items():
        if k == ln:
            return v
    l = list(mapping.items())
    l.sort(key=lambda i: len(i[0]), reverse=True)
    for k, v in l:
        if k[0] == '*' and ln.endswith(k[1:]):
            return v
    raise KeyError(uri)
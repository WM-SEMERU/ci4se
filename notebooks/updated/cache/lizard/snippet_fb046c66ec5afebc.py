def build_sourcemap(sources):
    sourcemap = {}
    for sfile in sources:
        inc = find_includes(sfile)
        sourcemap[sfile] = set(inc)
    return sourcemap
def open_source_package(dr=None):
    if dr is None:
        dr = getcwd()
    for i, e in enumerate(walk_up(dr)):
        intr = set([DEFAULT_METATAB_FILE, LINES_METATAB_FILE,
            IPYNB_METATAB_FILE]) & set(e[2])
        if intr:
            return op(join(e[0], list(intr)[0]))
        if i > 2:
            break
    return None
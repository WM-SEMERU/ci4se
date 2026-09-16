def parse_treebanks(st):
    d = dict()
    for path in get_paths(st):
        set_path(d, path[:-1], path[-1])
    return d
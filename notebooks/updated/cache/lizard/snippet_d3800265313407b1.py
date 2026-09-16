def read_tree_nexus(nexus):
    if not isinstance(nexus, str):
        raise TypeError('nexus must be a str')
    if nexus.lower().endswith('.gz'):
        f = gopen(expanduser(nexus))
    elif isfile(expanduser(nexus)):
        f = open(expanduser(nexus))
    else:
        f = nexus.splitlines()
    trees = dict()
    for line in f:
        if isinstance(line, bytes):
            l = line.decode().strip()
        else:
            l = line.strip()
        if l.lower().startswith('tree '):
            i = l.index('=')
            left = l[:i].strip()
            right = l[i + 1:].strip()
            name = ' '.join(left.split(' ')[1:])
            trees[name] = read_tree_newick(right)
    if hasattr(f, 'close'):
        f.close()
    return trees
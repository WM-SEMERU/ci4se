def getnodes(fnods, up=None, verbose=False):
    f = open(fnods)
    l = [int(x) for x in f.readline().split()]
    npoints, dim, nattrib, nbound = l
    if dim == 2:
        ndapp = [0.0]
    else:
        ndapp = []
    if verbose and up is not None:
        up.init(npoints)
    nodes = []
    for line in f:
        if line[0] == '#':
            continue
        l = [float(x) for x in line.split()]
        l = l[:dim + 1]
        assert_(int(l[0]) == len(nodes) + 1)
        l = l[1:]
        nodes.append(tuple(l + ndapp))
        if verbose and up is not None:
            up.update(len(nodes))
    assert_(npoints == len(nodes))
    return nodes
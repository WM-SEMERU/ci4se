def classes(equivalences):
    node = OrderedDict()

    def N(x):
        if x in node:
            return node[x]
        n = node[x] = Node(x)
        return n
    for x, y in equivalences:
        union(N(x), N(y))
    eqclass = OrderedDict()
    for x, n in node.iteritems():
        x_ = find(n).element
        if x_ not in eqclass:
            eqclass[x_] = []
        eqclass[x_].append(x)
        eqclass[x] = eqclass[x_]
    return eqclass
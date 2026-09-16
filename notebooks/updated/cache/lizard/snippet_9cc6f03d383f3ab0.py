def default_tree_traversal(root, leaves):
    objs = [('#', root)]
    while len(objs) > 0:
        path, obj = objs.pop()
        if obj.__class__ not in leaves:
            objs.extend(map(lambda i: (path + '/' + i[0],) + (i[1],), six.
                iteritems(obj._children_)))
        yield path, obj
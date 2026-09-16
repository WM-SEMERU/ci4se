def _permission_trees(permissions):
    treecache = PermissionTreeCache()
    cached = treecache.get()
    if not cached:
        tree = PermissionTreeBuilder()
        for permission in permissions:
            tree.insert(permission)
        result = tree.serialize()
        treecache.set(result)
        return result
    return cached
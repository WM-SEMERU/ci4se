def parent_resources(cls):
    parent = cls.parent_resource
    parents = [parent]
    try:
        while True:
            parent = parent.parent_resource
            parents.append(parent)
    except AttributeError:
        pass
    parents.reverse()
    return parents
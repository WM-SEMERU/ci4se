def get(cls, parent=None, id=None, data=None):
    if parent is not None:
        route = copy(parent.route)
    else:
        route = {}
    if id is not None and cls.ID_NAME is not None:
        route[cls.ID_NAME] = id
    obj = cls(key=parent.key, route=route, config=parent.config)
    if data:
        obj.data = data
    else:
        obj.fetch()
    return obj
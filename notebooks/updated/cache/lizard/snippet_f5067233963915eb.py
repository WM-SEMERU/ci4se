def get(key, default=-1):
    if isinstance(key, int):
        return Routing(key)
    if key not in Routing._member_map_:
        extend_enum(Routing, key, default)
    return Routing[key]
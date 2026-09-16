def _validate_stone_cfg(self):

    def mk_route_schema():
        s = Struct('Route', ApiNamespace('stone_cfg'), None)
        s.set_attributes(None, [], None)
        return s
    try:
        stone_cfg = self.api.namespaces.pop('stone_cfg')
    except KeyError:
        return mk_route_schema()
    if stone_cfg.routes:
        route = stone_cfg.routes[0]
        raise InvalidSpec(
            'No routes can be defined in the stone_cfg namespace.', route.
            _ast_node.lineno, route._ast_node.path)
    if not stone_cfg.data_types:
        return mk_route_schema()
    for data_type in stone_cfg.data_types:
        if data_type.name != 'Route':
            raise InvalidSpec(
                "Only a struct named 'Route' can be defined in the stone_cfg namespace."
                , data_type._ast_node.lineno, data_type._ast_node.path)
    return data_type
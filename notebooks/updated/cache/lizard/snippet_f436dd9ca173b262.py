def _prepare_routes(self, routes):
    if not isinstance(routes, list):
        raise ValueError('Routes parameter must be a list of tuples')
    prepared_routes = list()
    for parts in routes:
        route = self._prepare_route(parts)
        if route:
            LOGGER.info('Appending handler: %r', route)
            prepared_routes.append(route)
    return prepared_routes
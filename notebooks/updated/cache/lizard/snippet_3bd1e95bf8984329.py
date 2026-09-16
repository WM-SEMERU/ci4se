def add_routes(self, routes):
    if isinstance(routes, bottle.Bottle):
        routes = routes.routes
    for route in routes:
        route.app = self.app
        self.app.add_route(route)
    return self
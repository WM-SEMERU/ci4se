def add_route(self, route):
    self.routes.append(route)
    self.router.add(route.rule, route.method, route, name=route.name)
    if DEBUG:
        route.prepare()
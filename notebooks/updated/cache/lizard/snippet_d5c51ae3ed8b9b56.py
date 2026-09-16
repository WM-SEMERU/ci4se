def cli(self, method):
    routes = getattr(method, '_hug_cli_routes', [])
    routes.append(self.route)
    method._hug_cli_routes = routes
    return method
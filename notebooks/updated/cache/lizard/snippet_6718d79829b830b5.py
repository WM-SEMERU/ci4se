def find_route_by_view_name(self, view_name):
    if not view_name:
        return None, None
    for uri, route in self.routes_all.items():
        if route.name == view_name:
            return uri, route
    return None, None
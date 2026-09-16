def find_route_by_view_name(self, view_name, name=None):
    if not view_name:
        return None, None
    if view_name == 'static' or view_name.endswith('.static'):
        return self.routes_static_files.get(name, (None, None))
    return self.routes_names.get(view_name, (None, None))
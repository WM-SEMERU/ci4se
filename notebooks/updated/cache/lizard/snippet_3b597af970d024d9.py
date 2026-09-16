def get_supported_methods(self, url):
    route = self.routes_all.get(url)
    return getattr(route, 'methods', None) or frozenset()
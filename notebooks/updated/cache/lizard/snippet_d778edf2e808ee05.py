def patch(self, route: str(), callback: object()):
    self.__set_route('patch', {route: callback})
    return RouteMapping
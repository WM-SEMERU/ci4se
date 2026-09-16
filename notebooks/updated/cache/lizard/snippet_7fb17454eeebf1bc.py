def put(self, route: str(), callback: object()):
    self.__set_route('put', {route: callback})
    return RouteMapping
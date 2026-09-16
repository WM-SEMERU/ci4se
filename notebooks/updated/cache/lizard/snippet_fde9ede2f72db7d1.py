def search_rule(self, search):
    return [RouteMapRule(**rule) for rule in self.make_request(resource=
        'search_rule', params={'filter': search})]
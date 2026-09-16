def _load_resources(self):
    for resource in self.RESOURCES:
        if isinstance(resource, goldman.ModelsResource):
            route = '/%s' % resource.rtype
        elif isinstance(resource, goldman.ModelResource):
            route = '/%s/{rid}' % resource.rtype
        elif isinstance(resource, goldman.RelatedResource):
            route = '/%s/{rid}/{related}' % resource.rtype
        else:
            raise TypeError('unsupported resource type')
        self.add_route(*(route, resource))
def add_preflight_handler(self, routing_entity: Union[web.Resource, web.
    StaticResource, web.ResourceRoute], handler):
    if isinstance(routing_entity, web.Resource):
        resource = routing_entity
        if resource in self._resources_with_preflight_handlers:
            return
        for route_obj in resource:
            if route_obj.method == hdrs.METH_OPTIONS:
                if route_obj.handler is handler:
                    return
                else:
                    raise ValueError('{!r} already has OPTIONS handler {!r}'
                        .format(resource, route_obj.handler))
            elif route_obj.method == hdrs.METH_ANY:
                if _is_web_view(route_obj):
                    self._preflight_routes.add(route_obj)
                    self._resources_with_preflight_handlers.add(resource)
                    return
                else:
                    raise ValueError(
                        "{!r} already has a '*' handler for all methods".
                        format(resource))
        preflight_route = resource.add_route(hdrs.METH_OPTIONS, handler)
        self._preflight_routes.add(preflight_route)
        self._resources_with_preflight_handlers.add(resource)
    elif isinstance(routing_entity, web.StaticResource):
        resource = routing_entity
        if resource in self._resources_with_preflight_handlers:
            return
        resource.set_options_route(handler)
        preflight_route = resource._routes[hdrs.METH_OPTIONS]
        self._preflight_routes.add(preflight_route)
        self._resources_with_preflight_handlers.add(resource)
    elif isinstance(routing_entity, web.ResourceRoute):
        route = routing_entity
        if not self.is_cors_for_resource(route.resource):
            self.add_preflight_handler(route.resource, handler)
    else:
        raise ValueError('Resource or ResourceRoute expected, got {!r}'.
            format(routing_entity))
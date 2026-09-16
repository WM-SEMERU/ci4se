def add_static_route(self, gateway, destination, network=None):
    routing_node_gateway = RoutingNodeGateway(gateway, destinations=destination
        )
    return self._add_gateway_node('router', routing_node_gateway, network)
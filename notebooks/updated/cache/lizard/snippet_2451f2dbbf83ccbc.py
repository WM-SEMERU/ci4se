def nodes(self):
    return devicetools.Nodes(self.node_prefix + routers for routers in self
        ._router_numbers) + devicetools.Node(self.last_node)
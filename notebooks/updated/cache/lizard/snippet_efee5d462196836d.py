def distance(self, other, config):
    node_distance = 0.0
    if self.nodes or other.nodes:
        disjoint_nodes = 0
        for k2 in iterkeys(other.nodes):
            if k2 not in self.nodes:
                disjoint_nodes += 1
        for k1, n1 in iteritems(self.nodes):
            n2 = other.nodes.get(k1)
            if n2 is None:
                disjoint_nodes += 1
            else:
                node_distance += n1.distance(n2, config)
        max_nodes = max(len(self.nodes), len(other.nodes))
        node_distance = (node_distance + config.
            compatibility_disjoint_coefficient * disjoint_nodes) / max_nodes
    connection_distance = 0.0
    if self.connections or other.connections:
        disjoint_connections = 0
        for k2 in iterkeys(other.connections):
            if k2 not in self.connections:
                disjoint_connections += 1
        for k1, c1 in iteritems(self.connections):
            c2 = other.connections.get(k1)
            if c2 is None:
                disjoint_connections += 1
            else:
                connection_distance += c1.distance(c2, config)
        max_conn = max(len(self.connections), len(other.connections))
        connection_distance = (connection_distance + config.
            compatibility_disjoint_coefficient * disjoint_connections
            ) / max_conn
    distance = node_distance + connection_distance
    return distance
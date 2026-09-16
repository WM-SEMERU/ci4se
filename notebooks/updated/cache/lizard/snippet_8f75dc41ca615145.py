def rings_full_data(self):
    for circ_breaker in self.circuit_breakers():
        if not circ_breaker.status == 'closed':
            circ_breaker.close()
            logger.info(
                'Circuit breakers were closed in order to find MV rings')
    for ring_nodes in nx.cycle_basis(self._graph, root=self._station):
        edges_ring = []
        for node in ring_nodes:
            for edge in self.graph_branches_from_node(node):
                nodes_in_the_branch = self.graph_nodes_from_branch(edge[1][
                    'branch'])
                if nodes_in_the_branch[0
                    ] in ring_nodes and nodes_in_the_branch[1] in ring_nodes:
                    if not edge[1]['branch'] in edges_ring:
                        edges_ring.append(edge[1]['branch'])
        yield edges_ring[0].ring, edges_ring, ring_nodes
def remove_node(self, node):
    affected_nodes = [v for u, v in self.edges() if u == node]
    for affected_node in affected_nodes:
        node_cpd = self.get_cpds(node=affected_node)
        if node_cpd:
            node_cpd.marginalize([node], inplace=True)
    if self.get_cpds(node=node):
        self.remove_cpds(node)
    super(BayesianModel, self).remove_node(node)
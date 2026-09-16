def add_node(self, node, node_data=None):
    if node in self.hidden_nodes:
        return
    if node not in self.nodes:
        self.nodes[node] = [], [], node_data
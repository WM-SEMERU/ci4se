def _add_node(self, node):
    node_id = len(self.node_list)
    self.node_to_id[node] = node_id
    self.node_list.append(node)
    self.adj_list[node_id] = []
    self.reverse_adj_list[node_id] = []
    return node_id
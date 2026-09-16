def add_edge(self, from_node, to_node):
    if to_node not in self.nodes:
        self.add_node(to_node)
    try:
        self.nodes[from_node]['sons'].append(to_node)
    except KeyError:
        self.nodes[from_node] = {'dfs_loop_status': '', 'sons': [to_node]}
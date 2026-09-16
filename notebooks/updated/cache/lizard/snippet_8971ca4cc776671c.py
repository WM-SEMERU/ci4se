def loop_check(self):
    in_loop = []
    for node in list(self.nodes.values()):
        node['dfs_loop_status'] = 'DFS_UNCHECKED'
    for node_id, node in self.nodes.items():
        if node['dfs_loop_status'] == 'DFS_UNCHECKED':
            self.dfs_loop_search(node_id)
        if node['dfs_loop_status'] == 'DFS_LOOP_INSIDE':
            in_loop.append(node_id)
    for node in list(self.nodes.values()):
        del node['dfs_loop_status']
    return in_loop
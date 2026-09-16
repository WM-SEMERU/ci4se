def __sort_adjacency_lists(dfs_data):
    new_adjacency_lists = {}
    adjacency_lists = dfs_data['adj']
    edge_weights = dfs_data['edge_weights']
    edge_lookup = dfs_data['edge_lookup']
    for node_id, adj_list in list(adjacency_lists.items()):
        node_weight_lookup = {}
        frond_lookup = {}
        for node_b in adj_list:
            edge_id = dfs_data['graph'].get_first_edge_id_by_node_ids(node_id,
                node_b)
            node_weight_lookup[node_b] = edge_weights[edge_id]
            frond_lookup[node_b] = 1 if edge_lookup[edge_id
                ] == 'backedge' else 2
        new_list = sorted(adj_list, key=lambda n: frond_lookup[n])
        new_list.sort(key=lambda n: node_weight_lookup[n])
        new_adjacency_lists[node_id] = new_list
    return new_adjacency_lists
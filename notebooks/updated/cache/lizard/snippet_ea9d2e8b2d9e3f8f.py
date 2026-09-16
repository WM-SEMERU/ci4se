def is_frond(u, v, dfs_data):
    d_u = D(u, dfs_data)
    d_v = D(v, dfs_data)
    edge_id = dfs_data['graph'].get_first_edge_id_by_node_ids(u, v)
    return True if dfs_data['edge_lookup'][edge_id
        ] == 'backedge' and d_v < d_u else False
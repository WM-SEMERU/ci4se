def update_nodes(nodes, **kwargs):
    user_id = kwargs.get('user_id')
    updated_nodes = []
    for n in nodes:
        updated_node_i = update_node(n, flush=False, user_id=user_id)
        updated_nodes.append(updated_node_i)
    db.DBSession.flush()
    return updated_nodes
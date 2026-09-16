async def create_link(project, nodes):
    node1 = random.choice(list(nodes.values()))
    for port in range(0, 8):
        node2 = random.choice(list(nodes.values()))
        if node1 == node2:
            continue
        data = {'nodes': [{'adapter_number': 0, 'node_id': node1['node_id'],
            'port_number': port}, {'adapter_number': 0, 'node_id': node2[
            'node_id'], 'port_number': port}]}
        try:
            await post('/projects/{}/links'.format(project['project_id']),
                body=data)
        except (HTTPConflict, HTTPNotFound):
            pass
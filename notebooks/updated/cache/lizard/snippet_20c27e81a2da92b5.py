def update_labels(self, node_name: str, labels: dict):
    if not self._manager:
        raise RuntimeError(
            'Only the Swarm manager node can update node details.')
    node_spec = {'Availability': 'active', 'Name': node_name, 'Role':
        'manager', 'Labels': labels}
    node = self._client.nodes.get(node_name)
    node.update(node_spec)
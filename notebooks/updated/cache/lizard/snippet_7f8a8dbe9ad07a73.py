def close_node(self, node_id, *args, **kwargs):
    node = self.get_node(node_id)
    if node_id in self._used_mac_ids:
        i = self._used_mac_ids[node_id]
        self._free_mac_ids[node.project.id].insert(0, i)
        del self._used_mac_ids[node_id]
    yield from super().close_node(node_id, *args, **kwargs)
    return node
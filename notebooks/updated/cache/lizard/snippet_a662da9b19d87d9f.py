def remove_hyperedge(self, hyperedge_id):
    if not self.has_hyperedge_id(hyperedge_id):
        raise ValueError('No such hyperedge exists.')
    frozen_nodes = self._hyperedge_attributes[hyperedge_id]['__frozen_nodes']
    for node in frozen_nodes:
        self._star[node].remove(hyperedge_id)
    del self._node_set_to_hyperedge[frozen_nodes]
    del self._hyperedge_attributes[hyperedge_id]
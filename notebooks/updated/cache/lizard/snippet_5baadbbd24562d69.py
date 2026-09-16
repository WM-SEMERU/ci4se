def _node_add_without_peer_container(self, node_sum, child_other):
    e = deepcopy(child_other)
    node_sum.append(self._del_attrib(e))
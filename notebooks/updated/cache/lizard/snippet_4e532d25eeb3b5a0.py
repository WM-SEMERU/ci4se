def get_parent_log_nodes(self):
    parent_log_nodes = []
    for node in self._my_map['parentNodes']:
        parent_log_nodes.append(LogNode(node._my_map, runtime=self._runtime,
            proxy=self._proxy, lookup_session=self._lookup_session))
    return LogNodeList(parent_log_nodes)
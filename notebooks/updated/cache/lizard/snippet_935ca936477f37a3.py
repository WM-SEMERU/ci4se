def router_add(self, cluster_id, params):
    cluster = self._storage[cluster_id]
    result = cluster.router_add(params)
    self._storage[cluster_id] = cluster
    return result
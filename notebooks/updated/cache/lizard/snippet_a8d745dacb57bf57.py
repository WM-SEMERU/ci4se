def router_del(self, cluster_id, router_id):
    cluster = self._storage[cluster_id]
    result = cluster.router_remove(router_id)
    self._storage[cluster_id] = cluster
    return result
def member_info(self, cluster_id, member_id):
    cluster = self._storage[cluster_id]
    return cluster.member_info(member_id)
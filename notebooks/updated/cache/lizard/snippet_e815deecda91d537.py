def get_replicas(self, keyspace, token):
    tokens_to_hosts = self.tokens_to_hosts_by_ks.get(keyspace, None)
    if tokens_to_hosts is None:
        self.rebuild_keyspace(keyspace, build_if_absent=True)
        tokens_to_hosts = self.tokens_to_hosts_by_ks.get(keyspace, None)
    if tokens_to_hosts:
        point = bisect_left(self.ring, token)
        if point == len(self.ring):
            return tokens_to_hosts[self.ring[0]]
        else:
            return tokens_to_hosts[self.ring[point]]
    return []
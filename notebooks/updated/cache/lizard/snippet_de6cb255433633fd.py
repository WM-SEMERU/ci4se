def get_friends(self, limit=50, cacheable=False):
    seq = []
    for node in _collect_nodes(limit, self, self.ws_prefix + '.getFriends',
        cacheable):
        seq.append(User(_extract(node, 'name'), self.network))
    return seq
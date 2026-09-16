def get_nodes(self, jid, node=None):
    response = yield from self._disco.query_items(jid, node=node)
    result = []
    for item in response.items:
        if item.jid != jid:
            continue
        result.append((item.node, item.name))
    return result
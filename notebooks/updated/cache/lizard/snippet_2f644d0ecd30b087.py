def get_peer_resources(self, peer_jid):
    try:
        d = dict(self._presences[peer_jid])
        d.pop(None, None)
        return d
    except KeyError:
        return {}
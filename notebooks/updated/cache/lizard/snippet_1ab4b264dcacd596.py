def get_stanza(self, peer_jid):
    try:
        return self._presences[peer_jid.bare()][peer_jid.resource]
    except KeyError:
        pass
    try:
        return self._presences[peer_jid.bare()][None]
    except KeyError:
        pass
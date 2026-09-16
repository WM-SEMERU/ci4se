def register(self, peer):
    assert isinstance(peer, beans.Peer)
    with self.__lock:
        peer_id = peer.peer_id
        if peer_id in self.peers:
            raise KeyError('Already known peer: {0}'.format(peer))
        self.peers[peer_id] = peer
        for name in peer.groups:
            self.groups.setdefault(name, set()).add(peer_id)
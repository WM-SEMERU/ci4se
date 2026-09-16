def update_new_peers(self, num_new_peers, current_peers, peer_queue=None,
    peer_table=None, con=None, path=None):
    if path is None:
        path = self.atlasdb_path
    peer_queue = atlas_peer_dequeue_all(peer_queue=peer_queue)
    new_peers = self.canonical_new_peer_list(peer_queue)
    if len(new_peers) > 0:
        log.debug('Add at most %s new peers out of %s options' % (
            num_new_peers, len(new_peers)))
    added, present, filtered = self.add_new_peers(num_new_peers, new_peers,
        current_peers, con=con, path=path, peer_table=peer_table)
    for peer in filtered:
        if peer in new_peers:
            new_peers.remove(peer)
    new_peers = self.canonical_new_peer_list(added)
    max_new_peers = atlas_max_new_peers(self.max_neighbors)
    if len(new_peers) > max_new_peers:
        new_peers = new_peers[:max_new_peers]
    self.new_peers = new_peers
    return len(added)
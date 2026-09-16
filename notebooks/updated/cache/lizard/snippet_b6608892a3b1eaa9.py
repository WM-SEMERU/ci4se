def update_existing_peers(self, num_to_remove, peer_table=None, con=None,
    path=None):
    if path is None:
        path = self.atlasdb_path
    if self.last_clean_time + atlas_peer_clean_interval() < time_now():
        log.debug('%s: revalidate old peers' % self.my_hostport)
        atlas_revalidate_peers(con=con, path=path, peer_table=peer_table)
        self.last_clean_time = time_now()
    removed = self.remove_unhealthy_peers(num_to_remove, con=con, path=path,
        peer_table=peer_table)
    for peer in removed:
        if peer in self.new_peers:
            self.new_peers.remove(peer)
    return len(removed)
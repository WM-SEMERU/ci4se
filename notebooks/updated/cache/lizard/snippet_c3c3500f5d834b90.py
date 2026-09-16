def show_bgp_peer(self, peer_id, **_params):
    return self.get(self.bgp_peer_path % peer_id, params=_params)
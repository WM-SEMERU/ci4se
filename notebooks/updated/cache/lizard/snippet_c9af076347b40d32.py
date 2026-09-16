def remove_peer_from_bgp_speaker(self, speaker_id, body=None):
    return self.put(self.bgp_speaker_path % speaker_id + '/remove_bgp_peer',
        body=body)
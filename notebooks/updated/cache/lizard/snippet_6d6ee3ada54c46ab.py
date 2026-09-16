def list_dragents_hosting_bgp_speaker(self, bgp_speaker, **_params):
    return self.get((self.bgp_speaker_path + self.BGP_DRAGENTS) %
        bgp_speaker, params=_params)
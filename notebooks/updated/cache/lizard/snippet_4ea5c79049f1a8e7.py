def add_bgp_speaker_to_dragent(self, bgp_dragent, body):
    return self.post((self.agent_path + self.BGP_DRINSTANCES) % bgp_dragent,
        body=body)
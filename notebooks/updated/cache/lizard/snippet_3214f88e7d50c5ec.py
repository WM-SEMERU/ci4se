def export_to_json(self):
    return {hostname: sorted(self._encode_key(key) for key in pins) for 
        hostname, pins in self._storage.items()}
def import_from_json(self, data, *, override=False):
    if override:
        self._storage = {hostname: set(self._decode_key(key) for key in
            pins) for hostname, pins in data.items()}
        return
    for hostname, pins in data.items():
        existing_pins = self._storage.setdefault(hostname, set())
        existing_pins.update(self._decode_key(key) for key in pins)
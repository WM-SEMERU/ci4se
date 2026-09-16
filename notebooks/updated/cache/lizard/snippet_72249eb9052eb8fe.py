def switch(self, device_id, obj_slot_id):
    payload = {'device-context': self._build_payload(device_id, obj_slot_id)}
    return self._post(self.url_prefix, payload)
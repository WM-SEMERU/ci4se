def _send_update(self, data):
    if isinstance(data, dict):
        data = json.dumps(data)
    self.update_callback(data)
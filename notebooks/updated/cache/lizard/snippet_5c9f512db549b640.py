def upload_keys(self, device_keys=None, one_time_keys=None):
    content = {}
    if device_keys:
        content['device_keys'] = device_keys
    if one_time_keys:
        content['one_time_keys'] = one_time_keys
    return self._send('POST', '/keys/upload', content=content)
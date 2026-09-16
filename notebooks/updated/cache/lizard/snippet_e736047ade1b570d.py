def _on_scan(self, info):
    device_id = info['uuid']
    expiration_time = info.get('validity_period', 60)
    infocopy = deepcopy(info)
    infocopy['expiration_time'] = monotonic() + expiration_time
    with self._scan_lock:
        self._scanned_devices[device_id] = infocopy
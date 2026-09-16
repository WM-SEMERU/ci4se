def update_device(self, device_id, **kwargs):
    api = self._get_api(device_directory.DefaultApi)
    device = Device._create_request_map(kwargs)
    body = DeviceDataPostRequest(**device)
    return Device(api.device_update(device_id, body))
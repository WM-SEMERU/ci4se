def add_device(self, **kwargs):
    api = self._get_api(device_directory.DefaultApi)
    device = Device._create_request_map(kwargs)
    device = DeviceData(**device)
    return Device(api.device_create(device))
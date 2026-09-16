def get_status(self, device_id):
    devices = self.get_devices()
    if devices != False:
        for device in devices:
            if device['door'] == device_id:
                return device['status']
    return False
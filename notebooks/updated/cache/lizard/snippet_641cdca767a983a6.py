def update(self, data):
    if data is None:
        for device in self.devices:
            device.clear_info()
    else:
        for device, device_info in zip(self.devices, data):
            device.device_info = device_info
            self.connection.log('Device information updated -> [{}]'.format
                (device))
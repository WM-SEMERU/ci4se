def get_devices(self):
    devices = []
    for element in self.get_device_elements():
        device = FritzhomeDevice(self, node=element)
        devices.append(device)
    return devices
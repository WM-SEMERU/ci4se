def list_contents(self):
    target = DeviceTarget(self.device_id)
    return self._fssapi.list_files(target, self.path)[self.device_id]
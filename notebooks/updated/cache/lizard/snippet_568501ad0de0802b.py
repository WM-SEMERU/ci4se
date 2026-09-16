def _add_device_to_device_group(self, device):
    device_name = get_device_info(device).name
    dg = pollster(self._get_device_group)(device)
    dg.devices_s.devices.create(name=device_name, partition=self.partition)
    pollster(self._check_device_exists_in_device_group)(device_name)
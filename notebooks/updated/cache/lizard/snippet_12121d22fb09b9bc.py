def get_server_capabilities(self):
    capabilities = self._call_method('get_server_capabilities')
    if 'Gen10' not in self.model:
        major_minor = self._call_method(
            'get_ilo_firmware_version_as_major_minor')
        nic_capacity = ipmi.get_nic_capacity(self.ipmi_host_info, major_minor)
        if nic_capacity:
            capabilities.update({'nic_capacity': nic_capacity})
    if capabilities:
        return capabilities
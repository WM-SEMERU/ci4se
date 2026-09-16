def _drives_list(self):
    drives_list = []
    for member in self.drives:
        drives_list.append(sys_drives.Drive(self._conn, member.get(
            '@odata.id'), self.redfish_version))
    return drives_list
def pending_settings(self):
    return BIOSPendingSettings(self._conn, utils.get_subresource_path_by(
        self, ['@Redfish.Settings', 'SettingsObject']), redfish_version=
        self.redfish_version)
def device_unlocked(self, device):
    if not self._mounter.is_handleable(device):
        return
    self._show_notification('device_unlocked', _('Device unlocked'), _(
        '{0.device_presentation} unlocked', device), device.icon_name)
def device_locked(self, device):
    if not self._mounter.is_handleable(device):
        return
    self._show_notification('device_locked', _('Device locked'), _(
        '{0.device_presentation} locked', device), device.icon_name)
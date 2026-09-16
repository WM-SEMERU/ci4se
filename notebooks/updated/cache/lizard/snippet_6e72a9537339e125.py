async def terminal(self, device):
    device = self._find_device(device)
    if not device.is_mounted:
        self._log.error(_('not opening terminal {0}: not mounted', device))
        return False
    if not self._terminal:
        self._log.error(_('not opening terminal {0}: no program', device))
        return False
    self._log.debug(_('opening {0} on {0.mount_paths[0]}', device))
    self._terminal(device.mount_paths[0])
    self._log.info(_('opened {0} on {0.mount_paths[0]}', device))
    return True
def Reboot(self, target_mode=b'', timeout_ms=None):
    return self._SimpleCommand(b'reboot', arg=target_mode or None,
        timeout_ms=timeout_ms)
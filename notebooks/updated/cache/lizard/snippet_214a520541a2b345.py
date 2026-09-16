def read_channel(self):
    output = ''
    self._lock_netmiko_session()
    try:
        output = self._read_channel()
    finally:
        self._unlock_netmiko_session()
    return output
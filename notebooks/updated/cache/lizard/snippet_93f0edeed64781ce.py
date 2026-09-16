def connect(self, timeout=None, key=None):
    if self.port is not None:
        return
    self._wait_for_device(timeout)
    self._setup_port_forwarding()
    self._purge_known_hosts_entry()
    self._copy_ssh_key(key)
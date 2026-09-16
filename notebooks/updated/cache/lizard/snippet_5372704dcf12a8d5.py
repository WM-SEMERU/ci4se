def port_manager(self):
    if self._port_manager is None:
        self._port_manager = PortManager.instance()
    return self._port_manager
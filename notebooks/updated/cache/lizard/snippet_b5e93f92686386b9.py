def ConnectDevice(self, port_path=None, serial=None, default_timeout_ms=
    None, chunk_kb=1024, **kwargs):
    if 'handle' in kwargs:
        self._handle = kwargs['handle']
    else:
        self._handle = common.UsbHandle.FindAndOpen(DeviceIsAvailable,
            port_path=port_path, serial=serial, timeout_ms=default_timeout_ms)
    self._protocol = FastbootProtocol(self._handle, chunk_kb)
    return self
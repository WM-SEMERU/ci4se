def PortPathMatcher(cls, port_path):
    if isinstance(port_path, str):
        port_path = [int(part) for part in SYSFS_PORT_SPLIT_RE.split(port_path)
            ]
    return lambda device: device.port_path == port_path
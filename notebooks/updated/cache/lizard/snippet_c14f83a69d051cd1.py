def available_ports(self):
    from mbuild.port import Port
    return [port for port in self.labels.values() if isinstance(port, Port) and
        not port.used]
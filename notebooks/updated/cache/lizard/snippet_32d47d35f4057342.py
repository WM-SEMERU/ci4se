def pair(self):
    if self.ip is NotSpecified:
        if self.ip is NotSpecified:
            second = self.host_port
        else:
            second = self.ip,
    else:
        second = self.ip, self.host_port
    return self.container_port.port_str, second
def get(self, interface_id, interface_ip=None):
    interfaces = []
    for interface in iter(self):
        if interface.interface_id == str(interface_id):
            if interface_ip:
                if interface.interface_ip == interface_ip:
                    return interface
            else:
                interfaces.append(interface)
    return interfaces
def find_host_network_interfaces_of_type(self, type_p):
    if not isinstance(type_p, HostNetworkInterfaceType):
        raise TypeError(
            'type_p can only be an instance of type HostNetworkInterfaceType')
    network_interfaces = self._call('findHostNetworkInterfacesOfType', in_p
        =[type_p])
    network_interfaces = [IHostNetworkInterface(a) for a in network_interfaces]
    return network_interfaces
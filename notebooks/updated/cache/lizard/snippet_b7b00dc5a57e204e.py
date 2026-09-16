def find_host_network_interface_by_name(self, name):
    if not isinstance(name, basestring):
        raise TypeError('name can only be an instance of type basestring')
    network_interface = self._call('findHostNetworkInterfaceByName', in_p=[
        name])
    network_interface = IHostNetworkInterface(network_interface)
    return network_interface
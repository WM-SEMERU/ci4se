def EnumerateInterfacesFromClient(args):
    del args
    pythoncom.CoInitialize()
    for interface in (wmi.WMI().Win32_NetworkAdapterConfiguration() or []):
        addresses = []
        for ip_address in (interface.IPAddress or []):
            addresses.append(rdf_client_network.NetworkAddress(
                human_readable_address=ip_address))
        response = rdf_client_network.Interface(ifname=interface.Description)
        if interface.MACAddress:
            response.mac_address = binascii.unhexlify(interface.MACAddress.
                replace(':', ''))
        if addresses:
            response.addresses = addresses
        yield response
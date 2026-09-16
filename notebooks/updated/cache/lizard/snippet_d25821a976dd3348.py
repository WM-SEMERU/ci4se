def create_nic(client, target, nic):
    for network in target.network:
        if network.name == nic['network_name']:
            net = network
            break
    else:
        return None
    backing = client.create('VirtualEthernetCardNetworkBackingInfo')
    backing.deviceName = nic['network_name']
    backing.network = net
    connect_info = client.create('VirtualDeviceConnectInfo')
    connect_info.allowGuestControl = True
    connect_info.connected = False
    connect_info.startConnected = True
    new_nic = client.create(nic['type'])
    new_nic.backing = backing
    new_nic.key = 2
    new_nic.unitNumber = 1
    new_nic.addressType = 'generated'
    new_nic.connectable = connect_info
    nic_spec = client.create('VirtualDeviceConfigSpec')
    nic_spec.device = new_nic
    nic_spec.fileOperation = None
    operation = client.create('VirtualDeviceConfigSpecOperation')
    nic_spec.operation = operation.add
    return nic_spec
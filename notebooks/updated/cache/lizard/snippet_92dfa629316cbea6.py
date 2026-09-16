def url_generator(network=None, path=''):
    network_object = ipaddress.ip_network(network)
    if network_object.num_addresses > 256:
        logger.error('Scan limited to 256 addresses, requested %d.',
            network_object.num_addresses)
        raise NotImplementedError
    elif network_object.num_addresses > 1:
        network_hosts = network_object.hosts()
    else:
        network_hosts = [network_object.network_address]
    return (urlunsplit(('http', str(ip), path, '', '')) for ip in network_hosts
        )
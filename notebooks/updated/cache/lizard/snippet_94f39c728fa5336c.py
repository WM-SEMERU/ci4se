def get_net_start(ipaddr, netmask):
    net = ipaddress.ip_network('{0}/{1}'.format(ipaddr, netmask), strict=False)
    return six.text_type(net.network_address)
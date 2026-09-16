def random_ipv4(cidr='10.0.0.0/8'):
    try:
        u_cidr = unicode(cidr)
    except NameError:
        u_cidr = cidr
    network = ipaddress.ip_network(u_cidr)
    start = int(network.network_address) + 1
    end = int(network.broadcast_address)
    randint = random.randrange(start, end)
    return ipaddress.ip_address(randint)
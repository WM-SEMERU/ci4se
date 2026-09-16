def valid_hosts(hosts):
    if _empty.match(hosts):
        return False
    for host in hosts.split(','):
        if not valid_host_with_port(host):
            return False
    return True
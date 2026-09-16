def remote_ip(local_ip):
    local_ip = ip2int(local_ip)
    network = local_ip & pfxlen2mask_int(30)
    return int2ip(network + 3 - (local_ip - network))
def add_port_fwd(zone, src, dest, proto='tcp', dstaddr='', permanent=True):
    cmd = (
        '--zone={0} --add-forward-port=port={1}:proto={2}:toport={3}:toaddr={4}'
        .format(zone, src, proto, dest, dstaddr))
    if permanent:
        cmd += ' --permanent'
    return __firewall_cmd(cmd)
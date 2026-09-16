def add_port(zone, port, permanent=True):
    cmd = '--zone={0} --add-port={1}'.format(zone, port)
    if permanent:
        cmd += ' --permanent'
    return __firewall_cmd(cmd)
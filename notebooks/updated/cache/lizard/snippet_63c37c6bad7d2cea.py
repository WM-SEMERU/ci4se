def remove_service(service, zone=None, permanent=True):
    if zone:
        cmd = '--zone={0} --remove-service={1}'.format(zone, service)
    else:
        cmd = '--remove-service={0}'.format(service)
    if permanent:
        cmd += ' --permanent'
    return __firewall_cmd(cmd)
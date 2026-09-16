def list_zones(permanent=True):
    zones = {}
    cmd = '--list-all-zones'
    if permanent:
        cmd += ' --permanent'
    for i in __firewall_cmd(cmd).splitlines():
        if i.strip():
            if bool(re.match('^[a-z0-9]', i, re.I)):
                zone_name = i.rstrip()
            else:
                id_, val = i.strip().split(':')
                if zones.get(zone_name, None):
                    zones[zone_name].update({id_: val})
                else:
                    zones[zone_name] = {id_: val}
    return zones
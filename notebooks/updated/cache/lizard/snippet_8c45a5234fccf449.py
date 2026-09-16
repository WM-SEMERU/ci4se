def delete_zone(zone, restart=True):
    out = __mgmt(zone, 'zone', 'delete')
    if restart:
        if out == 'success':
            return __firewall_cmd('--reload')
    return out
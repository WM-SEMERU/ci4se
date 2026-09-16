def get_masquerade(zone=None, permanent=True):
    zone_info = list_all(zone, permanent)
    if 'no' in [zone_info[i]['masquerade'][0] for i in zone_info]:
        return False
    return True
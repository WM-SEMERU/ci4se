def avail_locations(call=None):
    if call == 'action':
        raise SaltCloudSystemExit(
            'The avail_images function must be called with -f or --function, or with the --list-locations option'
            )
    ret = {}
    conn = get_conn()
    for item in conn.list_locations()['items']:
        reg, loc = item['id'].split('/')
        location = {'id': item['id']}
        if reg not in ret:
            ret[reg] = {}
        ret[reg][loc] = location
    return ret
def list(gandi, state, id, vhosts, type, limit):
    options = {'items_per_page': limit}
    if state:
        options['state'] = state
    output_keys = ['name', 'state']
    if id:
        output_keys.append('id')
    if vhosts:
        output_keys.append('vhost')
    if type:
        output_keys.append('type')
    paas_hosts = {}
    result = gandi.paas.list(options)
    for num, paas in enumerate(result):
        paas_hosts[paas['id']] = []
        if vhosts:
            list_vhost = gandi.vhost.list({'paas_id': paas['id']})
            for host in list_vhost:
                paas_hosts[paas['id']].append(host['name'])
        if num:
            gandi.separator_line()
        output_paas(gandi, paas, [], paas_hosts[paas['id']], output_keys)
    return result
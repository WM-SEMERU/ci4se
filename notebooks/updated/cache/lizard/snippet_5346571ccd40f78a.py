def get(method, hmc, uri, uri_parms, logon_required):
    query_str = uri_parms[0]
    filter_args = parse_query_parms(method, uri, query_str)
    result_storage_groups = []
    for sg in hmc.consoles.console.storage_groups.list(filter_args):
        result_sg = {}
        for prop in sg.properties:
            if prop in ('object-uri', 'cpc-uri', 'name', 'status',
                'fulfillment-state', 'type'):
                result_sg[prop] = sg.properties[prop]
        result_storage_groups.append(result_sg)
    return {'storage-groups': result_storage_groups}
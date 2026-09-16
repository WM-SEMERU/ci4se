def get(method, hmc, uri, uri_parms, logon_required):
    query_str = uri_parms[0]
    try:
        console = hmc.consoles.lookup_by_oid(None)
    except KeyError:
        raise InvalidResourceError(method, uri)
    result_ucpcs = []
    filter_args = parse_query_parms(method, uri, query_str)
    for ucpc in console.unmanaged_cpcs.list(filter_args):
        result_ucpc = {}
        for prop in ucpc.properties:
            if prop in ('object-uri', 'name'):
                result_ucpc[prop] = ucpc.properties[prop]
        result_ucpcs.append(result_ucpc)
    return {'cpcs': result_ucpcs}
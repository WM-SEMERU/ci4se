def smart_search(cls, query_string, search_options=None, extra_query=None):
    if search_options is None:
        search_options = {}
    xmlrpc = XMLRPCConnection()
    try:
        smart_result = xmlrpc.connection.smart_search_vrf({'query_string':
            query_string, 'search_options': search_options, 'auth':
            AuthOptions().options, 'extra_query': extra_query})
    except xmlrpclib.Fault as xml_fault:
        raise _fault_to_exception(xml_fault)
    result = dict()
    result['interpretation'] = smart_result['interpretation']
    result['search_options'] = smart_result['search_options']
    result['error'] = smart_result['error']
    if 'error_message' in smart_result:
        result['error_message'] = smart_result['error_message']
    result['result'] = list()
    for v in smart_result['result']:
        result['result'].append(VRF.from_dict(v))
    return result
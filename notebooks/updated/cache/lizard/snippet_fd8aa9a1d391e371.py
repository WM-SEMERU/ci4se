def post(method, hmc, uri, uri_parms, body, logon_required, wait_for_completion
    ):
    assert wait_for_completion is True
    storage_group_oid = uri_parms[0]
    storage_group_uri = '/api/storage-groups/' + storage_group_oid
    try:
        storage_group = hmc.lookup_by_uri(storage_group_uri)
    except KeyError:
        raise InvalidResourceError(method, uri)
    check_required_fields(method, uri, body, ['adapter-port-uris'])
    candidate_adapter_port_uris = storage_group.properties[
        'candidate-adapter-port-uris']
    for ap_uri in body['adapter-port-uris']:
        if ap_uri in candidate_adapter_port_uris:
            raise ConflictError(method, uri, 483, 
                'Adapter port is already in candidate list of storage group %s: %s'
                 % (storage_group.name, ap_uri))
        else:
            candidate_adapter_port_uris.append(ap_uri)
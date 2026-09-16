def post(method, hmc, uri, uri_parms, body, logon_required, wait_for_completion
    ):
    assert wait_for_completion is True
    storage_group_oid = uri_parms[0]
    storage_group_uri = '/api/storage-groups/' + storage_group_oid
    try:
        storage_group = hmc.lookup_by_uri(storage_group_uri)
    except KeyError:
        raise InvalidResourceError(method, uri)
    body2 = body.copy()
    sv_requests = body2.pop('storage-volumes', None)
    storage_group.update(body2)
    sv_uris = []
    if sv_requests:
        for sv_req in sv_requests:
            check_required_fields(method, uri, sv_req, ['operation'])
            operation = sv_req['operation']
            if operation == 'create':
                sv_props = sv_req.copy()
                del sv_props['operation']
                if 'element-uri' in sv_props:
                    raise BadRequestError(method, uri, 7,
                        "The 'element-uri' field in storage-volumes is invalid for the create operation"
                        )
                sv_uri = storage_group.storage_volumes.add(sv_props)
                sv_uris.append(sv_uri)
            elif operation == 'modify':
                check_required_fields(method, uri, sv_req, ['element-uri'])
                sv_uri = sv_req['element-uri']
                storage_volume = hmc.lookup_by_uri(sv_uri)
                storage_volume.update_properties(sv_props)
            elif operation == 'delete':
                check_required_fields(method, uri, sv_req, ['element-uri'])
                sv_uri = sv_req['element-uri']
                storage_volume = hmc.lookup_by_uri(sv_uri)
                storage_volume.delete()
            else:
                raise BadRequestError(method, uri, 5, 
                    "Invalid value for storage-volumes 'operation' field: %s" %
                    operation)
    return {'element-uris': sv_uris}
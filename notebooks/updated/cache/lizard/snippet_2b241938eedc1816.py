def post(method, hmc, uri, uri_parms, body, logon_required, wait_for_completion
    ):
    assert wait_for_completion is True
    cpc_oid = uri_parms[0]
    try:
        cpc = hmc.cpcs.lookup_by_oid(cpc_oid)
    except KeyError:
        raise InvalidResourceError(method, uri)
    check_required_fields(method, uri, body, ['power-saving'])
    power_saving = body['power-saving']
    if power_saving not in ['high-performance', 'low-power', 'custom']:
        raise BadRequestError(method, uri, reason=7, message=
            'Invalid power-saving value: %r' % power_saving)
    cpc.properties['cpc-power-saving'] = power_saving
    cpc.properties['cpc-power-saving-state'] = power_saving
    cpc.properties['zcpc-power-saving'] = power_saving
    cpc.properties['zcpc-power-saving-state'] = power_saving
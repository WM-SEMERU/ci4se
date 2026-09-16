def post(method, hmc, uri, uri_parms, body, logon_required, wait_for_completion
    ):
    assert wait_for_completion is True
    adapter_uri = uri.split('/operations/')[0]
    try:
        adapter = hmc.lookup_by_uri(adapter_uri)
    except KeyError:
        raise InvalidResourceError(method, uri)
    cpc = adapter.manager.parent
    assert cpc.dpm_enabled
    check_required_fields(method, uri, body, ['crypto-type'])
    crypto_type = body['crypto-type']
    if crypto_type not in ['accelerator', 'cca-coprocessor', 'ep11-coprocessor'
        ]:
        raise BadRequestError(method, uri, reason=8, message=
            "Invalid value for 'crypto-type' field: %s" % crypto_type)
    adapter.properties['crypto-type'] = crypto_type
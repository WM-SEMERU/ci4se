def post(method, hmc, uri, uri_parms, body, logon_required, wait_for_completion
    ):
    assert wait_for_completion is True
    partition_oid = uri_parms[0]
    partition_uri = '/api/partitions/' + partition_oid
    try:
        partition = hmc.lookup_by_uri(partition_uri)
    except KeyError:
        raise InvalidResourceError(method, uri)
    cpc = partition.manager.parent
    assert cpc.dpm_enabled
    check_valid_cpc_status(method, uri, cpc)
    check_partition_status(method, uri, partition, invalid_statuses=[
        'starting', 'stopping'])
    check_required_fields(method, uri, body, [])
    adapter_uris, domain_configs = ensure_crypto_config(partition)
    remove_adapter_uris = body.get('crypto-adapter-uris', [])
    remove_domain_indexes = body.get('crypto-domain-indexes', [])
    for uri in remove_adapter_uris:
        if uri in adapter_uris:
            adapter_uris.remove(uri)
    for remove_di in remove_domain_indexes:
        for i, dc in enumerate(domain_configs):
            if dc['domain-index'] == remove_di:
                del domain_configs[i]
def delete(method, hmc, uri, uri_parms, logon_required):
    try:
        hba = hmc.lookup_by_uri(uri)
    except KeyError:
        raise InvalidResourceError(method, uri)
    partition = hba.manager.parent
    cpc = partition.manager.parent
    assert cpc.dpm_enabled
    check_valid_cpc_status(method, uri, cpc)
    check_partition_status(method, uri, partition, invalid_statuses=[
        'starting', 'stopping'])
    partition.hbas.remove(hba.oid)
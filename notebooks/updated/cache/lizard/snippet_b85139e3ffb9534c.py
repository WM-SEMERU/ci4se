def record_sets_list_by_dns_zone(zone_name, resource_group, top=None,
    recordsetnamesuffix=None, **kwargs):
    result = {}
    dnsconn = __utils__['azurearm.get_client']('dns', **kwargs)
    try:
        record_sets = __utils__['azurearm.paged_object_to_list'](dnsconn.
            record_sets.list_by_dns_zone(zone_name=zone_name,
            resource_group_name=resource_group, top=top,
            recordsetnamesuffix=recordsetnamesuffix))
        for record_set in record_sets:
            result[record_set['name']] = record_set
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('dns', str(exc), **kwargs)
        result = {'error': str(exc)}
    return result
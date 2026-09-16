def record_set_delete(name, zone_name, resource_group, record_type, **kwargs):
    result = False
    dnsconn = __utils__['azurearm.get_client']('dns', **kwargs)
    try:
        record_set = dnsconn.record_sets.delete(relative_record_set_name=
            name, zone_name=zone_name, resource_group_name=resource_group,
            record_type=record_type, if_match=kwargs.get('if_match'))
        result = True
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('dns', str(exc), **kwargs)
    return result
def public_ip_address_get(name, resource_group, **kwargs):
    expand = kwargs.get('expand')
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        pub_ip = netconn.public_ip_addresses.get(public_ip_address_name=
            name, resource_group_name=resource_group, expand=expand)
        result = pub_ip.as_dict()
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
        result = {'error': str(exc)}
    return result
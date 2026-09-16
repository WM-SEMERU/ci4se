def check_ip_address_availability(ip_address, virtual_network,
    resource_group, **kwargs):
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        check_ip = netconn.virtual_networks.check_ip_address_availability(
            resource_group_name=resource_group, virtual_network_name=
            virtual_network, ip_address=ip_address)
        result = check_ip.as_dict()
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
        result = {'error': str(exc)}
    return result
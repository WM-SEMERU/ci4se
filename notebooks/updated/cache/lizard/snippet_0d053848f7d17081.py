def get_vnet(access_token, subscription_id, resource_group, vnet_name):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/resourceGroups/', resource_group,
        '/providers/Microsoft.Network/virtualNetworks/', vnet_name,
        '?api-version=', NETWORK_API])
    return do_get(endpoint, access_token)
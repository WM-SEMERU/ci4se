def delete_load_balancer(access_token, subscription_id, resource_group, lb_name
    ):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/resourceGroups/', resource_group,
        '/providers/Microsoft.Network/loadBalancers/', lb_name,
        '?api-version=', NETWORK_API])
    return do_delete(endpoint, access_token)
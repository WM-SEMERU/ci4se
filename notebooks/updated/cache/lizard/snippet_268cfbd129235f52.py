def list_asgs_all(access_token, subscription_id):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/providers/Microsoft.Network/virtualNetworks/',
        '?api-version=', NETWORK_API])
    return do_get(endpoint, access_token)
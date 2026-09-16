def get_resource_group(access_token, subscription_id, rgname):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/resourceGroups/', rgname, '?api-version=',
        RESOURCE_API])
    return do_get(endpoint, access_token)
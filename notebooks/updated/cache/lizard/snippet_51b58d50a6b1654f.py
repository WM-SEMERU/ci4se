def list_vms_sub(access_token, subscription_id):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/providers/Microsoft.Compute/virtualMachines',
        '?api-version=', COMP_API])
    return do_get_next(endpoint, access_token)
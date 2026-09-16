def put_vmss(access_token, subscription_id, resource_group, vmss_name,
    vmss_body):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/resourceGroups/', resource_group,
        '/providers/Microsoft.Compute/virtualMachineScaleSets/', vmss_name,
        '?api-version=', COMP_API])
    body = json.dumps(vmss_body)
    return do_put(endpoint, body, access_token)
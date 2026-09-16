def delete_vmss_vms(access_token, subscription_id, resource_group,
    vmss_name, vm_ids):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/resourceGroups/', resource_group,
        '/providers/Microsoft.Compute/virtualMachineScaleSets/', vmss_name,
        '/delete?api-version=', COMP_API])
    body = '{"instanceIds" : ' + vm_ids + '}'
    return do_post(endpoint, body, access_token)
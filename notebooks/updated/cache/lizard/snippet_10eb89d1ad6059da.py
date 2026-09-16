def get_vmss_vm(access_token, subscription_id, resource_group, vmss_name,
    instance_id):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/resourceGroups/', resource_group,
        '/providers/Microsoft.Compute/virtualMachineScaleSets/', vmss_name,
        '/virtualMachines/', str(instance_id), '?api-version=', COMP_API])
    return do_get(endpoint, access_token)
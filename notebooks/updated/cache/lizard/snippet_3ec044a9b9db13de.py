def virtual_machine_generalize(name, resource_group, **kwargs):
    result = False
    compconn = __utils__['azurearm.get_client']('compute', **kwargs)
    try:
        compconn.virtual_machines.generalize(resource_group_name=
            resource_group, vm_name=name)
        result = True
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('compute', str(exc), **kwargs)
    return result
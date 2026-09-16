def register_vm(name, datacenter, placement, vmx_path, service_instance=None):
    log.trace(
        'Registering virtual machine with properties datacenter=%s, placement=%s, vmx_path=%s'
        , datacenter, placement, vmx_path)
    datacenter_object = salt.utils.vmware.get_datacenter(service_instance,
        datacenter)
    if 'cluster' in placement:
        cluster_obj = salt.utils.vmware.get_cluster(datacenter_object,
            placement['cluster'])
        cluster_props = salt.utils.vmware.get_properties_of_managed_object(
            cluster_obj, properties=['resourcePool'])
        if 'resourcePool' in cluster_props:
            resourcepool = cluster_props['resourcePool']
        else:
            raise salt.exceptions.VMwareObjectRetrievalError(
                "The cluster's resource pool object could not be retrieved.")
        salt.utils.vmware.register_vm(datacenter_object, name, vmx_path,
            resourcepool)
    elif 'host' in placement:
        hosts = salt.utils.vmware.get_hosts(service_instance,
            datacenter_name=datacenter, host_names=[placement['host']])
        if not hosts:
            raise salt.exceptions.VMwareObjectRetrievalError(
                "ESXi host named '{0}' wasn't found.".format(placement['host'])
                )
        host_obj = hosts[0]
        host_props = salt.utils.vmware.get_properties_of_managed_object(
            host_obj, properties=['parent'])
        if 'parent' in host_props:
            host_parent = host_props['parent']
            parent = salt.utils.vmware.get_properties_of_managed_object(
                host_parent, properties=['parent'])
            if 'parent' in parent:
                resourcepool = parent['parent']
            else:
                raise salt.exceptions.VMwareObjectRetrievalError(
                    "The host parent's parent object could not be retrieved.")
        else:
            raise salt.exceptions.VMwareObjectRetrievalError(
                "The host's parent object could not be retrieved.")
        salt.utils.vmware.register_vm(datacenter_object, name, vmx_path,
            resourcepool, host_object=host_obj)
    result = {'comment': 'Virtual machine registration action succeeded',
        'changes': {'register_vm': True}}
    return result
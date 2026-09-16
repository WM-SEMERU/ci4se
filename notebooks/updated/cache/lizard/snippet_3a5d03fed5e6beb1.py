def create_dvportgroup(portgroup_dict, portgroup_name, dvs,
    service_instance=None):
    log.trace("Creating portgroup'%s' in dvs '%s' with dict = %s",
        portgroup_name, dvs, portgroup_dict)
    proxy_type = get_proxy_type()
    if proxy_type == 'esxdatacenter':
        datacenter = __salt__['esxdatacenter.get_details']()['datacenter']
        dc_ref = _get_proxy_target(service_instance)
    elif proxy_type == 'esxcluster':
        datacenter = __salt__['esxcluster.get_details']()['datacenter']
        dc_ref = salt.utils.vmware.get_datacenter(service_instance, datacenter)
    dvs_refs = salt.utils.vmware.get_dvss(dc_ref, dvs_names=[dvs])
    if not dvs_refs:
        raise VMwareObjectRetrievalError("DVS '{0}' was not retrieved".
            format(dvs))
    portgroup_dict['name'] = portgroup_name
    spec = vim.DVPortgroupConfigSpec()
    _apply_dvportgroup_config(portgroup_name, spec, portgroup_dict)
    salt.utils.vmware.create_dvportgroup(dvs_refs[0], spec)
    return True
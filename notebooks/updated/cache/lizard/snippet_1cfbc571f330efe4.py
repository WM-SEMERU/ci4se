def list_ssds(host, username, password, protocol=None, port=None,
    host_names=None):
    service_instance = salt.utils.vmware.get_service_instance(host=host,
        username=username, password=password, protocol=protocol, port=port)
    host_names = _check_hosts(service_instance, host, host_names)
    ret = {}
    names = []
    for host_name in host_names:
        host_ref = _get_host_ref(service_instance, host, host_name=host_name)
        disks = _get_host_ssds(host_ref)
        for disk in disks:
            names.append(disk.canonicalName)
        ret.update({host_name: names})
    return ret
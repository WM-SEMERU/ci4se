def get_vsan_eligible_disks(host, username, password, protocol=None, port=
    None, host_names=None):
    service_instance = salt.utils.vmware.get_service_instance(host=host,
        username=username, password=password, protocol=protocol, port=port)
    host_names = _check_hosts(service_instance, host, host_names)
    response = _get_vsan_eligible_disks(service_instance, host, host_names)
    ret = {}
    for host_name, value in six.iteritems(response):
        error = value.get('Error')
        if error:
            ret.update({host_name: {'Error': error}})
            continue
        disks = value.get('Eligible')
        if disks and isinstance(disks, list):
            disk_names = []
            for disk in disks:
                disk_names.append(disk.canonicalName)
            ret.update({host_name: {'Eligible': disk_names}})
        else:
            ret.update({host_name: {'Eligible': disks}})
    return ret
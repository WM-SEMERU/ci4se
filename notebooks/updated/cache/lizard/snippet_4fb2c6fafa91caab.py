def vm_virt_type(domain):
    ret = __salt__['vmadm.lookup'](search='uuid={uuid}'.format(uuid=domain),
        order='type')
    if not ret:
        raise CommandExecutionError("We can't determine the type of this VM")
    return ret[0]['type']
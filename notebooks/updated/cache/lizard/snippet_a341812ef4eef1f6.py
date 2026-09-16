def exists(name, runas=None):
    vm_info = list_vms(name, info=True, runas=runas).splitlines()
    for info_line in vm_info:
        if 'Name: {0}'.format(name) in info_line:
            return True
    return False
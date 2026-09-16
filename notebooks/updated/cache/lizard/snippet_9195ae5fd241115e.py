def setmem(domain, memory):
    vmtype = vm_virt_type(domain)
    if vmtype == 'OS':
        return __salt__['vmadm.update'](vm=domain, max_physical_memory=memory)
    elif vmtype == 'LX':
        return __salt__['vmadm.update'](vm=domain, max_physical_memory=memory)
    elif vmtype == 'KVM':
        log.warning('Changes will be applied after the VM restart.')
        return __salt__['vmadm.update'](vm=domain, ram=memory)
    else:
        raise CommandExecutionError('Unknown VM type')
    return False
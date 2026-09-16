def reset(name, soft=False, call=None):
    if call != 'action':
        raise SaltCloudSystemExit(
            'The reset action must be called with -a or --action.')
    vm_properties = ['name', 'summary.runtime.powerState']
    vm_list = salt.utils.vmware.get_mors_with_properties(_get_si(), vim.
        VirtualMachine, vm_properties)
    for vm in vm_list:
        if vm['name'] == name:
            if vm['summary.runtime.powerState'] == 'suspended' or vm[
                'summary.runtime.powerState'] == 'poweredOff':
                ret = 'cannot reset in suspended/powered off state'
                log.info('VM %s %s', name, ret)
                return ret
            try:
                log.info('Resetting VM %s', name)
                if soft:
                    vm['object'].RebootGuest()
                else:
                    task = vm['object'].ResetVM_Task()
                    salt.utils.vmware.wait_for_task(task, name, 'reset')
            except Exception as exc:
                log.error('Error while resetting VM %s: %s', name, exc,
                    exc_info_on_loglevel=logging.DEBUG)
                return 'failed to reset'
    return 'reset'
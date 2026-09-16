def enter_maintenance_mode(kwargs=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The enter_maintenance_mode function must be called with -f or --function.'
            )
    host_name = kwargs.get('host') if kwargs and 'host' in kwargs else None
    host_ref = salt.utils.vmware.get_mor_by_property(_get_si(), vim.
        HostSystem, host_name)
    if not host_name or not host_ref:
        raise SaltCloudSystemExit(
            'You must specify a valid name of the host system.')
    if host_ref.runtime.inMaintenanceMode:
        return {host_name: 'already in maintenance mode'}
    try:
        task = host_ref.EnterMaintenanceMode(timeout=0,
            evacuatePoweredOffVms=True)
        salt.utils.vmware.wait_for_task(task, host_name,
            'enter maintenance mode')
    except Exception as exc:
        log.error('Error while moving host system %s in maintenance mode: %s',
            host_name, exc, exc_info_on_loglevel=logging.DEBUG)
        return {host_name: 'failed to enter maintenance mode'}
    return {host_name: 'entered maintenance mode'}
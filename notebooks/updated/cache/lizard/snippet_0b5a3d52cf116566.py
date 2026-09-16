def create_datacenter(service_instance, datacenter_name):
    root_folder = get_root_folder(service_instance)
    log.trace("Creating datacenter '%s'", datacenter_name)
    try:
        dc_obj = root_folder.CreateDatacenter(datacenter_name)
    except vim.fault.NoPermission as exc:
        log.exception(exc)
        raise salt.exceptions.VMwareApiError(
            'Not enough permissions. Required privilege: {}'.format(exc.
            privilegeId))
    except vim.fault.VimFault as exc:
        log.exception(exc)
        raise salt.exceptions.VMwareApiError(exc.msg)
    except vmodl.RuntimeFault as exc:
        log.exception(exc)
        raise salt.exceptions.VMwareRuntimeError(exc.msg)
    return dc_obj
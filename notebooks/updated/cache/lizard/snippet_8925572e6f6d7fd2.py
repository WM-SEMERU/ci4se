def set_dvs_network_resource_management_enabled(dvs_ref, enabled):
    dvs_name = get_managed_object_name(dvs_ref)
    log.trace("Setting network resource management enable to %s on dvs '%s'",
        enabled, dvs_name)
    try:
        dvs_ref.EnableNetworkResourceManagement(enable=enabled)
    except vim.fault.NoPermission as exc:
        log.exception(exc)
        raise salt.exceptions.VMwareApiError(
            'Not enough permissions. Required privilege: {0}'.format(exc.
            privilegeId))
    except vim.fault.VimFault as exc:
        log.exception(exc)
        raise salt.exceptions.VMwareApiError(exc.msg)
    except vmodl.RuntimeFault as exc:
        log.exception(exc)
        raise salt.exceptions.VMwareRuntimeError(exc.msg)
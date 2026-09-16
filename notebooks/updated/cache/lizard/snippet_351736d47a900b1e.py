def create_dvs(dc_ref, dvs_name, dvs_create_spec=None):
    dc_name = get_managed_object_name(dc_ref)
    log.trace("Creating DVS '%s' in datacenter '%s'", dvs_name, dc_name)
    if not dvs_create_spec:
        dvs_create_spec = vim.DVSCreateSpec()
    if not dvs_create_spec.configSpec:
        dvs_create_spec.configSpec = vim.VMwareDVSConfigSpec()
        dvs_create_spec.configSpec.name = dvs_name
    netw_folder_ref = get_network_folder(dc_ref)
    try:
        task = netw_folder_ref.CreateDVS_Task(dvs_create_spec)
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
    wait_for_task(task, dvs_name, six.text_type(task.__class__))
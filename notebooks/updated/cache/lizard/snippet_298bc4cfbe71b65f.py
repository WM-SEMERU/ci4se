def get_datastore_files(service_instance, directory, datastores,
    container_object, browser_spec):
    files = []
    datastore_objects = get_datastores(service_instance, container_object,
        datastore_names=datastores)
    for datobj in datastore_objects:
        try:
            task = datobj.browser.SearchDatastore_Task(datastorePath=
                '[{}] {}'.format(datobj.name, directory), searchSpec=
                browser_spec)
        except vim.fault.NoPermission as exc:
            log.exception(exc)
            raise salt.exceptions.VMwareApiError(
                'Not enough permissions. Required privilege: {}'.format(exc
                .privilegeId))
        except vim.fault.VimFault as exc:
            log.exception(exc)
            raise salt.exceptions.VMwareApiError(exc.msg)
        except vmodl.RuntimeFault as exc:
            log.exception(exc)
            raise salt.exceptions.VMwareRuntimeError(exc.msg)
        try:
            files.append(salt.utils.vmware.wait_for_task(task, directory,
                'query virtual machine files'))
        except salt.exceptions.VMwareFileNotFoundError:
            pass
    return files
def _erase_vm_info(name):
    try:
        vm_ = get_vm_info(name)
        if vm_['machine']:
            key = _build_machine_uri(vm_['machine'], vm_.get('cwd', '.'))
            try:
                __utils__['sdb.sdb_delete'](key, __opts__)
            except KeyError:
                __utils__['sdb.sdb_set'](key, None, __opts__)
    except Exception:
        pass
    uri = _build_sdb_uri(name)
    try:
        __utils__['sdb.sdb_delete'](uri, __opts__)
    except KeyError:
        __utils__['sdb.sdb_set'](uri, {}, __opts__)
    except Exception:
        pass
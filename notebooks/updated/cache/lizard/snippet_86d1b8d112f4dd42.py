def delete_value(hive, key, vname=None, use_32bit_registry=False):
    local_hive = _to_unicode(hive)
    local_key = _to_unicode(key)
    local_vname = _to_unicode(vname)
    registry = Registry()
    try:
        hkey = registry.hkeys[local_hive]
    except KeyError:
        raise CommandExecutionError('Invalid Hive: {0}'.format(local_hive))
    access_mask = registry.registry_32[use_32bit_registry
        ] | win32con.KEY_ALL_ACCESS
    handle = None
    try:
        handle = win32api.RegOpenKeyEx(hkey, local_key, 0, access_mask)
        win32api.RegDeleteValue(handle, local_vname)
        broadcast_change()
        return True
    except Exception as exc:
        if exc.winerror == 2:
            return None
        else:
            log.error(exc, exc_info=True)
            log.error('Hive: %s', local_hive)
            log.error('Key: %s', local_key)
            log.error('ValueName: %s', local_vname)
            log.error('32bit Reg: %s', use_32bit_registry)
            return False
    finally:
        if handle:
            win32api.RegCloseKey(handle)
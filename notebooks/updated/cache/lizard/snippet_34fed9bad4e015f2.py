def list_keys(hive, key=None, use_32bit_registry=False):
    local_hive = _to_unicode(hive)
    local_key = _to_unicode(key)
    registry = Registry()
    try:
        hkey = registry.hkeys[local_hive]
    except KeyError:
        raise CommandExecutionError('Invalid Hive: {0}'.format(local_hive))
    access_mask = registry.registry_32[use_32bit_registry]
    subkeys = []
    handle = None
    try:
        handle = win32api.RegOpenKeyEx(hkey, local_key, 0, access_mask)
        for i in range(win32api.RegQueryInfoKey(handle)[0]):
            subkey = win32api.RegEnumKey(handle, i)
            if PY2:
                subkeys.append(_to_mbcs(subkey))
            else:
                subkeys.append(subkey)
    except Exception:
        log.debug('Cannot find key: %s\\%s', hive, key, exc_info=True)
        return False, 'Cannot find key: {0}\\{1}'.format(hive, key)
    finally:
        if handle:
            handle.Close()
    return subkeys
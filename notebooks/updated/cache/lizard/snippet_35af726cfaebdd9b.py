def get_pending_file_rename():
    vnames = 'PendingFileRenameOperations', 'PendingFileRenameOperations2'
    key = 'SYSTEM\\CurrentControlSet\\Control\\Session Manager'
    for vname in vnames:
        reg_ret = __utils__['reg.read_value']('HKLM', key, vname)
        if reg_ret['success']:
            log.debug('Found key: %s', key)
            if reg_ret['vdata'] and reg_ret['vdata'] != '(value not set)':
                return True
        else:
            log.debug('Unable to access key: %s', key)
    return False
def remove_vdir(name, site, app=_DEFAULT_APP):
    current_vdirs = list_vdirs(site, app)
    app_path = os.path.join(*app.rstrip('/').split('/'))
    if app_path:
        app_path = '{0}\\'.format(app_path)
    vdir_path = 'IIS:\\Sites\\{0}\\{1}{2}'.format(site, app_path, name)
    if name not in current_vdirs:
        log.debug('Virtual directory already absent: %s', name)
        return True
    ps_cmd = ['Remove-Item', '-Path', "'{0}'".format(vdir_path), '-Recurse']
    cmd_ret = _srvmgr(ps_cmd)
    if cmd_ret['retcode'] != 0:
        msg = 'Unable to remove virtual directory: {0}\nError: {1}'.format(name
            , cmd_ret['stderr'])
        raise CommandExecutionError(msg)
    new_vdirs = list_vdirs(site, app)
    if name not in new_vdirs:
        log.debug('Virtual directory removed successfully: %s', name)
        return True
    log.error('Unable to remove virtual directory: %s', name)
    return False
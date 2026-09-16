def install_var(instance, clear_target, clear_all):
    _check_root()
    log('Checking frontend library and cache directories', emitter='MANAGE')
    uid = pwd.getpwnam('hfos').pw_uid
    gid = grp.getgrnam('hfos').gr_gid
    join = os.path.join
    target_paths = '/var/www/challenges', join('/var/lib/hfos', instance
        ), join('/var/local/hfos', instance), join('/var/local/hfos',
        instance, 'backup'), join('/var/cache/hfos', instance), join(
        '/var/cache/hfos', instance, 'tilecache'), join('/var/cache/hfos',
        instance, 'rastertiles'), join('/var/cache/hfos', instance,
        'rastercache')
    logfile = '/var/log/hfos-' + instance + '.log'
    for item in target_paths:
        if os.path.exists(item):
            log('Path already exists: ' + item)
            if clear_all or clear_target and 'cache' in item:
                log('Cleaning up: ' + item, lvl=warn)
                shutil.rmtree(item)
        if not os.path.exists(item):
            log('Creating path: ' + item)
            os.mkdir(item)
            os.chown(item, uid, gid)
    open(logfile, 'a').close()
    os.chown(logfile, uid, gid)
    log('Done: Install Var')
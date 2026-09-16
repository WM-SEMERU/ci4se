def service_pause(service_name, init_dir='/etc/init', initd_dir=
    '/etc/init.d', **kwargs):
    stopped = True
    if service_running(service_name, **kwargs):
        stopped = service_stop(service_name, **kwargs)
    upstart_file = os.path.join(init_dir, '{}.conf'.format(service_name))
    sysv_file = os.path.join(initd_dir, service_name)
    if init_is_systemd():
        service('disable', service_name)
        service('mask', service_name)
    elif os.path.exists(upstart_file):
        override_path = os.path.join(init_dir, '{}.override'.format(
            service_name))
        with open(override_path, 'w') as fh:
            fh.write('manual\n')
    elif os.path.exists(sysv_file):
        subprocess.check_call(['update-rc.d', service_name, 'disable'])
    else:
        raise ValueError(
            'Unable to detect {0} as SystemD, Upstart {1} or SysV {2}'.
            format(service_name, upstart_file, sysv_file))
    return stopped
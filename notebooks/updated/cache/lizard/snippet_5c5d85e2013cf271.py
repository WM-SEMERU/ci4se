def service(action, service_name, **kwargs):
    if init_is_systemd():
        cmd = ['systemctl', action, service_name]
    else:
        cmd = ['service', service_name, action]
        for key, value in six.iteritems(kwargs):
            parameter = '%s=%s' % (key, value)
            cmd.append(parameter)
    return subprocess.call(cmd) == 0
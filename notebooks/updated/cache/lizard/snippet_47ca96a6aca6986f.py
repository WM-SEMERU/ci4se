def _service_is_sysv(name):
    script = '/etc/init.d/{0}'.format(name)
    return not _service_is_upstart(name) and os.access(script, os.X_OK)
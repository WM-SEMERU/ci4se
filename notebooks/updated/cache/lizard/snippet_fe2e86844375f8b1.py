def enable(name, **kwargs):
    stat_cmd = '{0} set {1} status on'.format(_cmd(), name)
    stat_retcode = __salt__['cmd.retcode'](stat_cmd)
    flag_retcode = None
    if os.path.exists('/etc/rc.d/{0}'.format(name)):
        flags = _get_flags(**kwargs)
        flag_cmd = '{0} set {1} flags {2}'.format(_cmd(), name, flags)
        flag_retcode = __salt__['cmd.retcode'](flag_cmd)
    return not any([stat_retcode, flag_retcode])
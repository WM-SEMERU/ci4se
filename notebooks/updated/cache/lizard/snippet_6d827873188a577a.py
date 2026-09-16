def _date_bin_set_datetime(new_date):
    cmd = ['date']
    if new_date.utcoffset() is not None:
        new_date = new_date - new_date.utcoffset()
        new_date = new_date.replace(tzinfo=_FixedOffset(0))
        cmd.append('-u')
    non_posix = '{1:02}{2:02}{3:02}{4:02}{0:04}.{5:02}'.format(*new_date.
        timetuple())
    non_posix_cmd = cmd + [non_posix]
    ret_non_posix = __salt__['cmd.run_all'](non_posix_cmd, python_shell=False)
    if ret_non_posix['retcode'] != 0:
        posix = ' {1:02}{2:02}{3:02}{4:02}{0:04}'.format(*new_date.timetuple())
        posix_cmd = cmd + [posix]
        ret_posix = __salt__['cmd.run_all'](posix_cmd, python_shell=False)
        if ret_posix['retcode'] != 0:
            msg = 'date failed: {0}'.format(ret_non_posix['stderr'])
            raise CommandExecutionError(msg)
    return True
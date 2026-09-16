def refresh_db(**kwargs):
    salt.utils.pkg.clear_rtag(__opts__)
    retcodes = {(100): True, (0): None, (1): False}
    ret = True
    check_update_ = kwargs.pop('check_update', True)
    options = _get_options(**kwargs)
    clean_cmd = ['--quiet', '--assumeyes', 'clean', 'expire-cache']
    clean_cmd.extend(options)
    _call_yum(clean_cmd, ignore_retcode=True)
    if check_update_:
        update_cmd = ['--quiet', '--assumeyes', 'check-update']
        if __grains__.get('os_family') == 'RedHat' and __grains__.get(
            'osmajorrelease') == 7:
            update_cmd.append('--setopt=autocheck_running_kernel=false')
        update_cmd.extend(options)
        ret = retcodes.get(_call_yum(update_cmd, ignore_retcode=True)[
            'retcode'], False)
    return ret
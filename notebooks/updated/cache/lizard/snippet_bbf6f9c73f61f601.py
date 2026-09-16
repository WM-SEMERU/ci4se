def set_locale(locale):
    lc_ctl = salt.utils.systemd.booted(__context__)
    if lc_ctl and not (__grains__['os_family'] in ['Suse'] and __grains__[
        'osmajorrelease'] in [12]):
        return _localectl_set(locale)
    if 'Suse' in __grains__['os_family']:
        if not __salt__['file.file_exists']('/etc/sysconfig/language'):
            __salt__['file.touch']('/etc/sysconfig/language')
        __salt__['file.replace']('/etc/sysconfig/language', '^RC_LANG=.*',
            'RC_LANG="{0}"'.format(locale), append_if_not_found=True)
    elif 'RedHat' in __grains__['os_family']:
        if not __salt__['file.file_exists']('/etc/sysconfig/i18n'):
            __salt__['file.touch']('/etc/sysconfig/i18n')
        __salt__['file.replace']('/etc/sysconfig/i18n', '^LANG=.*',
            'LANG="{0}"'.format(locale), append_if_not_found=True)
    elif 'Debian' in __grains__['os_family']:
        update_locale = salt.utils.path.which('update-locale')
        if update_locale is None:
            raise CommandExecutionError(
                'Cannot set locale: "update-locale" was not found.')
        __salt__['cmd.run'](update_locale)
        __salt__['file.replace']('/etc/default/locale', '^LANG=.*',
            'LANG="{0}"'.format(locale), append_if_not_found=True)
    elif 'Gentoo' in __grains__['os_family']:
        cmd = 'eselect --brief locale set {0}'.format(locale)
        return __salt__['cmd.retcode'](cmd, python_shell=False) == 0
    elif 'Solaris' in __grains__['os_family']:
        if locale not in __salt__['locale.list_avail']():
            return False
        __salt__['file.replace']('/etc/default/init', '^LANG=.*',
            'LANG="{0}"'.format(locale), append_if_not_found=True)
    else:
        raise CommandExecutionError('Error: Unsupported platform!')
    return True
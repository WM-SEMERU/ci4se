def get_locale():
    ret = ''
    lc_ctl = salt.utils.systemd.booted(__context__)
    if lc_ctl and not (__grains__['os_family'] in ['Suse'] and __grains__[
        'osmajorrelease'] in [12]):
        ret = (_parse_dbus_locale() if dbus is not None else
            _localectl_status()['system_locale']).get('LANG', '')
    else:
        if 'Suse' in __grains__['os_family']:
            cmd = 'grep "^RC_LANG" /etc/sysconfig/language'
        elif 'RedHat' in __grains__['os_family']:
            cmd = 'grep "^LANG=" /etc/sysconfig/i18n'
        elif 'Debian' in __grains__['os_family']:
            cmd = 'grep "^LANG=" /etc/default/locale'
        elif 'Gentoo' in __grains__['os_family']:
            cmd = 'eselect --brief locale show'
            return __salt__['cmd.run'](cmd).strip()
        elif 'Solaris' in __grains__['os_family']:
            cmd = 'grep "^LANG=" /etc/default/init'
        else:
            raise CommandExecutionError('Error: "{0}" is unsupported!'.
                format(__grains__['oscodename']))
        if cmd:
            try:
                ret = __salt__['cmd.run'](cmd).split('=')[1].replace('"', '')
            except IndexError as err:
                log.error('Error occurred while running "%s": %s', cmd, err)
    return ret
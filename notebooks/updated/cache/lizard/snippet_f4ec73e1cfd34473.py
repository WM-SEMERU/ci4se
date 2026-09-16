def set_permissions(vhost, user, conf='.*', write='.*', read='.*', runas=None):
    if runas is None and not salt.utils.platform.is_windows():
        runas = salt.utils.user.get_user()
    res = __salt__['cmd.run_all']([RABBITMQCTL, 'set_permissions', '-p',
        vhost, user, conf, write, read], reset_system_locale=False, runas=
        runas, python_shell=False)
    msg = 'Permissions Set'
    return _format_response(res, msg)
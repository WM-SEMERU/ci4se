def add_vhost(vhost, runas=None):
    if runas is None and not salt.utils.platform.is_windows():
        runas = salt.utils.user.get_user()
    res = __salt__['cmd.run_all']([RABBITMQCTL, 'add_vhost', vhost],
        reset_system_locale=False, runas=runas, python_shell=False)
    msg = 'Added'
    return _format_response(res, msg)
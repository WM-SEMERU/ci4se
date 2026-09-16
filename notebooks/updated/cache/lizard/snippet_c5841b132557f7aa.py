def list_available_plugins(runas=None):
    if runas is None and not salt.utils.platform.is_windows():
        runas = salt.utils.user.get_user()
    cmd = [_get_rabbitmq_plugin(), 'list', '-m']
    ret = __salt__['cmd.run_all'](cmd, reset_system_locale=False,
        python_shell=False, runas=runas)
    _check_response(ret)
    return _output_to_list(ret['stdout'])
def set_user_tags(name, tags, runas=None):
    if runas is None and not salt.utils.platform.is_windows():
        runas = salt.utils.user.get_user()
    if not isinstance(tags, (list, tuple)):
        tags = [tags]
    res = __salt__['cmd.run_all']([RABBITMQCTL, 'set_user_tags', name] +
        list(tags), reset_system_locale=False, runas=runas, python_shell=False)
    msg = 'Tag(s) set'
    return _format_response(res, msg)
def policy_exists(vhost, name, runas=None):
    if runas is None and not salt.utils.platform.is_windows():
        runas = salt.utils.user.get_user()
    policies = list_policies(runas=runas)
    return bool(vhost in policies and name in policies[vhost])
def server_hardreset(host=None, admin_username=None, admin_password=None,
    module=None):
    return __execute_cmd('serveraction hardreset', host=host,
        admin_username=admin_username, admin_password=admin_password,
        module=module)
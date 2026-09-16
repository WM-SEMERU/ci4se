def set_slotname(slot, name, host=None, admin_username=None, admin_password
    =None):
    return __execute_cmd('config -g cfgServerInfo -o cfgServerName -i {0} {1}'
        .format(slot, name), host=host, admin_username=admin_username,
        admin_password=admin_password)
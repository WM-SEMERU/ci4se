def idrac_general(blade_name, command, idrac_password=None, host=None,
    admin_username=None, admin_password=None):
    module_network = network_info(host, admin_username, admin_password,
        blade_name)
    if idrac_password is not None:
        password = idrac_password
    else:
        password = admin_password
    idrac_ip = module_network['Network']['IP Address']
    ret = __execute_ret(command, host=idrac_ip, admin_username='root',
        admin_password=password)
    if ret['retcode'] == 0:
        return ret['stdout']
    else:
        return ret
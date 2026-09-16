def delete_user(username, uid=None, host=None, admin_username=None,
    admin_password=None):
    if uid is None:
        user = list_users()
        uid = user[username]['index']
    if uid:
        return __execute_cmd(
            'config -g cfgUserAdmin -o cfgUserAdminUserName -i {0} ""'.
            format(uid), host=host, admin_username=admin_username,
            admin_password=admin_password)
    else:
        log.warning("User '%s' does not exist", username)
        return False
def get_users(self):
    users = {}
    _JUNOS_CLASS_CISCO_PRIVILEGE_LEVEL_MAP = {'super-user': 15, 'superuser':
        15, 'operator': 5, 'read-only': 1, 'unauthorized': 0}
    _DEFAULT_USER_DETAILS = {'level': 0, 'password': '', 'sshkeys': []}
    users_table = junos_views.junos_users_table(self.device)
    users_table.get()
    users_items = users_table.items()
    root_user = self._get_root()
    for user_entry in users_items:
        username = user_entry[0]
        user_details = _DEFAULT_USER_DETAILS.copy()
        user_details.update({d[0]: d[1] for d in user_entry[1] if d[1]})
        user_class = user_details.pop('class', '')
        user_details = {key: py23_compat.text_type(user_details[key]) for
            key in user_details.keys()}
        level = _JUNOS_CLASS_CISCO_PRIVILEGE_LEVEL_MAP.get(user_class, 0)
        user_details.update({'level': level})
        user_details['sshkeys'] = [user_details.pop(key) for key in [
            'ssh_rsa', 'ssh_dsa', 'ssh_ecdsa'] if user_details.get(key, '')]
        users[username] = user_details
    users.update(root_user)
    return users
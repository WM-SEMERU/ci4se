def is_member(self, ldap_user, group_dn):
    try:
        user_uid = ldap_user.attrs['uid'][0]
        try:
            is_member = ldap_user.connection.compare_s(group_dn,
                'memberUid', user_uid.encode())
        except (ldap.UNDEFINED_TYPE, ldap.NO_SUCH_ATTRIBUTE):
            is_member = False
        if not is_member:
            try:
                user_gid = ldap_user.attrs['gidNumber'][0]
                is_member = ldap_user.connection.compare_s(group_dn,
                    'gidNumber', user_gid.encode())
            except (ldap.UNDEFINED_TYPE, ldap.NO_SUCH_ATTRIBUTE):
                is_member = False
    except (KeyError, IndexError):
        is_member = False
    return is_member
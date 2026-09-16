def get_group_members(self, group):
    conn = self.bind
    try:
        records = conn.search_s(current_app.config['LDAP_BASE_DN'], ldap.
            SCOPE_SUBTREE, ldap_filter.filter_format(current_app.config[
            'LDAP_GROUP_OBJECT_FILTER'], (group,)), [current_app.config[
            'LDAP_GROUP_MEMBERS_FIELD']])
        conn.unbind_s()
        if records:
            if current_app.config['LDAP_GROUP_MEMBERS_FIELD'] in records[0][1]:
                members = records[0][1][current_app.config[
                    'LDAP_GROUP_MEMBERS_FIELD']]
                if sys.version_info[0] > 2:
                    members = [m.decode('utf-8') for m in members]
                return members
    except ldap.LDAPError as e:
        raise LDAPException(self.error(e.args))
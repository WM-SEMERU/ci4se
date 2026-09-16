def user_groups(self, ldap_user, group_search):
    groups = []
    try:
        user_uid = ldap_user.attrs['uid'][0]
        if 'gidNumber' in ldap_user.attrs:
            user_gid = ldap_user.attrs['gidNumber'][0]
            filterstr = '(|(gidNumber={})(memberUid={}))'.format(self.ldap.
                filter.escape_filter_chars(user_gid), self.ldap.filter.
                escape_filter_chars(user_uid))
        else:
            filterstr = '(memberUid={})'.format(self.ldap.filter.
                escape_filter_chars(user_uid))
        search = group_search.search_with_additional_term_string(filterstr)
        groups = search.execute(ldap_user.connection)
    except (KeyError, IndexError):
        pass
    return groups
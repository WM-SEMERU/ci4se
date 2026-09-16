def get_groups(self, username):
    username = ldap.filter.escape_filter_chars(self._byte_p2(username))
    userdn = self._get_user(username, NO_ATTR)
    searchfilter = self.group_filter_tmpl % {'userdn': userdn, 'username':
        username}
    groups = self._search(searchfilter, NO_ATTR, self.groupdn)
    ret = []
    for entry in groups:
        ret.append(self._uni(entry[0]))
    return ret
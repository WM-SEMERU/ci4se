def search(self, searchstring):
    searchstring = ldap.filter.escape_filter_chars(self._byte_p2(searchstring))
    searchfilter = self.search_filter_tmpl % {'searchstring': searchstring}
    ret = {}
    for u in self._search(searchfilter, DISPLAYED_ATTRS, self.userdn):
        attrs = {}
        attrs_tmp = u[1]
        for attr in attrs_tmp:
            value_tmp = attrs_tmp[attr]
            if len(value_tmp) == 1:
                attrs[attr] = value_tmp[0]
            else:
                attrs[attr] = value_tmp
        if self.key in attrs:
            ret[attrs[self.key]] = attrs
    return ret
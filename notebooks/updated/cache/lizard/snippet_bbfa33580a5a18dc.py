def paged_search_ext_s(self, base, scope, filterstr='(objectClass=*)',
    attrlist=None, attrsonly=0, serverctrls=None, clientctrls=None, timeout
    =-1, sizelimit=0):
    req_ctrl = SimplePagedResultsControl(True, size=self.
        conf_LDAP_SYNC_BIND_PAGESIZE, cookie='')
    msgid = self.search_ext(base, ldap.SCOPE_SUBTREE, filterstr, attrlist=
        attrlist, serverctrls=(serverctrls or []) + [req_ctrl])
    results = []
    while True:
        rtype, rdata, rmsgid, rctrls = self.result3(msgid)
        results.extend(rdata)
        pctrls = [c for c in rctrls if c.controlType ==
            SimplePagedResultsControl.controlType]
        if pctrls:
            if pctrls[0].cookie:
                req_ctrl.cookie = pctrls[0].cookie
                msgid = self.search_ext(base, ldap.SCOPE_SUBTREE, filterstr,
                    attrlist=attrlist, serverctrls=(serverctrls or []) + [
                    req_ctrl])
            else:
                break
    return results
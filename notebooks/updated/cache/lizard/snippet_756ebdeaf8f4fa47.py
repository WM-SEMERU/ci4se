def get_members(self):
    res = self.__con__.search_s(self.__ldap_base_dn__, ldap.SCOPE_SUBTREE, 
        '(memberof=%s)' % self.__dn__, ['uid'])
    ret = []
    for val in res:
        val = val[1]['uid'][0]
        try:
            ret.append(val.decode('utf-8'))
        except UnicodeDecodeError:
            ret.append(val)
        except KeyError:
            continue
    return [CSHMember(self.__lib__, result, uid=True) for result in ret]
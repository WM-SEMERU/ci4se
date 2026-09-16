def search(self, base=False, trim=False, objects=False, **kwargs):
    scope = pyldap.SCOPE_SUBTREE
    if not base:
        base = self.users
    filterstr = ''
    for key, value in kwargs.iteritems():
        filterstr += '({0}={1})'.format(key, value)
        if key == 'dn':
            filterstr = '(objectClass=*)'
            base = value
            scope = pyldap.SCOPE_BASE
            break
    if len(kwargs) > 1:
        filterstr = '(&' + filterstr + ')'
    result = self.ldap.search_s(base, pyldap.SCOPE_SUBTREE, filterstr, ['*',
        '+'])
    if base == self.users:
        for member in result:
            groups = self.getGroups(member[0])
            member[1]['groups'] = groups
            if 'eboard' in member[1]['groups']:
                member[1]['committee'] = self.search(base=self.committees,
                    head=member[0])[0][1]['cn'][0]
    if objects:
        return self.memberObjects(result)
    finalResult = self.trimResult(result) if trim else result
    return finalResult
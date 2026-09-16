def list_my(self):
    org_list = self.call_contract_command('Registry', 'listOrganizations', [])
    rez_owner = []
    rez_member = []
    for idx, org_id in enumerate(org_list):
        (found, org_id, org_name, owner, members, serviceNames, repositoryNames
            ) = (self.call_contract_command('Registry',
            'getOrganizationById', [org_id]))
        if not found:
            raise Exception(
                'Organization was removed during this call. Please retry.')
        if self.ident.address == owner:
            rez_owner.append((org_name, bytes32_to_str(org_id)))
        if self.ident.address in members:
            rez_member.append((org_name, bytes32_to_str(org_id)))
    if rez_owner:
        self._printout('# Organizations you are the owner of')
        self._printout('# OrgName OrgId')
        for n, i in rez_owner:
            self._printout('%s   %s' % (n, i))
    if rez_member:
        self._printout('# Organizations you are the member of')
        self._printout('# OrgName OrgId')
        for n, i in rez_member:
            self._printout('%s   %s' % (n, i))
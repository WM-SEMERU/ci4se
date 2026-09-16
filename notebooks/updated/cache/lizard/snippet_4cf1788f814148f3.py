def group(self, base_dn, samaccountname, attributes=(),
    explicit_membership_only=False):
    groups = self.groups(base_dn, samaccountnames=[samaccountname],
        attributes=attributes, explicit_membership_only=
        explicit_membership_only)
    try:
        return groups[0]
    except IndexError:
        logging.info('%s - unable to retrieve object from AD by sAMAccountName'
            , samaccountname)
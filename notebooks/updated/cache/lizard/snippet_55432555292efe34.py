def group_samaccountnames(self, base_dn):
    mappings = self.samaccountnames(base_dn, self.memberof)
    groups = [samaccountname for samaccountname in mappings.values()]
    if not groups:
        logging.info(
            '%s - unable to retrieve any groups for the current ADUser instance'
            , self.samaccountname)
    return groups
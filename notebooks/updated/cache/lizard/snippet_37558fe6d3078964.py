def get_contacts_by_explosion(self, contactgroups):
    self.already_exploded = True
    if self.rec_tag:
        logger.error('[contactgroup::%s] got a loop in contactgroup definition'
            , self.get_name())
        if hasattr(self, 'members'):
            return self.members
        return ''
    self.rec_tag = True
    cg_mbrs = self.get_contactgroup_members()
    for cg_mbr in cg_mbrs:
        contactgroup = contactgroups.find_by_name(cg_mbr.strip())
        if contactgroup is not None:
            value = contactgroup.get_contacts_by_explosion(contactgroups)
            if value is not None:
                self.add_members(value)
    if hasattr(self, 'members'):
        return self.members
    return ''
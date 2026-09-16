def from_dict(self, dirent):
    for k in ['perms', 'owner', 'group', 'name', 'dir']:
        if k not in dirent:
            raise ValueError("Need required key '{k}'".format(k=k))
    for k in dirent:
        setattr(self, k, dirent[k])
    self.perms_owner = self.perms[0:3]
    self.perms_group = self.perms[3:6]
    self.perms_other = self.perms[6:9]
    return self
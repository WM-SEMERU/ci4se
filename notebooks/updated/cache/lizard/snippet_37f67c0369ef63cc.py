def physical_drives_maximum_size_mib(self):
    return utils.max_safe([member.physical_drives.maximum_size_mib for
        member in self.get_members()])
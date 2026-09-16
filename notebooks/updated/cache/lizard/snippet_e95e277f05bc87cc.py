def mount_disks(self):
    result = True
    for disk in self.disks:
        result = disk.mount() and result
    return result
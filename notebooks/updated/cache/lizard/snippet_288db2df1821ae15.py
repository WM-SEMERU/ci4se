def is_removable(self, device):
    if not self.is_handleable(device):
        return False
    if device.is_filesystem:
        return device.is_mounted
    if device.is_crypto:
        return device.is_unlocked
    if device.is_partition_table or device.is_drive:
        return any(self.is_removable(dev) for dev in self.
            get_all_handleable() if _is_parent_of(device, dev))
    return False
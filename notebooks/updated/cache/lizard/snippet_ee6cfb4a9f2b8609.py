def add_pv(self, device):
    if not os.path.exists(device):
        raise ValueError('%s does not exist.' % device)
    self.open()
    ext = lvm_vg_extend(self.handle, device)
    if ext != 0:
        self.close()
        raise CommitError('Failed to extend Volume Group.')
    self._commit()
    self.close()
    return PhysicalVolume(self, name=device)
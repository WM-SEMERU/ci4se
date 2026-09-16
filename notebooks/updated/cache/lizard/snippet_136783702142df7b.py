def size(self, units='MiB'):
    self.open()
    size = lvm_pv_get_size(self.handle)
    self.close()
    return size_convert(size, units)
def read(self, offset):
    if not self.mode & 1:
        raise WriteOnlyError('Device is Write-Only')
    if offset >= self.size:
        raise AddressError('Offset({}) not in address space({})'.format(
            offset, self.size))
    return self.repr_[offset].getvalue()
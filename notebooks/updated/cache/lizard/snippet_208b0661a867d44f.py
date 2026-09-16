def toMBI(self, getMemoryDump=False):
    mbi = win32.MemoryBasicInformation()
    mbi.BaseAddress = self.address
    mbi.RegionSize = self.size
    mbi.State = self._parse_state(self.state)
    mbi.Protect = self._parse_access(self.access)
    mbi.Type = self._parse_type(self.type)
    if self.alloc_base is not None:
        mbi.AllocationBase = self.alloc_base
    else:
        mbi.AllocationBase = mbi.BaseAddress
    if self.alloc_access is not None:
        mbi.AllocationProtect = self._parse_access(self.alloc_access)
    else:
        mbi.AllocationProtect = mbi.Protect
    if self.filename is not None:
        mbi.filename = self.filename
    if getMemoryDump and self.content is not None:
        mbi.content = self.content
    return mbi
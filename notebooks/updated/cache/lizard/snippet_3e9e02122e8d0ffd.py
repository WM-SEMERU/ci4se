def iter_memory_map(self, minAddr=None, maxAddr=None):
    minAddr, maxAddr = MemoryAddresses.align_address_range(minAddr, maxAddr)
    prevAddr = minAddr - 1
    currentAddr = minAddr
    while prevAddr < currentAddr < maxAddr:
        try:
            mbi = self.mquery(currentAddr)
        except WindowsError:
            e = sys.exc_info()[1]
            if e.winerror == win32.ERROR_INVALID_PARAMETER:
                break
            raise
        yield mbi
        prevAddr = currentAddr
        currentAddr = mbi.BaseAddress + mbi.RegionSize
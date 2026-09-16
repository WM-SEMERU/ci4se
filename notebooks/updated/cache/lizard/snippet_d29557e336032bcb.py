def set_preferred(self, preferred_addr, addr_1, addr_2):
    if addr_1 > addr_2:
        addr_1, addr_2 = addr_2, addr_1
    self._cache[addr_1, addr_2] = preferred_addr
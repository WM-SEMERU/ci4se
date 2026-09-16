def putsz(self, addr, s):
    self.puts(addr, s)
    self._buf[addr + len(s)] = 0
def REVSH(self, params):
    Ra, Rb = self.get_two_parameters(
        '\\s*([^\\s,]*),\\s*([^\\s,]*)(,\\s*[^\\s,]*)*\\s*', params)
    self.check_arguments(low_registers=(Ra, Rb))

    def REVSH_func():
        self.register[Ra] = (self.register[Rb] & 65280) >> 8 | (self.
            register[Rb] & 255) << 8
        if self.register[Ra] & 1 << 15:
            self.register[Ra] |= 4294901760
    return REVSH_func
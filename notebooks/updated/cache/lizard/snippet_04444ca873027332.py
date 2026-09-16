def inspect_mem(self, mem):
    if isinstance(mem, RomBlock):
        raise PyrtlError('ROM blocks are not stored in the simulation object')
    return self.mems[self._mem_varname(mem)]
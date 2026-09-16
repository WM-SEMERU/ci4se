def shrink(self, new_size):
    self.size = new_size
    if self.sort == 'string':
        self.null_terminated = False
        self._content[0] = self._content[0][:self.size]
    elif self.sort == 'pointer-array':
        pointer_size = self.binary.project.arch.bytes
        if self.size % pointer_size != 0:
            raise BinaryError('Fails at Data.shrink()')
        pointers = self.size // pointer_size
        self._content = self._content[:pointers]
    else:
        self._content = [self._content[0][:self.size]]
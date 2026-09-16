def _load_string_from_native_memory(self, addr_):
    if self.state.solver.symbolic(addr_):
        l.error(
            'Loading strings from symbolic addresses is not implemented. Continue execution with an empty string.'
            )
        return ''
    addr = self.state.solver.eval(addr_)
    chars = []
    for i in itertools.count():
        str_byte = self.state.memory.load(addr + i, size=1)
        if self.state.solver.symbolic(str_byte):
            l.error(
                'Loading of strings with symbolic chars is not supported. Character %d is concretized.'
                , i)
        str_byte = self.state.solver.eval(str_byte)
        if str_byte == 0:
            break
        chars.append(chr(str_byte))
    return ''.join(chars)
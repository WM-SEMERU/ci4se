def decode(self, bytes, raw=False):
    opcode = super(CmdType, self).decode(bytes)
    result = None
    if raw:
        result = opcode
    elif opcode in self.cmddict.opcodes:
        result = self.cmddict.opcodes[opcode]
    else:
        raise ValueError('Unrecognized command opcode: %d' % opcode)
    return result
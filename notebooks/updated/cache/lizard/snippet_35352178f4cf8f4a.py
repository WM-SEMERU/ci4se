def __create(self, opcode):
    tftpassert(opcode in self.classes, 'Unsupported opcode: %d' % opcode)
    packet = self.classes[opcode]()
    return packet
def translate(self, start=None, end=None, arch_mode=None):
    start_addr = start if start else self.binary.ea_start
    end_addr = end if end else self.binary.ea_end
    self.ir_translator.reset()
    for addr, asm, _ in self.disassemble(start=start_addr, end=end_addr,
        arch_mode=arch_mode):
        yield addr, asm, self.ir_translator.translate(asm)
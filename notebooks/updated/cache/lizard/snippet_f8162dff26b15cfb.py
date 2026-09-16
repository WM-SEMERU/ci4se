def _setup_x86_arch(self, arch_mode=None):
    if arch_mode is None:
        arch_mode = self.binary.architecture_mode
    self.name = 'x86'
    self.arch_info = X86ArchitectureInformation(arch_mode)
    self.disassembler = X86Disassembler(arch_mode)
    self.ir_translator = X86Translator(arch_mode)
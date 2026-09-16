def prepare_call_state(self, calling_state, initial_state=None,
    preserve_registers=(), preserve_memory=()):
    if isinstance(self.arch, ArchMIPS32):
        if initial_state is not None:
            initial_state = self.state_blank()
        mips_caller_saves = ('s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
            'gp', 'sp', 'bp', 'ra')
        preserve_registers = preserve_registers + mips_caller_saves + ('t9',)
    if initial_state is None:
        new_state = calling_state.copy()
    else:
        new_state = initial_state.copy()
        for reg in set(preserve_registers):
            new_state.registers.store(reg, calling_state.registers.load(reg))
        for addr, val in set(preserve_memory):
            new_state.memory.store(addr, calling_state.memory.load(addr, val))
    return new_state
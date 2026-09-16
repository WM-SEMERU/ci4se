def initialize_segment_register_x64(self, state, concrete_target):
    _l.debug('Synchronizing fs segment register')
    state.regs.fs = self._read_fs_register_x64(concrete_target)
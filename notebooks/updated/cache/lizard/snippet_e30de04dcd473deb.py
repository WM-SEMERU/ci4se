def _alias_analysis(self, mock_sp=True, mock_bp=True):
    state = SimLightState(regs={self._arch.sp_offset: self._arch.initial_sp,
        self._arch.bp_offset: self._arch.initial_sp + 8192}, temps={},
        options={'mock_sp': mock_sp, 'mock_bp': mock_bp})
    for stmt_idx, stmt in list(enumerate(self._statements)):
        self._forward_handler_stmt(stmt, state)
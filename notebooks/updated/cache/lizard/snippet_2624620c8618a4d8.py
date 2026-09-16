def copy(self):
    new_cfg = CFGEmulated.__new__(CFGEmulated)
    super(CFGEmulated, self).make_copy(new_cfg)
    new_cfg._indirect_jump_target_limit = self._indirect_jump_target_limit
    new_cfg.named_errors = dict(self.named_errors)
    new_cfg.errors = list(self.errors)
    new_cfg._fail_fast = self._fail_fast
    new_cfg._max_steps = self._max_steps
    new_cfg.project = self.project
    new_cfg._edge_map = self._edge_map.copy()
    new_cfg._loop_back_edges = self._loop_back_edges[:]
    new_cfg._executable_address_ranges = self._executable_address_ranges[:]
    new_cfg._unresolvable_runs = self._unresolvable_runs.copy()
    new_cfg._overlapped_loop_headers = self._overlapped_loop_headers[:]
    new_cfg._thumb_addrs = self._thumb_addrs.copy()
    new_cfg._keep_state = self._keep_state
    return new_cfg
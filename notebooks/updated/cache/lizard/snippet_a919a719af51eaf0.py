def _indirect_jump_resolved(self, jump, jump_addr, resolved_by, targets):
    from .indirect_jump_resolvers.jumptable import JumpTableResolver
    source_addr = jump.addr
    if isinstance(resolved_by, JumpTableResolver):
        self.jump_tables[jump.addr] = jump
    jump.resolved_targets = targets
    all_targets = set(targets)
    for addr in all_targets:
        to_outside = (addr in self.functions or not self.
            _addrs_belong_to_same_section(jump.addr, addr))
        target_func_addr = jump.func_addr if not to_outside else addr
        func_edge = FunctionTransitionEdge(self._nodes[source_addr], addr,
            jump.func_addr, to_outside=to_outside, dst_func_addr=
            target_func_addr)
        job = CFGJob(addr, target_func_addr, jump.jumpkind, last_addr=
            source_addr, src_node=self._nodes[source_addr], src_ins_addr=
            None, src_stmt_idx=None, func_edges=[func_edge])
        self._insert_job(job)
        self._register_analysis_job(target_func_addr, job)
    self._deregister_analysis_job(jump.func_addr, jump)
    CFGBase._indirect_jump_resolved(self, jump, jump.addr, resolved_by, targets
        )
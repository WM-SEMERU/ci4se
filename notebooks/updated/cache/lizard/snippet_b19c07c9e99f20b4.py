def _remove_pending_return(self, job, pending_returns):
    tpls_to_remove = []
    call_stack_copy = job.call_stack_copy()
    while call_stack_copy.current_return_target is not None:
        ret_target = call_stack_copy.current_return_target
        call_stack_copy = call_stack_copy.ret(ret_target)
        call_stack_suffix = call_stack_copy.stack_suffix(self.
            _context_sensitivity_level)
        tpl = call_stack_suffix + (ret_target,)
        tpls_to_remove.append(tpl)
    for tpl in tpls_to_remove:
        if tpl in pending_returns:
            del pending_returns[tpl]
            l.debug('Removed (%s) from FakeExits dict.', ','.join([(hex(i) if
                i is not None else 'None') for i in tpl]))
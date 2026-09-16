def _analyze_all_function_features(self, all_funcs_completed=False):
    while True:
        new_changes = self._iteratively_analyze_function_features(
            all_funcs_completed=all_funcs_completed)
        new_returning_functions = new_changes['functions_return']
        new_not_returning_functions = new_changes['functions_do_not_return']
        if not new_returning_functions and not new_not_returning_functions:
            break
        for returning_function in new_returning_functions:
            self._pending_jobs.add_returning_function(returning_function.addr)
            if returning_function.addr in self._function_returns:
                for fr in self._function_returns[returning_function.addr]:
                    if not self.kb.functions.contains_addr(fr.caller_func_addr
                        ):
                        continue
                    if self.kb.functions.get_by_addr(fr.caller_func_addr
                        ).returning is not True:
                        self._updated_nonreturning_functions.add(fr.
                            caller_func_addr)
                    return_to_node = self._nodes.get(fr.return_to, None)
                    if return_to_node is None:
                        return_to_snippet = self._to_snippet(addr=fr.
                            return_to, base_state=self._base_state)
                    else:
                        return_to_snippet = self._to_snippet(cfg_node=self.
                            _nodes[fr.return_to])
                    self.kb.functions._add_return_from_call(fr.
                        caller_func_addr, fr.callee_func_addr,
                        return_to_snippet)
                del self._function_returns[returning_function.addr]
        for nonreturning_function in new_not_returning_functions:
            self._pending_jobs.add_nonreturning_function(nonreturning_function
                .addr)
            if nonreturning_function.addr in self._function_returns:
                for fr in self._function_returns[nonreturning_function.addr]:
                    if self.kb.functions.contains_addr(fr.caller_func_addr
                        ) and self.kb.functions.get_by_addr(fr.caller_func_addr
                        ).returning is not True:
                        self._updated_nonreturning_functions.add(fr.
                            caller_func_addr)
                del self._function_returns[nonreturning_function.addr]
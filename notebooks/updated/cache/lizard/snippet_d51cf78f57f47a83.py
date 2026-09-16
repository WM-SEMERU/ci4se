def _pre_analysis(self):
    for item in self._starts:
        callstack = None
        if isinstance(item, tuple):
            ip = item[0]
            state = self._create_initial_state(item[0], item[1])
        elif isinstance(item, SimState):
            state = item.copy()
            ip = state.solver.eval_one(state.ip)
            self._reset_state_mode(state, 'fastpath')
        else:
            raise AngrCFGError('Unsupported CFG start type: %s.' % str(type
                (item)))
        self._symbolic_function_initial_state[ip] = state
        path_wrapper = CFGJob(ip, state, self._context_sensitivity_level,
            None, None, call_stack=callstack)
        key = path_wrapper.block_id
        if key not in self._start_keys:
            self._start_keys.append(key)
        self._insert_job(path_wrapper)
        self._register_analysis_job(path_wrapper.func_addr, path_wrapper)
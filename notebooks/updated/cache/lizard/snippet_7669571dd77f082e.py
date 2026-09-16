def _job_sorting_key(self, job):
    MAX_BLOCKS_PER_FUNCTION = 1000000
    task_functions = list(reversed(list(task.function_address for task in
        self._task_stack if isinstance(task, FunctionAnalysis))))
    try:
        function_pos = task_functions.index(job.func_addr)
    except ValueError:
        l.warning('Function address %#x is not found in task stack.', job.
            func_addr)
        return 0
    try:
        block_in_function_pos = self._ordered_node_addrs(job.func_addr).index(
            job.addr)
    except ValueError:
        block_in_function_pos = min(job.addr - job.func_addr, 
            MAX_BLOCKS_PER_FUNCTION - 1)
    return block_in_function_pos + MAX_BLOCKS_PER_FUNCTION * function_pos
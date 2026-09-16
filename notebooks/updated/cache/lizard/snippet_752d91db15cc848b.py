def next(self):
    try:
        return next(self._execution_context)
    except HTTPFailure as e:
        if self._is_partitioned_execution_info(e):
            query_execution_info = self._get_partitioned_execution_info(e)
            self._execution_context = self._create_pipelined_execution_context(
                query_execution_info)
        else:
            raise e
    return next(self._execution_context)
def wrap_threading_start(start_func):

    def call(self):
        self._opencensus_context = (execution_context.
            get_opencensus_full_context())
        return start_func(self)
    return call
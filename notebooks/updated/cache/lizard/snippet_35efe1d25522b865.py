def StopProfiling(self):
    if self._cpu_time_profiler:
        self._cpu_time_profiler.Stop()
        self._cpu_time_profiler = None
    if self._memory_profiler:
        self._memory_profiler.Stop()
        self._memory_profiler = None
    self._process_information = None
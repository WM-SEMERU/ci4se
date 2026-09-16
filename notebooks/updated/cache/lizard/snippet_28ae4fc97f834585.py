def SampleMemoryUsage(self, parser_name):
    if self._memory_profiler:
        used_memory = self._process_information.GetUsedMemory() or 0
        self._memory_profiler.Sample(parser_name, used_memory)
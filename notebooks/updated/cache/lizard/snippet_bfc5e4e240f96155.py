def memory_used(self):
    if self._end_memory:
        memory_used = self._end_memory - self._start_memory
        return memory_used
    else:
        return None
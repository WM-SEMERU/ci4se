def _StartProfiling(self, configuration):
    if not configuration:
        return
    if configuration.HaveProfileMemoryGuppy():
        self._guppy_memory_profiler = profilers.GuppyMemoryProfiler(self.
            _name, configuration)
        self._guppy_memory_profiler.Start()
    if configuration.HaveProfileMemory():
        self._memory_profiler = profilers.MemoryProfiler(self._name,
            configuration)
        self._memory_profiler.Start()
    if configuration.HaveProfileProcessing():
        identifier = '{0:s}-processing'.format(self._name)
        self._processing_profiler = profilers.ProcessingProfiler(identifier,
            configuration)
        self._processing_profiler.Start()
    if configuration.HaveProfileSerializers():
        identifier = '{0:s}-serializers'.format(self._name)
        self._serializers_profiler = profilers.SerializersProfiler(identifier,
            configuration)
        self._serializers_profiler.Start()
    if configuration.HaveProfileStorage():
        self._storage_profiler = profilers.StorageProfiler(self._name,
            configuration)
        self._storage_profiler.Start()
    if configuration.HaveProfileTasks():
        self._tasks_profiler = profilers.TasksProfiler(self._name,
            configuration)
        self._tasks_profiler.Start()
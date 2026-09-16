def _FillEventSourceHeap(self, storage_writer, event_source_heap,
    start_with_first=False):
    if self._processing_profiler:
        self._processing_profiler.StartTiming('fill_event_source_heap')
    if self._processing_profiler:
        self._processing_profiler.StartTiming('get_event_source')
    if start_with_first:
        event_source = storage_writer.GetFirstWrittenEventSource()
    else:
        event_source = storage_writer.GetNextWrittenEventSource()
    if self._processing_profiler:
        self._processing_profiler.StopTiming('get_event_source')
    while event_source:
        event_source_heap.PushEventSource(event_source)
        if event_source_heap.IsFull():
            break
        if self._processing_profiler:
            self._processing_profiler.StartTiming('get_event_source')
        event_source = storage_writer.GetNextWrittenEventSource()
        if self._processing_profiler:
            self._processing_profiler.StopTiming('get_event_source')
    if self._processing_profiler:
        self._processing_profiler.StopTiming('fill_event_source_heap')
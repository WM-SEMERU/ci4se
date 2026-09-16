def _ExtractContentFromDataStream(self, mediator, file_entry, data_stream_name
    ):
    self.processing_status = definitions.STATUS_INDICATOR_EXTRACTING
    if self._processing_profiler:
        self._processing_profiler.StartTiming('extracting')
    self._event_extractor.ParseDataStream(mediator, file_entry,
        data_stream_name)
    if self._processing_profiler:
        self._processing_profiler.StopTiming('extracting')
    self.processing_status = definitions.STATUS_INDICATOR_RUNNING
    self.last_activity_timestamp = time.time()
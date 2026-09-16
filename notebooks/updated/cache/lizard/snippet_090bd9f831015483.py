def process(self):
    super(NativeBLEVirtualInterface, self).process()
    if not self._stream_sm_running and not self.reports.empty():
        self._stream_data()
    if not self._trace_sm_running and not self.traces.empty():
        self._send_trace()
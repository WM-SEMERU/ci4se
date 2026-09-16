def start_stream_subscriber(self):
    if not self._stream_process_started:
        if sys.platform.startswith('win'):
            self._stream_process_started = True
            self._stream()
        self._stream_process_started = True
        self._stream_process.start()
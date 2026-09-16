def fetch_timeline_history_files(self, max_timeline):
    while max_timeline > 1:
        self.c.execute('TIMELINE_HISTORY {}'.format(max_timeline))
        timeline_history = self.c.fetchone()
        history_filename = timeline_history[0]
        history_data = timeline_history[1].tobytes()
        self.log.debug('Received timeline history: %s for timeline %r',
            history_filename, max_timeline)
        compression_event = {'type': 'CLOSE_WRITE', 'compress_to_memory':
            True, 'delete_file_after_compression': False, 'input_data':
            BytesIO(history_data), 'full_path': history_filename, 'site':
            self.site}
        self.compression_queue.put(compression_event)
        max_timeline -= 1
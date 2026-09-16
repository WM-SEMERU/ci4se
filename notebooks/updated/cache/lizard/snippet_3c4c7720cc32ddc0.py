def _create_process_thread(self):
    thread = threading.Thread(target=self._process_data_events)
    thread.setDaemon(True)
    thread.start()
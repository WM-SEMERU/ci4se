def _run_process(self, start_path, stop_path, process_num=0):
    self.producer.initialize_worker(process_num)
    self.consumer.initialize_worker(process_num)
    for path in range(start_path, stop_path):
        self._run_path(path)
    self.consumer.finalize_worker(process_num)
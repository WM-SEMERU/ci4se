def update_process_died_status(self):
    queue_should_hold_result = (self._results_pending and self.
        decoder_process is not None and not self.decoder_process.is_alive())
    if queue_should_hold_result and self.decoder_metric_queue.empty():
        self._any_process_died = True
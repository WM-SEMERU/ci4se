def start_worker(self):
    if not self.is_shutting_down(shutdown_event=self.shutdown_event
        ) and self.sleep_interval > 0.1:
        self.processes = []
        self.debug_log('start_worker - start multiprocessing.Process')
        p = multiprocessing.Process(target=self.perform_work, args=(self.
            queue, self.shutdown_event, self.shutdown_ack, self.already_done))
        p.daemon = True
        p.start()
        self.processes.append({'process': p, 'shutdown_event': self.
            shutdown_event, 'shutdown_ack_event': self.shutdown_ack,
            'already_done_event': self.already_done})
        self.debug_log('start_worker - done')
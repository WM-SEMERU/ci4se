def finish_and_die(self):
    self.logstate('finish_and_die')
    self.stop_working_on_queue()
    if self.jobphase != 'pending_request':
        self.stopFactory()
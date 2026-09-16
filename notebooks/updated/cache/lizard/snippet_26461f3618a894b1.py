def icontinue(self):
    if self.status != 'paused':
        print_(
            'No sampling to continue. Please initiate sampling with isample.')
        return

    def sample_and_finalize():
        self._loop()
        self._finalize()
    self._sampling_thread = Thread(target=sample_and_finalize)
    self.status = 'running'
    self._sampling_thread.start()
    self.iprompt()
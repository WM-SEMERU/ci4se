def _update_trial_queue(self, blocking=False, timeout=600):
    trials = self._search_alg.next_trials()
    if blocking and not trials:
        start = time.time()
        while not trials and not self.is_finished() and time.time(
            ) - start < timeout:
            logger.info('Blocking for next trial...')
            trials = self._search_alg.next_trials()
            time.sleep(1)
    for trial in trials:
        self.add_trial(trial)
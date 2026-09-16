def _function(self):
    start_time = datetime.datetime.now()
    if self.settings['wait_mode'] == 'absolute':
        stop_time = start_time + datetime.timedelta(seconds=self.settings[
            'wait_time'])
    elif self.settings['wait_mode'] == 'loop_interval':
        if self.last_execution is None:
            stop_time = start_time
        else:
            loop_time = start_time - self.last_execution
            wait_time = datetime.timedelta(seconds=self.settings['wait_time'])
            if wait_time.total_seconds() < 0:
                stop_time = start_time
            else:
                stop_time = start_time + wait_time
    else:
        TypeError('unknown wait_mode')
    current_time = start_time
    while current_time < stop_time:
        if self._abort:
            break
        current_time = datetime.datetime.now()
        time.sleep(1)
        self.progress = 100.0 * (current_time - start_time).total_seconds() / (
            stop_time - start_time).total_seconds()
        self.updateProgress.emit(int(self.progress))
    if self.settings['wait_mode'] == 'absolute':
        self.last_execution = None
    else:
        self.last_execution = start_time
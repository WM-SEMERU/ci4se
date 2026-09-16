def new_log(self):
    log_id = self._num_logs
    self._logs[log_id] = []
    self._num_logs += 1
    return log_id
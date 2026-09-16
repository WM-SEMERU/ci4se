def queues(self):
    if self._queues is None:
        self._queues = QueueList(self._version, account_sid=self._solution[
            'sid'])
    return self._queues
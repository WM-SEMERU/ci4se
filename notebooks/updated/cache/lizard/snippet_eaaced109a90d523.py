def watch_statuses(self, observer, batch_ids):
    with self._lock:
        statuses = self.get_statuses(batch_ids)
        if self._has_no_pendings(statuses):
            observer.notify_batches_finished(statuses)
        else:
            self._observers[observer] = statuses
def _flush_queue(self, q, ignore_priority=False):
    assert isinstance(q, PriorityQueue)
    current_timestamp = compute_release_time(lag_in_minutes=0)
    for _ in range(len(q)):
        entry = q.pop()
        assert isinstance(entry, PriorityEntry)
        if ignore_priority or entry.release_time < current_timestamp:
            self._resubmit_uow(entry.entry)
        else:
            q.put(entry)
            break
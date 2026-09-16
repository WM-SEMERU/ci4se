def pop(self, queue_name):
    self._only_watch_from(queue_name)
    job = self.conn.reserve(timeout=0)
    job.delete()
    return job.body
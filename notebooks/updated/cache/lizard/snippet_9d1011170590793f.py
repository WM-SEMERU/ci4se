def queue_get_stoppable(self, q):
    while not self.stopped():
        try:
            return q.get(timeout=5)
        except queue.Empty:
            pass
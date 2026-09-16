def clear_queues(self, manager):
    for queue in (self.to_q, self.from_q):
        if queue is None:
            continue
        if not manager:
            try:
                queue.close()
                queue.join_thread()
            except AttributeError:
                pass
    self.to_q = self.from_q = None
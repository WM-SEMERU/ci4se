def timeout_queue_add(self, item, cache_time=0):
    self.timeout_add_queue.append((item, cache_time))
    if self.timeout_due is None or cache_time < self.timeout_due:
        self.update_request.set()
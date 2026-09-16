def pop_all(self):
    with self.lock:
        output = list(self.queue)
        self.queue.clear()
    return output
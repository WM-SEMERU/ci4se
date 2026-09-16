def result(self):
    for _ in range(self.num_threads):
        self.tasks_queue.put(None)
    self.tasks_queue.join()
    if not self.exceptions_queue.empty():
        raise self.exceptions_queue.get()
    return self.results_queue
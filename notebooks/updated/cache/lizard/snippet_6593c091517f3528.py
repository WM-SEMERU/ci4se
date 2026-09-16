def enqueue(self, pipeline):
    copied = Pipeline().append(pipeline)
    copied.group = self
    self._queue.put(copied)
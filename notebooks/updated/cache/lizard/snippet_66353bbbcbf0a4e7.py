def _start_managers(self):
    self._task_queue = _Weave(self._tasks, self.stride)
    self._semaphore_value = self.buffer or len(self._tasks) * self.stride
    self._pool_semaphore = Semaphore(self._semaphore_value)
    self._pool_getter = Thread(target=self._pool_get, args=(self._getout,
        self._task_results, self._next_available, self._task_next_lock,
        self._next_skipped, len(self._tasks), len(self.pool), id(self)))
    self._pool_getter.deamon = True
    self._pool_getter.start()
    self._pool_putter = Thread(target=self._pool_put, args=(self.
        _pool_semaphore, self._task_queue, self._putin, len(self.pool), id(
        self), self._stopping.isSet))
    self._pool_putter.deamon = True
    self._pool_putter.start()
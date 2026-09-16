def _timed_queue_join(self, timeout):
    deadline = time.time() + timeout
    with self._queue.all_tasks_done:
        while self._queue.unfinished_tasks:
            delay = deadline - time.time()
            if delay <= 0:
                return False
            self._queue.all_tasks_done.wait(timeout=delay)
        return True
def _train(self):
    if self._runner.is_alive():
        self._continue_semaphore.release()
    else:
        self._status_reporter._start()
        try:
            self._runner.start()
        except RuntimeError:
            pass
    result = None
    while result is None and self._runner.is_alive():
        try:
            result = self._results_queue.get(block=True, timeout=
                RESULT_FETCH_TIMEOUT)
        except queue.Empty:
            pass
    if result is None:
        try:
            result = self._results_queue.get(block=False)
        except queue.Empty:
            pass
    if result is None:
        self._report_thread_runner_error(block=True)
        raise TuneError(
            'Wrapped function ran until completion without reporting results or raising an exception.'
            )
    elif not self._error_queue.empty():
        logger.warning(
            'Runner error waiting to be raised in main thread. Logging all available results first.'
            )
    if '__duplicate__' in result:
        new_result = self._last_result.copy()
        new_result.update(result)
        result = new_result
    self._last_result = result
    return result
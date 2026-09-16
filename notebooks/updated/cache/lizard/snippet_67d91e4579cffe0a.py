def log_coroutine(self, cor, *args, **kwargs):
    if self.stopping:
        raise LoopStoppingError(
            'Could not launch coroutine because loop is shutting down: %s' %
            cor)
    self.start()
    cor = _instaniate_coroutine(cor, args, kwargs)

    def _run_and_log():
        task = self.loop.create_task(cor)
        task.add_done_callback(lambda x: _log_future_exception(x, self._logger)
            )
    if self.inside_loop():
        _run_and_log()
    else:
        self.loop.call_soon_threadsafe(_run_and_log)
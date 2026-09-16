def run(self):
    self._logger.info('starting all runners')
    try:
        with self._lock:
            assert not self.running.set(), 'cannot re-run: %s' % self
            self.running.set()
        thread_runner = self.runners[threading]
        for runner in self.runners.values():
            if runner is not thread_runner:
                thread_runner.register_payload(runner.run)
        if threading.current_thread() == threading.main_thread():
            asyncio_main_run(root_runner=thread_runner)
        else:
            thread_runner.run()
    except Exception as err:
        self._logger.exception('runner terminated: %s', err)
        raise RuntimeError from err
    finally:
        self._stop_runners()
        self._logger.info('stopped all runners')
        self.running.clear()
def stop(self, timeout=None, callback=None):
    if timeout:
        self._running.wait(timeout)
    stopped_future = Future()

    @gen.coroutine
    def _stop():
        if callback:
            try:
                yield gen.maybe_future(callback())
            except Exception:
                self._logger.exception(
                    'Unhandled exception calling stop callback')
        if self._ioloop_managed:
            self._logger.info('Stopping ioloop {0!r}'.format(self._ioloop))
            yield gen.moment
            self._ioloop.stop()
        self._running.clear()
    try:
        self._ioloop.add_callback(lambda : gen.chain_future(_stop(),
            stopped_future))
    except AttributeError:
        pass
    return stopped_future
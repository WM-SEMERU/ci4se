def get_output(self):
    self._closing = True
    if not self.has_finished():
        if self._debug:
            underrun_debug_timer = timeit.default_timer()
            logger.warning('NBSR underrun')
        self._thread.join()
        if not self.has_finished():
            if self._debug:
                logger.debug(
                    'NBSR join after %f seconds, underrun not resolved' % (
                    timeit.default_timer() - underrun_debug_timer))
            raise Exception('thread did not terminate')
        if self._debug:
            logger.debug('NBSR underrun resolved after %f seconds' % (
                timeit.default_timer() - underrun_debug_timer))
    if self._closed:
        raise Exception('streamreader double-closed')
    self._closed = True
    data = self._buffer.getvalue()
    self._buffer.close()
    return data
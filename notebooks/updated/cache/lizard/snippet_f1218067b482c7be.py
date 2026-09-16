def _read_result(self, num_retries):
    for i in range(num_retries):
        self._assert_alive()
        try:
            return self._result_channel.get()
        except IOError as ex:
            if ex.errno == 4:
                logger.exception(
                    'attempt to read from channel was interrupted by something'
                    )
                sys.exc_clear()
            else:
                raise ex
    raise ChannelError('failed to read from channel after %d retries' %
        num_retries)
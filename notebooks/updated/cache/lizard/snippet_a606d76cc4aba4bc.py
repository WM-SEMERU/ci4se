def _schedule_processing_blocks(self):
    LOG.info('Starting to Schedule Processing Blocks.')
    while True:
        time.sleep(0.5)
        if not self._queue:
            continue
        if self._num_pbcs >= self._max_pbcs:
            LOG.warning('Resource limit reached!')
            continue
        _inspect = Inspect(app=APP)
        if self._queue and _inspect.active() is not None:
            next_pb = self._queue[-1]
            LOG.info('Considering %s for execution...', next_pb[2])
            utc_now = datetime.datetime.utcnow()
            time_in_queue = utc_now - datetime_from_isoformat(next_pb[4])
            if time_in_queue.total_seconds() >= 10:
                item = self._queue.get()
                LOG.info('------------------------------------')
                LOG.info('>>> Executing %s! <<<', item)
                LOG.info('------------------------------------')
                execute_processing_block.delay(item)
                self._num_pbcs += 1
            else:
                LOG.info('Waiting for resources for %s', next_pb[2])
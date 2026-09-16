def _process_queue_message(self, message_queue, new_queue_found, batch_exit,
    start_time, timeout, batch_timeout):
    for queue in self._filter_queues([message_queue]):
        if queue not in self._queue_set:
            if not new_queue_found:
                new_queue_found = True
                batch_exit = time.time() + batch_timeout
                if batch_exit > start_time + timeout:
                    batch_exit = start_time + timeout
            self._queue_set.add(queue)
            self.log.debug('new queue', queue=queue)
    return new_queue_found, batch_exit
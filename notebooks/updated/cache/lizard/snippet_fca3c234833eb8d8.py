def _sender_main(self):
    if not self._http_host:
        self._choose_host()
    last_batch_time = datetime.datetime.utcnow()
    while not (self._is_terminated.is_set() and self._event_queue.empty()):
        batch = None
        try:
            if not self._is_connected.is_set():
                self._verify_connection()
            batch = self._get_batch(last_batch_time)
            self._send_batch(batch)
        except exceptions.ConnectionFailed:
            time.sleep(consts.NO_CONNECTION_SLEEP_TIME)
            self._is_connected.clear()
        except exceptions.EmptyBatch:
            time.sleep(consts.EMPTY_BATCH_SLEEP_TIME)
        except exceptions.SendFailed as ex:
            self._notify(ex.severity, str(ex))
            self._is_connected.clear()
            if batch:
                self._enqueue_batch(batch)
                logger.debug(consts.LOG_MSG_ENQUEUED_FAILED_BATCH, len(batch))
        else:
            self._is_connected.set()
        finally:
            last_batch_time = datetime.datetime.utcnow()
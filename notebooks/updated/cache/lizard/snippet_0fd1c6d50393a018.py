def _verify_connection(self):
    try:
        res = self._session.get(self._connection_validation_url, json={})
        logger.debug(consts.LOG_MSG_VERIFYING_CONNECTION, self.
            _connection_validation_url, res if res else
            'No result from backend')
        if not res.ok:
            raise requests.exceptions.RequestException(res.content)
        remote_batch_size = res.json().get(consts.MAX_REQUEST_SIZE_FIELD,
            consts.DEFAULT_BATCH_SIZE)
        if remote_batch_size < self._batch_max_size:
            self._batch_max_size = remote_batch_size
            self._notify(logging.INFO, consts.LOG_MSG_NEW_BATCH_SIZE %
                remote_batch_size)
        self._is_connected.set()
        return True
    except requests.exceptions.RequestException as ex:
        msg = consts.LOG_MSG_CONNECTION_FAILED % str(ex)
        self._notify(logging.ERROR, msg)
        raise exceptions.ConnectionFailed(msg)
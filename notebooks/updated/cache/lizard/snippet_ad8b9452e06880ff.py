def _finish_transaction_with_retry(self, command_name, explict_retry):
    try:
        return self._finish_transaction(command_name, explict_retry)
    except ServerSelectionTimeoutError:
        raise
    except ConnectionFailure as exc:
        try:
            return self._finish_transaction(command_name, True)
        except ServerSelectionTimeoutError:
            raise exc
    except OperationFailure as exc:
        if exc.code not in _RETRYABLE_ERROR_CODES:
            raise
        try:
            return self._finish_transaction(command_name, True)
        except ServerSelectionTimeoutError:
            raise exc
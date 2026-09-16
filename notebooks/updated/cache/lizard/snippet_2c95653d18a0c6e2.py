def _notify(self, log_level, message):
    timestamp = datetime.datetime.utcnow()
    logger.log(log_level, str(message))
    try:
        self._callback(log_level, message, timestamp)
    except Exception as ex:
        logger.warning(consts.LOG_MSG_CALLBACK_FAILURE % str(ex))
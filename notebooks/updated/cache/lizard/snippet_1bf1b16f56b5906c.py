def emit(self, record):
    try:
        msg = self.format(record)
        level = _STORM_LOG_LEVELS.get(record.levelname.lower(), _STORM_LOG_INFO
            )
        self.serializer.send_message({'command': 'log', 'msg': str(msg),
            'level': level})
    except Exception:
        self.handleError(record)
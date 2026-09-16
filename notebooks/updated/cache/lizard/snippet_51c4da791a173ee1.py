def _init_trace_logging(self, app):
    enabled = not app.config.get(CONF_DISABLE_TRACE_LOGGING, False)
    if not enabled:
        return
    self._trace_log_handler = LoggingHandler(self._key, telemetry_channel=
        self._channel)
    app.logger.addHandler(self._trace_log_handler)
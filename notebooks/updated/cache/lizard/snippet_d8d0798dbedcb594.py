def _init_request_logging(self, app):
    enabled = not app.config.get(CONF_DISABLE_REQUEST_LOGGING, False)
    if not enabled:
        return
    self._requests_middleware = WSGIApplication(self._key, app.wsgi_app,
        telemetry_channel=self._channel)
    app.wsgi_app = self._requests_middleware
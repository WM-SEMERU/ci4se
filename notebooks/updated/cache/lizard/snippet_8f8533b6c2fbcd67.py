def install_handler(self, app):
    if app.config['LOGGING_CONSOLE_PYWARNINGS']:
        self.capture_pywarnings(logging.StreamHandler())
    if app.config['LOGGING_CONSOLE_LEVEL'] is not None:
        for h in app.logger.handlers:
            h.setLevel(app.config['LOGGING_CONSOLE_LEVEL'])
    app.logger.addFilter(add_request_id_filter)
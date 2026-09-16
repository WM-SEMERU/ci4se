def setup(self, app):
    super().setup(app)
    if self.cfg.secret == 'InsecureSecret':
        app.logger.warning(
            'Use insecure secret key. Change SESSION_SECRET option in configuration.'
            )
    self._user_loader = asyncio.coroutine(lambda id_: id_)
    app.on_response_prepare.append(self.save)
    if self.cfg.auto_load:
        app.middlewares.append(self._middleware)
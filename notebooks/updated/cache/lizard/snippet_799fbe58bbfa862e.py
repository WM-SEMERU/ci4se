def on_finish(self):
    super(SessionRequestHandler, self).on_finish()
    LOGGER.debug('Entering SessionRequestHandler.on_finish: %s', self.
        session.id)
    self.session.last_request_at = self.current_epoch()
    self.session.last_request_uri = self.request.uri
    if self.session.dirty:
        result = yield self.session.save()
        LOGGER.debug('on_finish yield save: %r', result)
    self.session = None
    LOGGER.debug('Exiting SessionRequestHandler.on_finish: %r', self.session)
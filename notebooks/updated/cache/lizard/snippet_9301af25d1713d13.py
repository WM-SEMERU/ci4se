def prepare(self):
    super(SessionRequestHandler, self).prepare()
    result = yield gen.Task(self.start_session)
    LOGGER.debug('Exiting SessionRequestHandler.prepare: %r', result)
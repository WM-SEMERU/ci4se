def _create(self):
    from .tools import makedirs_safe
    makedirs_safe(os.path.dirname(self._database))
    Base.metadata.create_all(self._engine)
    logger.debug("Created new empty database '%s'" % self._database)
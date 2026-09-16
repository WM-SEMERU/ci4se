def set_references(self, references):
    super(CompositeLogger, self).set_references(references)
    loggers = references.get_optional(Descriptor(None, 'logger', None, None,
        None))
    for logger in loggers:
        if isinstance(logger, ILogger):
            self._loggers.append(logger)
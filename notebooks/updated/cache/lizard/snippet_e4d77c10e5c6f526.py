def send_error(self, status_code=500, **kwargs):
    if hasattr(super(SentryMixin, self), 'log_exception'):
        return super(SentryMixin, self).send_error(status_code, **kwargs)
    else:
        rv = super(SentryMixin, self).send_error(status_code, **kwargs)
        if 500 <= status_code <= 599:
            self.captureException(exc_info=kwargs.get('exc_info'))
        return rv
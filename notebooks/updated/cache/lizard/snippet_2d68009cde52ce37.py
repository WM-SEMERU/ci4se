def send(self, smtp=None, **kw):
    smtp_options = {}
    smtp_options.update(self.config.smtp_options)
    if smtp:
        smtp_options.update(smtp)
    return super(Message, self).send(smtp=smtp_options, **kw)
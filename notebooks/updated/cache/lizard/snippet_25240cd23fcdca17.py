def set_sentry_context(self, tag, value):
    if self.sentry_client:
        self.logger.debug('Setting sentry context for %s to %s', tag, value)
        self.sentry_client.tags_context({tag: value})
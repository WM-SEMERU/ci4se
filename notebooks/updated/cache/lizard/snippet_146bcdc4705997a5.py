def webhooks(self):
    if self._webhooks is None:
        self._webhooks = WebhookList(self)
    return self._webhooks
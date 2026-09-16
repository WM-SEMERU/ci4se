def remove_webhook(self):
    if self._webhook.get('hook_id'):
        self._request('{}/{}'.format(MINUT_WEBHOOKS_URL, self._webhook[
            'hook_id']), request_type='DELETE')
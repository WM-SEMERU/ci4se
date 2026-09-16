def update(self, webhook_method=values.unset, webhook_filters=values.unset,
    pre_webhook_url=values.unset, post_webhook_url=values.unset,
    pre_webhook_retry_count=values.unset, post_webhook_retry_count=values.
    unset, target=values.unset):
    data = values.of({'WebhookMethod': webhook_method, 'WebhookFilters':
        serialize.map(webhook_filters, lambda e: e), 'PreWebhookUrl':
        pre_webhook_url, 'PostWebhookUrl': post_webhook_url,
        'PreWebhookRetryCount': pre_webhook_retry_count,
        'PostWebhookRetryCount': post_webhook_retry_count, 'Target': target})
    payload = self._version.update('POST', self._uri, data=data)
    return WebhookInstance(self._version, payload)
def update_webhook(self, url, headers=None):
    headers = headers or {}
    api = self._get_api(mds.NotificationsApi)
    api.delete_long_poll_channel()
    webhook_obj = WebhookData(url=url, headers=headers)
    api.register_webhook(webhook_obj)
    return
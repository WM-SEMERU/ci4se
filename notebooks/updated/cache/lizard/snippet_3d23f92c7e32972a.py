def get_notification(self, notification_id, **params):
    response = self._get('v2', 'notifications', notification_id, params=params)
    return self._make_api_object(response, Notification)
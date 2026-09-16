def get_subscriber(self, subscriber_id):
    route_values = {}
    if subscriber_id is not None:
        route_values['subscriberId'] = self._serialize.url('subscriber_id',
            subscriber_id, 'str')
    response = self._send(http_method='GET', location_id=
        '4d5caff1-25ba-430b-b808-7a1f352cc197', version='5.0-preview.1',
        route_values=route_values)
    return self._deserialize('NotificationSubscriber', response)
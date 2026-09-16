def create_alarm_subscription(self, on_data=None, timeout=60):
    manager = WebSocketSubscriptionManager(self._client, resource='alarms')
    subscription = AlarmSubscription(manager)
    wrapped_callback = functools.partial(_wrap_callback_parse_alarm_data,
        subscription, on_data)
    manager.open(wrapped_callback, instance=self._instance, processor=self.
        _processor)
    subscription.reply(timeout=timeout)
    return subscription
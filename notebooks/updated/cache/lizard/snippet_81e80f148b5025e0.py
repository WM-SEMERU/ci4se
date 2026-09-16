def create_event_subscription(self, instance, on_data, timeout=60):
    manager = WebSocketSubscriptionManager(self, resource='events')
    subscription = WebSocketSubscriptionFuture(manager)
    wrapped_callback = functools.partial(_wrap_callback_parse_event, on_data)
    manager.open(wrapped_callback, instance)
    subscription.reply(timeout=timeout)
    return subscription
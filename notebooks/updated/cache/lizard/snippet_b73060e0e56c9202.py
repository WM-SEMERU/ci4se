def create_subscription(self, name, topic, push_config=None,
    ack_deadline_seconds=None, retain_acked_messages=None,
    message_retention_duration=None, labels=None, enable_message_ordering=
    None, expiration_policy=None, retry=google.api_core.gapic_v1.method.
    DEFAULT, timeout=google.api_core.gapic_v1.method.DEFAULT, metadata=None):
    if 'create_subscription' not in self._inner_api_calls:
        self._inner_api_calls['create_subscription'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_subscription, default_retry=self._method_configs[
            'CreateSubscription'].retry, default_timeout=self.
            _method_configs['CreateSubscription'].timeout, client_info=self
            ._client_info)
    request = pubsub_pb2.Subscription(name=name, topic=topic, push_config=
        push_config, ack_deadline_seconds=ack_deadline_seconds,
        retain_acked_messages=retain_acked_messages,
        message_retention_duration=message_retention_duration, labels=
        labels, enable_message_ordering=enable_message_ordering,
        expiration_policy=expiration_policy)
    if metadata is None:
        metadata = []
    metadata = list(metadata)
    try:
        routing_header = [('name', name)]
    except AttributeError:
        pass
    else:
        routing_metadata = (google.api_core.gapic_v1.routing_header.
            to_grpc_metadata(routing_header))
        metadata.append(routing_metadata)
    return self._inner_api_calls['create_subscription'](request, retry=
        retry, timeout=timeout, metadata=metadata)
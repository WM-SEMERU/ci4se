def create_message(self, message_data, delivery_mode=None, priority=None,
    content_type=None, content_encoding=None, serializer=None):
    delivery_mode = delivery_mode or self.delivery_mode
    if not content_type:
        serializer = serializer or self.serializer
        content_type, content_encoding, message_data = serialization.encode(
            message_data, serializer=serializer)
    elif isinstance(message_data, unicode):
        if not content_encoding:
            content_encoding = 'utf-8'
        message_data = message_data.encode(content_encoding)
    elif not content_encoding:
        content_encoding = 'binary'
    return self.backend.prepare_message(message_data, delivery_mode,
        priority=priority, content_type=content_type, content_encoding=
        content_encoding)
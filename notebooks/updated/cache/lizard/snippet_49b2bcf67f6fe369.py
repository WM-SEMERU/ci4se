def value_from_message(self, message):
    if not isinstance(message, self.message_type):
        raise DecodeError('Expected type %s, got %s: %r' % (self.
            message_type.__name__, type(message).__name__, message))
    return message
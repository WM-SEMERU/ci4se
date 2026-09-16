def _coerce_topic(topic):
    if not isinstance(topic, string_types):
        raise TypeError('topic={!r} must be text'.format(topic))
    if not isinstance(topic, text_type):
        topic = topic.decode('ascii')
    if len(topic) < 1:
        raise ValueError('invalid empty topic name')
    if len(topic) > 249:
        raise ValueError('topic={!r} name is too long: {} > 249'.format(
            topic, len(topic)))
    return topic
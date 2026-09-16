def subscribe(self, topic, callback, ordered=True):
    if '+' in topic or '#' in topic:
        regex = re.compile(topic.replace('+', '[^/]+').replace('#', '.*'))
        self.wildcard_queues.append((topic, regex, callback, ordered))
    else:
        self.queues[topic] = PacketQueue(0, callback, ordered)
    try:
        self.client.subscribe(topic, 1, self._on_receive)
    except operationError as exc:
        raise InternalError('Could not subscribe to topic', topic=topic,
            message=exc.message)
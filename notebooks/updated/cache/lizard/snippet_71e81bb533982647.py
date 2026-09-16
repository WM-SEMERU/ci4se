def publish(self, topic, messages, key=None, timeout=2):
    if not isinstance(messages, list):
        messages = [messages]
    try:
        for m in messages:
            m = encodeutils.safe_encode(m, incoming='utf-8')
            self._producer.produce(topic, m, key, callback=KafkaProducer.
                delivery_report)
            self._producer.poll(0)
        return self._producer.flush(timeout)
    except (BufferError, confluent_kafka.KafkaException, NotImplementedError):
        log.exception('Error publishing to {} topic.'.format(topic))
        raise
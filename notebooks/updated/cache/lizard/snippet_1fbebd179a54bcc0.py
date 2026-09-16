def delivery_report(err, msg):
    if err is not None:
        log.exception('Message delivery failed: {}'.format(err))
        raise confluent_kafka.KafkaException(err)
    else:
        log.debug('Message delivered to {} [{}]: {}'.format(msg.topic(),
            msg.partition(), msg.value()))
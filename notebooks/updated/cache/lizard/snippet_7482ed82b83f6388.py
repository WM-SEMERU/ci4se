def consume(topic, conf):
    from confluent_kafka.avro import AvroConsumer
    from confluent_kafka.avro.serializer import SerializerError
    print('Consuming user records from topic {} with group {}. ^c to exit.'
        .format(topic, conf['group.id']))
    c = AvroConsumer(conf, reader_value_schema=record_schema)
    c.subscribe([topic])
    while True:
        try:
            msg = c.poll(1)
            if msg is None:
                continue
            if msg.error():
                print('Consumer error: {}'.format(msg.error()))
                continue
            record = User(msg.value())
            print('name: {}\n\tfavorite_number: {}\n\tfavorite_color: {}\n'
                .format(record.name, record.favorite_number, record.
                favorite_color))
        except SerializerError as e:
            print('Message deserialization failed {}'.format(e))
            continue
        except KeyboardInterrupt:
            break
    print('Shutting down consumer..')
    c.close()
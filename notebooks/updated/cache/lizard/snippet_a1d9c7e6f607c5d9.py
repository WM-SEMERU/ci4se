def rewind_consumer_offsets(kafka_client, group, topics, raise_on_error=True):
    kafka_client.load_metadata_for_topics()
    return _commit_offsets_to_watermark(kafka_client, group, topics,
        LOW_WATERMARK, raise_on_error)
def encode_metadata_request(cls, topics=(), payloads=None):
    if payloads is not None:
        topics = payloads
    return kafka.protocol.metadata.MetadataRequest[0](topics)
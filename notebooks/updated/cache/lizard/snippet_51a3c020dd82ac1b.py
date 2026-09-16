def encode_offset_commit_request(cls, group, payloads):
    return kafka.protocol.commit.OffsetCommitRequest[0](consumer_group=
        group, topics=[(topic, [(partition, payload.offset, payload.
        metadata) for partition, payload in six.iteritems(topic_payloads)]) for
        topic, topic_payloads in six.iteritems(group_by_topic_and_partition
        (payloads))])
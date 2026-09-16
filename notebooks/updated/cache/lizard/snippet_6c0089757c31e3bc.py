def get_partition_leaders(cluster_config):
    client = KafkaClient(cluster_config.broker_list)
    result = {}
    for topic, topic_data in six.iteritems(client.topic_partitions):
        for partition, p_data in six.iteritems(topic_data):
            topic_partition = topic + '-' + str(partition)
            result[topic_partition] = p_data.leader
    return result
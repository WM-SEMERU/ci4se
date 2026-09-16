def get_topics(self, topic_name=None, names_only=False,
    fetch_partition_state=True):
    try:
        topic_ids = [topic_name] if topic_name else self.get_children(
            '/brokers/topics')
    except NoNodeError:
        _log.error('Cluster is empty.')
        return {}
    if names_only:
        return topic_ids
    topics_data = {}
    for topic_id in topic_ids:
        try:
            topic_info = self.get('/brokers/topics/{id}'.format(id=topic_id))
            topic_data = load_json(topic_info[0])
            topic_ctime = topic_info[1].ctime / 1000.0
            topic_data['ctime'] = topic_ctime
        except NoNodeError:
            _log.info("topic '{topic}' not found.".format(topic=topic_id))
            return {}
        partitions_data = {}
        for p_id, replicas in six.iteritems(topic_data['partitions']):
            partitions_data[p_id] = {}
            if fetch_partition_state:
                partition_state = self._fetch_partition_state(topic_id, p_id)
                partitions_data[p_id] = load_json(partition_state[0])
                partitions_data[p_id]['ctime'] = partition_state[1
                    ].ctime / 1000.0
            else:
                partition_info = self._fetch_partition_info(topic_id, p_id)
                partitions_data[p_id]['ctime'] = partition_info.ctime / 1000.0
            partitions_data[p_id]['replicas'] = replicas
        topic_data['partitions'] = partitions_data
        topics_data[topic_id] = topic_data
    return topics_data
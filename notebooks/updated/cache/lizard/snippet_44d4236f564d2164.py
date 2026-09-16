def empty_channel(self, topic, channel):
    nsq.assert_valid_topic_name(topic)
    nsq.assert_valid_channel_name(channel)
    return self._request('POST', '/channel/empty', fields={'topic': topic,
        'channel': channel})
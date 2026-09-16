def parse_topic(self, params, region, topic):
    topic['arn'] = topic.pop('TopicArn')
    topic['name'] = topic['arn'].split(':')[-1]
    prefix, partition, service, region, account, name = topic['arn'].split(':')
    api_client = api_clients[region]
    attributes = api_client.get_topic_attributes(TopicArn=topic['arn'])[
        'Attributes']
    for k in ['Owner', 'DisplayName']:
        topic[k] = attributes[k] if k in attributes else None
    for k in ['Policy', 'DeliveryPolicy', 'EffectiveDeliveryPolicy']:
        topic[k] = json.loads(attributes[k]) if k in attributes else None
    topic['name'] = topic['arn'].split(':')[-1]
    manage_dictionary(topic, 'subscriptions', {})
    manage_dictionary(topic, 'subscriptions_count', 0)
    self.topics[topic['name']] = topic
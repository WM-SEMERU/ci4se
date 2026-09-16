def get_property_id_from_set_topic(self, topic):
    topic = topic.decode()
    return int(topic.split('/')[-3].split('_')[-1])
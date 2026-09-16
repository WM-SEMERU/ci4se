def publish(self, topic, data, defer=None):
    if defer is None:
        self.send(nsq.publish(topic, data))
    else:
        self.send(nsq.deferpublish(topic, data, defer))
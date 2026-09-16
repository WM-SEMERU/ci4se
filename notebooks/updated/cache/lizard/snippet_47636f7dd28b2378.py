def configureLastWill(self, topic, payload, QoS):
    self._AWSIoTMQTTClient.configureLastWill(topic, payload, QoS)
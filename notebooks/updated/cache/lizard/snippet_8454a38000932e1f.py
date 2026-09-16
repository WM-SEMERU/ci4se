def unsubscribe(self, topic):
    try:
        tmp = self._mqttc
    except AttributeError:
        logger.info(
            'No MQTT Client instance found so nothing to unsubscribe from.')
        return
    if self._background_mqttc:
        logger.info('Closing background loop')
        self._background_mqttc.loop_stop()
        self._background_mqttc = None
    if topic in self._messages:
        del self._messages[topic]
    logger.info('Unsubscribing from topic: %s' % topic)
    self._unsubscribed = False
    self._mqttc.on_unsubscribe = self._on_unsubscribe
    self._mqttc.unsubscribe(str(topic))
    timer_start = time.time()
    while not self._unsubscribed and time.time(
        ) < timer_start + self._loop_timeout:
        self._mqttc.loop()
    if not self._unsubscribed:
        logger.warn("Client didn't receive an unsubscribe callback")
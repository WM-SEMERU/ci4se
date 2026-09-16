def configureAutoReconnectBackoffTime(self, baseReconnectQuietTimeSecond,
    maxReconnectQuietTimeSecond, stableConnectionTimeSecond):
    self._AWSIoTMQTTClient.configureAutoReconnectBackoffTime(
        baseReconnectQuietTimeSecond, maxReconnectQuietTimeSecond,
        stableConnectionTimeSecond)
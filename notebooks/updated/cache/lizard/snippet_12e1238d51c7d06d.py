def _handle_message_flow(self, app_message):
    if app_message.qos == QOS_0:
        yield from self._handle_qos0_message_flow(app_message)
    elif app_message.qos == QOS_1:
        yield from self._handle_qos1_message_flow(app_message)
    elif app_message.qos == QOS_2:
        yield from self._handle_qos2_message_flow(app_message)
    else:
        raise HBMQTTException("Unexcepted QOS value '%d" % str(app_message.qos)
            )
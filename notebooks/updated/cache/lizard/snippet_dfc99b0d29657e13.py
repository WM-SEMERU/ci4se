def handle_publish(self):
    self.logger.debug('PUBLISH received')
    header = self.in_packet.command
    message = NyamukMsgAll()
    message.direction = NC.DIRECTION_IN
    message.dup = (header & 8) >> 3
    message.msg.qos = (header & 6) >> 1
    message.msg.retain = header & 1
    ret, ba_data = self.in_packet.read_string()
    message.msg.topic = ba_data.decode('utf8')
    if ret != NC.ERR_SUCCESS:
        return ret
    if message.msg.qos > 0:
        ret, word = self.in_packet.read_uint16()
        message.msg.mid = word
        if ret != NC.ERR_SUCCESS:
            return ret
    message.msg.payloadlen = (self.in_packet.remaining_length - self.
        in_packet.pos)
    if message.msg.payloadlen > 0:
        ret, message.msg.payload = self.in_packet.read_bytes(message.msg.
            payloadlen)
        if ret != NC.ERR_SUCCESS:
            return ret
    self.logger.debug('Received PUBLISH(dup = %d,qos=%d,retain=%s', message
        .dup, message.msg.qos, message.msg.retain)
    self.logger.debug('\tmid=%d, topic=%s, payloadlen=%d', message.msg.mid,
        message.msg.topic, message.msg.payloadlen)
    message.timestamp = time.time()
    qos = message.msg.qos
    if qos in (0, 1, 2):
        evt = event.EventPublish(message.msg)
        self.push_event(evt)
        return NC.ERR_SUCCESS
    else:
        return NC.ERR_PROTOCOL
    return NC.ERR_SUCCESS
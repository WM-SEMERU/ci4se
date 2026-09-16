def subscribe_multi(self, topics):
    if self.sock == NC.INVALID_SOCKET:
        return NC.ERR_NO_CONN
    self.logger.info('SUBSCRIBE: %s', ', '.join([t for t, q in topics]))
    return self.send_subscribe(False, [(utf8encode(topic), qos) for topic,
        qos in topics])
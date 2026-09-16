def __publish(self, qmsg):
    with self.__seqnum_lock:
        seqnum = self.__seqnum
        self.__seqnum = (self.__seqnum + 1) % _SEQ_WRAP_SIZE
    innermsg = ubjdumpb(qmsg.inner_msg)
    clevel = COMP_NONE
    if len(innermsg) >= self.__comp_size:
        logger.debug('Compressing payload')
        try:
            innermsg = COMPRESSORS[self.__comp_default].compress(innermsg)
        except KeyError:
            logger.warning('Unknown compression method %s, not compressing',
                self.__comp_default)
        else:
            clevel = self.__comp_default
    p = {W_SEQ: seqnum, W_MESSAGE: innermsg, W_HASH: self.__make_hash(
        innermsg, self.__token, seqnum), W_COMPRESSION: clevel}
    msg = ubjdumpb(p)
    if len(msg) > self.__max_encoded_length:
        self.__request_except(qmsg.requestId, ValueError(
            'Message Payload too large %d > %d' % (len(msg), self.
            __max_encoded_length)))
        return False
    self.__amqplink.send(msg, content_type='application/ubjson')
    if DEBUG_ENABLED:
        p[W_MESSAGE] = qmsg.inner_msg
        logger.debug(decode_sent_msg('decode_sent_msg', p))
    self.__fire_callback(_CB_DEBUG_SEND, msg)
    return True
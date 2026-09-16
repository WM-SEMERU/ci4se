def __perform_unsolicited_callbacks(self, msg):
    type_ = msg[M_TYPE]
    payload = msg[M_PAYLOAD]
    if type_ in _RSP_PAYLOAD_CB_MAPPING:
        self.__fire_callback(_RSP_PAYLOAD_CB_MAPPING[type_], msg)
    elif type_ == E_FEEDDATA:
        self.__simulate_feeddata(payload[P_FEED_ID], *self.
            __decode_data_time(payload))
    elif type_ == E_SUBSCRIBED:
        self.__fire_callback(_CB_SUBSCRIPTION, payload)
    else:
        logger.error('Unexpected message type for unsolicited callback %s',
            type_)
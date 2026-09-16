def handle_unsuback(self):
    self.logger.info('UNSUBACK received')
    ret, mid = self.in_packet.read_uint16()
    if ret != NC.ERR_SUCCESS:
        return ret
    evt = event.EventUnsuback(mid)
    self.push_event(evt)
    return NC.ERR_SUCCESS
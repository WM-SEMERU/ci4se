def _recv_nack(self, method_frame):
    if self._nack_listener:
        delivery_tag = method_frame.args.read_longlong()
        multiple, requeue = method_frame.args.read_bits(2)
        if multiple:
            while self._last_ack_id < delivery_tag:
                self._last_ack_id += 1
                self._nack_listener(self._last_ack_id, requeue)
        else:
            self._last_ack_id = delivery_tag
            self._nack_listener(self._last_ack_id, requeue)
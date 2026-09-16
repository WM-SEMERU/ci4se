def _receive_packet(self, timeout=3.0):
    while True:
        response_data = self._stream.read_packet(timeout=timeout)
        response = BGAPIPacket(is_event=response_data[0] == 128,
            command_class=response_data[2], command=response_data[3],
            payload=response_data[4:])
        if response.is_event:
            if self.event_handler is not None:
                self.event_handler(response)
            continue
        return response
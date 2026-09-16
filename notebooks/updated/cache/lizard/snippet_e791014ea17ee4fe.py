def _read_message(self):
    payload_info = self._read_bytes_from_socket(4)
    read_len = unpack('>I', payload_info)[0]
    payload = self._read_bytes_from_socket(read_len)
    message = cast_channel_pb2.CastMessage()
    message.ParseFromString(payload)
    return message
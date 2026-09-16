def encode_message(self):
    if not self._message:
        raise ValueError('No message data to encode.')
    cloned_data = self._message.clone()
    self._populate_message_attributes(cloned_data)
    encoded_data = []
    c_uamqp.get_encoded_message_size(cloned_data, encoded_data)
    return b''.join(encoded_data)
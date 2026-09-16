def streaming_callback(self, body_part):
    b64_body_string = base64.b64encode(body_part).decode('utf-8')
    response = {'message_id': self._message_id, 'data': b64_body_string}
    if self._last_response is None:
        response.update(self._generate_metadata_body())
    else:
        self._last_response['done'] = False
        self._write_message_func(self._last_response)
    self._last_response = response
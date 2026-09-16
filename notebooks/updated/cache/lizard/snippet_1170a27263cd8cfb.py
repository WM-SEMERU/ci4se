def send_command_response(self, source: list, command: str, *args, **kwargs):
    args = json.dumps(args).encode('utf8')
    kwargs = json.dumps(kwargs).encode('utf8')
    frame = *source, b'', command.encode('utf8'), args, kwargs
    self.add_callback(self.command_socket.send_multipart, frame)
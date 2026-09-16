def send_empty(self, message):
    host, port = message.destination
    key_token = hash(str(host) + str(port) + str(message.token))
    if key_token in self._relations and message.type == defines.Types['RST']:
        del self._relations[key_token]
    return message
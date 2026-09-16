def _message(self, beacon_config, invert_hello=False):
    message = self.hello_message(invert_hello=invert_hello
        ) + self._message_address_generate(beacon_config)
    return message
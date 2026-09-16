def register_catchall_controlreq(self, callback, callback_parsed=None):
    if callback_parsed:
        callback = self._get_parsed_control_callback(callback_parsed, callback)
    return self.__client.register_callback_controlreq(callback)
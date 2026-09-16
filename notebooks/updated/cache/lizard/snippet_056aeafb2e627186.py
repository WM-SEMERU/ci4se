def uninstall_visa_handler(self, session, event_type, handler, user_handle=None
    ):
    for ndx, element in enumerate(self.handlers[session]):
        if element[0] is handler and element[1] is user_handle and element[4
            ] == event_type:
            del self.handlers[session][ndx]
            break
    else:
        raise errors.UnknownHandler(event_type, handler, user_handle)
    self.uninstall_handler(session, event_type, element[2], user_handle)
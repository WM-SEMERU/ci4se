def install_visa_handler(self, session, event_type, handler, user_handle=None):
    try:
        new_handler = self.install_handler(session, event_type, handler,
            user_handle)
    except TypeError as e:
        raise errors.VisaTypeError(str(e))
    self.handlers[session].append(new_handler + (event_type,))
    return new_handler[1]
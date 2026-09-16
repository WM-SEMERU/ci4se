def add_listener(self, callback, event_type=None):
    listener_uid = uuid4()
    self.listeners.append({'uid': listener_uid, 'callback': callback,
        'event_type': event_type})
    return listener_uid
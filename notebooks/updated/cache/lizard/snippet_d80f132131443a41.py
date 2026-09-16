def register_on_state_changed(self, callback):
    event_type = library.VBoxEventType.on_state_changed
    return self.event_source.register_callback(callback, event_type)
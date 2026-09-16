def register_on_medium_changed(self, callback):
    event_type = library.VBoxEventType.on_medium_changed
    return self.event_source.register_callback(callback, event_type)
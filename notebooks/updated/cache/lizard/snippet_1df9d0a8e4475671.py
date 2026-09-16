def register_on_extra_data_can_change(self, callback):
    event_type = library.VBoxEventType.on_extra_data_can_change
    return self.event_source.register_callback(callback, event_type)
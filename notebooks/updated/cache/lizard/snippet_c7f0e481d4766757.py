def _remove(self, handler, send_event=True):
    for event in self:
        event.remove_handlers_bound_to_instance(handler)
    self.handlers.remove(handler)
    if send_event:
        self.on_handler_remove(handler)
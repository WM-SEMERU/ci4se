def handle_event(self, event):
    if not isinstance(event, IEvent):
        raise TypeError('event can only be an instance of type IEvent')
    self._call('handleEvent', in_p=[event])
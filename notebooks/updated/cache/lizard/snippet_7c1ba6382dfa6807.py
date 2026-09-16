def on_any_event(self, event):
    for delegate in self.delegates:
        if hasattr(delegate, 'on_any_event'):
            delegate.on_any_event(event)
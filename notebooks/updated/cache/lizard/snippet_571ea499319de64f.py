def safe_trigger(self, event, *args):
    event_hook = self.get_or_create(event)
    event_hook.safe_trigger(*args)
    return self
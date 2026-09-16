def _self_event(self, event_name, cmd, *pargs, **kwargs):
    if hasattr(self, event_name):
        getattr(self, event_name)(cmd, *pargs, **kwargs)
def _call_watcher(self_, watcher, event):
    if self_.self_or_cls.param._TRIGGER:
        pass
    elif watcher.onlychanged and not self_._changed(event):
        return
    if self_.self_or_cls.param._BATCH_WATCH:
        self_._events.append(event)
        if watcher not in self_._watchers:
            self_._watchers.append(watcher)
    elif watcher.mode == 'args':
        with batch_watch(self_.self_or_cls, run=False):
            watcher.fn(self_._update_event_type(watcher, event, self_.
                self_or_cls.param._TRIGGER))
    else:
        with batch_watch(self_.self_or_cls, run=False):
            event = self_._update_event_type(watcher, event, self_.
                self_or_cls.param._TRIGGER)
            watcher.fn(**{event.name: event.new})
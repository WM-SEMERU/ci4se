def _update_event_type(self_, watcher, event, triggered):
    if triggered:
        event_type = 'triggered'
    else:
        event_type = 'changed' if watcher.onlychanged else 'set'
    return Event(what=event.what, name=event.name, obj=event.obj, cls=event
        .cls, old=event.old, new=event.new, type=event_type)
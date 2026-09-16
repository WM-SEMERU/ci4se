def ObjectTransitionedEventHandler(obj, event):
    if not supports_snapshots(obj):
        return
    entry = {'modified': DateTime().ISO(), 'action': event.action}
    history = api.get_review_history(obj, rev=True)
    if history:
        entry = history[0]
        timestamp = entry.pop('time', DateTime())
        entry['modified'] = timestamp.ISO()
        entry['action'] = event.action
    take_snapshot(obj, **entry)
    reindex_object(obj)
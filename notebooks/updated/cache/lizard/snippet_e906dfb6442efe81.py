def monitor_resource_sync_state(resource, callback, exit_event=None):
    exit_event = exit_event or AsyncEvent()
    callback(False)
    while not exit_event.is_set():
        yield until_any(resource.until_synced(), exit_event.until_set())
        if exit_event.is_set():
            break
        else:
            callback(True)
        yield until_any(resource.until_not_synced(), exit_event.until_set())
        if exit_event.is_set():
            break
        else:
            callback(False)
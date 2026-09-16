def from_dict(event_dict):
    return SnippetEvent(callback_id=event_dict['callbackId'], name=
        event_dict['name'], creation_time=event_dict['time'], data=
        event_dict['data'])
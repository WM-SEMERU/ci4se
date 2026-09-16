def validate(cls, event_info):
    assert 'routing_key' in event_info
    assert isinstance(event_info['routing_key'], six.string_types)
    assert 'event_action' in event_info
    assert event_info['event_action'] in cls.EVENT_TYPES
    assert 'payload' in event_info
    payload = event_info['payload']
    assert payload['summary']
    assert payload['source']
    assert payload['severity'] in cls.SEVERITY_TYPES
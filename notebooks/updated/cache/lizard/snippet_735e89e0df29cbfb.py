def decode_event(abi: Dict, log: Dict):
    if isinstance(log['topics'][0], str):
        log['topics'][0] = decode_hex(log['topics'][0])
    elif isinstance(log['topics'][0], int):
        log['topics'][0] = decode_hex(hex(log['topics'][0]))
    event_id = log['topics'][0]
    events = filter_by_type('event', abi)
    topic_to_event_abi = {event_abi_to_log_topic(event_abi): event_abi for
        event_abi in events}
    event_abi = topic_to_event_abi[event_id]
    return get_event_data(event_abi, log)
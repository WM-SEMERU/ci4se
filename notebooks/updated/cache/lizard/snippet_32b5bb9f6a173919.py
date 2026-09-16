def normalize_events_list(old_list):
    new_list = []
    for _event in old_list:
        new_event = dict(_event)
        if new_event.get('args'):
            new_event['args'] = dict(new_event['args'])
            encode_byte_values(new_event['args'])
        if new_event.get('queue_identifier'):
            del new_event['queue_identifier']
        hexbytes_to_str(new_event)
        name = new_event['event']
        if name == 'EventPaymentReceivedSuccess':
            new_event['initiator'] = to_checksum_address(new_event['initiator']
                )
        if name in ('EventPaymentSentSuccess', 'EventPaymentSentFailed'):
            new_event['target'] = to_checksum_address(new_event['target'])
        encode_byte_values(new_event)
        encode_object_to_str(new_event)
        new_list.append(new_event)
    return new_list
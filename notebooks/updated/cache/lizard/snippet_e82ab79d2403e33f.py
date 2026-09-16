def describe_event_source_mapping(UUID=None, EventSourceArn=None,
    FunctionName=None, region=None, key=None, keyid=None, profile=None):
    ids = _get_ids(UUID, EventSourceArn=EventSourceArn, FunctionName=
        FunctionName)
    if not ids:
        return {'event_source_mapping': None}
    UUID = ids[0]
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        desc = conn.get_event_source_mapping(UUID=UUID)
        if desc:
            keys = ('UUID', 'BatchSize', 'EventSourceArn', 'FunctionArn',
                'LastModified', 'LastProcessingResult', 'State',
                'StateTransitionReason')
            return {'event_source_mapping': dict([(k, desc.get(k)) for k in
                keys])}
        else:
            return {'event_source_mapping': None}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}
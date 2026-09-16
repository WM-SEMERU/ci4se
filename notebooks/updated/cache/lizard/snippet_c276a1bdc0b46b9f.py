def unpack_kinesis_event(kinesis_event, deserializer=None, unpacker=None,
    embed_timestamp=False):
    records = kinesis_event['Records']
    events = []
    shard_ids = set()
    for rec in records:
        data = rec['kinesis']['data']
        try:
            payload = b64decode(data)
        except TypeError:
            payload = b64decode(data.encode('utf-8'))
        if unpacker:
            payload = unpacker(payload)
        shard_ids.add(rec['eventID'].split(':')[0])
        try:
            payload = payload.decode()
        except AttributeError:
            pass
        if deserializer:
            try:
                payload = deserializer(payload)
            except ValueError:
                try:
                    payload = deserializer(payload.replace("\\'", "'"))
                except:
                    logger.error('Invalid searialized payload: {}'.format(
                        payload))
                    raise
        if isinstance(payload, dict) and embed_timestamp:
            ts = rec['kinesis'].get('approximateArrivalTimestamp')
            if ts:
                ts = datetime.fromtimestamp(ts, tz=tz.tzutc())
                ts_str = (
                    '{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'
                    .format(year=ts.year, month=ts.month, day=ts.day, hour=
                    ts.hour, minute=ts.minute, second=ts.second))
            else:
                ts_str = ''
            payload[embed_timestamp] = ts_str
        events.append(payload)
    if len(shard_ids) > 1:
        msg = 'Kinesis event contains records from several shards: {}'.format(
            shard_ids)
        raise BadKinesisEventError(msg)
    return events, shard_ids.pop()
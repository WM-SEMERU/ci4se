def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        serial = obj.isoformat()
        return serial
    from ..time_interval import TimeInterval, TimeIntervals
    if isinstance(obj, (TimeInterval, TimeIntervals)):
        return obj.to_json()
    from ..stream import StreamId
    if isinstance(obj, StreamId):
        return obj.to_json()
    from ..channels import BaseChannel
    if isinstance(obj, BaseChannel):
        return json.dumps({'channel_id': obj.channel_id})
    raise TypeError('Type %s not serializable' % type(obj))
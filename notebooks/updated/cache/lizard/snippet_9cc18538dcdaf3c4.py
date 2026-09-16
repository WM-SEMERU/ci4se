def _parse_status(data, cast_type):
    data = data.get('status', {})
    volume_data = data.get('volume', {})
    try:
        app_data = data['applications'][0]
    except KeyError:
        app_data = {}
    is_audio = cast_type in (CAST_TYPE_AUDIO, CAST_TYPE_GROUP)
    status = CastStatus(data.get('isActiveInput', None if is_audio else
        False), data.get('isStandBy', None if is_audio else True),
        volume_data.get('level', 1.0), volume_data.get('muted', False),
        app_data.get(APP_ID), app_data.get('displayName'), [item['name'] for
        item in app_data.get('namespaces', [])], app_data.get(SESSION_ID),
        app_data.get('transportId'), app_data.get('statusText', ''))
    return status
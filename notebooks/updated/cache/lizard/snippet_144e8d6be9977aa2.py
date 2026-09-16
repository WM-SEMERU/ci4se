def _track_from_response(result, timeout):
    response = result['response']
    status = response['track']['status'].lower()
    if status == 'pending':
        result = _wait_for_pending_track(response['track']['id'], timeout)
        response = result['response']
        status = response['track']['status'].lower()
    if not status == 'complete':
        track_id = response['track']['id']
        if status == 'pending':
            raise Exception(
                "%s: the operation didn't complete before the timeout (%d secs)"
                 % (track_id, timeout))
        else:
            raise Exception(
                '%s: there was an error analyzing the track, status: %s' %
                (track_id, status))
    else:
        track_properties = response['track']
        identifier = track_properties.pop('id')
        md5 = track_properties.pop('md5', None)
        track_properties.update(track_properties.pop('audio_summary'))
        return Track(identifier, md5, track_properties)
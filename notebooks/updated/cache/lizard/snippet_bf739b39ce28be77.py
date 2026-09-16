def validate_signature(request, secret_key):
    data = request.GET.copy()
    if request.method != 'GET':
        message_body = getattr(request, request.method, {})
        data.update(message_body)
    if data.get('sig', False):
        sig = data['sig']
        del data['sig']
    else:
        return False
    if data.get('t', False):
        timestamp = int(data.get('t', False))
        del data['t']
    else:
        return False
    local_time = datetime.utcnow()
    remote_time = datetime.utcfromtimestamp(timestamp)
    if local_time > remote_time:
        delta = local_time - remote_time
    else:
        delta = remote_time - local_time
    if delta.seconds > 5 * 60:
        return False
    return sig == calculate_signature(secret_key, data, timestamp)
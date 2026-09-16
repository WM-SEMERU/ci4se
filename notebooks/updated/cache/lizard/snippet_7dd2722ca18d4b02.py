def get_request_data(request=None):
    if request is None:
        request = api.get_request()
    if not request:
        return {}
    forwarded_for = request.get_header('X_FORWARDED_FOR')
    real_ip = request.get_header('X_REAL_IP')
    remote_address = request.get_header('REMOTE_ADDR')
    return {'comments': request.form.get('comments', ''), 'remote_address':
        forwarded_for or real_ip or remote_address, 'user_agent': request.
        get_header('HTTP_USER_AGENT'), 'referer': request.get_header(
        'HTTP_REFERER')}
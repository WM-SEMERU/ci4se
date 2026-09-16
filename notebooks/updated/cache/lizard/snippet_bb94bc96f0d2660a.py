def show_csrs():
    data = salt.utils.http.query('{0}/certificaterequests'.format(_base_url
        ()), status=True, decode=True, decode_type='json', header_dict={
        'tppl-api-key': _api_key()})
    status = data['status']
    if six.text_type(status).startswith('4') or six.text_type(status
        ).startswith('5'):
        raise CommandExecutionError('There was an API error: {0}'.format(
            data['error']))
    return data.get('dict', {})